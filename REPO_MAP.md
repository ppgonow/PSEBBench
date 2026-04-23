# Repository Map

## Top-level directories
- `analysis/` — scripts and exported CSV/MD tables used to aggregate experiment results
- `data/` — local data and safe tracked fixtures (`data/web/`)
- `external/` — external benchmark references / imported materials
- `oracles/` — oracle notes and labeling helpers
- `paper/` — paper drafts, outlines, claim notes, figure plans
- `plots/` — generated figures (currently gitignored)
- `presentation/` — slide decks and slide-generation scripts
- `results/` — experiment logs, stage summaries, and raw run artifacts under `results/runs/`
- `runner/` — benchmark runners and harness scripts
- `scenarios/` — benchmark scenarios grouped by family / slice

## Important files
- `README.md` — project overview and benchmark framing
- `REPRODUCIBILITY.md` — reproduction commands and artifact conventions
- `OPEN_SOURCE_PREP.md` — release-oriented cleanup notes
- `EXPERIMENT_LOG.md` — root-level historical notes (review before release)
- `NOTES.md` / `NOTES_PERMISSIVE.md` — working notes (review before release)

## Key experimental slices
- `scenarios/hybrid/` — core cron matched slice
- `scenarios/hybrid-contrast-cron/` — authorization-boundary contrast
- `scenarios/hybrid-implicit-cron/` — implicit durability slice
- `scenarios/hybrid-failure-cron/` — lexical / negation failure stress set
- `scenarios/hybrid-file/` — file persistence families
- `scenarios/hybrid-calendar/` — calendar recurrence families
- `scenarios/hybrid-msg/` — recipient broadening / hijack family

## New baseline outputs
- `analysis/confirm_all_persistent_summary.csv`
- `analysis/slc_summary.csv`
- `analysis/new_baseline_comparison_table.csv`
- `results/STAGE_SUMMARY_CONFIRM_ALL_PERSISTENT.md`
- `results/STAGE_SUMMARY_SLC.md`
- `results/STAGE_SUMMARY_NEW_BASELINES.md`
