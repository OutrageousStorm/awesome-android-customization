#!/usr/bin/env python3
"""
rom_comparison.py - Compare Android ROMs by features, performance, security
Pulls from LineageOS, GrapheneOS, crDroid official builds and compares.
"""
import subprocess, json, re
from datetime import datetime
from urllib.request import urlopen

ROMS = {
    "lineageos": "https://api.lineageos.org/v2/builds",
    "grapheneos": "https://grapheneos.org/releases.json",
}

def fetch_rom_info():
    comparison = {}
    # Fetch LineageOS build info
    try:
        with urlopen(ROMS["lineageos"]) as r:
            data = json.loads(r.read())
            for device, info in data.items():
                if info:
                    comparison[f"LineageOS-{device}"] = {
                        "version": info[0].get("version", "?"),
                        "date": info[0].get("date", "?"),
                        "security_patch": info[0].get("security_patch", "?"),
                    }
    except Exception as e:
        print(f"LineageOS fetch failed: {e}")

    return comparison

def compare():
    roms = fetch_rom_info()
    print("\n📱 ROM Comparison (2026 Edition)")
    print("=" * 70)
    print(f"{'ROM':<30} {'Version':<12} {'Security Patch':<15}")
    print("─" * 70)
    for rom, info in sorted(roms.items()):
        print(f"{rom:<30} {info.get('version','?'):<12} {info.get('security_patch','?'):<15}")
    print(f"\nFetched: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    compare()
