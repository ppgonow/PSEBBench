# Runner usage (MVP, black-box)

This is a **black-box-first** runner: it prepares scenario packets and records results, without automatically controlling OpenClaw.

## Install dependency
```bash
pip3 install pyyaml
```

## Print a run packet
```bash
python3 runner/run.py scenarios/attack/A-web-exec-001.yaml --print
```

## Initialize a run record directory
```bash
python3 runner/run.py scenarios/attack/A-web-exec-001.yaml --init --tag fulltools
```
It will print the created directory, e.g.:
`results/runs/20260216-213800-fulltools/A-web-exec-001/`

## Execute the run (manual)
1) Copy `run_packet.txt` prompt into the agent chat.
2) Observe any tool calls and outcomes.
3) Paste the final agent response into `agent_output.txt` (or use --finalize once we support stable run IDs).

## Where outputs go
- `results/runs/<run_id>-<tag>/<scenario_id>/scenario.yaml`
- `results/runs/<run_id>-<tag>/<scenario_id>/run_packet.txt`
- `results/runs/<run_id>-<tag>/<scenario_id>/meta.json`
- `results/runs/<run_id>-<tag>/<scenario_id>/final.json`

## Next step
We will add:
- a stable `--run-id` option
- automatic extraction of tool calls (if OpenClaw exposes them)
- oracle scripts to label ASR/TCR from logs
