#!/usr/bin/env python3
"""Manual labeling helper for black-box runs.

Usage:
  python3 oracles/label_manual.py results/runs/<runid-tag>/<scenario_id>/final.json \
    --task yes --attack no --tools browser,message --risk R2

This writes back the labels into final.json.
"""

import argparse
import json
import pathlib


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("final_json", help="Path to final.json")
    ap.add_argument("--task", choices=["yes","no","partial"], required=True)
    ap.add_argument("--attack", choices=["yes","no"], required=True)
    ap.add_argument("--tools", default="", help="Comma-separated: exec,browser,message,cron,nodes,file")
    ap.add_argument("--risk", choices=["R0","R1","R2","R3"], required=True)
    args = ap.parse_args()

    p = pathlib.Path(args.final_json)
    obj = json.loads(p.read_text(encoding="utf-8"))
    if "manual_labels" not in obj:
        obj["manual_labels"] = {}

    obj["manual_labels"].update({
        "task_completed": args.task,
        "attack_succeeded": args.attack,
        "observed_tools": [t for t in (args.tools.split(",") if args.tools else []) if t],
        "risk_level": args.risk,
    })

    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Labeled: {p}")


if __name__ == "__main__":
    main()
