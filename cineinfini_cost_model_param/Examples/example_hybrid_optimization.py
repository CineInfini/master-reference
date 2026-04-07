#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Optimise the trade-off between AI iterations and human supervision.
"""

import sys
sys.path.append('..')
from src.cineinfini_cost_model_param import compute_cost_ia

def compute_hybrid_cost(base_ai_cost, rejection_rate, human_hours, human_rate=50.0):
    ai_cost = base_ai_cost * (1 + rejection_rate)
    human_cost = human_hours * human_rate
    return ai_cost + human_cost

# Base AI cost for a 90-min film (median scenario, zero regeneration)
base_params = {
    "film_duration_sec": 5400,
    "vfx_duration_sec": 1200,
    "regen_video": 0.0,   # no regeneration for base cost
    "regen_tts": 0.0,
    "regen_music": 0.0,
    "regen_vfx": 0.0,
    "regen_editing": 0.0
}
base_ai_cost = compute_cost_ia(scenario="medium", user_params=base_params)
print(f"Base AI cost (zero rejection): {base_ai_cost:.2f} USD\n")

rejection_rates = [0.5, 2, 5, 10, 20, 50, 100]
human_hours_list = [0, 1, 5, 10, 20, 40]

print("Rejection rate | Human hours | Total cost (USD)")
print("-" * 50)
for r in rejection_rates:
    for h in human_hours_list:
        total = compute_hybrid_cost(base_ai_cost, r, h)
        print(f"{r:14.1f} | {h:11} | {total:14.2f}")
