#!/usr/bin/env python3
"""
Compile-time table generator, PoC scope: one application ("Matter Gateway"),
three chips.

This demonstrates the core claim: the README table cell is a DERIVED
artifact, not a source of truth. The rule below is deliberately simple
(readable in ~10 lines) — the point isn't a sophisticated scoring model,
it's that the *reasoning is auditable code* instead of hand-typed prose
that can silently drift from the underlying facts (which is exactly what
happened with the datasheet version numbers we had to fix by hand).

Rule for "Matter Gateway" (needs Wi-Fi AND/OR 802.15.4 to bridge Matter):
    both wifi and 802.15.4          -> ++  "all-in-one gateway"
    802.15.4 only, has ethernet     -> ++  "wired uplink + Thread"
    802.15.4 only, no other uplink  -> +   "Thread native, needs Wi-Fi companion"
    wifi only                       -> +   "Wi-Fi only, needs Thread companion"
    neither                         -> --  "no relevant radio"
    RCP without 802.15.4 (E22 case) -> -   "Wi-Fi capable but no Thread; wrong
                                             role for this application"

Usage:
    python3 tools/render_table.py
"""

import glob
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load_chip(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def score_matter_gateway(chip: dict) -> tuple[str, str]:
    wifi = chip["radios"]["wifi"]["value"]
    zigbee_thread = chip["radios"]["ieee802_15_4"]["value"]
    has_ethernet = chip["interfaces"].get("ethernet_mac_mbps", {}).get("value") is not None
    wifi_detail = chip["radios"]["wifi"].get("detail", "Wi-Fi")
    thread_detail = chip["radios"]["ieee802_15_4"].get("detail", "802.15.4")

    if wifi and zigbee_thread:
        reason = f"{wifi_detail} + {thread_detail}"
        if has_ethernet:
            reason += " + Ethernet"
        return "++", reason
    if zigbee_thread and has_ethernet:
        return "++", f"{thread_detail} + wired Ethernet uplink"
    if zigbee_thread:
        return "+", f"{thread_detail} native, but no Wi-Fi of its own — typically paired with a Wi-Fi SoC"
    if wifi:
        return "+", f"{wifi_detail}, but no 802.15.4 — requires an external Thread radio"
    return "--", "no relevant radio for Matter bridging"


def main():
    chip_files = sorted(glob.glob(str(ROOT / "data" / "chips" / "*.yaml")))
    chips = [load_chip(p) for p in chip_files]

    print("Generated from data/chips/*.yaml — do not hand-edit this row in README.md,\n"
          "edit the source YAML and re-run this script instead.\n")

    header = "| Application | " + " | ".join(f"**{c['id']}**" for c in chips) + " |"
    sep = "|---|" + "---|" * len(chips)
    cells = []
    for c in chips:
        symbol, reason = score_matter_gateway(c)
        cells.append(f"{symbol} ({reason})")
    row = "| 49. Matter Gateway | " + " | ".join(cells) + " |"

    print(header)
    print(sep)
    print(row)

    print("\n--- Provenance trace for this row (for audit / AI consumption) ---")
    for c in chips:
        symbol, reason = score_matter_gateway(c)
        print(f"\n{c['id']}: {symbol}")
        for field in ("wifi", "ieee802_15_4"):
            f = c["radios"][field]
            print(f"  radios.{field} = {f['value']}  <- source_ref={f['source_ref']}, verified={f['last_verified']}")
        eth = c["interfaces"].get("ethernet_mac_mbps", {})
        print(f"  interfaces.ethernet_mac_mbps = {eth.get('value')}  <- source_ref={eth.get('source_ref')}, verified={eth.get('last_verified')}")


if __name__ == "__main__":
    main()
