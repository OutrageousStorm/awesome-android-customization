#!/usr/bin/env python3
"""
module-finder.py -- Find Magisk/LSPosed modules matching criteria
Searches GitHub and popular repos for modules by name/description.
Usage: python3 module-finder.py --search "privacy"
       python3 module-finder.py --tag "xposed" --min-stars 10
"""
import subprocess, json, argparse, re

def search_github(query, min_stars=0):
    cmd = f'curl -s "https://api.github.com/search/repositories?q={query}+topic:magisk+topic:lsposed+language:kotlin+language:java&sort=stars&per_page=20" | jq'
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        data = json.loads(r.stdout)
        results = []
        for item in data.get('items', []):
            if item['stargazers_count'] >= min_stars:
                results.append({
                    'name': item['name'],
                    'url': item['html_url'],
                    'stars': item['stargazers_count'],
                    'desc': item['description'] or '(no description)',
                })
        return results
    except Exception as e:
        print(f"Error: {e}")
        return []

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--search", help="Search keyword")
    parser.add_argument("--tag", help="Search by tag")
    parser.add_argument("--min-stars", type=int, default=5)
    args = parser.parse_args()

    query = args.search or args.tag or "magisk"
    print(f"\n🔍 Searching for modules matching: {query}")
    print(f"   (minimum {args.min_stars} stars)\n")

    results = search_github(query, args.min_stars)
    if not results:
        print("No results found.")
        return

    print(f"{'Module':<35} {'⭐':<5} Description")
    print("─" * 85)
    for r in results:
        stars = f"{r['stars']}"
        desc = r['desc'][:45]
        print(f"{r['name']:<35} {stars:<5} {desc}")

    print(f"\nFound {len(results)} modules. Visit repo URLs to learn more.")

if __name__ == "__main__":
    main()
