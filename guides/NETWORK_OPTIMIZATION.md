# Network Optimization for Android

Reduce data usage, lower latency, and improve connection stability.

## Data reduction

```bash
# Check data usage per app
adb shell dumpsys netpolicy | grep -E "networks|UID"

# Restrict background data for specific apps
adb shell cmd netpolicy set restrict-background-on
adb shell cmd netpolicy set uid-policy <UID> POLICY_REJECT_METERED_BACKGROUND

# Enable data saver mode
adb shell settings put global data_saver_mode 1
```

## Network quality metrics

```bash
# Check signal strength
adb shell dumpsys telephony.registry | grep "signalStrength"

# Latency test
adb shell ping -c 4 8.8.8.8

# Speed test (requires speedtest tool)
python3 network_speedtest.py
```

## WiFi optimization

| Setting | Command | Effect |
|---------|---------|--------|
| Reduce TX power | `settings put global wifi_tx_power_mode 0` | Lower interference |
| Enable 802.11r | `settings put global wifi_enable_802_11r true` | Fast roaming |
| Enable STA+STA | `settings put global wifi_sta_concurrency 2` | Dual connect |
| Reduce scan interval | `settings put global wifi_scan_interval_ms 30000` | Save battery |

## DNS optimization

```bash
# Set private DNS
adb shell settings put global private_dns_mode hostname
adb shell settings put global private_dns_specifier 1.1.1.1

# Or: quad9 (1.1.1.1 alternative with malware blocking)
adb shell settings put global private_dns_specifier quad9.net
```

## Cellular

```bash
# Check preferred network type (0=auto, 3=LTE, 9=5G)
adb shell settings get global preferred_network_mode

# Force LTE (skip 5G if slower)
adb shell settings put global preferred_network_mode 3
```
