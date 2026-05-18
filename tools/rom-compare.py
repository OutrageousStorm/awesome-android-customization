#!/usr/bin/env python3
"""
rom-compare.py -- Compare Android ROMs side-by-side
Shows LineageOS vs GrapheneOS vs crDroid features, privacy, features matrix
Usage: python3 rom-compare.py [--rom grapheneos|lineageos|crroid|e-os]
"""
import json

ROMS = {
    "grapheneos": {
        "name": "GrapheneOS",
        "privacy": 10, "security": 10, "performance": 8, "customization": 5,
        "aosp_based": True, "root": False, "gapps": "Sandboxed Play",
        "features": ["Hardened bionic", "Exploit mitigations", "Sandboxed Play Services",
                     "Per-app network access", "Per-app language", "Restricted USB access"],
    },
    "lineageos": {
        "name": "LineageOS",
        "privacy": 7, "security": 8, "performance": 9, "customization": 10,
        "aosp_based": True, "root": "Optional", "gapps": "Optional",
        "features": ["Extensive device support", "Magisk/root support", "Highly customizable",
                     "Active development", "Wide ROM ports available"],
    },
    "crroid": {
        "name": "crDroid",
        "privacy": 6, "security": 7, "performance": 9, "customization": 10,
        "aosp_based": True, "root": "Magisk", "gapps": "Included",
        "features": ["Pixel-like experience", "Heavy customization", "Gaming-optimized",
                     "Per-app refresh rate", "Custom ambient display"],
    },
    "e-os": {
        "name": "e/OS",
        "privacy": 9, "security": 8, "performance": 7, "customization": 4,
        "aosp_based": True, "root": False, "gapps": "MicroG (no Google)",
        "features": ["Privacy-focused", "No Google services", "FOSS alternative apps",
                     "Blissful launcher", "Cloud storage control"],
    },
}

def bar(val, max_val=10):
    filled = int((val / max_val) * 10)
    return "█" * filled + "░" * (10 - filled)

def compare():
    print("\\n📊 Android ROM Comparison\\n")
    print(f"{'ROM':<15} {'Privacy':<12} {'Security':<12} {'Performance':<12} {'Customization'}")
    print("─" * 65)
    for key, rom in ROMS.items():
        print(f"{rom['name']:<15} {bar(rom['privacy']):<12} {bar(rom['security']):<12} "
              f"{bar(rom['performance']):<12} {bar(rom['customization'])}")

    print("\\n" + "─" * 65 + "\\n")
    print(f"{'ROM':<15} {'Root':<20} {'GApps':<20} {'AOSP'}")
    print("─" * 65)
    for key, rom in ROMS.items():
        print(f"{rom['name']:<15} {str(rom['root']):<20} {rom['gapps']:<20} "
              f"{'Yes' if rom['aosp_based'] else 'No'}")

    print("\\n" + "─" * 65)
    for key, rom in ROMS.items():
        print(f"\\n{rom['name']}:")
        for feat in rom['features']:
            print(f"  • {feat}")

if __name__ == "__main__":
    compare()
