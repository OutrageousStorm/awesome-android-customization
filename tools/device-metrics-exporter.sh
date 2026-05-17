#!/bin/bash
# device-metrics-exporter.sh -- Export detailed device metrics to JSON
# Usage: ./device-metrics-exporter.sh > device_report.json
set -e

cat << 'JSON'
{
  "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "device": {
    "model": "$(adb shell getprop ro.product.model)",
    "brand": "$(adb shell getprop ro.product.brand)",
    "android": "$(adb shell getprop ro.build.version.release)",
    "security_patch": "$(adb shell getprop ro.build.version.security_patch)",
    "hardware": "$(adb shell getprop ro.hardware)",
    "cpu_abi": "$(adb shell getprop ro.product.cpu.abi)"
  },
  "performance": {
    "uptime_seconds": $(adb shell cat /proc/uptime | awk '{print int($1)}'),
    "load_average": "$(adb shell cat /proc/loadavg | awk '{print $1, $2, $3}')",
    "cpu_cores": $(adb shell nproc),
    "ram_total_mb": $(adb shell cat /proc/meminfo | grep MemTotal | awk '{print int($2/1024)}'),
    "ram_available_mb": $(adb shell cat /proc/meminfo | grep MemAvailable | awk '{print int($2/1024)}')
  },
  "storage": {
    "data_used_mb": $(adb shell df /data | tail -1 | awk '{print int($3)}'),
    "data_total_mb": $(adb shell df /data | tail -1 | awk '{print int($2)}'),
    "system_used_mb": $(adb shell du -s /system | awk '{print int($1/1024)}')
  },
  "battery": {
    "level": $(adb shell dumpsys battery | grep level | awk '{print $2}'),
    "status": "$(adb shell dumpsys battery | grep status | awk '{print $2}')",
    "temperature_c": $(adb shell dumpsys battery | grep temperature | awk '{print $2/10}'),
    "voltage_mv": $(adb shell dumpsys battery | grep voltage | awk '{print $2}')
  },
  "network": {
    "wifi_ssid": "$(adb shell dumpsys wifi | grep mWifiInfo | grep -oP 'SSID: \K[^,]+' || echo 'N/A')",
    "wifi_ip": "$(adb shell ip addr show wlan0 | grep 'inet ' | awk '{print $2}' | cut -d/ -f1 || echo 'N/A')"
  }
}
JSON
