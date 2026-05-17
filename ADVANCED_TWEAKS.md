# Advanced Android Tweaks

Deep system modifications for power users. Requires root or Shizuku.

## System partition tweaks

### Disable carrier WiFi offload
```bash
adb shell settings put global wifi_on_when_proxy_set 0
adb shell settings put global http_proxy ""
```

### Aggressive memory management
```bash
adb shell settings put global PSS_MIN_CHANGE_FORCE_GC 100
adb shell settings put global KERNEL_LOG_SIZE 262144
```

### Force 90Hz/120Hz on all apps
```bash
# Pixel devices
adb shell settings put system min_refresh_rate 90
adb shell settings put system peak_refresh_rate 120

# Force refresh rate globally
adb shell settings put secure user_preferred_refresh_rate 120
```

## Battery optimizations (advanced)

### Disable motion sensors when screen off
```bash
# Only sensors that drain battery
adb shell settings put global sensor_use_when_display_off 0
adb shell am force-stop com.google.android.sensorglass
```

### CPU governor tweaks (rooted)
```bash
# Set to powersave when unplugged
echo "powersave" | su -c 'tee /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor'
```

### Thermal throttling (rooted — risky!)
```bash
# Check current throttle point
cat /sys/module/msm_thermal/parameters/throttling_temp_degC
# Raise to 50°C (default 50°C) — use with caution
echo 50 | su -c 'tee /sys/module/msm_thermal/parameters/throttling_temp_degC'
```

## Display hacks

### Enable highest resolution if available
```bash
# List resolutions
adb shell wm density

# Set to 560 DPI (very sharp)
adb shell wm density 560
```

### Disable blue light filter at night (alternative to Night Light)
```bash
adb shell settings put secure screen_night_light_color_temperature 5000
```

### Force dark mode system-wide
```bash
adb shell settings put secure ui_night_mode 2
```

## Network tweaks

### Force IPv6 in apps
```bash
adb shell settings put secure ipv6_preferred 1
```

### DNS over HTTPS hardening
```bash
# Google DoH
adb shell settings put global private_dns_specifier dns.google

# Quad9
adb shell settings put global private_dns_specifier dns.quad9.net
```

### Disable IPv4 fallback (force DNS-only IPv6)
```bash
adb shell settings put global ipv4_fallback_disabled 1
```

## Dangerous tweaks ⚠️

### Enable ADB over network permanently
```bash
adb shell settings put global adb_enabled 1
adb shell setprop service.adb.tcp.port 5555
adb shell stop adbd && sleep 1 && adb shell start adbd
```

### Disable signature verification (CorePatch + Magisk only)
```bash
# Requires CorePatch module
# Allows installing modified APKs without resignation
```

### Disable SELinux (rooted)
```bash
su -c 'setenforce 0'  # permissive mode
# WARNING: this breaks security hardening — temp only
```

## Hidden developer options

```bash
# Extended power menu (Power, Restart, Advanced, Emergency SOS, etc.)
adb shell settings put secure advanced_power_menu_enabled 1

# Show touch feedback
adb shell settings put system show_touches 1

# Full gesture logging
adb shell settings put secure debug_gesture_input 1

# Enable wireless debugging from boot (some devices)
adb shell settings put global adb_wifi_enabled 1
```

---

⚠️ **Use at your own risk.** These tweaks can break functionality, drain battery faster, or cause security issues. Test in a safe environment first.
