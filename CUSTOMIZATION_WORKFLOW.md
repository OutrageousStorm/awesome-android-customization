# Android Customization Workflow Guide

## Beginner (Stock Android)
```
1. Pick a launcher (Lawnchair or Niagara recommended)
2. Install from Play Store
3. Set as default: Settings → Apps → Default apps → Home app
4. Customize home screen grid, icon size, gesture
```

## Intermediate (De-Google + Custom ROMs)
```
1. Unlock bootloader (device-specific)
2. Flash TWRP recovery
3. Flash custom ROM (LineageOS or crDroid)
4. Flash GApps or use microG
5. Install Magisk for root modules
6. Enable Zygisk for deep system tweaks
7. Install launcher + widgets + themes
```

## Advanced (Full Control)
```
1. Custom ROM (LineageOS or GrapheneOS)
2. Magisk + LSPosed for app-level control
3. Xposed modules (Iconify, Hide My AppList, etc.)
4. Custom kernel with frequency scaling
5. Battery optimization modules (GMS Doze, ACC)
6. ADB tweaks for network/telemetry hardening
```

---

## Tool Chain by Use Case

### Privacy
- Custom ROM: GrapheneOS, CalyxOS, or LineageOS
- Root: Magisk + PlayIntegrityFix + TrickyStore
- App control: LSPosed + Hide My AppList + XPrivacyLua
- Network: Private DNS (quad9.net) + NetGuard + Tor

### Gaming
- Custom kernel with performance governor
- Magisk modules: GMS Doze, battery limiter
- Launcher: Niagara or Pixel Launcher (low overhead)
- Settings: 90fps cap, minimal background apps

### Battery Life
- Universal GMS Doze module
- Battery limiter (charge to 80%)
- Aggressive doze + WiFi scanning off
- Low brightness theme + dark OLED
- Kill tracker background processes

### Look & Feel
- Launcher: Nova or Lawnchair
- Icon pack: Crayon, Lyan, Arcticons
- Widget pack: KWGT, Zooper Pro
- Font: Custom fonts via Magisk
- Accent color: Iconify (Material You colors)
