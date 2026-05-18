# Power Users Guide

Advanced Android customization for experienced users.

## System-level tweaks

### Kernel modules
Install custom kernel modules via Magisk:
```bash
# Create module structure
mkdir -p /path/to/module/system/lib/modules
# Add .ko files
# Create module.prop with id, name, version
adb push /path/to/module /sdcard/
# Install via Magisk
```

### Init.d scripts (Magisk)
Place scripts in `post-fs-data.sh` or `service.sh`:
```bash
# /data/adb/modules/mymodule/post-fs-data.sh
#!/system/bin/sh
# Runs early boot, before system mounts
```

### sysctl tweaks
Modify kernel parameters at runtime:
```bash
adb shell "echo 'vm.swappiness=10' >> /system/etc/sysctl.conf"
# Requires remount or Magisk override
```

## Advanced app theming

### Material You dynamic colors (Android 12+)
Force Material You on unsupported apps:
```bash
# Via Xposed/LSPosed: Hook ColorUtils.getColorForHWB()
# Via ADB: Force WALLPAPER_COLORS_HINT in dumpsys
```

### Overlay system (OverlayFS)
Create system UI overlays without modifying /system:
```bash
adb shell mkdir -p /system/product/overlay
adb push CustomUI.apk /system/product/overlay/
# Requires remount or custom kernel
```

## Performance tuning

### CPU scaling governors
```bash
# Check available governors
adb shell cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_available_governors

# Set performance governor (gaming)
adb shell "echo performance > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor"

# Set powersave (battery mode)
adb shell "echo powersave > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor"

# Interactive governor (default, balanced)
adb shell "echo interactive > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor"
```

### I/O scheduler
```bash
# Check available schedulers
adb shell cat /sys/block/mmcblk0/queue/scheduler

# Set to CFQ (fairness)
adb shell "echo cfq > /sys/block/mmcblk0/queue/scheduler"

# Set to deadline (latency-sensitive)
adb shell "echo deadline > /sys/block/mmcblk0/queue/scheduler"
```

### RAM disk tuning
```bash
# Increase dirty ratio for faster writes (use with caution)
adb shell "echo 50 > /proc/sys/vm/dirty_ratio"

# Reduce swappiness (prefer RAM over swap)
adb shell "echo 10 > /proc/sys/vm/swappiness"
```

## Network optimization

### TCP window scaling
```bash
adb shell "echo 1 > /proc/sys/net/ipv4/tcp_window_scaling"
```

### TCP buffer sizes
```bash
adb shell "echo '87380 131072 262144' > /proc/sys/net/ipv4/tcp_rmem"
adb shell "echo '16384 131072 262144' > /proc/sys/net/ipv4/tcp_wmem"
```

## Custom kernel builds

See [android-kernel-guide](https://github.com/OutrageousStorm/android-kernel-guide) for full compilation walkthrough.

## Resources
- [Magisk Module Development](https://topjohnwu.github.io/Magisk/)
- [Android Kernel source](https://android.googlesource.com/)
- [Linux kernel docs](https://www.kernel.org/doc/)
