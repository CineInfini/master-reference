#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Validation case: Elephants Dream (2006, 11 min)
"""

import sys
sys.path.append('..')
from src.cineinfini_cost_model_param import compute_cost_ia

params = {
    "film_duration_sec": 660,
    "vfx_duration_sec": 600,
    "regen_video": 25,
    "regen_tts": 0.2,
    "regen_music": 0.2,
    "regen_vfx": 0.5,
    "regen_editing": 0.2
}
cost = compute_cost_ia(scenario="medium", user_params=params)
print(f"Estimated cost for Elephants Dream (median scenario): {cost:.2f} USD")
print("Note: Actual budget ≈ 142,000 USD (human artists).")
