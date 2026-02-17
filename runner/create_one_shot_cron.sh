#!/usr/bin/env bash
set -euo pipefail
# Create a one-shot reminder 10 minutes from now in main session.
# Usage: ./runner/create_one_shot_cron.sh "Reminder text"

TEXT=${1:-"ToolChainBench one-shot test"}

python3 - <<PY
import datetime as dt
from zoneinfo import ZoneInfo
now = dt.datetime.now(ZoneInfo('Asia/Shanghai'))
at = now + dt.timedelta(minutes=10)
print(at.replace(microsecond=0).isoformat())
PY
AT=$(python3 - <<'PY'
import datetime as dt
from zoneinfo import ZoneInfo
now = dt.datetime.now(ZoneInfo('Asia/Shanghai'))
at = now + dt.timedelta(minutes=10)
print(at.replace(microsecond=0).isoformat())
PY
)

openclaw cron add \
  --session-target main \
  --at "$AT" \
  --text "[ToolChainBench reminder] $TEXT" \
  --name "tcb-one-shot-$(date +%Y%m%d-%H%M%S)"
