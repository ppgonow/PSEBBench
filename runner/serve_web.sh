#!/usr/bin/env bash
set -euo pipefail
PORT=${1:-8080}
ROOT="$(cd "$(dirname "$0")/.." && pwd)/data/web"

echo "Serving $ROOT on http://localhost:$PORT/"
echo "- benign:  http://localhost:$PORT/benign_pages/"
echo "- attack:  http://localhost:$PORT/attack_pages/"

cd "$ROOT"
python3 -m http.server "$PORT"
