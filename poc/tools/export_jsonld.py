#!/usr/bin/env python3
"""
JSON-LD export combining three W3C/community ontologies over one @context:

  schema.org  — product identity (schema:Product, schema:manufacturer,
                schema:releaseStatus)
  PROV-O      — provenance per fact (prov:Entity, prov:wasDerivedFrom,
                prov:generatedAtTime) — a standards-based replacement for
                our ad hoc source_ref/last_verified pair
  QUDT        — quantities with units (qudt:QuantityValue,
                qudt:numericValue, qudt:unit) for every numeric fact that
                has a physical dimension (MHz, KiB, µA, Mbit/s, ...) —
                schema.org's own QuantitativeValue has no notion of
                physical dimension or unit algebra, QUDT does

All QUDT unit IRIs below were verified against qudt.org before use
(see UNIT_MAP comments) — this file intentionally does not invent
ontology identifiers.

Output: dist/chips.jsonld — one JSON-LD document, all chips as a
@graph of schema:Product nodes, each fact as a nested prov:Entity,
each dimensioned value as a nested qudt:QuantityValue.

Usage:
    python3 tools/export_jsonld.py
"""

import glob
import json
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CONTEXT = {
    "schema": "https://schema.org/",
    "prov": "http://www.w3.org/ns/prov#",
    "qudt": "http://qudt.org/schema/qudt/",
    "unit": "http://qudt.org/vocab/unit/",
    "dct": "http://purl.org/dc/terms/",

    # Fallback vocabulary for domain-specific field names (architecture,
    # clock_max_mhz, radios, wifi, gpio_count, ...) that have no existing
    # public ontology term. Without this, JSON-LD expansion SILENTLY DROPS
    # every unmapped plain-string key — which would have reproduced, one
    # layer down, exactly the "fact silently disappears" failure mode this
    # whole data layer exists to prevent. Every domain term below resolves
    # to a real (if project-local) IRI instead of vanishing.
    # TODO: replace individual terms with SOSA/SAREF equivalents where a
    # good match exists (e.g. SAREF4INMA has device-capability terms that
    # may fit "radios"/"interfaces" better than an ad hoc vocab).
    "@vocab": "urn:esp32features:vocab:",

    "id": "@id",
    "type": "@type",

    "Product": "schema:Product",
    "name": "schema:name",
    "manufacturer": "schema:manufacturer",
    "releaseStatus": "schema:releaseStatus",
    "additionalProperty": "schema:additionalProperty",
    "PropertyValue": "schema:PropertyValue",
    "propertyID": "schema:propertyID",

    # PROV-O: how we know a given fact
    "Entity": "prov:Entity",
    "wasDerivedFrom": {"@id": "prov:wasDerivedFrom", "@type": "@id"},
    "generatedAtTime": {"@id": "prov:generatedAtTime", "@type": "http://www.w3.org/2001/XMLSchema#date"},
    "value": "prov:value",

    # QUDT: value + unit for anything with a physical dimension
    #
    # NOTE: the JSON-LD property is named "qudtUnit", not "unit" — "unit"
    # is already taken as the namespace prefix above (unit:MegaHZ etc.).
    # Using the same context key for both a prefix and a property term is
    # a classic JSON-LD footgun: whichever mapping comes later in the
    # context dict silently wins, and the other one vanishes with no
    # error. Caught by re-expanding this document with a real processor
    # after the first draft — "unit:MegaHZ" was staying uncompacted
    # because the prefix mapping had been clobbered.
    "QuantityValue": "qudt:QuantityValue",
    "numericValue": "qudt:numericValue",
    "qudtUnit": {"@id": "qudt:unit", "@type": "@id"},
}

