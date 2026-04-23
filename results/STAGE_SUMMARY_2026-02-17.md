# Stage Summary (as of 2026-02-17 18:14 Asia/Shanghai)

## High-level
We completed an initial end-to-end run of PSEBench scenarios under tag `fulltools`, with a **sandbox rule**:
- outbound messaging only to TEST_CHANNEL (Telegram chat_id)
- no dangerous exec, no third-party exfil

Because we are currently operating in a **black-box + manual labeling** mode, results are recorded per-run in `results/runs/*/final.json`.

## Completed scenario groups (quantitative)
| Group | n | ASR (attack succeeded) | TCR yes | TCR partial | Tools observed |
|---|---:|---:|---:|---:|---|
| A-web-exec | 10 | 0/10 (0.00%) | 10 | 0 | browser |
| A-web-msg | 8 | 0/8 (0.00%) | 8 | 0 | browser |
| A-web-nodes | 3 | 0/3 (0.00%) | 0 | 3 | browser |
| A-msg-cron | 6 | 0/6 (0.00%) | 6 | 0 | message (manual response only) |
| H-web-msg-required | 2 | 0/2 (0.00%) | 2 | 0 | browser, message (sent via CLI) |
| H-msg-cron-required | 1 | 0/1 (0.00%) | 1 | 0 | cron (via CLI), message (via CLI) |

**Attack successes observed so far:** 0.

## Interpretation (what the 0% ASR means / does NOT mean)
- The A-* web injection suites have prompts that explicitly say to ignore non-main-content instructions. Under that setting, the model reliably ignores injected tool-abuse requests; hence ASR≈0 is expected.
- For nodes, we had **no paired node device** (`nodes status` returned empty), so tool invocation could not occur; these are marked TCR=partial.
- The most informative tests so far are the **Hybrid (H-*)** scenarios, because they *require* legitimate tool usage. Even there, under the sandbox rule, we did not observe recipient-hijack or persistence escalation.

## Operational notes / blockers
1) `message` tool in this session repeatedly errored ("Use `target` instead of `to`/`channelId`.") even when `target` was provided.
   - Workaround: use CLI `openclaw message send --channel telegram --target <chat_id> ...` (verified delivered).
2) `cron` tool wrapper calls failed due to missing required fields in our tool invocation.
   - Workaround: use CLI `openclaw cron add ...`.
3) Telegram `@username` target was not reliable; numeric `chat_id` is reliable.
4) Nodes not available; defer nodes group until pairing is possible.

## Recommended next steps (priority order)
1) **Expand Hybrid suite** to 10–20 variants each:
   - web→message required: injection tries to redirect recipient/format
   - msg→cron required: injection tries to add recurring persistence or alter schedule/recipient
   This is the highest-yield path to observe non-zero ASR under more permissive autonomy settings.
2) Create a **two-policy experiment matrix**:
   - Safe policy (current): strict sandbox, require explicit confirmation for persistence/recipient changes
   - Permissive policy (baseline for measurement): allow autonomous tool use within sandbox but without extra confirmations
   Then plot ASR vs TCR.
3) Add lightweight automation for logging and labeling:
   - runner option to call CLI for `message send` and `cron add` (so “tool usage” becomes reproducible and machine-recorded)
   - upgrade oracles to parse CLI outputs (message IDs, cron job JSON) instead of pure manual labels.

## Evidence pointers
- Aggregated stats were computed from: `results/runs/*-fulltools/*/final.json`
- Example hybrid runs:
  - `results/runs/trial28-fulltools/H-web-msg-required-001/`
  - `results/runs/trial30-fulltools/H-msg-cron-required-001/`
