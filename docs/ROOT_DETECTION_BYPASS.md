# Root Detection Bypass Techniques

Complete guide to detecting and defeating root detection in Android apps.

## Detection methods used by apps

### File-based checks
```
/system/xbin/su
/sbin/su
/system/bin/su
/data/local/tmp/su
/system/etc/init.d/99SuperSUDaemon
/system/app/Superuser.apk
/sbin/.magisk
/data/adb/magisk
/dev/com.koushikdutta.superuser.daemon
```

### Process checks
- Running processes: check for `su` daemon, `magiskd`
- File descriptor scanning: look for open sockets to privileged services

### Property-based checks
- `ro.build.tags` — "test-keys" = rooted (debug build)
- `ro.debuggable` — true = rooted
- `ro.secure` — false = rooted
- Custom magisk props: `ro.magisk.hide`, `ro.magisk.version`

### SELinux enforcement
```bash
getenforce  # "Enforcing" vs "Permissive"
```

### Xposed/LSPosed detection
- Check for Xposed bridge class: `de.robv.android.xposed.XposedBridge`
- Check for LSPosed modules in `/data/adb/lsposed`

### KernelSU detection
- Check for `/dev/memfd_create` availability
- Look for `SUPATH` environment variable

## Bypass strategies

### 1. Shizuku (no root, no detection)
Best option — apps can't detect it because it's not root.
```bash
adb install Shizuku.apk
adb shell sh /sdcard/Android/data/moe.shizuku.privileged.api/start.sh
```

### 2. Magisk Hide (deprecated, still works on some)
```bash
# In Magisk:
adb shell magiskhide enable
adb shell magiskhide add com.target.app
```

### 3. Zygisk + DenyList
```bash
# In Magisk Manager:
Settings → Zygisk → DenyList
Add package to hide root from it
```

### 4. Shamiko Module
Combines Zygisk + advanced hiding. Install from Magisk.

### 5. TrickyStore
Hardware-level spoofing for attestation checks (SafetyNet, Play Integrity).

### 6. APK patching
Patch the app directly to remove root checks:
```bash
python3 apk_patch.py --apk app.apk --root-bypass --sign
```

### 7. Frida on-the-fly hooking
```bash
frida -U -f com.target.app -l root-bypass.js --no-pause
```
See `frida-scripts-android` repo for ready-to-run scripts.

## Detecting what's actually checking

```bash
# Monitor with Frida
frida -U -f com.app -l crypto_hook.js

# Or check the APK source
jadx target.apk
# Search for: "isRooted", "checkRoot", "/system/bin/su", "getenforce"
```

## Prevention (if you're an app dev)

Don't do root checks. Instead:
- Request only the permissions you actually need
- Use Google Play Integrity API (with SafetyNet fallback)
- Accept rooted devices — many power users root for privacy

---

**Related:** android-forensics-guide, apk-patcher, frida-scripts-android
