# Android Tweaks & System Mods

Tweaks that modify Android behavior without flashing a custom ROM.

## Magisk Modules (Root)

| Module | Effect | Source |
|--------|--------|--------|
| Universal GMS Doze | Forces Google Play Services into aggressive doze | Magisk Repo |
| PlayIntegrityFix | Passes Play Integrity API checks on rooted devices | [GitHub](https://github.com/chiteroman/PlayIntegrityFix) |
| Shamiko | Advanced root hiding via Zygisk | [GitHub](https://github.com/LSPosed/Shamiko) |
| BootloaderSpoofer | Reports locked bootloader to apps | [GitHub](https://github.com/chiteroman/BootloaderSpoofer) |
| Riru-LocationReporter | Fake GPS location system-wide | XDA Forum |

## LSPosed Hooks (Requires LSPosed + Magisk)

| Module | Effect |
|--------|--------|
| Hide My AppList | Prevent apps from detecting other installed apps |
| TrickyStore | Hardware attestation spoofing for banking apps |
| DisableFlagSecure | Allow screenshots in restricted apps |
| XPrivacyLua | Fine-grained permission restrictions |

## ADB-Only (No Root)

```bash
# Kill system telemetry
adb shell pm disable-user --user 0 com.google.android.gms.analytics

# Aggressive doze for background apps
adb shell cmd appops set --all RUN_IN_BACKGROUND deny

# Disable ad tracking
adb shell settings put global limit_ad_tracking 1

# Restrict location
adb shell settings put secure location_mode 0
```

## Battery Tweaks

| Tweak | Command |
|-------|---------|
| Disable WiFi scanning | `adb shell settings put global wifi_scan_always_enabled 0` |
| Disable BLE scanning | `adb shell settings put global ble_scan_always_enabled 0` |
| Reduce screen timeout | `adb shell settings put system screen_off_timeout 60000` |
| Disable always-on display | Custom ROM setting or Shizuku |

## Performance Tweaks

| Tweak | Effect |
|-------|--------|
| GPU rendering | Settings → Developer Options → Force GPU rendering |
| Animation scale | Set to 0.5x for snappier feel |
| Show GPU rendering | Developer → Show GPU overdraw |
