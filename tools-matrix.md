# Android Customization Tools Matrix

Quick reference for choosing the right tool for the job.

## Root vs No-Root

| Task | No-Root | Root | Recommended |
|------|---------|------|-------------|
| Debloat | App Ops, ADB | pm uninstall | ADB (safe) |
| Ad blocking | NetGuard, Blokada | hosts file | NetGuard (transparent) |
| Battery | Greenify, Doze | Kernel tweaks | Magisk module |
| Permissions | Storage Scopes | SELinux mod | GrapheneOS |
| Bootloader | ✗ | fastboot unlock | Custom ROM |
| SSL pinning | Frida | Magisk module | Frida (dynamic) |

## Performance Tools Comparison

| Tool | Method | Best For | Cost |
|------|--------|----------|------|
| **Greenify** | Hibernation | Battery, RAM | Free |
| **Tasker** | Automation | Complex workflows | $7 |
| **Custom Kernel** | Undervolting, underclocking | Gaming, battery | Free (build own) |
| **Kernel Adiutor** | Kernel interface | Live tuning | Free |
| **UKM (Kernel Manager)** | Kernel control | Real-time tweaks | Free |
| **Performance Control** | CPU/IO tuning | Gaming | Free |

## Privacy Tools Ranked

| Rank | Tool | Type | Verdict |
|------|------|------|---------|
| 1 | GrapheneOS | ROM | Best all-around |
| 2 | NetGuard | Firewall | Works without root |
| 3 | Shizuku + App Manager | Permissions | Granular control |
| 4 | Orbot | VPN/Tor | Maximum anonymity |
| 5 | Aegis | TOTP | Secure 2FA |

## Custom ROM Recommendations by Goal

| Goal | Best ROM | Why |
|------|----------|-----|
| Maximum privacy | GrapheneOS | Hardened, verified boot |
| De-Google | CalyxOS | microG included |
| Stock Android feel | LineageOS | Minimal bloat |
| Features | crDroid | Custom settings |
| Gaming | Stock OEM | Best driver support |
| Long-term support | LineageOS | 2+ years per version |
| Lightweight | Paranoid Android | Minimal footprint |

## Glossary

- **Systemless** — Magisk-style modifications that don't touch /system
- **Verified boot** — Bootloader cryptographically verifies OS integrity
- **A/B partitions** — Two system partitions for atomic OTA updates
- **Treble** — Project Treble separates framework from drivers
- **GKI** — Generic Kernel Image — standardized kernel across devices
- **SELinux** — Mandatory Access Control enforcement
- **Knox** — Samsung security platform (tripped by bootloader unlock)
