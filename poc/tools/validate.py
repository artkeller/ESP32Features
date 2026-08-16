#!/usr/bin/env python3
"""
QA gate for the ESP32Features data layer.

Runs three checks over every file in data/chips/*.yaml:
  1. Schema validity        (jsonschema against schema/chip.schema.json)
  2. Source-reference integrity  (every source_ref must exist in the
                                   central registry data/sources/*.yaml)
  3. Staleness                   (last_verified older than STALE_DAYS
                                   raises a warning, not a hard failure —
                                   this is meant to spawn a re-verification
                                   issue, not block a build outright)

Exit code is non-zero if any hard error (1 or 2) occurred. Staleness
warnings never fail the build by themselves — that's a deliberate choice:
"we know this might be outdated" is a healthier state than a red build
nobody has time to fix, but it must be VISIBLE, hence the separate
warning list printed at the end.

Usage:
    python3 tools/validate.py
"""

import sys
import json
import glob
import datetime
from pathlib import Path

import yaml
import jsonschema

ROOT = Path(__file__).resolve().parent.parent
STALE_DAYS = 180


def load_yaml(path: Path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_sources() -> dict:
    """Flatten all data/sources/*.yaml files into {id: record}."""
    registry = {}
    for path in sorted(glob.glob(str(ROOT / "data" / "sources" / "*.yaml"))):
        doc = load_yaml(Path(path))
        for src in doc.get("sources", []):
            if src["id"] in registry:
                print(f"  [ERROR] duplicate source id '{src['id']}' (also in {path})")
            registry[src["id"]] = src
    return registry


def walk_fact_nodes(obj, path=""):
    """Yield (path, node) for every dict that looks like a 'fact' leaf,
    i.e. it has both 'value' and 'source_ref' keys."""
    if isinstance(obj, dict):
        if "value" in obj and "source_ref" in obj:
            yield path, obj
            return
        for k, v in obj.items():
            yield from walk_fact_nodes(v, f"{path}.{k}" if path else k)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from walk_fact_nodes(v, f"{path}[{i}]")


def main():
    schema_path = ROOT / "schema" / "chip.schema.json"
    with open(schema_path, encoding="utf-8") as f:
        schema = json.load(f)

    sources = load_sources()
    print(f"Loaded {len(sources)} source records from data/sources/*.yaml\n")

    chip_files = sorted(glob.glob(str(ROOT / "data" / "chips" / "*.yaml")))
    if not chip_files:
        print("No chip files found under data/chips/*.yaml — nothing to validate.")
        sys.exit(1)

    errors = 0
    warnings = []
    today = datetime.date.today()

    for path in chip_files:
        rel = Path(path).relative_to(ROOT)
        chip = load_yaml(Path(path))
        chip_id = chip.get("id", "<missing id>")
        print(f"Validating {rel}  ({chip_id})")

        # 1. Schema validity
        try:
            jsonschema.validate(instance=chip, schema=schema)
            print("  [OK]    schema valid")
        except jsonschema.exceptions.ValidationError as e:
            errors += 1
            print(f"  [ERROR] schema violation: {e.message}  (at {'/'.join(str(p) for p in e.path)})")
            continue  # don't bother with fact-level checks on a broken file

        # 2. Source-reference integrity + 3. staleness, per fact leaf
        fact_count = 0
        for fpath, node in walk_fact_nodes(chip):
            fact_count += 1
            ref = node.get("source_ref")
            if ref not in sources:
                errors += 1
                print(f"  [ERROR] {fpath}: source_ref '{ref}' not found in source registry")
                continue

            src = sources[ref]
            if src.get("status") == "no_public_pdf":
                warnings.append(
                    f"{chip_id}.{fpath}: sourced from '{src['title']}' — "
                    f"no public datasheet PDF, treat with caution"
                )

            lv = node.get("last_verified")
            try:
                lv_date = datetime.date.fromisoformat(lv)
                age = (today - lv_date).days
                if age > STALE_DAYS:
                    warnings.append(
                        f"{chip_id}.{fpath}: last_verified {lv} is {age} days old "
                        f"(> {STALE_DAYS}d threshold) — re-verify against '{src['title']}'"
                    )
            except (TypeError, ValueError):
                errors += 1
                print(f"  [ERROR] {fpath}: invalid last_verified date: {lv!r}")

        print(f"  [OK]    {fact_count} attributed facts checked\n")

    print("=" * 70)
    if warnings:
        print(f"{len(warnings)} warning(s) (non-blocking, but should be triaged):")
        for w in warnings:
            print(f"  [WARN]  {w}")
    else:
        print("No staleness/provenance warnings.")

    print("=" * 70)
    if errors:
        print(f"FAILED: {errors} hard error(s). Fix before merging.")
        sys.exit(1)
    else:
        print(f"PASSED: {len(chip_files)} chip file(s), 0 hard errors.")
        sys.exit(0)


if __name__ == "__main__":
    main()
