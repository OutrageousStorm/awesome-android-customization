#!/usr/bin/env python3
"""
rom_matrix_builder.py -- Generate feature comparison matrix for Android ROMs
Builds a comparison table: GrapheneOS vs LineageOS vs CalyxOS vs stock, etc.
Usage: python3 rom_matrix_builder.py --output roms.csv
"""
import json, csv, argparse
from dataclasses import dataclass

@dataclass
class ROM:
    name: str
    base: str  # AOSP, LineageOS, etc
    security: int  # 1-5 score
    privacy: int
    performance: int
    customization: int
    kernel_support: str  # "latest" / "LTS" / "12"
    features: list

ROMS = [
    ROM("GrapheneOS", "AOSP", 5, 5, 4, 3, "latest", 
        ["Sandboxed Play Services", "Hardened WebView", "Secure Scavenger Hunt"]),
    ROM("CalyxOS", "AOSP", 4, 5, 3, 2, "latest",
        ["Datura Firewall", "Micro G", "No Google"]),
    ROM("LineageOS", "AOSP", 3, 3, 4, 5, "LTS",
        ["Huge device support", "Customizable", "Community"]),
    ROM("crDroid", "LineageOS", 3, 3, 4, 5, "LTS",
        ["AOSP base", "Per-app language", "Pixel feel"]),
    ROM("Stock (Pixel)", "AOSP", 3, 2, 5, 1, "latest",
        ["Official", "Fast updates", "Pixel features"]),
]

def compare():
    print(f"\n📊 Android ROM Feature Matrix\n")
    print(f"{'ROM':<18} {'Security':<10} {'Privacy':<10} {'Perf':<6} {'Custom':<6} {'Base':<12}")
    print("─" * 65)
    for rom in sorted(ROMS, key=lambda r: r.security, reverse=True):
        sec_bar = "█" * rom.security + "░" * (5 - rom.security)
        priv_bar = "█" * rom.privacy + "░" * (5 - rom.privacy)
        print(f"{rom.name:<18} {sec_bar:<10} {priv_bar:<10} {rom.performance}/5  {rom.customization}/5  {rom.base:<12}")

if __name__ == '__main__':
    compare()
