# Android Internals & Deep Dive

Understanding the Android OS at a technical level.

## SELinux & MACF

SELinux on Android enforces Mandatory Access Control:

```bash
# Check SELinux mode
adb shell getenforce

# View policies
adb shell cat /proc/cmdline | grep -o 'androidboot.selinux=[^ ]*'
```

### Key policies:
- **Kernel**: controls system calls
- **Framework**: app permissions enforced via `Manifest.xml`
- **Hardware**: device driver access
- **Apps**: sandbox isolation via UID/GID

## Binder IPC

The core inter-process communication mechanism:

```
App ← (request) → ServiceManager ← (lookup) → Service
         (Parcel)
```

Every system service (WindowManager, ActivityManager, PackageManager) uses Binder.

### Binder tokens & permission checks:
```
Binder.getCallingUid()  — who called me?
Binder.getCallingPid()  — what process?
checkPermission()       — enforce SELinux
```

### Shizuku hooks Binder:
```
ShizukuUserService → aidl interface → shell context
```

## zygote — App Process Factory

All Java apps fork from a single `zygote` process:

```
zygote (pre-loaded classes, Java runtime)
  ↓
  ├─ app process 1
  ├─ app process 2
  └─ app process N
```

This is why:
- App startup is instant (JVM already warm)
- All apps share libc, OpenSSL, etc.
- Root/Magisk can inject into zygote for system-wide hooks (Xposed)

## References
- [AOSP SELinux docs](https://source.android.com/docs/security/selinux)
- [Binder kernel driver](https://source.android.com/docs/core_topics/hidl/binder)
