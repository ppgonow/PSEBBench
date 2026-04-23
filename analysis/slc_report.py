#!/usr/bin/env python3
import csv
import glob
import json
import os
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUN_GLOB = os.path.join(ROOT, 'results', 'runs', 'slc*', '*', 'final.json')

rows = []
for fp in glob.glob(RUN_GLOB):
    parts = fp.split(os.sep)
    run = parts[-3]
    scenario = parts[-2]
    with open(fp, 'r', encoding='utf-8') as f:
        j = json.load(f)
    ml = j.get('manual_labels', {})
    g = j.get('guard', {})
    rows.append({
        'run': run,
        'scenario': scenario,
        'family': scenario.rsplit('-', 1)[0] if scenario.rsplit('-',1)[-1].isdigit() else scenario,
        'guard_policy': g.get('guard_policy',''),
        'task_completed': ml.get('task_completed'),
        'attack_succeeded': ml.get('attack_succeeded'),
    })

run_table = os.path.join(ROOT, 'analysis', 'slc_run_table.csv')
with open(run_table, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=['run','scenario','family','guard_policy','task_completed','attack_succeeded'])
    w.writeheader()
    for r in sorted(rows, key=lambda x: (x['run'], x['scenario'])):
        w.writerow(r)

agg = defaultdict(lambda: {'n':0, 'attack_yes':0, 'task_yes':0})
for r in rows:
    agg[r['run']]['n'] += 1
    if r['attack_succeeded'] == 'yes':
        agg[r['run']]['attack_yes'] += 1
    if r['task_completed'] == 'yes':
        agg[r['run']]['task_yes'] += 1

summary = os.path.join(ROOT, 'analysis', 'slc_summary.csv')
with open(summary, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=['run','n','attack_successes','asr','task_successes','tcr'])
    w.writeheader()
    for run, v in sorted(agg.items()):
        n = v['n']
        w.writerow({
            'run': run,
            'n': n,
            'attack_successes': v['attack_yes'],
            'asr': round(v['attack_yes']/n, 3) if n else 0.0,
            'task_successes': v['task_yes'],
            'tcr': round(v['task_yes']/n, 3) if n else 0.0,
        })

print(run_table)
print(summary)
