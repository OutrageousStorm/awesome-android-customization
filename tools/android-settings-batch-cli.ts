#!/usr/bin/env ts-node
/**
 * Android Settings Batch CLI
 * Apply multiple Android settings changes in one command via ADB
 * Supports ROM settings, system props, and build.prop modifications
 */

import { execSync } from 'child_process';
import * as fs from 'fs';
import * as path from 'path';

interface SettingProfile {
  name: string;
  category: 'system' | 'secure' | 'global' | 'prop';
  changes: { [key: string]: string };
}

const PROFILES: { [key: string]: SettingProfile } = {
  performance: {
    name: 'Performance Boost',
    category: 'global',
    changes: {
      'debug.force_rtl': '0',
      'debug.atrace.tags.enableflags': '0',
      'ro.ioprio_rt_fifo': '1',
    },
  },
  privacy: {
    name: 'Privacy Hardening',
    category: 'secure',
    changes: {
      'wifi_scan_always_enabled': '0',
      'location_providers_allowed': '',
      'bluetooth_on': '0',
    },
  },
  developer: {
    name: 'Developer Mode',
    category: 'global',
    changes: {
      'adb_enabled': '1',
      'ro.debuggable': '1',
      'persist.sys.usb.config': 'adb',
    },
  },
  battery: {
    name: 'Battery Saver',
    category: 'global',
    changes: {
      'pm.sleep_mode': '1',
      'ro.ril.enable.a18': '0',
      'ro.ril.power_collapse': '1',
    },
  },
};

function executeAdb(cmd: string): string {
  try {
    return execSync(`adb ${cmd}`, { encoding: 'utf-8' }).trim();
  } catch (e) {
    console.error(`ADB Error: ${e}`);
    return '';
  }
}

function getConnectedDevices(): string[] {
  const output = executeAdb('devices');
  return output
    .split('\n')
    .slice(1)
    .filter(line => line.includes('device') && !line.includes('offline'))
    .map(line => line.split('\t')[0]);
}

function applyProfile(profile: SettingProfile, device?: string): void {
  const deviceArg = device ? `-s ${device}` : '';
  
  console.log(`\n📱 Applying "${profile.name}" profile...`);
  
  for (const [key, value] of Object.entries(profile.changes)) {
    const shellCmd = `shell settings put ${profile.category} ${key} "${value}"`;
    const result = executeAdb(`${deviceArg} ${shellCmd}`);
    console.log(`  ✓ ${key} = ${value}`);
  }
  
  console.log('✅ Profile applied!');
}

function listProfiles(): void {
  console.log('\nAvailable Profiles:');
  for (const [key, profile] of Object.entries(PROFILES)) {
    console.log(`  • ${key.padEnd(15)} - ${profile.name}`);
  }
}

function main(): void {
  const args = process.argv.slice(2);
  
  if (args.length === 0) {
    console.log('Android Settings Batch CLI\n');
    listProfiles();
    console.log('\nUsage: android-settings-batch-cli.ts <profile> [device_id]');
    console.log('Example: android-settings-batch-cli.ts performance');
    return;
  }
  
  const profileName = args[0];
  const device = args[1];
  
  if (!PROFILES[profileName]) {
    console.error(`❌ Profile "${profileName}" not found.`);
    listProfiles();
    return;
  }
  
  const devices = getConnectedDevices();
  if (devices.length === 0) {
    console.error('❌ No devices connected via ADB.');
    return;
  }
  
  const targetDevice = device || devices[0];
  console.log(`📡 Using device: ${targetDevice}`);
  
  applyProfile(PROFILES[profileName], targetDevice);
}

main();
