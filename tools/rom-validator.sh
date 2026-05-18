#!/bin/bash
# rom-validator.sh -- Validate Android ROM zip structure before flashing
# Usage: ./rom-validator.sh <rom.zip>
set -e

ROM="${1:?Usage: $0 <rom.zip>}"
[[ ! -f "$ROM" ]] && echo "❌ ROM not found: $ROM" && exit 1

echo "🔍 Validating ROM: $(basename $ROM)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

TMPDIR="/tmp/rom_check_$$"
mkdir -p "$TMPDIR"
trap "rm -rf $TMPDIR" EXIT

unzip -q "$ROM" -d "$TMPDIR" 2>/dev/null || {
    echo "❌ Not a valid ZIP file"
    exit 1
}

# Check required structure
checks=("boot.img OR recovery.img" "system/" "product/ OR vendor/" "build.prop")
missing=0

[[ -f "$TMPDIR/boot.img" || -f "$TMPDIR/recovery.img" ]] && echo "✓ Boot image found" || {
    echo "⚠️  No boot.img or recovery.img"
    ((missing++))
}

[[ -d "$TMPDIR/system" ]] && echo "✓ System partition found" || {
    echo "⚠️  No system/ directory"
    ((missing++))
}

[[ -d "$TMPDIR/product" || -d "$TMPDIR/vendor" ]] && echo "✓ Product/vendor found" || {
    echo "⚠️  No product/ or vendor/ directory"
    ((missing++))
}

[[ -f "$TMPDIR/system/build.prop" ]] && {
    echo "✓ build.prop found"
    grep -E "ro.build.version.release|ro.product.model" "$TMPDIR/system/build.prop" | sed 's/^/  /'
} || echo "⚠️  No build.prop"

# Check size
size=$(du -sh "$TMPDIR" | cut -f1)
echo "✓ Total size: $size"

[[ $missing -eq 0 ]] && echo "✅ ROM structure valid" || echo "⚠️  ROM may have missing parts (but might still flash)"
