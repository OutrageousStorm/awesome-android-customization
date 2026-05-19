# Android 16 Preview & Customization

Android 16 (2025 release) brings new customization surfaces and modding opportunities.

## New Features

### Adaptive Battery 2.0
AI-driven battery management that learns your usage patterns.

```bash
# Force disable for testing (breaks Doze)
adb shell settings put global adaptive_battery_management_enabled 0

# View battery threshold
adb shell dumpsys battery | grep adaptive
```

### Per-App Locale Override
Android 13+ feature expanded in Android 16 — change language per-app without rooting.

```bash
# Set app to Japanese
adb shell cmd locale set-app-locales com.example.app ja-JP

# Reset to system locale
adb shell cmd locale set-app-locales com.example.app --reset
```

### Partial Screen Record
Record audio from specific apps, not system.

```bash
# Record with selected app audio only
adb shell cmd media.metrics record_screen --media-source "com.spotify.music"
```

### Enhanced Theming
Material You themes now support:
- Custom accent colors (not just wallpaper-derived)
- Per-app theme overrides
- Dark mode scheduling

```bash
# Apply custom theme color (hex)
adb shell cmd theme set_accent "#FF6200EE"

# Save theme preset
adb shell settings put secure theme_preset_name "CustomDark"
```

## New Customization Hooks

### Lockscreen Clock Styles
More clock face options available via overlays.

```bash
# List available clock styles
adb shell pm list features | grep lockscreen

# Change via secure settings
adb shell settings put secure lock_screen_custom_clock_face "analog_minimal"
```

### Quick Settings Reordering
Full control over QS tile order via System UI Tuner.

```bash
adb shell settings put secure qs_tiles "wifi,bt,dnd,flashlight,rotation,battery,cast,soundsearch,airplane,hotspot"
```

## Magisk & LSPosed in Android 16

- **KernelSU** gaining adoption — systemless root without modifying boot
- **LSPosed** modules work but Android 16 restricts certain hooks
- **Play Integrity bypass** harder — TrickyStore + CorePatch combo needed

## Custom ROM Status

- LineageOS 23 (Android 16 base) in alpha
- GrapheneOS porting in progress
- crDroid waiting for stable LineageOS upstream