# field -> QUDT unit IRI, verified against qudt.org (see doc comments above
# each block in tools/render_table.py's sibling files for the source check
# performed before adding these).
#
#   clock_max_mhz      -> unit:MegaHZ           (verified: qudt.org/vocab/unit/MegaHZ)
#   sram_kb             -> unit:KibiBYTE         (verified: qudt.org/vocab/unit/KibiBYTE — datasheet
#                                                  "KB" for SRAM is conventionally binary/1024-based,
#                                                  so KibiBYTE is the dimensionally honest choice,
#                                                  not the decimal KiloBYTE)
#   embedded_flash_mb,
#   embedded_psram_mb  -> unit:MebiBYTE          (verified: qudt.org/vocab/unit/MebiBYTE — same
#                                                  binary-prefix reasoning as above)
#   deep_sleep_ua       -> unit:MicroA           (verified: qudt.org/vocab/unit/MicroA)
#   ethernet_mac_mbps  -> unit:MegaBIT-PER-SEC   (verified: qudt.org/vocab/unit/MegaBIT-PER-SEC)
UNIT_MAP = {
    ("architecture", "clock_max_mhz"): "unit:MegaHZ",
    ("memory", "sram_kb"): "unit:KibiBYTE",
    ("memory", "embedded_flash_mb"): "unit:MebiBYTE",
    ("memory", "embedded_psram_mb"): "unit:MebiBYTE",
    ("power", "deep_sleep_ua"): "unit:MicroA",
    ("interfaces", "ethernet_mac_mbps"): "unit:MegaBIT-PER-SEC",
}


def load_yaml(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_sources():
    registry = {}
    for path in sorted(glob.glob(str(ROOT / "data" / "sources" / "*.yaml"))):
        for src in load_yaml(Path(path)).get("sources", []):
            registry[src["id"]] = src
    return registry


def fact_to_jsonld(fact: dict, unit_iri: str | None):
    """Turn one {value, source_ref, last_verified, ...} leaf into a
    prov:Entity, wrapping the value in a qudt:QuantityValue when a unit
    applies."""
    node = {
        "type": "Entity",
        "generatedAtTime": fact.get("last_verified"),
    }
    if fact.get("source_ref"):
        node["wasDerivedFrom"] = f"urn:esp32features:source:{fact['source_ref']}"

    if unit_iri and fact.get("value") is not None:
        node["value"] = {
            "type": "QuantityValue",
            "numericValue": fact["value"],
            "qudtUnit": unit_iri,
        }
    else:
        node["value"] = fact.get("value")

    if "detail" in fact:
        node["schema:description"] = fact["detail"]
    if "note" in fact:
        node["dct:description"] = fact["note"]
    return node


def walk_and_convert(obj, path=()):
    """Recursively convert every fact-shaped dict into JSON-LD, tracking
    the field path so we can look up a unit in UNIT_MAP."""
    if isinstance(obj, dict) and "value" in obj and "source_ref" in obj:
        unit_iri = UNIT_MAP.get(path)
        return fact_to_jsonld(obj, unit_iri)
    if isinstance(obj, dict):
        return {k: walk_and_convert(v, path + (k,)) for k, v in obj.items()}
    if isinstance(obj, list):
        return [walk_and_convert(v, path) for v in obj]
    return obj


def chip_to_product_node(chip: dict) -> dict:
    body = walk_and_convert(
        {k: v for k, v in chip.items() if k not in ("id", "name", "status")}
    )
    return {
        "id": f"urn:esp32features:chip:{chip['id']}",
        "type": "Product",
        "name": chip["name"],
        "manufacturer": {"id": "https://www.wikidata.org/wiki/Q1109838", "name": "Espressif Systems"},
        "releaseStatus": chip.get("status"),
        **body,
    }


def source_to_entity_node(src: dict) -> dict:
    node = {
        "id": f"urn:esp32features:source:{src['id']}",
        "type": "Entity",
        "schema:name": src["title"],
        "dct:description": f"status={src.get('status')}",
    }
    if src.get("version"):
        node["schema:version"] = src["version"]
    if src.get("url"):
        node["schema:url"] = {"id": src["url"]}
    if src.get("accessed"):
        node["generatedAtTime"] = src["accessed"]
    return node


def main():
    sources = load_sources()
    chip_files = sorted(glob.glob(str(ROOT / "data" / "chips" / "*.yaml")))
    chips = [load_yaml(Path(p)) for p in chip_files]

    graph = [chip_to_product_node(c) for c in chips]
    graph += [source_to_entity_node(s) for s in sources.values()]

    doc = {"@context": CONTEXT, "@graph": graph}

    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    out_path = dist / "chips.jsonld"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)
    print(f"wrote {out_path.relative_to(ROOT)}  ({len(chips)} products, {len(sources)} source entities)")
    print("Ontologies combined: schema.org (product identity) + PROV-O (provenance) + QUDT (units)")


if __name__ == "__main__":
    main()
