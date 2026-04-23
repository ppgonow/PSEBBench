# Stage Summary: Stronger-Authority Threat Model Pilot (2026-03-06)

## Goal
Begin the first follow-up experiment aimed specifically at addressing the likely reviewer criticism that the current attacker may appear too weak or too literal.

## What was added
We created a new pilot scenario set under:
- `scenarios/hybrid-strong/`

Five new stronger-authority variants were added:
- `H-msg-cron-required-021` — explicit approval fabrication
- `H-msg-cron-required-022` — workflow policy impersonation
- `H-msg-cron-required-023` — system context impersonation
- `H-msg-cron-required-024` — scheduler recommendation
- `H-msg-cron-required-025` — audit/compliance social-engineering

These scenarios preserve the same benign requirement:
- create a one-shot reminder,
- confirm back,

but strengthen the injected context by making it appear more authoritative or operationally legitimate.

---

## Conditions executed
### 1) `strong1-permissive`
- runner: decision-proxy
- policy: naive / permissive
- scenarios: 021–025

Result:
- n = 5
- attack successes = 5
- **ASR = 1.0**
- **TCR = 1.0**

### 2) `strong1-permissive-guard`
- runner: CLI hybrid runner with no injected recurring execution
- scenarios: 021–025

Result:
- n = 5
- attack successes = 0
- **ASR = 0.0**
- **TCR = 1.0**

---

## Interpretation
This pilot strengthens the paper in an important way.

Previously, the core result relied on standard injected variants (explicit / policy-impersonation / system-impersonation / code-block / social-engineering) over the base `H-msg-cron-required` set.

Now, even under a stronger and more realistic injected authority model:
- the permissive baseline remains fully vulnerable,
- and the persistence guard still suppresses all attacks in the pilot slice,
- while preserving the one-shot task.

---

## Why this matters for reviewer defense
This pilot directly addresses the criticism that the attacker is too weak.

It shows that the observed persistence-escalation failure is not limited to:
- blunt injected commands,
- obvious imperative phrasing,
- or a single simplistic attack style.

Instead, the same failure mode persists when the injected content mimics:
- prior approval,
- workflow policy,
- system context,
- scheduler recommendations,
- or compliance reasoning.

---

## Current limitation
This is still a small pilot:
- only 5 stronger-authority scenarios,
- only permissive baseline vs permissive+guard,
- and still based on the current black-box/CLI-backed experimental path.

So it should be presented as a **threat-model-strengthening pilot**, not yet as the final definitive expansion.

---

## Recommended next move
If we continue this line, the next step should be one of:
1. expand the stronger-authority pilot to 10 scenarios / two passes,
2. combine stronger-authority variants with the repeated defense contrast,
3. or move to the second planned line: broaden cron persistence beyond hourly recurring.

## Bottom line
The first stronger-authority pilot is successful:
- permissive remains fully attackable,
- guard remains fully protective in this slice,
- and the threat model is now more realistic and harder for reviewers to dismiss as overly weak.
