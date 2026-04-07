#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sobol sensitivity analysis for the CineInfini cost model.
Requires: pip install SALib
"""

import sys
sys.path.append('..')
import numpy as np
from SALib.sample import saltelli
from SALib.analyze import sobol
from src.cineinfini_cost_model_param import compute_cost_ia

# ----------------------------------------------------------------------
# 1. Define the parameter ranges (uniform distributions)
# ----------------------------------------------------------------------
problem = {
    'num_vars': 5,
    'names': ['video_cost',          # K_vid_cost (USD/s)
              'regen_video',         # V_regen_video (attempts per shot)
              'film_duration',       # V_duration (s)
              'vfx_duration',        # V_vfx_dur (s)
              'regen_vfx'],          # V_regen_vfx (attempts for VFX)
    'bounds': [[0.30, 0.50],         # video cost (low/medium/high range)
               [20.0, 30.0],         # video regeneration rate
               [3600, 7200],         # film duration (60-120 min)
               [600, 2400],          # VFX duration (10-40 min)
               [0.2, 1.0]]           # VFX regeneration rate
}

# ----------------------------------------------------------------------
# 2. Generate samples (Saltelli sampling)
# ----------------------------------------------------------------------
param_values = saltelli.sample(problem, 1024)  # 1024 * (2*5+2) = 12288 evaluations

# ----------------------------------------------------------------------
# 3. Evaluate model for each sample
# ----------------------------------------------------------------------
costs = []
for vals in param_values:
    user_params = {
        "video_ia_par_sec": vals[0],
        "regen_video": vals[1],
        "film_duration_sec": vals[2],
        "vfx_duration_sec": vals[3],
        "regen_vfx": vals[4],
        # Keep other components at default
        "regen_tts": 0.2,
        "regen_music": 0.2,
        "regen_editing": 0.2,
        "use_dynamic_video_cost": False
    }
    cost = compute_cost_ia(scenario="medium", user_params=user_params)
    costs.append(cost)

# ----------------------------------------------------------------------
# 4. Perform Sobol analysis
# ----------------------------------------------------------------------
Si = sobol.analyze(problem, np.array(costs), print_to_console=True)

# ----------------------------------------------------------------------
# 5. Print results in a table format
# ----------------------------------------------------------------------
print("\n=== Sobol Sensitivity Indices (First-order) ===\n")
print("Parameter           | S1 (first-order) | S1_conf | ST (total) | ST_conf")
print("-" * 70)
for i, name in enumerate(problem['names']):
    print(f"{name:20s} | {Si['S1'][i]:.4f}        | {Si['S1_conf'][i]:.4f}  | {Si['ST'][i]:.4f}   | {Si['ST_conf'][i]:.4f}")
