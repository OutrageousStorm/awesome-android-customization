# Troubleshooting Android Customization

Common issues and solutions when customizing Android.

## ROMs won't boot

**Symptom:** Device stuck on bootlogo after flashing ROM

**Causes & fixes:**
- Wrong ROM for device — verify device codename matches ROM filename
- Corrupted cache — wipe cache in recovery before flashing
- Vendor mismatch — use vendor.img from same build as system.img
- GApps incompatible — try without GApps first, then add compatible version
- Recovery issue — try flashing with `fastboot flash system system.img` instead

```bash
# Check device codename
adb shell getprop ro.product.device
```

---

## Bootloader locked, can't flash

**Symptom:** `FAILED (remote: Check 'Allow OEM unlock' in Developer Options)`

**Fixes:**
1. Enable "OEM Unlock" in Developer Options (Settings → About → tap Build Number 7x → Developer Options)
2. Make sure device is recognized: `adb devices`
3. Unlock with: `fastboot flashing unlock`
4. Accept the confirmation on device screen
5. Flash your ROM

---

## Screen freezes during setup

**Symptom:** Stuck on initial setup screen for 5+ minutes

**Causes:**
- Google Play Services crash loop
- Missing device firmware/modem
- RAM issues

**Fixes:**
- Skip Google setup: press Home key repeatedly
- Reinstall GApps from recovery
- Try ROM without GApps
- Restore from backup if available
- Check RAM: `adb shell cat /proc/meminfo | grep MemTotal`

---

## Battery drains immediately

**Symptom:** Phone dies in 30 minutes from full charge

**Causes:**
- Wakelock from bad app
- Aggressive doze not working
- Background data eating power
- WiFi/BT scanning always on

**Fixes:**
1. Check wakelocks: `adb bugreport && unzip bugreport.zip && cat FS/data/anr/traces.txt`
2. Disable WiFi scan always: `adb shell settings put global wifi_scan_always_enabled 0`
3. Force aggressive doze: `adb shell dumpsys deviceidle step deep`
4. Check app permissions and uninstall drainers
5. Use Battery Historian to visualize drain: https://bathist.ef.lc

---

## Apps keep crashing

**Symptom:** App crashes immediately or on specific action

**Causes:**
- Incompatible ROM/API level
- Missing library
- Corrupted cache

**Fixes:**
```bash
# View crash logs
adb logcat | grep FATAL

# Clear app cache
adb shell pm clear com.example.app

# Reinstall app
adb uninstall com.example.app
adb install app.apk

# Check API compatibility
aapt dump badging app.apk | grep sdkVersion
```

---

## Custom ROM won't receive OTAs

**Symptom:** "No updates available" or system update broken

**Reason:** Custom ROMs don't have OTA servers. You must manually flash each new version.

**How to update:**
1. Download new ROM zip
2. Boot to recovery
3. Flash ROM (usually wipes /data and /cache)
4. Keep Magisk by flashing after ROM

Or use **OTA survival method** on A/B devices:
```bash
adb reboot bootloader
fastboot boot TWRP.img
# In TWRP: Install → ROM zip → reboot (system stays installed)
```

---

## Magisk won't install or keeps uninstalling

**Symptom:** Magisk app disappears or modules don't load

**Fixes:**
1. Verify you patched the correct boot.img: `adb shell dumpsys package | grep magisk`
2. Check Zygisk enabled: open Magisk app → Settings → Zygisk
3. Try alternate install: patch via app, manually flash patched_boot.img
4. Disable all modules and reboot: `adb shell magisk --remove-modules`
5. Reflash latest Magisk APK: https://github.com/topjohnwu/Magisk/releases

---

## DenyList not working (apps detect root)

**Symptom:** Banking/Google Play thinks device is rooted despite DenyList

**Causes:**
- App uses advanced detection (SafetyNet/Play Integrity)
- Magisk version outdated
- Zygisk not enabled

**Fixes:**
1. Install **TrickyStore** + **PlayIntegrityFix** modules
2. Enable Zygisk in Magisk settings
3. Add app to DenyList via Magisk Manager
4. Reboot
5. Verify: run "SafetyNet Checker" app

---

## WiFi keeps disconnecting

