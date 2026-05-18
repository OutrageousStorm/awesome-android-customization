# Android 15+ Features & Customization Guide

Quick reference for Android 15 features and how to customize them via ADB.

## Android 15 (2024)
- **Per-app language** — set different language for each app independently
- **Ultra HDR photography** — capture 10-bit HDR photos with better colors
- **Spatial audio** — 3D audio support in compatible apps
- **Scheduled power off** — device automatically powers down at set time
- **Private Space** — hidden, biometric-locked app folder
- **Rich clipboard** — paste images, documents, formatted text

### Enable via ADB
```bash
# Private Space (show in launcher)
adb shell pm enable-user com.android.systemui/.settings.PrivateSpaceSettings

# Per-app language (change language for WhatsApp to Japanese)
adb shell cmd locale set-app-locale com.whatsapp ja-JP

# Enable Ultra HDR mode
adb shell settings put global enable_ultra_hdr 1

# Scheduled power off (10 PM)
adb shell settings put secure power_off_time 22:00
```

## Android 14 (2023)
- Material You 2.0 dynamic theming
- Per-app volume control
- Enhanced notification grouping
- Passkey support for passwordless auth

### Customize Android 14
```bash
# Apply system-wide Material You colors
adb shell cmd overlay enable-all com.android.theme.icon.adaptive

# Enable per-app volume
adb shell settings put system per_app_volume_enabled 1
```

## Hidden Settings (Android 14+)
```bash
# Adaptive battery (learns usage patterns)
adb shell settings put global adaptive_battery_management_enabled 1

# Force high refresh rate (disable adaptive)
adb shell settings put secure min_refresh_rate 90
adb shell settings put secure peak_refresh_rate 90

# Faster UI animations
adb shell settings put global transition_animation_scale 0.5
```
