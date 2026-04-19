#!/bin/bash
# Search and install Magisk modules interactively via GitHub API
# Uses: https://modules.lsposed.org (LSPosed repo, Magisk-compatible)
QUERY="${1:-}"
if [[ -z "$QUERY" ]]; then
  echo "Magisk Module Finder"
  read -p "Search modules (e.g. 'playintegrity'): " QUERY
fi
echo "Searching for '$QUERY'..."
curl -s "https://modules.lsposed.org/api/v2/modules?search=$QUERY" | jq '.modules[0:10] | .[] | "\(.id) - \(.name)\n  \(.description)"'
echo ""
echo "Install module via Magisk app → Modules → select ZIP"
