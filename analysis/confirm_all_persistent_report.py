#!/usr/bin/env python3
import csv
import glob
import json
import os
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUN_GLOB = os.path.join(ROOT, 'results', 'runs', 'confirm-all-persistent*', '*', 'final.json')

rows = []
for fp in glob.glob(RUN_GLOB):
    parts = fp.split(os.sep)
    run = parts[-3]
    scenario = parts[-2]
    with open(fp, 'r', encoding='utf-8') as f:
        j = json.load(f)
    ml = j.get('manual_labels', {})
    guard = j.get('guard', {})
    rows.append({
        'run': run,
        'scenario': scenario,
        'family': scenario.rsplit('-', 1)[0] if scenario.rsplit('-',1)[-1].isdigit() else scenario,
        'guard_policy': guard.get('guard_policy', ''),
        'task_completed': ml.get('task_completed'),
        'attack_succeeded': ml.get('attack_succeeded'),
        'confirmation_triggered': bool(ml.get('confirmation_triggered')),
    })

run_table_path = os.path.join(ROOT, 'analysis', 'confirm_all_persistent_run_table.csv')
with open(run_table_path, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=['run','scenario','family','guard_policy','task_completed','attack_succeeded','confirmation_triggered'])
    w.writeheader()
    for r in sorted(rows, key=lambda x: (x['run'], x['scenario'])):
        w.writerow(r)

agg = defaultdict(lambda: {'n':0, 'attack_yes':0, 'task_yes':0, 'confirmation_count':0})
for r in rows:
    key = r['run']
    agg[key]['n'] += 1
    if r['attack_succeeded'] == 'yes':
        agg[key]['attack_yes'] += 1
    if r['task_completed'] == 'yes':
        agg[key]['task_yes'] += 1
    if r['confirmation_triggered']:
        agg[key]['confirmation_count'] += 1

summary_rows = []
for key, v in sorted(agg.items()):
    n = v['n']
    summary_rows.append({
        'run': key,
        'n': n,
        'attack_successes': v['attack_yes'],
        'asr': round(v['attack_yes']/n, 3) if n else 0.0,
        'task_successes': v['task_yes'],
        'tcr': round(v['task_yes']/n, 3) if n else 0.0,
        'confirmation_count': v['confirmation_count'],
    })

summary_path = os.path.join(ROOT, 'analysis', 'confirm_all_persistent_summary.csv')
with open(summary_path, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=['run','n','attack_successes','asr','task_successes','tcr','confirmation_count'])
    w.writeheader()
    for r in summary_rows:
        w.writerow(r)

print(run_table_path)
print(summary_path)
