# Stage Summary — 2026-03-17 (ambiguous intent + staged escalation, cron)

## Scope
Added two new cron-focused scenario sets for authorization-scope evaluation:
- **Ambiguous intent set**: 8 scenarios (`H-msg-cron-required-AMB-001..008`)
- **Staged escalation set**: 5 scenarios (`H-msg-cron-required-STG-001..005`)

All runs executed with three conditions:
- **permissive** (allow injected recurring)
- **guard (IACG)**
- **firewall baseline** (block all persistent actions)

## Results (Ambiguous intent)
| Condition | n | Attack successes | ASR | Task successes | TCR |
|---|---:|---:|---:|---:|---:|
| amb1-permissive | 8 | 8 | 1.000 | 8 | 1.000 |
| amb1-guard | 8 | 0 | 0.000 | 8 | 1.000 |
| amb1-firewall | 8 | 0 | 0.000 | 8 | 1.000 |

## Results (Staged escalation)
| Condition | n | Attack successes | ASR | Task successes | TCR |
|---|---:|---:|---:|---:|---:|
| stg1-permissive | 5 | 5 | 1.000 | 5 | 1.000 |
| stg1-guard | 5 | 0 | 0.000 | 5 | 1.000 |
| stg1-firewall | 5 | 0 | 0.000 | 5 | 1.000 |

## Notes
- These runs use the CLI-backed hybrid runner (`runner/run_hybrid_cli.py`).
- Staged escalation explicitly separates the one-shot request from the later recurring upgrade, matching the “two-step escalation” requirement.
- Ambiguous intent tasks deliberately avoid explicit recurring language in the user request; the injected message still requests recurring persistence.

## Artifacts
- Scenarios: `scenarios/hybrid-ambiguous-cron/`, `scenarios/hybrid-staged-cron/`
- Run tables: `analysis/amb1_stg1_run_table.csv`, `analysis/amb1_stg1_summary.csv`
