#!/usr/bin/env bash
set -euo pipefail
# Create a one-shot reminder 10 minutes from now in main session.
# Usage: ./runner/create_one_shot_cron.sh "Reminder text"

TEXT=${1:-"ToolChainBench one-shot test"}

openclaw cron add \
  --session main \
  --at 10m \
  --keep-after-run \
  --name "tcb-one-shot-$(date +%Y%m%d-%H%M%S)" \
  --system-event "[ToolChainBench reminder] ${TEXT}"
