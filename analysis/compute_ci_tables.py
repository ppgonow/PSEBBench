#!/usr/bin/env python3
"""Compute ASR/TCR with Wilson 95% CIs for key slices.

Outputs:
- analysis/main_table_by_run.csv
- analysis/main_table_by_family.csv
- analysis/main_table_by_group.csv
- analysis/main_table_main_evidence.csv
"""

import csv
import glob
import json
import math
import os
from collections import Counter, defaultdict

FILES = glob.glob('results/runs/**/final.json', recursive=True)

# ----- helpers -----

def wilson_ci(k, n, z=1.96):
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    denom = 1 + z*z/n
    center = (p + z*z/(2*n)) / denom
    margin = (z * math.sqrt((p*(1-p) + z*z/(4*n)) / n)) / denom
    lo = max(0.0, center - margin)
    hi = min(1.0, center + margin)
    return (lo, hi)


def scenario_family(s):
    parts = s.split('-') if s else []
    if parts and parts[-1].isdigit():
        return '-'.join(parts[:-1])
    return s


rows = []
for fp in FILES:
    parts = fp.split(os.sep)
    if len(parts) < 4:
        continue
    scenario = parts[-2]
    run = parts[-3]
    group = scenario.split('-')[0] if scenario else 'UNK'
    family = scenario_family(scenario)

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
        'family': family,
        'task_completed': ml.get('task_completed') or ml.get('task_completed'.replace('_','')) or ml.get('task_completed', ''),
        'attack_succeeded': ml.get('attack_succeeded'),
        'confirmation_triggered': ml.get('confirmation_triggered'),
        'risk_level': ml.get('risk_level'),
        'observed_tools': ','.join(ml.get('observed_tools') or []),
        'path': fp,
    })


def agg(key):
    c = defaultdict(Counter)
    for r in rows:
        k = r[key]
        c[k]['n'] += 1
        if r['attack_succeeded'] == 'yes' or r['attack_succeeded'] is True:
            c[k]['attack_yes'] += 1
        if r['task_completed'] == 'yes' or r['task_completed'] is True:
            c[k]['task_yes'] += 1
        if r['task_completed'] == 'partial':
            c[k]['task_partial'] += 1
        if r['confirmation_triggered'] is True:
            c[k]['confirmation_count'] += 1
        if r['risk_level']:
            c[k][f"risk_{r['risk_level']}"] += 1
    return c


def to_table(counters):
    # gather columns
    cols = set(['key','n','attack_yes','task_yes','task_partial'])
    for k,ct in counters.items():
        cols |= set(ct.keys())
    cols = ['key'] + [c for c in sorted(cols) if c not in ('key')]

    out = []
    for k,ct in sorted(counters.items(), key=lambda kv: kv[1].get('n',0), reverse=True):
        n = ct.get('n',0)
        ay = ct.get('attack_yes',0)
        ty = ct.get('task_yes',0)
        asr = ay / n if n else 0.0
        tcr = ty / n if n else 0.0
        asr_lo, asr_hi = wilson_ci(ay, n)
        tcr_lo, tcr_hi = wilson_ci(ty, n)
        row = {'key': k, **ct,
               'asr': round(asr, 3), 'asr_ci_low': round(asr_lo, 3), 'asr_ci_high': round(asr_hi, 3),
               'tcr': round(tcr, 3), 'tcr_ci_low': round(tcr_lo, 3), 'tcr_ci_high': round(tcr_hi, 3)}
        out.append(row)
    return out


def write_csv(path, rows):
    if not rows:
        return
    cols = []
    for r in rows:
        for k in r.keys():
            if k not in cols:
                cols.append(k)
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in rows:
            w.writerow(r)


os.makedirs('analysis', exist_ok=True)

by_run = to_table(agg('run'))
by_family = to_table(agg('family'))
by_group = to_table(agg('group'))

write_csv('analysis/main_table_by_run.csv', by_run)
write_csv('analysis/main_table_by_family.csv', by_family)
write_csv('analysis/main_table_by_group.csv', by_group)

# Main evidence slice used in the paper
main_run_ids = {
    'r1-safe','r1-permissive','r2-safe','r2-permissive',
    'dp1-decision-proxy-strict','dp1-decision-proxy-naive',
    'p2-p2-proxy-strict','p2-p2-proxy-naive',
    'md2-model-strict','md2-model-permissive',
    'g1fixed-permissive','g2-permissive-guard','g2-strict-noguard','g1fixed-strict-guard',
    # live-agent 2x2 (model-driven decision path)
    'live5-permissive','live5-guard','live5-strict','live5-strict-guard'
}
main_rows = [r for r in by_run if r['key'] in main_run_ids]
write_csv('analysis/main_table_main_evidence.csv', main_rows)

print(f"Loaded {len(rows)} labeled finals from {len(FILES)} final.json files")
