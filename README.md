# 📱 Awesome Android Customization

Curated list of the best Android customization tools, ROMs, and resources.

## 🔧 ADB Tools & Scripts
- **android-toolkit-scripts** — 6 working Python ADB tools (device info, permission audit, app extractor, network monitor, backup)
- **android-adb-cheatsheet** — 150+ ADB commands organized by category
- **android-tweaks-toolkit** — ADB toolkit with screensaver control, auto-brightness, app launcher
- **android-scrcpy-tools** — scrcpy launcher with profiles + automation replay engine

## 🛡️ Security & Forensics
- **frida-scripts-android** — 9 Frida hooks for SSL bypass, root hiding, crypto logging, HTTP interception, notification monitoring
- **apk-patcher** — Automated APK SSL pinning + root detection bypass via apktool
- **android-forensics-guide** — Complete reverse engineering + MITM setup guide
- **android-wakelock-analyzer** — Parse bugreport and find battery drain culprits

## 🎨 ROMs & Builds
- **custom-rom-notes** — GrapheneOS/LineageOS quick-start guides
- **grapheneos-guide** — Complete GrapheneOS setup with app recommendations
- **android-rom-guide** — Samsung/Xiaomi/OnePlus/Pixel ROM flashing guides
- **android-gsi-guide** — Generic System Image (Project Treble) guide
- **twrp-device-trees** — Build TWRP recovery from scratch

## 🔐 Privacy & Hardening
- **android-privacy-guide** — 3-level privacy hardening (baseline → advanced)
- **android-privacy-hardener** — Automated hardening script with audit checks
- **android-security-research** — Root detection methods, Shizuku internals, ADB attack surface
- **android-debloat-lists** — Safe-to-remove package lists for Samsung, Xiaomi, Pixel, OnePlus
- **android-permission-auditor** — Scan every app for dangerous permissions

## 🚀 Development & Automation
- **android-kernel-guide** — KernelSU vs Magisk, custom kernel compilation
- **android-notification-listener** — Capture & auto-reply to notifications
- **android-wakelock-analyzer** — Battery drain diagnosis tool

---
**Total repositories:** 40+  
**Last updated:** $(date +%Y-%m-%d)

## Batch ADB Command Executor (Bash)
Execute ADB commands across multiple connected devices simultaneously.

```bash
bash tools/batch-adb-commands.sh list
bash tools/batch-adb-commands.sh exec 'settings get global adb_enabled'
bash tools/batch-adb-commands.sh install app.apk
bash tools/batch-adb-commands.sh uninstall com.example.app
```

Perfect for managing multiple devices without manual commands.

---

## 🛠️ Tools

### android-ui-analyzer.py
Detects and reports installed overlays, custom launchers, themes, and Magisk modules on a connected Android device.

**Usage:**
```bash
python3 tools/android-ui-analyzer.py
```

Requirements: adb, Python 3.6+

