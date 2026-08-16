# ESP32Features — Data Layer PoC

Proof of concept for a machine-readable layer underneath the human-facing
`README.md` in [artkeller/ESP32Features](https://github.com/artkeller/ESP32Features).
The README stays the human interface. This is the fact layer beneath it —
every number in the README should, in the target architecture, trace back
to a file in here.

## Directory layout

```
poc/
├── data/
│   ├── chips/              one YAML file per chip — the actual facts
│   │   ├── ESP32-C6.yaml       (standard case)
│   │   ├── ESP32-E22.yaml      (RCP edge case: no standalone MCU,
│   │   │                        no public datasheet PDF)
│   │   └── ESP32-S31.yaml      (pre-release edge case: some fields
│   │                            explicitly null = "not yet published",
│   │                            not guessed)
│   └── sources/
│       └── espressif.yaml  central citation registry — update a
│                            datasheet version ONCE here, every chip
│                            file that cites it is corrected automatically
├── schema/
│   └── chip.schema.json    JSON Schema: every fact leaf MUST carry
│                            source_ref + last_verified, or validation
│                            fails
├── tools/
│   ├── validate.py         QA gate: schema + source-reference integrity
│   │                        + staleness warnings (>180 days since
│   │                        last_verified)
│   ├── render_table.py     compile-time example: derives a README
│   │                        table row ("Matter Gateway") from raw data
│   │                        via an auditable rule instead of hand-typed
│   │                        symbols, and prints the provenance trace
│   │                        that justifies each cell
│   └── export_config.py    two consumer-facing exports (see below)
└── dist/                   generated, never hand-edited
    ├── chips.config.json       flat value-only JSON, for build tooling
    │                            / config generators
    ├── chips.ai_context.json   provenance-preserving JSON, for an AI
    │                            coding assistant to load at generation
    │                            time and cite its source when it makes
    │                            a capability claim
    └── chips.jsonld            JSON-LD, combining three ontologies over
                                 one @context: schema.org (product
                                 identity), PROV-O (provenance — the
                                 standards-based version of source_ref/
                                 last_verified), and QUDT (quantities
                                 with units — 512, "KB" becomes a real
                                 qudt:QuantityValue with a resolvable
                                 unit IRI, not two loose strings)
```

## Running it

```bash
pip install pyyaml jsonschema pyld

# 1. QA gate — schema, source integrity, staleness
python3 tools/validate.py

# 2. Compile-time table generation, one worked example
python3 tools/render_table.py

# 3. Consumer exports (config + AI context)
python3 tools/export_config.py

# 4. JSON-LD export (schema.org + PROV-O + QUDT)
python3 tools/export_jsonld.py

# sanity-check the JSON-LD actually expands correctly under a real
# processor — see "Two bugs this JSON-LD layer caught" below for why
# this step is not optional
python3 -c "from pyld import jsonld; import json; jsonld.expand(json.load(open('dist/chips.jsonld')))"
```

## What each layer is *for*

| Layer | Consumer | Question it answers |
|---|---|---|
| `data/chips/*.yaml` | humans editing facts | "What do we actually know, and where from?" |
| `schema/chip.schema.json` + `tools/validate.py` | CI, before merge | "Is every fact attributed and current?" |
| `tools/render_table.py` | README generation | "What does this fact set imply for this application?" |
| `dist/chips.config.json` | build tooling, config generators | "Does chip X have feature Y? (just the value)" |
| `dist/chips.ai_context.json` | AI coding assistants at generation time | "Does chip X have feature Y — and what's the citation if I claim so in generated code/comments?" |
| `dist/chips.jsonld` | any generic Linked-Data / RDF consumer | "Give me this as standards-based RDF I can merge with other PROV/QUDT/schema.org data, without needing to understand ESP32Features' internal schema at all" |

## Deliberate design choices worth arguing about

- **`null` is a first-class value, not an omission.** ESP32-S31's
  `deep_sleep_ua` is explicitly `null` with a `note` explaining why —
  Espressif hasn't published it. A generator consuming this file can
  render "not yet published" instead of a guessed number or a silently
  blank table cell. This directly addresses the "SCHREIBE NICHTS, WENN
  ES NICHTS ZU VERMELDEN GIBT" principle from earlier in this project —
  now it's enforced structurally instead of relying on manual discipline
  in every future edit.

- **Central source registry, not per-fact URLs.** If Espressif ships a
  new ESP32-C6 datasheet revision, exactly one line in
  `data/sources/espressif.yaml` changes, and every fact citing
  `esp32c6_ds` is correct again. This is what actually would have
  prevented the version-drift bug this PoC was commissioned to fix.

- **`status: no_public_pdf` is tracked and surfaced, not hidden.**
  E22/H21/S31 currently have no indexed standalone datasheet PDF.
  Rather than silently treating a press announcement with the same
  confidence as a datasheet, the source registry marks this explicitly,
  and `validate.py` turns it into a visible (non-blocking) warning on
  every fact that depends on it.

- **The rule engine in `render_table.py` is intentionally minimal.**
  This PoC scores exactly one application (#49 Matter Gateway) across
  three chips to prove the mechanism, not to replace the full 50×12
  evaluation table on day one. A real migration would move application-
  by-application, keeping the hand-curated table as the fallback for any
  cell whose reasoning doesn't reduce to a clean rule (the RCP special
  cases especially resist simple rules and may stay hand-annotated with
  a `manual_override` field — not modeled yet in this PoC).


- Only 3 of 12 chips have data files (enough to exercise the standard
  case, the RCP edge case, and the pre-release edge case).
- Only 1 of 50 applications has a scoring rule.
- No CI wiring (GitHub Actions) yet — `validate.py` is meant to become
  a merge gate, but that's a follow-up, not part of this PoC.
- No `manual_override` mechanism for cells where rule-based scoring
  isn't appropriate (most of the RCP-specific reasoning today).
- No round-trip check that the *rendered* README table still matches
  what `render_table.py` would generate — that's the natural next step
  once more applications have rules.
