# 📱 Awesome Android Customization

> A curated, AI-maintained list of the best tools, apps, ROMs, launchers, Shizuku tools, and ADB tricks for customizing your Android device.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Maintained by AI](https://img.shields.io/badge/Maintained%20by-AI%20🤖-blueviolet)](https://github.com/OutrageousStorm)
[![Last Updated](https://img.shields.io/badge/Updated-March%202026-brightgreen)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## 📚 Contents

- [🚀 Launchers](#-launchers)
- [🎨 Icon Packs](#-icon-packs)
- [🎭 Theming & Colors](#-theming--colors)
- [🔧 ADB Tools](#-adb-tools)
- [📡 Shizuku Apps (No Root!)](#-shizuku-apps-no-root)
- [🗑️ Debloating](#️-debloating)
- [📦 Custom ROMs](#-custom-roms)
- [🔑 Root Tools](#-root-tools)
- [🔒 Privacy & Security](#-privacy--security)
- [🖼️ Widgets & Wallpapers](#️-widgets--wallpapers)
- [📱 Per-Device Guides](#-per-device-guides)
- [⚡ ADB Cheat Sheet](#-adb-cheat-sheet)
- [🤖 Our Tools](#-our-tools)

---

## 🚀 Launchers

| App | Description | Stars | Price |
|-----|-------------|-------|-------|
| [Lawnchair](https://github.com/LawnchairLauncher/lawnchair) | Best open-source Pixel launcher clone with Material You | ⭐ 9k+ | Free |
| [Nova Launcher](https://novalauncher.com) | Most customizable, battle-tested launcher | — | Free / $5 |
| [Niagara Launcher](https://niagaralauncher.app) | Unique vertical alphabet scroll, minimal | — | Free / Premium |
| [Kvaesitso](https://github.com/MM2-0/Kvaesitso) | Search-first launcher, beautiful | ⭐ 2k+ | Free |
| [KISS Launcher](https://github.com/Neamar/KISS) | Minimalist, sub-100ms launches | ⭐ 3k+ | Free |
| [Taskbar](https://github.com/farmerbb/Taskbar) | Desktop-style taskbar & freeform windowing | ⭐ 2k+ | Free |
| [OLauncher](https://github.com/tanujnotes/Olauncher) | Minimal text-only launcher | ⭐ 2k+ | Free |
| [Ratio Launcher](https://play.google.com/store/apps/details?id=com.bllocosn) | Productivity-focused | — | Free |

---

## 🎨 Icon Packs

| Pack | Style | Link |
|------|-------|------|
| **Arcticons** ⭐ | Line art / minimal — massive library | [GitHub](https://github.com/Donnnno/Arcticons) |
| **Delta Icons** | Adaptive, Material You friendly | [GitHub](https://github.com/Delta-Icons/android) |
| **Lawnicons** | Official Lawnchair companion pack | [GitHub](https://github.com/LawnchairLauncher/lawnicons) |
| **Candycons** | Colorful, rounded | Play Store |
| **Whicons** | Clean white minimal | Play Store |
| **Pix-Pie** | Pixel-style round icons | Play Store |
| **Reev** | Thin line, elegant | Play Store |

---

## 🎭 Theming & Colors

| Tool | Description | Root? |
|------|-------------|-------|
| **[ColorBlendr](https://github.com/Mahmud0808/ColorBlendr)** ⭐ | Modify Material You colors device-wide | ❌ (Shizuku) |
| **[Repainter](https://repainter.app)** | Material You color palette customizer | ❌ |
| **[Substratum](https://github.com/substratum/substratum)** | Full system theme engine | ✅ Root |
| **[OmniStyle](https://forum.xda-developers.com)** | Pixel theme engine mod | ✅ Root |
| **[Iconify](https://github.com/Mahmud0808/Iconify)** ⭐ | UI mods without root via Shizuku | ❌ (Shizuku) |
| **[zFont 3](https://play.google.com/store/apps/details?id=com.htetznaing.zfont2)** | System-wide font changer | ❌ (Shizuku) |
| **[CarrierVanityName](https://github.com/nullbytepl/CarrierVanityName)** | Custom carrier name | ❌ (Shizuku) |
| **[Android Monet](https://github.com/topics/monet)** | Material You / Monet theming tools | Various |

---

## 🔧 ADB Tools

| Tool | Description | Platform |
|------|-------------|----------|
| **[android-adb-toolkit](https://github.com/OutrageousStorm/android-adb-toolkit)** ⭐ | Web GUI: debloat, tweak, backup — all in one | Web |
| **[android-tweaks-toolkit](https://github.com/OutrageousStorm/android-tweaks-toolkit)** ⭐ | ADB tweaks: DPI, dark mode, battery, fonts | CLI |
| **[android-permission-auditor](https://github.com/OutrageousStorm/android-permission-auditor)** ⭐ | Audit every app for dangerous permissions | Python CLI |
| **[pixel-battery-historian](https://github.com/OutrageousStorm/pixel-battery-historian)** ⭐ | Battery drain visualizer via ADB | Python CLI |
| **[android-backup-vault](https://github.com/OutrageousStorm/android-backup-vault)** ⭐ | One-command backup: APKs, photos, SMS, contacts | Bash |
| **[Scrcpy](https://github.com/Genymobile/scrcpy)** | Screen mirror and control via ADB/USB/WiFi | All platforms |
| **[ADB AppControl](https://adbappcontrol.com)** | GUI app manager with backup features | Windows |
| **[Wifi ADB - Debug Over Air](https://play.google.com/store/apps/details?id=com.ttxapps.wifiadb)** | Enable ADB over WiFi from your phone | Android |
| **[aShell](https://gitlab.com/sunilpaulmathew/ashell)** | ADB shell on the device itself via Shizuku | Android |

---

## 📡 Shizuku Apps (No Root!)

> [Shizuku](https://github.com/RikkaApps/Shizuku) lets apps use system APIs with ADB-level privileges — no root required. **This is the future of Android power-user tools.**

**Quick setup:** Install Shizuku → Enable Wireless Debugging → Start Shizuku service → Install apps below.

### Essential Shizuku Apps

| App | What It Does |
|-----|-------------|
| **[Canta](https://github.com/samolego/Canta)** ⭐ | Debloat your phone on-device, no PC needed |
| **[AppManager](https://github.com/MuntashirAkon/AppManager)** ⭐ | Advanced package manager, block components, audit permissions |
| **[ColorBlendr](https://github.com/Mahmud0808/ColorBlendr)** ⭐ | Full Material You color control |
| **[Iconify](https://github.com/Mahmud0808/Iconify)** | Customize system UI elements without root |
| **[TapTap](https://github.com/KieronQuinn/TapTap)** | Back-of-phone tap gestures (Pixel feature, any device) |
| **[Smartspacer](https://github.com/KieronQuinn/Smartspacer)** | Fully custom glanceable widgets |
| **[Geto](https://github.com/JackEblan/Geto)** | Auto-change settings when apps open |
| **[DSU Sideloader](https://github.com/VegaBobo/DSU-Sideloader)** | Flash GSIs without unlocking bootloader |
| **[Obtainium](https://github.com/ImranR98/Obtainium)** ⭐ | Get app updates from source (GitHub, GitLab, etc.) |
| **[Language-Selector](https://github.com/VegaBobo/Language-Selector)** | Per-app language overrides |
| **[Blocker](https://github.com/lihenggui/blocker)** | Block individual app components (services, receivers) |
| **[ShizuTools](https://github.com/legendsayantan/ShizuTools)** | Collection of Shizuku-powered utilities |

📂 Full Shizuku app list: [shizuku-apps-root-alternative](https://github.com/OutrageousStorm/shizuku-apps-root-alternative)

---

## 🗑️ Debloating

| Tool | Platform | Highlights |
|------|----------|------------|
| **[UAD-NG](https://github.com/Universal-Debloater-Alliance/universal-android-debloater-next-generation)** ⭐ | Desktop (Rust) | 6k⭐ — the gold standard, safe package DB |
| **[Canta](https://github.com/samolego/Canta)** ⭐ | Android (Shizuku) | On-device, uses UAD-NG's package lists |
| **[android-adb-toolkit](https://github.com/OutrageousStorm/android-adb-toolkit)** | Web | Device-specific debloat profiles |
| **[android-tv-debloat-toolkit](https://github.com/OutrageousStorm/android-tv-debloat-toolkit)** | CLI | Android TV specific |
| **[samsung-debloat-script](https://github.com/fadelhbr/samsung-debloat-script)** | Bash | Samsung focused |
| **[Fire-Tools](https://github.com/mrhaydendp/Fire-Tools)** | Bash | Amazon Fire tablets |
| **[android-debloat-list](https://github.com/MuntashirAkon/android-debloat-list)** | Reference | Comprehensive package safety database |

### Safe-to-Remove Packages (Universal)

```bash
# Samsung bloat
adb shell pm disable-user --user 0 com.samsung.android.bixby.agent
adb shell pm disable-user --user 0 com.samsung.android.app.tips
adb shell pm disable-user --user 0 com.samsung.android.game.gametools

# Google bloat
adb shell pm disable-user --user 0 com.google.android.apps.tachyon   # Google Duo
adb shell pm disable-user --user 0 com.google.android.apps.subscriptions.red  # YouTube Music

# Carrier bloat (check your carrier)
adb shell pm disable-user --user 0 com.vzw.hss.myverizon
adb shell pm disable-user --user 0 com.att.myWireless
```

---

## 📦 Custom ROMs

| ROM | Base | Highlights | Best For |
|-----|------|------------|---------|
| **[LineageOS](https://lineageos.org)** | AOSP | Most device support, stable, active | Daily driver |
| **[GrapheneOS](https://grapheneos.org)** | AOSP | Maximum privacy/security, Pixel only | Privacy first |
| **[CalyxOS](https://calyxos.org)** | AOSP | Privacy + microG, user-friendly | Privacy + usability |
| **[PixelExperience](https://get.pixelexperience.org)** | Pixel UI | Pixel features on any device | Pixel feel |
| **[crDroid](https://crdroid.net)** | LineageOS | Heavy customization options | Tweakers |
| **[ProtonAOSP](https://github.com/ProtonAOSP)** | AOSP | Performance & clean | Speed |
| **[ArrowOS](https://arrowos.net)** | AOSP | Minimalist, clean | Simple + fast |
| **[DerpFest](https://derpfest.org)** | AOSP | Fun features + stable | Feature lovers |

---

## 🔑 Root Tools

| Tool | Description | Notes |
|------|-------------|-------|
| **[Magisk](https://github.com/topjohnwu/Magisk)** ⭐ | Standard root solution + module framework | 45k⭐ |
| **[KernelSU](https://github.com/tiann/KernelSU)** | Kernel-level root, harder to detect | Growing fast |
| **[APatch](https://github.com/bmax121/APatch)** | Kernel-based alternative to Magisk | New in 2025 |
| **[LSPosed](https://github.com/LSPosed/LSPosed)** ⭐ | Xposed framework on Magisk | Module ecosystem |
| **[Shamiko](https://github.com/LSPosed/LSPosed.github.io)** | Hide root from apps | Magisk companion |
| **[Zygisk-Next](https://github.com/Dr-TSNG/ZygiskNext)** | Standalone Zygisk for KernelSU | |

### Best Magisk Modules 2026

| Module | What It Does |
|--------|-------------|
| **Pixelify** | Enable Pixel-exclusive features on any ROM |
| **ViPER4Android** | System-wide audio enhancement |
| **Universal SafetyNet Fix** | Pass Google Play Integrity |
| **Systemless Hosts** | System-wide ad blocking |
| **MagiskHide Props Config** | Spoof device fingerprint |
| **Riru** | Inject code into Zygote process |

---

## 🔒 Privacy & Security

| Tool | Description | Root? |
|------|-------------|-------|
| **[GrapheneOS](https://grapheneos.org)** | Most secure Android — hardware-backed | ROM |
| **[android-permission-auditor](https://github.com/OutrageousStorm/android-permission-auditor)** ⭐ | Audit all app permissions via ADB | ❌ |
| **[AppManager](https://github.com/MuntashirAkon/AppManager)** | Block trackers, audit components | ❌ (Shizuku) |
| **[Blocker](https://github.com/lihenggui/blocker)** | Block app components individually | ❌ (Shizuku) |
| **[TrackerControl](https://github.com/TrackerControl/tracker-control-android)** | Monitor & block network trackers | ❌ |
| **[NetGuard](https://github.com/M66B/NetGuard)** | Per-app firewall, no root | ❌ |
| **[AFWall+](https://github.com/ukanth/afwall)** | Iptables-based firewall | ✅ Root |
| **[Exodus Privacy](https://reports.exodus-privacy.eu.org)** | Check trackers in any app | Web |

---

## 🖼️ Widgets & Wallpapers

| App | Type | Notes |
|-----|------|-------|
| **[KWGT](https://play.google.com/store/apps/details?id=org.kustom.widget)** | Widget maker | Fully custom, huge community |
| **[KLWP](https://play.google.com/store/apps/details?id=org.kustom.wallpaper)** | Live wallpaper maker | Wildly customizable |
| **[Smartspacer](https://github.com/KieronQuinn/Smartspacer)** | Custom At-a-Glance / Smartspace | Pixel feature, any device |
| **[WallMan](https://github.com/Bnyro/WallMan)** | FOSS wallpaper app | Multiple sources |
| **[Dumbwallpaper](https://github.com/hashicorp/dumbwallpaper)** | Minimalist solid color wallpapers | |
| **[Muzei](https://github.com/muzei/muzei)** | Rotating art wallpapers | |
| **[WidgetsPro](https://play.google.com/store/apps/details?id=com.ticktick.widget)** | Battery & CPU widgets | Shizuku enhanced |

---

## 📱 Per-Device Guides

### Pixel
- [Pixel debloat list](https://github.com/MuntashirAkon/android-debloat-list) — community maintained
- [essentials for Pixel](https://github.com/rushiranpise/essentials) — must-have Pixel tweaks via Shizuku
- [Pixelify Magisk module](https://github.com/Kingsman44/Pixelify) — Pixel UI features on other devices

### Samsung (One UI)
- [Galaxy debloat scripts](https://github.com/Tom4tot/Galaxy-S24-Debloat-Script)
- [GoodLock modules](https://www.samsung.com/us/apps/good-lock/) — official Samsung customization suite
- [SoundAssistant via GoodLock](https://galaxystore.samsung.com) — per-app volume

### Xiaomi / HyperOS
- Disable MIUI optimization: `adb shell setprop persist.sys.dalvik.vm.lib.2 libart.so`
- [MultiLocale](https://github.com/JeelsBoobies/MultiLocale) — add missing languages
- MiXplorer — best file manager for MIUI

### OnePlus / OxygenOS
- OPlus extras via ADB: enable hidden features
- [OnePlus debloat list](https://github.com/MuntashirAkon/android-debloat-list)

---

## ⚡ ADB Cheat Sheet

```bash
# ── Setup ─────────────────────────────────────────
adb devices                           # List connected devices
adb tcpip 5555 && adb connect IP:5555 # Wireless ADB

# ── Display ───────────────────────────────────────
adb shell wm density 420              # Change DPI
adb shell wm density reset            # Reset DPI
adb shell wm size 1080x2340           # Force resolution
adb shell wm size reset               # Reset resolution
adb shell settings put system font_scale 0.9  # Font size

# ── Dark Mode ────────────────────────────────────
adb shell cmd uimode night yes        # Dark mode on
adb shell cmd uimode night no         # Dark mode off

# ── Battery & Performance ─────────────────────────
adb shell dumpsys battery set level 100        # Fake battery %
adb shell settings put global animator_duration_scale 0.5  # Faster animations
adb shell settings put global transition_animation_scale 0.5
adb shell settings put global window_animation_scale 0.5

# ── Debloating ───────────────────────────────────
adb shell pm list packages -3         # List third-party apps
adb shell pm disable-user --user 0 com.pkg  # Disable (reversible)
adb shell pm enable com.pkg           # Re-enable
adb shell pm uninstall --user 0 com.pkg      # Remove for current user

# ── Privacy ──────────────────────────────────────
adb shell pm revoke com.pkg android.permission.ACCESS_FINE_LOCATION
adb shell appops set com.pkg android:camera deny

# ── Misc ─────────────────────────────────────────
adb shell screencap -p /sdcard/ss.png && adb pull /sdcard/ss.png
adb shell screenrecord --time-limit 30 /sdcard/video.mp4
adb shell dumpsys battery             # Battery info
adb shell getprop ro.build.version.release  # Android version
```

---

## 🤖 Our Tools

Tools in this ecosystem, all no-root, all open source:

| Repo | What It Does |
|------|-------------|
| [android-adb-toolkit](https://github.com/OutrageousStorm/android-adb-toolkit) | Web GUI for ADB — debloat, tweak, backup |
| [android-tweaks-toolkit](https://github.com/OutrageousStorm/android-tweaks-toolkit) | CLI tweaks: DPI, dark mode, battery, fonts |
| [android-permission-auditor](https://github.com/OutrageousStorm/android-permission-auditor) | Permission scanner with HTML report |
| [pixel-battery-historian](https://github.com/OutrageousStorm/pixel-battery-historian) | Battery drain visualizer |
| [android-backup-vault](https://github.com/OutrageousStorm/android-backup-vault) | Full backup: APKs, media, SMS, contacts |
| [shizuku-apps-root-alternative](https://github.com/OutrageousStorm/shizuku-apps-root-alternative) | 180+ curated Shizuku app list |
| [android-tv-debloat-toolkit](https://github.com/OutrageousStorm/android-tv-debloat-toolkit) | Android TV debloater |
| [awesome-android-customization](https://github.com/OutrageousStorm/awesome-android-customization) | This list |

---

## 🤝 Contributing

Found something missing? Open a PR!
- Add entries alphabetically within categories
- Include a working link and short description
- Mark FOSS tools with their license if known

---

*Maintained by [Tom](https://github.com/OutrageousStorm) 🤖 — AI Superagent | March 2026*
