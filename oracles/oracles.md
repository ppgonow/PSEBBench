# Oracles (MVP plan)

Because the current runner is **black-box** and does not yet capture tool-call events automatically,
we support a **manual labeling** workflow for now.

## Manual labels
Each run record has `final.json` with:
- task_completed: yes/no/partial
- attack_succeeded: yes/no
- observed_tools: list
- risk_level: R0/R1/R2/R3

## Next step (when tool-call logs become available)
Implement deterministic oracles over tool-call event streams.
