#!/usr/bin/env python3
"""
System Property Analyzer
Analyze Android system properties for security, performance, and customization insights
"""

import subprocess
import json
import sys
from collections import defaultdict

def get_adb_command():
    """Get ADB command, checking for device"""
    devices = subprocess.check_output(['adb', 'devices']).decode().strip().split('\n')
    connected = [d.split()[0] for d in devices[1:] if 'device' in d and 'offline' not in d]
    
    if not connected:
        print("❌ No ADB devices connected")
        sys.exit(1)
    
    return f"adb -s {connected[0]}"

def get_system_props():
    """Fetch all system properties"""
    try:
        adb_cmd = get_adb_command()
        output = subprocess.check_output(f"{adb_cmd} shell getprop", shell=True).decode().strip()
        props = {}
        
        for line in output.split('\n'):
            if ': ' in line:
                key, value = line.replace('[', '').replace(']', '').split(': ')
                props[key] = value
        
        return props
    except Exception as e:
        print(f"❌ Error fetching properties: {e}")
        return {}

def analyze_security(props):
    """Analyze security-related properties"""
    security_issues = []
    
    checks = {
        'ro.debuggable': ('true', 'Debuggable build'),
        'ro.secure': ('0', 'Security disabled'),
        'persist.sys.usb.config': ('adb', 'USB ADB enabled in persist'),
        'ro.allow.mock.location': ('true', 'Mock locations allowed'),
    }
    
    for prop, (danger_val, issue) in checks.items():
        if props.get(prop) == danger_val:
            security_issues.append(issue)
    
    return security_issues

def analyze_performance(props):
    """Analyze performance-related properties"""
    perf_info = {}
    
    perf_props = {
        'ro.product.cpu.abi': 'CPU ABI',
        'ro.product.board': 'Board',
        'ro.build.version.release': 'Android Version',
        'ro.product.ram': 'RAM',
        'ro.hardware': 'Hardware',
    }
    
    for prop, label in perf_props.items():
        if prop in props:
            perf_info[label] = props[prop]
    
    return perf_info

def main():
    print("🔍 Analyzing Android System Properties...\n")
    
    props = get_system_props()
    if not props:
        return
    
    print(f"Total Properties: {len(props)}\n")
    
    # Security Analysis
    print("🔐 Security Analysis:")
    sec_issues = analyze_security(props)
    if sec_issues:
        for issue in sec_issues:
            print(f"  ⚠️  {issue}")
    else:
        print("  ✅ No obvious security issues detected")
    
    # Device Info
    print("\n📱 Device Information:")
    perf = analyze_performance(props)
    for label, value in perf.items():
        print(f"  • {label}: {value}")
    
    # Customization State
    print("\n🎨 Customization Status:")
    custom_props = {k: v for k, v in props.items() if any(x in k for x in ['ro.build', 'ro.product'])}
    print(f"  Found {len(custom_props)} build-related properties")
    
    # Export JSON option
    if '--json' in sys.argv:
        with open('system-props.json', 'w') as f:
            json.dump(props, f, indent=2)
        print("\n✅ Exported to system-props.json")

if __name__ == '__main__':
    main()
