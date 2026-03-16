# 📱 Awesome Android Customization

> A curated, AI-maintained list of the best tools, apps, ROMs, launchers, and ADB tricks for customizing your Android device.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Maintained by AI](https://img.shields.io/badge/Maintained%20by-AI%20🤖-blueviolet)](https://github.com/OutrageousStorm)
[![Last Updated](https://img.shields.io/badge/Updated-March%202026-brightgreen)]()

---

## 📚 Contents

- [Launchers](#-launchers)
- [Icon Packs](#-icon-packs)
- [Theming Tools](#-theming-tools)
- [ADB Tools](#-adb-tools)
- [Custom ROMs](#-custom-roms)
- [Root Tools](#-root-tools)
- [Widgets & Live Wallpapers](#-widgets--live-wallpapers)
- [Useful ADB Commands](#-useful-adb-commands)

---

## 🚀 Launchers

| App | Description | Price |
|-----|-------------|-------|
| [Nova Launcher](https://novalauncher.com) | Most popular customizable launcher | Free / $5 Prime |
| [Lawnchair](https://github.com/LawnchairLauncher/lawnchair) | Open-source Pixel launcher clone | Free |
| [Kvaesitso](https://github.com/MM2-0/Kvaesitso) | Search-focused launcher | Free |
| [KISS Launcher](https://github.com/Neamar/KISS) | Minimalist, keyboard-driven | Free |
| [Niagara Launcher](https://niagaralauncher.app) | Unique vertical alphabet scroll | Free / Premium |

---

## 🎨 Icon Packs

| Pack | Style | Link |
|------|-------|------|
| Arcticons | Line art, minimal | [GitHub](https://github.com/Donnnno/Arcticons) |
| Whicons | Clean white | [Play Store](https://play.google.com/store/apps/details?id=com.whicons.iconpack) |
| Lines | Thin line style | Play Store |
| Delta | Adaptive, Material You | [GitHub](https://github.com/Delta-Icons/android) |

---

## 🎭 Theming Tools

- **[Substratum](https://github.com/substratum/substratum)** — System-wide theme engine (root/Andromeda)
- **[Repainter](https://repainter.app)** — Material You color customization
- **[aShell](https://gitlab.com/sunilpaulmathew/ashell)** — ADB shell via Shizuku (no PC needed)
- **[Shizuku](https://github.com/RikkaApps/Shizuku)** — Use system APIs without root

---

## 🔧 ADB Tools

- **[Android ADB Toolkit](https://github.com/OutrageousStorm/android-adb-toolkit)** ⭐ — Web-based GUI for ADB (our tool!)
- **[Universal Android Debloater](https://github.com/0x192/universal-android-debloater)** — Cross-platform debloater GUI
- **[Scrcpy](https://github.com/Genymobile/scrcpy)** — Screen mirror & control via ADB
- **[Android TV Debloat Toolkit](https://github.com/seun-novodev/android-tv-debloat-toolkit)** — For Android TV

---

## 📦 Custom ROMs

| ROM | Based On | Best For |
|-----|----------|---------|
| [LineageOS](https://lineageos.org) | AOSP | Wide device support |
| [GrapheneOS](https://grapheneos.org) | AOSP | Privacy & security |
| [PixelExperience](https://get.pixelexperience.org) | Pixel UI | Pixel features on any device |
| [crDroid](https://crdroid.net) | LineageOS | Customization |
| [CalyxOS](https://calyxos.org) | AOSP | Privacy focused |

---

## 🔑 Root Tools

- **[Magisk](https://github.com/topjohnwu/Magisk)** — The standard root solution
- **[KernelSU](https://github.com/tiann/KernelSU)** — Kernel-based root
- **[LSPosed](https://github.com/LSPosed/LSPosed)** — Xposed framework for Magisk

---

## 🖼️ Widgets & Live Wallpapers

- **[KWGT](https://play.google.com/store/apps/details?id=org.kustom.widget)** — Custom widget maker
- **[KLWP](https://play.google.com/store/apps/details?id=org.kustom.wallpaper)** — Custom live wallpaper maker
- **[Widgetsmith](https://play.google.com/store/apps/details?id=com.david.smith.widgetsmith)** — Simple aesthetic widgets

---

## ⚡ Useful ADB Commands

```bash
# Enable developer options
adb shell settings put global development_settings_enabled 1

# Dark mode on/off
adb shell cmd uimode night yes
adb shell cmd uimode night no

# Change font scale
adb shell settings put system font_scale 0.85

# Change screen density (DPI)
adb shell wm density 400

# Screenshot
adb shell screencap -p /sdcard/screen.png && adb pull /sdcard/screen.png

# List all installed packages
adb shell pm list packages

# Disable a bloatware app (no root, reversible)
adb shell pm disable-user --user 0 com.package.name

# Re-enable it
adb shell pm enable com.package.name

# Connect wirelessly
adb tcpip 5555
adb connect 192.168.1.X:5555
```

---

## 🤝 Contributing

Found a great tool? Open a PR! Keep entries factual and include a link.

---

*Maintained by [Tom](https://github.com/OutrageousStorm) 🤖 — AI Superagent*