**Symptom:** WiFi drops every few minutes

**Causes:**
- WiFi scanning disabled → enables → disables loop
- Bluetooth interference
- Power save aggressive

**Fixes:**
```bash
# Disable WiFi power save
adb shell settings put global wifi_scan_always_enabled 1
adb shell settings put global wifi_scan_interval_ms 15000

# Check for BT interference
adb shell dumpsys wifi | grep "PowerSave"

# Reset WiFi module
adb shell wpa_cli REASSOCIATE
```

---

## Device won't charge past 80%

**Symptom:** Stuck at 80% even when plugged in for hours

**Causes:**
- Battery health degraded
- Magisk ACC module limiting charge
- Kernel-level charge limit active

**Fixes:**
1. Check battery health: `adb shell dumpsys batterymanager | grep health`
2. Disable ACC if installed: Magisk → Modules → disable ACC → reboot
3. Remove charge limit: `adb shell settings delete global battery_saver_threshold`
4. Factory reset if persistent

---

## Performance is slow after ROM flash

**Symptom:** Lag, stutter, animation drops after clean ROM install

**Causes:**
- Indexing still running (Android rebuilds package index)
- SELinux in permissive mode (slower)
- CPU governor set to conservative

**Fixes:**
1. Wait 5-10 minutes for indexing to complete
2. Check SELinux: `adb shell getenforce` (should be "Enforcing")
3. Check CPU governor: `adb shell cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor`
   - If conservative, switch to schedutil: `adb shell "echo schedutil > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor"`
4. Disable animations in Developer Options

---

## Fingerprint sensor doesn't work

**Symptom:** Fingerprint always fails or not recognized

**Causes:**
- Custom ROM missing fingerprint HAL
- Vendor mismatch
- FPC/Goodix library missing

**Fixes:**
1. Try different ROM (one known to work on your device)
2. Extract vendor.img from original OTA and flash: `fastboot flash vendor vendor.img`
3. Enable SafetyNet checker to verify HALs are loaded
4. Use PIN/pattern as fallback

---

## No sound after ROM flash

**Symptom:** Speaker/mic completely silent or muted

**Causes:**
- Missing audio HAL
- AudioFlinger crash
- Bluetooth audio default selected but not connected

**Fixes:**
```bash
# Check audio service
adb shell dumpsys audio | grep -i "AudioFlinger"

# Reset audio to defaults
adb shell settings delete global bluetooth_sco_channel_7
adb shell am broadcast -a android.media.action.RESET_AUDIO_SETTINGS

# Check mic levels
adb shell settings put secure mic_mute 0
```

---

## Camera app crashes or won't open

**Symptom:** "Camera has stopped" error or app won't launch

**Causes:**
- Missing camera HAL
- GApps conflicts (Google Lens)
- Camera permission issues

**Fixes:**
1. Try AOSP Camera instead of OEM camera
2. Disable Google Lens: `adb shell pm disable com.google.android.googlequicksearchbox/com.google.android.apps.search.lens.LensActivity`
3. Reinstall GApps
4. Grant camera permission: `adb shell pm grant com.android.camera android.permission.CAMERA`

---

## Device reboots on its own

**Symptom:** Random reboots, especially during specific app use

**Causes:**
- Kernel panic (bad kernel)
- Overheating
- Wakelock keeping CPU active (battery monitoring triggers reboot)
- Bootloader issue

**Fixes:**
1. Check kernel logs: `adb logcat -b kernel | grep -i "panic\|died\|reboot"`
2. Try different kernel if using custom
3. Clear /cache: boot to recovery and wipe cache
4. Downgrade ROM if it just updated
5. Check temps: `adb shell cat /sys/class/thermal/thermal_zone0/temp`

---

## Google Play won't open or apps won't install

**Symptom:** "Your device isn't compatible" or Play Store crashes

**Causes:**
- Magisk flagged as rooted (Play Integrity)
- API level mismatch
- Signature mismatch

**Fixes:**
1. Install PlayIntegrityFix + TrickyStore modules
2. Verify API level: `adb shell getprop ro.build.version.sdk`
3. Reinstall GApps if needed
4. Clear Play Services data: `adb shell pm clear com.google.android.gms`
