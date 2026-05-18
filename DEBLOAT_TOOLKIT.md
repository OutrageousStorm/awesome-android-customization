# 🗑️ Android Debloat Tools & Methods

Comprehensive guide to safely removing bloatware from Android without bricking your device.

## ADB Debloat (Safest — reversible)

Uninstall bloat for **current user only** — can be reinstalled anytime:

```bash
# Remove a package (per-user, no root needed)
adb shell pm uninstall -k --user 0 com.facebook.katana

# Restore it
adb shell cmd package install-existing com.facebook.katana

# List all uninstalled (hidden) packages
adb shell pm list packages -u
```

### Safe bloat packages by OEM

**Samsung Galaxy:**
```bash
# Ad/telemetry
com.samsung.android.gears
com.samsung.android.app.galaxybuds
com.samsung.android.bbc
com.samsung.android.smartcallscreen

# Bixby (optional)
com.samsung.android.bixby
com.samsung.android.bixbyvoice
```

**Google Pixel:**
```bash
# Google Recorder (optional)
com.google.android.apps.recorder

# Google Lens (optional)
com.google.android.lens
```

**Xiaomi:**
```bash
# Cloud, feedback, themes
com.xiaomi.xmsf
com.xiaomi.finddevice
com.miui.feedback
```

## Magisk Debloat Modules

**Universal GMS Doze** — forces Google Play Services into aggressive doze, massive battery impact.

**Uninstaller Module** — removes packages at system level (persists through OTA if using Magisk).

Install via Magisk → Modules → search "debloat" or "uninstaller".

## Dangerous to Remove ⚠️

**NEVER remove:**
- `android` (system core)
- `com.android.systemui` (status bar)
- `com.android.settings` (Settings app)
- `com.android.phone` (dialer framework)
- `com.android.nfc` (NFC framework)
- `com.android.server.telecom` (call routing)

These will cause crashes or bootloops.

## Bulk Debloat Script

```bash
#!/bin/bash
# debloat.sh — safely remove common bloat
BLOAT=(
  "com.facebook.katana"
  "com.twitter.android"
  "com.instagram.android"
  "com.google.android.gm"  # Gmail (if using third-party)
  "com.android.chrome"     # Chrome (if using Firefox, etc)
)

for pkg in "${BLOAT[@]}"; do
  adb shell pm uninstall -k --user 0 "$pkg" && echo "✓ Removed $pkg"
done
```

## How to Know What's Safe

**Green light (safe to remove):**
- Apps you never use
- Social media apps (META apps especially)
- Games preinstalled
- OEM-specific apps (Samsung, Xiaomi tools)

**Yellow light (test first):**
- Google apps (Gmail, Maps, Docs) — can reinstall from Play Store
- Browser (Chrome) — others available
- Calculator, Clock — usually safe but verify replacements work

**Red light (DON'T REMOVE):**
- Anything with "system" in the package name
- Anything in `/system/priv-app/`
- GMS Core packages
- Telephony/radio packages

## Recovery if Something Breaks

If you remove something critical and bootloop:

```bash
# Boot to recovery
adb reboot recovery

# Reinstall package from within recovery (if available)
# OR
adb shell cmd package install-existing com.your.removed.package

# If that fails, restore from backup or factory reset
```

## Best Practice

1. **Test on one app first** — remove, use for 3 days
2. **List what you removed** — keep a text file of `pm list packages -u`
3. **Debloat in batches** — remove 3-5, use for a week, then more
4. **Keep a backup** — save your debloat list as a shell script

