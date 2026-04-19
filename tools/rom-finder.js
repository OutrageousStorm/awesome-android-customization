#!/usr/bin/env node
/**
 * rom-finder.js -- CLI tool to find custom ROMs for your device
 * Usage: node rom-finder.js --device "Pixel 6" [--type LineageOS]
 */

const devices = [
    { name: "Pixel 6", codename: "oriole", compatible: ["LineageOS", "GrapheneOS", "crDroid"] },
    { name: "Pixel 7", codename: "panther", compatible: ["LineageOS", "GrapheneOS", "crDroid"] },
    { name: "Samsung S21", codename: "SM-G991B", compatible: ["LineageOS", "crDroid", "Evolution X"] },
    { name: "OnePlus 9", codename: "lemonade", compatible: ["LineageOS", "crDroid", "OxygenOS"] },
    { name: "Xiaomi 12", codename: "cupid", compatible: ["LineageOS", "crDroid", "Evolution X"] },
];

const romLinks = {
    "LineageOS": "https://lineageos.org/devices/",
    "GrapheneOS": "https://grapheneos.org",
    "CalyxOS": "https://calyxos.org",
    "crDroid": "https://crdroid.net",
    "Evolution X": "https://evolution-x.org",
};

function findDevice(query) {
    return devices.find(d => 
        d.name.toLowerCase().includes(query.toLowerCase()) ||
        d.codename.toLowerCase().includes(query.toLowerCase())
    );
}

function main() {
    const args = process.argv.slice(2);
    const deviceIdx = args.indexOf('--device');
    const typeIdx = args.indexOf('--type');

    if (deviceIdx === -1) {
        console.log('📱 ROM Finder CLI');
        console.log('\nUsage: node rom-finder.js --device "Device Name" [--type RomName]');
        console.log('\nAvailable devices:');
        devices.forEach(d => {
            console.log(`  ${d.name.padEnd(20)} (${d.codename})`);
        });
        return;
    }

    const deviceName = args[deviceIdx + 1];
    const device = findDevice(deviceName);

    if (!device) {
        console.log(`❌ Device not found: ${deviceName}`);
        console.log('Try: node rom-finder.js --device "Pixel 6"');
        return;
    }

    console.log(`\n✅ Found: ${device.name} (${device.codename})`);
    console.log('\n🔧 Compatible ROMs:');

    const filter = typeIdx !== -1 ? args[typeIdx + 1] : null;
    const compatible = filter ? 
        device.compatible.filter(r => r.toLowerCase().includes(filter.toLowerCase())) :
        device.compatible;

    compatible.forEach(rom => {
        const url = romLinks[rom];
        console.log(`  • ${rom}`);
        if (url) console.log(`    ${url}`);
    });
}

main();
