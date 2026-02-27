#!/usr/bin/env python3
"""Aggregate manual_labels from results/runs/**/final.json.

Outputs:
- analysis/manual_aggregate_by_group.csv
- analysis/manual_aggregate_by_run.csv
- analysis/manual_aggregate_by_scenario.csv

This is intentionally simple and schema-tolerant: it infers scenario/run from path.
"""

import csv
import glob
import json
import os
from collections import Counter, defaultdict

FILES = glob.glob('results/runs/**/final.json', recursive=True)

rows = []
for fp in FILES:
    parts = fp.split(os.sep)
    if len(parts) < 4:
        continue
    scenario = parts[-2]
    run = parts[-3]
    group = scenario.split('-')[0] if scenario else 'UNK'

    try:
        with open(fp, 'r', encoding='utf-8') as f:
            j = json.load(f)
    except Exception:
        continue

    ml = j.get('manual_labels') or {}
    if not ml:
        continue

    rows.append({
        'run': run,
        'scenario': scenario,
        'group': group,
        'task_completed': ml.get('task_completed') or ml.get('task_completed'.replace('_','')) or ml.get('task_completed', ''),
        'attack_succeeded': ml.get('attack_succeeded'),
        'risk_level': ml.get('risk_level'),
        'observed_tools': ','.join(ml.get('observed_tools') or []),
        'path': fp,
    })


def agg(key):
    c = defaultdict(Counter)
    for r in rows:
        k = r[key]
        c[k]['n'] += 1
        if r['attack_succeeded']:
            c[k][f"attack_{r['attack_succeeded']}"] += 1
        if r['task_completed']:
            c[k][f"task_{r['task_completed']}"] += 1
        if r['risk_level']:
            c[k][f"risk_{r['risk_level']}"] += 1
    return c


def write_table(path, key, counters):
    # gather columns
    cols = set(['key','n'])
    for k,ct in counters.items():
        cols |= set(ct.keys())
    cols = ['key'] + [c for c in sorted(cols) if c not in ('key')]

    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for k,ct in sorted(counters.items(), key=lambda kv: kv[1].get('n',0), reverse=True):
            row = {'key': k}
            row.update(ct)
            w.writerow(row)


os.makedirs('analysis', exist_ok=True)
write_table('analysis/manual_aggregate_by_group.csv', 'group', agg('group'))
write_table('analysis/manual_aggregate_by_run.csv', 'run', agg('run'))
write_table('analysis/manual_aggregate_by_scenario.csv', 'scenario', agg('scenario'))

print(f"Loaded {len(rows)} labeled finals from {len(FILES)} final.json files")
