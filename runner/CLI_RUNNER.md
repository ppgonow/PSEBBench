# CLI runner (hybrid)

This runner executes **message/cron** actions via `openclaw` CLI and records outputs as JSONL.
It is a reproducible fallback when the in-session tool API is unreliable.

Examples:

```bash
cd ~/Desktop/ToolChainBench
source .venv/bin/activate

# Safe (no recurring persistence)
python runner/run_hybrid_cli.py scenarios/hybrid/H-msg-cron-required-002.yaml \
  --run-id r1 --tag safe --chat-id 6132399305

# Permissive baseline (create recurring injected cron)
python runner/run_hybrid_cli.py scenarios/hybrid/H-msg-cron-required-002.yaml \
  --run-id r1 --tag permissive --chat-id 6132399305 --permissive
```

Outputs:
- `results/runs/<runid>-<tag>/<scenario_id>/cli_events.jsonl`
- `.../final.json`
