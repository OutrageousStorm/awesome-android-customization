#!/usr/bin/env ts-node
/**
 * adb-builder.ts — Interactive ADB command builder
 * Helps construct complex ADB commands with autocomplete
 * Usage: ts-node adb-builder.ts
 */

import * as fs from 'fs';
import * as readline from 'readline';

interface Command {
    name: string;
    usage: string;
    args: string[];
    example: string;
}

const COMMANDS: Command[] = [
    {
        name: 'install',
        usage: 'adb install [-r] [-d] <apk>',
        args: ['-r (reinstall)', '-d (allow downgrade)', '-g (grant perms)', '-s (sd card)'],
        example: 'adb install -r app.apk',
    },
    {
        name: 'pm revoke',
        usage: 'adb shell pm revoke <package> <permission>',
        args: [],
        example: 'adb shell pm revoke com.app android.permission.ACCESS_FINE_LOCATION',
    },
    {
        name: 'settings put',
        usage: 'adb shell settings put <namespace> <key> <value>',
        args: ['global', 'secure', 'system'],
        example: 'adb shell settings put global limit_ad_tracking 1',
    },
    {
        name: 'dumpsys package',
        usage: 'adb shell dumpsys package <package>',
        args: [],
        example: 'adb shell dumpsys package com.example.app | grep permission',
    },
    {
        name: 'input tap',
        usage: 'adb shell input tap <x> <y>',
        args: [],
        example: 'adb shell input tap 540 960',
    },
    {
        name: 'shell remove app',
        usage: 'adb shell pm uninstall -k --user 0 <package>',
        args: [],
        example: 'adb shell pm uninstall -k --user 0 com.facebook.katana',
    },
];

async function main() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
    });

    const question = (q: string) => new Promise<string>(r => rl.question(q, r));

    console.log('\n📋 ADB Command Builder\n');
    COMMANDS.forEach((c, i) => {
        console.log(`${i+1}. ${c.name}`);
    });
    console.log('\nSelect command number:');

    const choice = await question('> ');
    const idx = parseInt(choice) - 1;
    if (idx < 0 || idx >= COMMANDS.length) {
        console.log('Invalid choice.');
        rl.close();
        return;
    }

    const cmd = COMMANDS[idx];
    console.log(`\n${cmd.name}`);
    console.log(`Usage: ${cmd.usage}`);
    if (cmd.args.length) {
        console.log(`Args:  ${cmd.args.join(' | ')}`);
    }
    console.log(`Example: ${cmd.example}\n`);

    const result = await question('Enter command (or leave blank): ');
    if (result.trim()) {
        console.log(`\nBuilt command:\n  ${result}`);
        console.log('\nCopy to clipboard? Use: echo "' + result + '" | pbcopy');
    }
    rl.close();
}

main();
