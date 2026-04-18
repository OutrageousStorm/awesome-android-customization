#!/usr/bin/env node
/**
 * app-finder.js -- Find Android apps by keyword from the curated list
 * Usage: node app-finder.js "battery"
 *        node app-finder.js --category "Battery"
 */

const fs = require('fs');
const path = require('path');

const APPS = [
    { name: "App Manager", category: "System", keywords: ["control", "permissions", "uninstall"] },
    { name: "Hail", category: "System", keywords: ["freeze", "disable", "suspend"] },
    { name: "AccA", category: "Battery", keywords: ["charging", "limit", "health"] },
    { name: "NetGuard", category: "Privacy", keywords: ["firewall", "network", "blocking"] },
    { name: "Shizuku", category: "Framework", keywords: ["adb", "root-alternative", "permissions"] },
    { name: "LSPosed", category: "Framework", keywords: ["xposed", "hooks", "modding"] },
    { name: "MiXplorer", category: "Files", keywords: ["manager", "storage", "ftp"] },
    { name: "Settings Storage", category: "System", keywords: ["settings", "hidden", "tweaks"] },
    { name: "Tasker", category: "Automation", keywords: ["automate", "tasks", "scripts"] },
];

const query = process.argv.slice(2).join(' ').toLowerCase();

if (!query) {
    console.log("Usage: node app-finder.js <query>");
    console.log("\nExamples:");
    console.log("  node app-finder.js battery");
    console.log("  node app-finder.js firewall");
    console.log("  node app-finder.js root-alternative");
    process.exit(1);
}

const results = APPS.filter(app =>
    app.name.toLowerCase().includes(query) ||
    app.category.toLowerCase().includes(query) ||
    app.keywords.some(k => k.includes(query))
);

if (results.length === 0) {
    console.log(`No apps found matching "${query}"`);
    process.exit(1);
}

console.log(`\n📱 Found ${results.length} app(s):\n`);
results.forEach(app => {
    console.log(`  [${app.category}] ${app.name}`);
    console.log(`    Keywords: ${app.keywords.join(', ')}`);
});
