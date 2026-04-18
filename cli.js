#!/usr/bin/env node
/**
 * ROM Finder CLI -- Search awesome-android-customization database from terminal
 * Usage: rom-finder <keyword>
 *        rom-finder --device "Pixel 7"
 *        rom-finder --type "degoogle"
 */

const fs = require('fs');
const path = require('path');

const ROMS = [
  { name: "LineageOS", stars: 5, devices: "200+", type: "AOSP", privacy: true, url: "https://lineageos.org" },
  { name: "GrapheneOS", stars: 5, devices: "Pixel", type: "hardened", privacy: true, url: "https://grapheneos.org" },
  { name: "crDroid", stars: 4, devices: "150+", type: "AOSP+tweaks", privacy: true, url: "https://crdroid.net" },
  { name: "Evolution X", stars: 3, devices: "80+", type: "Pixel UI", privacy: true, url: "https://evox.dev" },
  { name: "Pixel Experience", stars: 3, devices: "150+", type: "Pixel UI", privacy: false, url: "https://pixelexperience.org" },
  { name: "DivestOS", stars: 3, devices: "200+", type: "hardened", privacy: true, url: "https://divestos.org" },
  { name: "CalyxOS", stars: 2, devices: "Pixel", type: "hardened", privacy: true, url: "https://calyxinstitute.org" },
];

const args = process.argv.slice(2);
const query = (args[0] || '').toLowerCase();
const isDevice = args[0] === '--device';
const isType = args[0] === '--type';
const searchTerm = (args[1] || '').toLowerCase();

console.log('\n📱 ROM Finder\n');

let results = ROMS;
if (query) {
  results = ROMS.filter(r =>
    r.name.toLowerCase().includes(query) ||
    r.type.toLowerCase().includes(query) ||
    r.devices.toLowerCase().includes(query)
  );
}
if (isDevice && searchTerm) {
  results = ROMS.filter(r => r.devices.toLowerCase().includes(searchTerm));
}
if (isType && searchTerm) {
  results = ROMS.filter(r => r.type.toLowerCase().includes(searchTerm));
}

if (results.length === 0) {
  console.log('  No results.\n');
  process.exit(0);
}

console.log(`Found ${results.length} ROM(s):\n`);
results.forEach(r => {
  const star = '⭐'.repeat(r.stars);
  const privacy = r.privacy ? '🔒' : '  ';
  console.log(`  ${privacy} ${r.name.padEnd(20)} ${star} ${r.type.padEnd(15)} [${r.devices}]`);
  console.log(`     ${r.url}\n`);
});
