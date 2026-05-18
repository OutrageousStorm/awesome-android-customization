# Battery Hacks & Optimization

Squeeze every drop from your Android battery without sacrificing usability.

## Aggressive doze on screen off

```bash
adb shell dumpsys deviceidle step deep
adb shell dumpsys deviceidle step deep
```

Runs every time screen turns off. Pair with automation script.

## Limit background syncs

Only Facebook, Gmail, and essential apps should auto-sync. Disable for everything else:

```bash
adb shell settings put global background_data_limit_mb_per_day 100
```

## CPU scaling governor

Switch to powersave when not gaming:

```bash
# Check current
adb shell "cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor"

# Set powersave (if supported)
adb shell "echo powersave | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor"
```

## Screen brightness curve

Reduce brightness boost during full sun — saves more than you'd think.

Most ROMs don't expose this, but if you have a custom kernel:

```bash
# Check if brightness is limited
adb shell settings get system screen_brightness

# Manual limit (persistent)
adb shell settings put system screen_brightness 180
```

## Game mode profile

For gaming sessions, create a profile that:
- Locks CPU to performance governor
- Disables WiFi scanning
- Locks screen on
- Disables auto-sync

Then switch back after gaming.

## Wakelocks to watch

Apps that hold wakelocks even when in Doze:

- Google Play Services (unless in Doze properly)
- Facebook
- Snapchat
- TikTok
- Any app with its own HTTP sync daemon

Use **LSPosed Universal GMS Doze** to force these into deep sleep.

## Battery saver mode limits

Android's "Battery saver" or "Low power mode":

```bash
# Enable
adb shell settings put global low_power_mode 1

# Check threshold (default 15%)
adb shell settings get global low_power_mode_trigger_level
```

## Screen timeout cascade

```bash
# 30s on battery, 5m on AC
adb shell settings put secure screen_off_timeout 30000  # battery
# Need to detect AC separately and use Tasker for auto-switching
```

---

**Most effective single change:** Put GMS into Doze via Magisk module + screen timeout 60s. Gains 20-30% extra SOT.
