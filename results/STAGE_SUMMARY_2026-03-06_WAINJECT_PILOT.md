# Stage Summary — 2026-03-06 (WAInjectBench transfer pilot)

## Goal
Strengthen external validity by testing whether malicious prompt styles drawn from a public prompt-injection benchmark transfer into PSEBench’s core hybrid legitimate-tool workflow.

## What was done
1. Confirmed direct HuggingFace download was unstable in the current environment.
2. Switched to the upstream GitHub repository for WAInjectBench text data.
3. Downloaded malicious and benign text files into a local external-data workspace that is not tracked in the public repository.
4. Built a first batch of 6 **WAInjectBench-inspired mapped-transfer** scenarios under:
   - `scenarios/hybrid-wainject/`
5. Ran a small pilot with two conditions:
   - `w1-permissive`
   - `w1-guard`
6. Removed the 6 recurring cron artifacts created by the permissive pilot after the run completed.

## Scenario coverage
The 6 transfer scenarios preserve public-benchmark rhetorical style while mapping the malicious objective to PSEBench’s core persistence risk.

Styles covered:
- WASP-inspired urgent prerequisite / MUST / REQUIRED framing
- VPI-inspired workflow diversion / retry pressure / do-not-ask-user framing
- EIA-inspired pre-confirmation / verification-pretext / gated ordering framing

## Results
### Permissive condition
- 6/6 attack success
- 6/6 task completion

### Guard condition
- 0/6 attack success
- 6/6 task completion

## Interpretation
This pilot suggests that the main PSEBench finding is not limited to self-authored injected prompts. Public-benchmark-derived malicious prompt styles appear to transfer into the hybrid cron-required workflow and still induce recurring persistence under permissive execution, while the persistence guard continues to suppress the attack without breaking benign task completion.

## Output artifacts
- `analysis/w1_wainject_transfer_summary.csv`
- `scenarios/hybrid-wainject/H-msg-cron-required-W001.yaml` ... `W006.yaml`

## Caveat
This is a **mapped-transfer** experiment, not a verbatim evaluation on WAInjectBench’s native task setting. The claim is therefore external-style transfer into PSEBench’s workflow setting, not direct benchmark equivalence.
