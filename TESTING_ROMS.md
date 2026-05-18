# Testing Custom ROMs

Guide for safely testing ROMs before committing.

## Pre-test setup

```bash
# Backup current system
adb shell pm list packages -3 > backup_packages.txt
adb bugreport > backup_bugreport.zip

# Save boot.img for quick recovery
adb pull /dev/block/by-name/boot stock_boot.img
```

## Test priority checklist

- [ ] Boot completes without loops
- [ ] All main radios work (WiFi, BT, cellular)
- [ ] Screen rotation + display scaling
- [ ] Camera (both front + rear)
- [ ] Audio playback + microphone
- [ ] Touch response + haptics
- [ ] Battery drain in idle
- [ ] SafetyNet / Play Integrity pass
- [ ] OTA update check works
- [ ] Daily app usage (Gmail, Maps, banking)

## Quick rollback

```bash
# If bootloop:
adb reboot bootloader
fastboot flash boot stock_boot.img
fastboot reboot

# Or via recovery:
adb reboot recovery
# Flash original ROM zip via TWRP
```

## Report template

For issues, include:
- Device model + Android version
- ROM version + build date
- Exact steps to reproduce
- `adb logcat` output around the error
- Screenshot or video if applicable
