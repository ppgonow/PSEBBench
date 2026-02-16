# Runner (planned)

Responsibilities:
- Load scenarios from `scenarios/*.yaml`
- Execute each scenario under a selected configuration (tool permissions / prompt policy)
- Collect tool-call logs + outputs into a structured record (JSONL)

Planned outputs:
- `results/runs/<timestamp>/<scenario_id>.jsonl`

