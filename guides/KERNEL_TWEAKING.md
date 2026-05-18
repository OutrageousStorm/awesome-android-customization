# Kernel Tweaking for Android

Advanced kernel parameter tuning — CPU governors, I/O schedulers, thermal management.

## Safe tweaks (root required)

### CPU Governor Selection
```bash
# Interactive (default, balanced)
adb shell "echo interactive > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor"

# Performance (max speed, high battery drain)
adb shell "echo performance > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor"

# Powersave (max battery, slower performance)
adb shell "echo powersave > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor"

# Schedutil (modern, kernel-driven)
adb shell "echo schedutil > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor"
```

### I/O Scheduler Tweaks
```bash
# List available schedulers
adb shell cat /sys/block/mmcblk0/queue/scheduler

# Switch to CFQ (fair queuing)
adb shell "echo cfq > /sys/block/mmcblk0/queue/scheduler"

# Switch to deadline (low latency)
adb shell "echo deadline > /sys/block/mmcblk0/queue/scheduler"

# Reduce queue depth for lower latency
adb shell "echo 32 > /sys/block/mmcblk0/queue/nr_requests"
```

### Thermal Management
```bash
# Disable thermal throttling (risky — can damage device)
# adb shell "echo 0 > /sys/module/msm_thermal/parameters/enabled"

# Check thermal zones
adb shell "cat /sys/class/thermal/thermal_zone*/temp | head -5"

# Set passive cooling threshold (in millidegrees)
adb shell "echo 60000 > /sys/class/thermal/thermal_zone0/trip_point_0_temp"
```

### Memory & Swap
```bash
# Check memory pressure
adb shell "cat /proc/pressure/memory"

# Increase VFS cache (for faster I/O)
adb shell "echo 50 > /proc/sys/vm/vfs_cache_pressure"

# Tune swappiness (0-100, lower = less swap)
adb shell "echo 10 > /proc/sys/vm/swappiness"
```

## Tools for tweaking
- **Kernel Auditor** — read/write kernel params via GUI
- **Franco Kernel Manager** — advanced kernel tuning + profiles
- **Magisk Universal Init.d** — auto-run tweaks on boot

## Disclaimer
Kernel tweaks can **brick your device** if done wrong. Always test one change at a time.
