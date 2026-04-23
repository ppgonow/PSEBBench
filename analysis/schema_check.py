#!/usr/bin/env python3
"""Validate scenario YAMLs for required fields.

Usage:
  python3 analysis/schema_check.py
"""
import glob
import sys
import yaml

REQUIRED = [
    'id','name','type','injection_source','injection_style','target_risk','target_chain','prompt','oracle_expectations'
]
RECOMMENDED = [
    'intent.user_intent','intent.required_action',
    'adversary.authority','adversary.source',
    'risk.class','risk.escalation',
    'attack_strength'
]


def get_nested(d, key):
    cur = d
    for part in key.split('.'):
        if not isinstance(cur, dict) or part not in cur:
            return None
        cur = cur[part]
    return cur

paths = glob.glob('scenarios/**/*.yaml', recursive=True)
missing_required = []
missing_recommended = []

for p in paths:
    with open(p,'r',encoding='utf-8') as f:
        data = yaml.safe_load(f)
    if not data:
        continue
    for k in REQUIRED:
        if k not in data:
            missing_required.append((p,k))
    for k in RECOMMENDED:
        if get_nested(data,k) is None:
            missing_recommended.append((p,k))

print(f"checked {len(paths)} files")
print(f"missing required: {len(missing_required)}")
print(f"missing recommended: {len(missing_recommended)}")
if missing_required:
    for p,k in missing_required[:50]:
        print('REQ',p,k)
    sys.exit(1)

if missing_recommended:
    for p,k in missing_recommended[:50]:
        print('REC',p,k)
"""End"""
