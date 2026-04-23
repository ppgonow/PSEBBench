# PSEBench

PSEBench is a benchmark and measurement pipeline for studying **security failures in tool-using agent frameworks**, with a current emphasis on **persistence escalation** and **authorization-aware defenses**.

It is designed to answer questions like:
- When can **untrusted text** cause an agent to take **higher-scope tool actions**?
- How often do attacks succeed under different runner / defense policies?
- Which defenses preserve utility while blocking unauthorized persistence?

---

## Current focus
The most mature part of the repository centers on **hybrid tasks** where the user legitimately needs tools, but injected content attempts to escalate a one-shot action into a **persistent / recurring / broader-scope** action.

Key current themes include:
- `message -> cron -> persistence`
- implicit vs. explicit persistence intent
- broader-scope actions such as recipient redirection
- tool-layer defenses:
  - **IACG** (authorization-aware guard)
  - **confirm-all-persistent** (coarse confirmation baseline)
  - **Shallow Lexical Comparator (SLC)** (lexical baseline)
  - **firewall** (deny-all persistence baseline)

---

## Repository map
See:
- `REPO_MAP.md`
- `OPEN_SOURCE_PREP.md`

---

## Core research question
Given tool-integrated agent frameworks (e.g., OpenClaw-like systems), how often can **untrusted inputs** (web pages, inbound messages, local files) induce **unauthorized tool actions**, and how well do different defenses preserve the boundary between:
- legitimate tool use
- persistence escalation
- broader-scope state changes

---

## Threat model
### Untrusted input sources
- **Web**: page body / comments / hidden content
- **Message**: IM/chat/email-like inbound text
- **File**: workspace documents with embedded instructions

### High-risk actions
- **Persistence / recurrence creation**
- **Recipient broadening / redirection**
- **Message exfiltration**
- **Command execution**
- **Sensitive device actions** (camera / screen / location)

### Attacker capability
The attacker controls only **content** (web/message/file), not framework internals or runner configuration.

---

## Main directories
- `scenarios/` — benchmark scenario YAMLs
- `runner/` — benchmark harnesses
- `analysis/` — summary scripts and result tables
- `oracles/` — oracle notes and labeling helpers
- `results/` — stage summaries and experiment logs
- `paper/` — paper drafts and writing notes
- `presentation/` — slide decks and deck sources

---

## Current important result files
### New baselines
- `results/STAGE_SUMMARY_CONFIRM_ALL_PERSISTENT.md`
- `results/STAGE_SUMMARY_SLC.md`
- `results/STAGE_SUMMARY_NEW_BASELINES.md`
- `analysis/new_baseline_comparison_table.csv`

### Main defense / persistence story
- `paper/PERSISTENCE_GUARD_METHOD.md`
- `results/STAGE_SUMMARY_2026-03-17_CTR.md`
- `results/STAGE_SUMMARY_2026-03-17_IMPLICIT.md`
- `results/STAGE_SUMMARY_2026-03-17_TRIPLE.md`
- `analysis/main_table_by_family_plus_persistent.md`

---

## Reproducibility
See:
- `REPRODUCIBILITY.md`
- `runner/README.md`

---

## Notes for future open-sourcing
This repository is still a research workspace. Before public release, review:
- `results/runs/` raw artifacts
- `runner/config.yaml`
- local notes in root markdown files
- optional draft material under `paper/` and `presentation/`

---

## LaTeX Local Writing Setup

### Structure
- `src/main.tex`
- `src/sections/abstract.tex`
- `src/sections/intro.tex`
- `src/sections/related_work.tex`
- `src/sections/method.tex`
- `src/sections/experiments.tex`
- `src/sections/conclusion.tex`
- `src/bib/refs.bib`
- `src/macros/custom.tex`
- `src/figures/`
- `src/tables/`
- `build/`
- `.vscode/settings.json`
- `Makefile`

### Build
Use:

```bash
make pdf
```

Output PDF:

```text
build/main.pdf
```

### Continuous build
Use:

```bash
make watch
```

### Clean
Use:

```bash
make clean
```
