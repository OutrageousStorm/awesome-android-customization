#!/usr/bin/env python3
"""
rom_selector.py -- Interactive ROM recommendation engine
Asks questions about your device, preferences, and use case — recommends best ROM
Usage: python3 rom_selector.py
"""
import sys

ROMS = {
    "grapheneos": {
        "name": "GrapheneOS",
        "stars": "Security-first, hardened kernel, Sandboxed Play",
        "best_for": "Privacy advocates, security researchers",
        "devices": ["Pixel 6a+"],
        "tradeoffs": "Less customization, Google ecosystem only",
    },
    "lineageos": {
        "name": "LineageOS",
        "stars": "Widest device support, stable, vanilla Android",
        "best_for": "Broader compatibility, balance",
        "devices": ["Most devices"],
        "tradeoffs": "Less hardening than GrapheneOS",
    },
    "crdroid": {
        "name": "crDroid",
        "stars": "Heavily customized, Pixel-like UI, active development",
        "best_for": "Customization lovers, feature-rich",
        "devices": ["Pixel, OnePlus, Samsung, Xiaomi"],
        "tradeoffs": "Larger ROM, heavier on battery",
    },
    "evolution_x": {
        "name": "Evolution X",
        "stars": "Pixel Experience + extra tweaks, clean UI",
        "best_for": "Pixel UI fans + customization",
        "devices": ["OnePlus, Xiaomi, Samsung"],
        "tradeoffs": "Smaller dev team than LineageOS",
    },
    "pixel_experience": {
        "name": "Pixel Experience",
        "stars": "Pure Pixel UI, Material You, Bluetooth audio codec support",
        "best_for": "Stock Android lovers",
        "devices": ["Wide support"],
        "tradeoffs": "Still less privacy hardening than GrapheneOS",
    },
}

QUESTIONS = [
    ("Device brand?", ["Pixel", "Samsung", "OnePlus", "Xiaomi", "Other"]),
    ("Priority?", ["Security", "Customization", "Battery life", "Stability"]),
    ("Experience level?", ["Beginner", "Intermediate", "Advanced"]),
    ("Want custom kernels/modules?", ["Yes", "No"]),
]

def recommend():
    print("\n📱 ROM Recommendation Engine")
    print("=" * 45)
    print("Answer a few questions to get personalized ROM recommendations.\n")

    answers = []
    for q, opts in QUESTIONS:
        print(f"{q}")
        for i, o in enumerate(opts, 1):
            print(f"  {i}. {o}")
        choice = input("> ").strip()
        try:
            answers.append(opts[int(choice) - 1])
        except:
            answers.append(opts[0])

    # Simple scoring
    score = {}
    for rom, info in ROMS.items():
        score[rom] = 0

    # Security-focused
    if answers[1] == "Security":
        score["grapheneos"] += 5
        score["lineageos"] += 2
    elif answers[1] == "Customization":
        score["crdroid"] += 5
        score["evolution_x"] += 3
    elif answers[1] == "Battery life":
        score["lineageos"] += 3
        score["pixel_experience"] += 2
    else:  # Stability
        score["lineageos"] += 4
        score["pixel_experience"] += 3

    # Device-based
    if "Pixel" in answers[0]:
        score["grapheneos"] += 3
        score["pixel_experience"] += 2
    elif "Samsung" in answers[0]:
        score["crdroid"] += 2
    elif "OnePlus" in answers[0]:
        score["evolution_x"] += 2

    # Custom kernels
    if answers[3] == "Yes":
        score["crdroid"] += 2
        score["evolution_x"] += 1

    # Beginner
    if answers[2] == "Beginner":
        score["lineageos"] += 2
        score["pixel_experience"] += 1

    ranked = sorted(score.items(), key=lambda x: x[1], reverse=True)

    print("\n" + "=" * 45)
    print("🎯 Recommendations (ranked):\n")
    for rank, (rom_key, pts) in enumerate(ranked[:3], 1):
        rom = ROMS[rom_key]
        print(f"{rank}. {rom['name']}")
        print(f"   ✓ {rom['stars']}")
        print(f"   👥 Best for: {rom['best_for']}")
        print(f"   ⚠️  Tradeoffs: {rom['tradeoffs']}\n")

if __name__ == "__main__":
    recommend()
