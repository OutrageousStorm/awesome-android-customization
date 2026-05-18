#!/usr/bin/env python3
"""
auto_app_killer.py -- Kill memory hog apps automatically
Monitors RAM, kills top offenders when threshold exceeded.
Usage: python3 auto_app_killer.py --threshold 2048  # kill when used RAM > 2GB
"""
import subprocess, time, argparse

def adb(cmd):
    r = subprocess.run(f"adb shell {cmd}", shell=True, capture_output=True, text=True)
    return r.stdout.strip()

def get_meminfo():
    out = adb("cat /proc/meminfo | head -3")
    lines = out.splitlines()
    total = int(lines[0].split()[1])
    free = int(lines[1].split()[1])
    available = int(lines[2].split()[1])
    return total, free, available

def get_top_memory_users():
    out = adb("dumpsys meminfo | grep -E '^\\s+[0-9]' | sort -rn -k2 | head -10")
    apps = []
    for line in out.splitlines():
        parts = line.split()
        if len(parts) >= 2:
            try:
                pid = int(parts[0])
                mem = int(parts[1])
                name = ' '.join(parts[10:]) if len(parts) > 10 else parts[-1]
                apps.append((name, mem, pid))
            except ValueError:
                pass
    return apps

def kill_app(pkg):
    adb(f"am force-stop {pkg}")

def monitor(threshold_kb=2097152):
    print(f"🔪 App Memory Monitor — threshold: {threshold_kb//1024}MB")
    while True:
        total, free, avail = get_meminfo()
        used = total - free
        pct = (used / total) * 100
        print(f"\n[{time.strftime('%H:%M:%S')}] RAM: {used//1024}MB / {total//1024}MB ({pct:.0f}%)")
        
        if used > threshold_kb:
            print(f"⚠️  Threshold exceeded! Killing top memory hogs...")
            for app, mem, pid in get_top_memory_users()[:3]:
                print(f"  Killing: {app} ({mem}MB)")
                kill_app(app)
            time.sleep(2)
        
        time.sleep(10)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--threshold", type=int, default=2097152, help="RAM threshold in KB")
    args = parser.parse_args()
    monitor(args.threshold)
