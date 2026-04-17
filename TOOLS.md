# Android Customization Tools

## GUI Tools
- **Launcher:** Nova Prime, Lawnchair, Poco, Niagra (minimal)
- **Icon packs:** Linebit, Glim, Cryos, Oreo Adapticons
- **Wallpaper:** Walli, Backdrops, Muzei, Kustom Live Wallpaper
- **Themes:** Flux, DarQ (per-app dark mode), Substratum (needs ROM)
- **Clock/lock:** Always On AMOLED, HyperOS AOD, Glimpse Notifications

## Customization via ADB (no root)
```bash
# Change system font (requires ROM support)
adb shell settings put secure font_size 120

# Disable Google Assistant
adb shell settings put secure google_assistant_disabled_notification 1

# Force dark mode (Android 10+)
adb shell settings put secure ui_night_mode 2

# Reduce animation speed (faster UI)
adb shell settings put global animator_duration_scale 0.5
```

## with Magisk modules
- **Gboard themes:** custom Gboard layouts + colors
- **Status bar mods:** hide icons, change background color
- **Quick settings layout:** custom QS tiles order
- **Navbar customization:** hide buttons, custom layout

## Web/Browser Tools
- **Favicon finder:** https://icons.duckduckgo.com/ip/ — get favicons for URLs
- **Wallpaper tools:** https://unsplash.com, https://pexels.com
- **Color picker:** https://chir.ag/projects/ntg/ — extract theme colors
