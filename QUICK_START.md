# Quick Start — Android Customization in 5 Minutes

## Level 1: No Root Required
```bash
# Enable USB debugging
Settings → Developer Options → USB Debugging

# Download ADB
# Mac: brew install android-platform-tools
# Linux: sudo apt install adb

# Connect and debloat
adb devices
adb shell pm list packages -3  # list installed apps
adb shell pm uninstall -k --user 0 com.facebook.katana  # uninstall Facebook
```

## Level 2: Custom ROM (1 hour)
1. Unlock bootloader: `adb reboot bootloader` + `fastboot flashing unlock`
2. Flash TWRP recovery: `fastboot flash recovery twrp.img`
3. Boot recovery, install LineageOS zip
4. Reboot → clean stock Android

## Level 3: Magisk Root (30 minutes)
1. Flash Magisk via TWRP recovery
2. Install modules: Magisk Manager → Browse → PlayIntegrityFix
3. Reboot → enjoy root

See [android-rom-guide](https://github.com/OutrageousStorm/android-rom-guide) for detailed walkthrough.
