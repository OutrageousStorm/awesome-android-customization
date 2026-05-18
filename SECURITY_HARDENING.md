# 🔐 Security Hardening Guide

Multi-layer Android security without root.

## Level 1: Network + Permissions
- Private DNS: `dns.quad9.net` (blocks malware)
- VPN: Wireguard or Mullvad (kills trackers before they leave device)
- Disable location: Settings → Privacy → Location OFF
- Revoke permissions: Settings → Privacy → Permission Manager

## Level 2: Behavioral
- Install **Netguard** (F-Droid) — per-app firewall
- **Shelter** — work profile isolation
- **Seedvault** — encrypted encrypted backup (replaces Google)
- **Exodus Privacy** — check for trackers in apps before install

## Level 3: ROM Level
- **GrapheneOS** (Pixel only) — AOSP hardened, verified boot, exploit mitigations
- **CalyxOS** — privacy-first ROM with integrated VPN + firewall
- **Divested** — Linux kernel hardening patches

## Custom kernel
- **kernel-adiutor** — tweak CPU scaling, disable excess wake locks
- **CFQ scheduler** — better disk I/O management

See: `android-privacy-hardener` for automation.
