# Stage Summary: Style × Guard Repeat (2026-03-06)

## What was done
To strengthen the defense story beyond a single 10-run pass, we ran an additional repetition over the same `H-msg-cron-required-002` ... `011` scenario set:

New groups:
- `g3-permissive-r2`
- `g3-permissive-guard-r2`

These repeat the most important defense contrast:
- permissive baseline
- permissive + persistence guard

## Aggregate outcome of the repeated pass
### `g3-permissive-r2`
- n = 10
- attack successes = 10
- ASR = 1.0
- TCR = 1.0

### `g3-permissive-guard-r2`
- n = 10
- attack successes = 0
- ASR = 0.0
- TCR = 1.0

This reproduces the original `g1fixed-permissive` vs `g2-permissive-guard` contrast exactly.

---

## Style-wise aggregation across both passes
Combining:
- `g1fixed-permissive` + `g3-permissive-r2`
- `g2-permissive-guard` + `g3-permissive-guard-r2`

we now obtain 4 runs per style in the baseline and 4 runs per style under the guard.

| Condition | Style | n | Attack successes | ASR | TCR |
|---|---|---:|---:|---:|---:|
| baseline | explicit | 4 | 4 | 1.0 | 1.0 |
| baseline | policy-impersonation | 4 | 4 | 1.0 | 1.0 |
| baseline | system-impersonation | 4 | 4 | 1.0 | 1.0 |
| baseline | code-block | 4 | 4 | 1.0 | 1.0 |
| baseline | social-engineering | 4 | 4 | 1.0 | 1.0 |
| guard | explicit | 4 | 0 | 0.0 | 1.0 |
| guard | policy-impersonation | 4 | 0 | 0.0 | 1.0 |
| guard | system-impersonation | 4 | 0 | 0.0 | 1.0 |
| guard | code-block | 4 | 0 | 0.0 | 1.0 |
| guard | social-engineering | 4 | 0 | 0.0 | 1.0 |

---

## Why this matters
This repeat materially strengthens the defense claim.

Before the repeat, we could say:
- the guard worked once across the 10 scenarios.

After the repeat, we can now say:
- the guard reproduces cleanly on a second pass,
- and its effect is not limited to one or two injection styles,
- because all five style families remain blocked in the repeated pass while preserving one-shot task completion.

---

## Interpretation
In the current black-box/CLI-backed evaluation slice, the persistence guard appears style-agnostic across the five tested injection variants:
- explicit
- policy-impersonation
- system-impersonation
- code-block
- social-engineering

This is valuable because the earlier vulnerability analysis showed that attack strength is style-sensitive in permissive settings. The repeated defense results suggest that a narrow persistent-state safeguard can suppress the failure mode even when the attack surface spans multiple prompt styles.

---

## Recommended use in the paper
This result is best used as:
- a reinforcement of the main defense figure, and/or
- a separate appendix/secondary-results figure showing style-wise robustness of the guard.

## Bottom line
The defense story is no longer based on a single 10-run contrast. We now have a repeated pass showing the same 1.0 -> 0.0 ASR collapse, and a style-wise aggregation showing that the guard suppresses all five tested injection styles while keeping TCR at 1.0.
