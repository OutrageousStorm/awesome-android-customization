#!/usr/bin/env python3
"""
rom_feature_matrix.py -- Interactive ROM feature comparison tool
Compare Android ROMs side-by-side: LineageOS, crDroid, Evolution X, GrapheneOS, Paranoid Android
Usage: python3 rom_feature_matrix.py [--compare rom1,rom2] [--export csv|json]
"""
import json, argparse, sys

ROMS = {
    "LineageOS": {
        "base": "AOSP", "privacy": "Good", "customization": "Excellent", "performance": "Good",
        "bootloader": "Unlocked", "treble": "Yes", "ab_slots": "Yes", "gapps": "Optional",
        "encryption": "Yes", "verified_boot": "Configurable", "selinux": "Enforcing",
        "updates": "Monthly", "ota": "Yes", "source": "Open",
    },
    "crDroid": {
        "base": "AOSP", "privacy": "Good", "customization": "Excellent", "performance": "Excellent",
        "bootloader": "Unlocked", "treble": "Yes", "ab_slots": "Yes", "gapps": "Optional",
        "encryption": "Yes", "verified_boot": "Configurable", "selinux": "Enforcing",
        "updates": "Weekly", "ota": "Yes", "source": "Open",
    },
    "GrapheneOS": {
        "base": "AOSP", "privacy": "Excellent", "customization": "Moderate", "performance": "Excellent",
        "bootloader": "Locked (enforced)", "treble": "N/A", "ab_slots": "Yes", "gapps": "Sandboxed Play",
        "encryption": "Yes", "verified_boot": "Enforced", "selinux": "Enforcing",
        "updates": "Monthly", "ota": "Yes", "source": "Open", "devices": "Pixels only",
    },
    "Evolution X": {
        "base": "AOSP", "privacy": "Good", "customization": "Excellent", "performance": "Excellent",
        "bootloader": "Unlocked", "treble": "Yes", "ab_slots": "Yes", "gapps": "Optional",
        "encryption": "Yes", "verified_boot": "Configurable", "selinux": "Enforcing",
        "updates": "Frequent", "ota": "Yes", "source": "Open",
    },
    "Paranoid Android": {
        "base": "AOSP", "privacy": "Good", "customization": "Good", "performance": "Good",
        "bootloader": "Unlocked", "treble": "Yes", "ab_slots": "Yes", "gapps": "Optional",
        "encryption": "Yes", "verified_boot": "Configurable", "selinux": "Enforcing",
        "updates": "Regular", "ota": "Yes", "source": "Open",
    },
}

def show_matrix():
    print("\n📊 Android ROM Feature Matrix\n")
    features = set()
    for rom_data in ROMS.values():
        features.update(rom_data.keys())
    features = sorted(features)

    print(f"{'Feature':<25}", end="")
    for rom in ROMS:
        print(f" {rom:<18}", end="")
    print()
    print("─" * (25 + len(ROMS) * 20))

    for feat in features:
        print(f"{feat:<25}", end="")
        for rom in ROMS:
            val = ROMS[rom].get(feat, "N/A")
            print(f" {val:<18}", end="")
        print()

def compare_roms(rom_list):
    print(f"\n🔍 Comparing: {', '.join(rom_list)}\n")
    for feat in sorted(set(k for r in rom_list for k in ROMS[r].keys())):
        print(f"\n{feat.upper()}")
        for rom in rom_list:
            val = ROMS[rom].get(feat, "N/A")
            print(f"  {rom:<20} {val}")

def export_json():
    return json.dumps(ROMS, indent=2)

def export_csv():
    import csv, io
    output = io.StringIO()
    features = sorted(set(k for r in ROMS.values() for k in r.keys()))
    writer = csv.writer(output)
    writer.writerow(["Feature"] + list(ROMS.keys()))
    for feat in features:
        row = [feat] + [ROMS[rom].get(feat, "N/A") for rom in ROMS]
        writer.writerow(row)
    return output.getvalue()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--compare", help="Compare specific ROMs (comma-separated)")
    parser.add_argument("--export", choices=["csv", "json"])
    args = parser.parse_args()

    if args.export == "json":
        print(export_json())
    elif args.export == "csv":
        print(export_csv())
    elif args.compare:
        roms = [r.strip() for r in args.compare.split(",")]
        invalid = [r for r in roms if r not in ROMS]
        if invalid:
            print(f"Unknown ROMs: {', '.join(invalid)}")
            print(f"Available: {', '.join(ROMS.keys())}")
            sys.exit(1)
        compare_roms(roms)
    else:
        show_matrix()

if __name__ == "__main__":
    main()
