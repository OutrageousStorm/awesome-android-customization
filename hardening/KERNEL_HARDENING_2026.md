# Kernel Hardening Checklist 2026

Android kernel hardening techniques for custom ROMs.

## CFI (Control Flow Integrity)
```
Enabled in: GrapheneOS (all builds), some crDroid variants
Check: cat /proc/config.gz | gunzip | grep CONFIG_CFI
Value: CONFIG_CFI_CLANG=y
Impact: 5-10% perf overhead, catches exploits before they execute
```

## MTE (Memory Tagging Extension) — ARM v8.5+
```
Enabled in: GrapheneOS Pixels (Pixel 4+), honor 8+
How it works: Tags each 16-byte memory block, catches use-after-free
Enable in ROM: Device-specific kernel patch
Check: cat /proc/cpuinfo | grep mte
```

## HARDENED_USERCOPY
```
Prevents buffer overflow copies between kernel/user space
CONFIG_HARDENED_USERCOPY=y
Catches: string formatting attacks, stack sprays
Impact: <1% overhead
```

## SMACK vs SELinux
```
SELinux (default): Per-file security contexts, strict labeling required
SMACK: Simpler, network-based, used in some custom kernels
Most ROMs: SELinux enforcing (default-deny)
Check: getenforce (should be "Enforcing")
```

## FORTIFY_SOURCE
```
Runtime buffer overflow detection in libc
CONFIG_FORTIFY_SOURCE=y
Catches sprintf/strcpy overflows before they crash
```

## ASLR (ASLR already ON)
Check: cat /proc/sys/kernel/randomize_va_space  (should be 2 = full ASLR)
Most Android devices: On by default
Jailbreaks disable it to predict gadget addresses

## For Custom Kernels
- Always use latest upstream patches
- Build with CONFIG_DEBUG_LIST (catches list corruption)
- Enable CONFIG_SLUB_DEBUG for heap hardening
- Test with: syzkaller (Android syscall fuzzer)
