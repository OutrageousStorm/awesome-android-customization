#!/usr/bin/env python3
import subprocess
def adb(cmd):
    return subprocess.run(f"adb shell {cmd}", shell=True, capture_output=True, text=True).stdout.strip()
def prop(k): return adb(f"getprop {k}")
print("\n[ROM Compatibility Check]")
print(f"Device: {prop('ro.product.model')}")
print(f"Android: {prop('ro.build.version.release')}")
print(f"Treble: {prop('ro.treble.enabled')}")
print(f"A/B: {adb('test -e /boot_a && echo yes || echo no')}")
print()
