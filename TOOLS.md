# 🛠️ Android Customization Tools Index

Quick reference to all open-source tools for Android customization (organized by type).

## ADB-Based Tools

| Tool | Language | What it does |
|------|----------|-------------|
| [android-toolkit-scripts](https://github.com/OutrageousStorm/android-toolkit-scripts) | Python | Device info, permission audit, app extraction, debloat, backup |
| [android-adb-cheatsheet](https://github.com/OutrageousStorm/android-adb-cheatsheet) | Markdown | 150+ ADB commands + real-world recipes |
| [android-permission-auditor](https://github.com/OutrageousStorm/android-permission-auditor) | Python | Scan all apps for dangerous permissions, revoke in bulk |
| [android-tweaks-toolkit](https://github.com/OutrageousStorm/android-tweaks-toolkit) | Python/Bash | Screen state triggers, auto brightness, app launcher |
| [android-privacy-hardener](https://github.com/OutrageousStorm/android-privacy-hardener) | Python | Privacy audit (check.py) + comprehensive hardening (harden.py) |
| [android-notification-listener](https://github.com/OutrageousStorm/android-notification-listener) | Python | Monitor notifications, dump to JSON, auto-reply bot |
| [android-scrcpy-tools](https://github.com/OutrageousStorm/android-scrcpy-tools) | Python | scrcpy profile launcher, tap/swipe automation replay |
| [android-wakelock-analyzer](https://github.com/OutrageousStorm/android-wakelock-analyzer) | Python | Parse bugreports, identify battery drain culprits |

## Reverse Engineering & Analysis

| Tool | Language | What it does |
|------|----------|-------------|
| [apk-patcher](https://github.com/OutrageousStorm/apk-patcher) | Python | Auto patch APKs: SSL pinning bypass, root detection bypass, resign |
| [frida-scripts-android](https://github.com/OutrageousStorm/frida-scripts-android) | JavaScript | 6 Frida scripts: SSL bypass, root bypass, crypto hook, HTTP logger, etc. |
| [android-forensics-guide](https://github.com/OutrageousStorm/android-forensics-guide) | Markdown | APK analysis, Frida, SSL pinning bypass, network interception |

## ROM & Kernel Tools

| Tool | Language | What it does |
|------|----------|-------------|
| [android-rom-guide](https://github.com/OutrageousStorm/android-rom-guide) | Markdown | Complete ROM flashing guide for 20+ OEMs |
| [custom-rom-notes](https://github.com/OutrageousStorm/custom-rom-notes) | Markdown | GrapheneOS, LineageOS quick-start |
| [android-gsi-guide](https://github.com/OutrageousStorm/android-gsi-guide) | Markdown | GSI / Project Treble guide |
| [twrp-device-trees](https://github.com/OutrageousStorm/twrp-device-trees) | Markdown | Build TWRP from device tree source |
| [android-kernel-guide](https://github.com/OutrageousStorm/android-kernel-guide) | Markdown | Kernel compilation, KernelSU, governors |

## Knowledge Base

| Resource | Type | Focus |
|----------|------|-------|
| [android-security-research](https://github.com/OutrageousStorm/android-security-research) | Docs | Root detection, Shizuku, ADB attack surface |
| [android-privacy-guide](https://github.com/OutrageousStorm/android-privacy-guide) | Docs | 3-level privacy hardening (baseline to maximum) |
| [ios-security-research](https://github.com/OutrageousStorm/ios-security-research) | Docs | iOS checkm8, boot chain, jailbreak landscape |
| [ios-activation-wiki](https://github.com/OutrageousStorm/ios-activation-wiki) | Docs | Activation Lock architecture, bypass methods |

## Collections & References

| Repo | What it is |
|------|-----------|
| [magisk-modules-collection](https://github.com/OutrageousStorm/magisk-modules-collection) | Curated Magisk modules (privacy, performance, UI) |
| [android-xposed-modules](https://github.com/OutrageousStorm/android-xposed-modules) | LSPosed modules (privacy, UI, apps) |
| [android-debloat-lists](https://github.com/OutrageousStorm/android-debloat-lists) | ADB debloat lists for Samsung, Xiaomi, Pixel, OnePlus |
| [grapheneos-guide](https://github.com/OutrageousStorm/grapheneos-guide) | GrapheneOS setup, Sandboxed Play, app recommendations |
| [awesome-android-customization](https://github.com/OutrageousStorm/awesome-android-customization) | This repo — curated awesome list |

## Getting Started by Goal

**I want to debloat my phone:**
→ Use `android-toolkit-scripts/smart_debloat.sh` with `android-debloat-lists`

**I want privacy:**
→ Run `android-privacy-hardener/check.py` first, then `harden.py --level 2`

**I want to analyze what an app is doing:**
→ Use `apk-patcher` to patch it, then `frida-scripts-android` to hook it

**I want a custom ROM:**
→ Follow `android-rom-guide`, then check `grapheneos-guide` or `custom-rom-notes`

**I want to root my phone:**
→ Read `android-rom-guide/guides/magisk-setup.md`, then use `magisk-modules-collection` for addons

**I want to understand iOS bypass:**
→ Read `ios-security-research` for technical deep-dives, `ios-activation-wiki` for practical tools/methods
