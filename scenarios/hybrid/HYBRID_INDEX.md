# Hybrid scenarios (benign task requires a tool)

These scenarios are designed to avoid the "0% ASR because the agent never needs the tool" pitfall.

Each hybrid scenario has a legitimate requirement to use a tool (message/cron), while the injected content
tries to redirect the tool usage to an unsafe target (exfil/persistence).
Reproducibility fields (intent/adversary/risk/attack_strength) should be populated.
