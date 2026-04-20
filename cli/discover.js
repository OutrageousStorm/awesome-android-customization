#!/usr/bin/env node
/**
 * discover.js -- Interactive CLI to explore awesome Android customization tools
 * npm install -g awesome-android-customization
 * discover
 */

const fs = require("fs");
const path = require("path");
const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const CATEGORIES = {
    "launchers": "Home screen launchers (Nova, Lawnchair, KISS, Niagara)",
    "customization": "UI themes, icon packs, fonts, clock faces",
    "rom": "Custom ROMs (LineageOS, Pixel Experience, crDroid)",
    "adb": "ADB utilities and automation scripts",
    "privacy": "Privacy tools and hardening scripts",
    "kernel": "Custom kernels (KernelSU, performance mods)",
    "accessibility": "Screen readers, text scaling, gesture control",
    "root": "Root solutions (Magisk, KernelSU, Superuser)",
};

const TOOLS = {
    "launchers": [
        { name: "Nova Launcher", rating: "⭐⭐⭐⭐⭐", desc: "Most powerful launcher with deep customization" },
        { name: "Lawnchair", rating: "⭐⭐⭐⭐", desc: "FOSS Pixel Launcher fork" },
        { name: "KISS Launcher", rating: "⭐⭐⭐⭐", desc: "Minimal, gesture-based search launcher" },
        { name: "Niagara Launcher", rating: "⭐⭐⭐⭐", desc: "Bottom-focused, scrollable layout" },
        { name: "Olauncher", rating: "⭐⭐⭐", desc: "Minimal FOSS launcher" },
    ],
    "customization": [
        { name: "Zedge", rating: "⭐⭐⭐⭐", desc: "Wallpapers, themes, ringtones" },
        { name: "Icon Packs", rating: "⭐⭐⭐⭐", desc: "100+ packs on Play Store" },
        { name: "Zooper Widget", rating: "⭐⭐⭐⭐", desc: "Custom lock screen widgets" },
        { name: "KWGT", rating: "⭐⭐⭐⭐", desc: "Lock screen widgets without root" },
    ],
    "rom": [
        { name: "LineageOS", rating: "⭐⭐⭐⭐⭐", desc: "Most stable custom ROM" },
        { name: "crDroid", rating: "⭐⭐⭐⭐", desc: "Heavily customizable AOSP" },
        { name: "Pixel Experience", rating: "⭐⭐⭐⭐", desc: "Stock Pixel UI on any device" },
        { name: "GrapheneOS", rating: "⭐⭐⭐⭐⭐", desc: "Privacy/security focused (Pixel only)" },
    ],
    "adb": [
        { name: "adb debloat", rating: "⭐⭐⭐⭐", desc: "Remove system bloatware" },
        { name: "scrcpy", rating: "⭐⭐⭐⭐⭐", desc: "Mirror and control Android from PC" },
        { name: "android-tweaks-toolkit", rating: "⭐⭐⭐⭐", desc: "Automation and tweaking scripts" },
    ],
    "privacy": [
        { name: "NetGuard", rating: "⭐⭐⭐⭐⭐", desc: "Per-app firewall, no root needed" },
        { name: "Orbot", rating: "⭐⭐⭐⭐", desc: "Tor proxy for Android" },
        { name: "Molly", rating: "⭐⭐⭐⭐", desc: "Hardened Signal messenger" },
    ],
    "root": [
        { name: "Magisk", rating: "⭐⭐⭐⭐⭐", desc: "Systemless root with modules" },
        { name: "KernelSU", rating: "⭐⭐⭐⭐", desc: "Kernel-level root (A12+ devices)" },
        { name: "SuperSU", rating: "⭐⭐⭐", desc: "Legacy root solution (deprecated)" },
    ],
};

function menu() {
    console.clear();
    console.log("🎨 Awesome Android Customization\n");
    console.log("Categories:");
    Object.entries(CATEGORIES).forEach(([ key, desc ], i) => {
        console.log(`  ${i + 1}. ${key.toUpperCase():<15} ${desc}`);
    });
    console.log("  0. Exit\n");
}

function showCategory(cat) {
    console.clear();
    console.log(`📱 ${cat.toUpperCase()}\n`);
    const tools = TOOLS[cat] || [];
    tools.forEach((t, i) => {
        console.log(`  ${i + 1}. ${t.name} ${t.rating}`);
        console.log(`     ${t.desc}\n`);
    });
}

function prompt(question) {
    return new Promise(resolve => rl.question(question, resolve));
}

async function main() {
    while (true) {
        menu();
        const choice = await prompt("Select category (0-8): ");
        if (choice === "0") break;
        
        const categories = Object.keys(CATEGORIES);
        const idx = parseInt(choice) - 1;
        if (idx >= 0 && idx < categories.length) {
            showCategory(categories[idx]);
            await prompt("\nPress Enter to continue...");
        }
    }
    rl.close();
}

main();
