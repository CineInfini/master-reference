#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CineInfini Parametric Cost Model
Author: Salah-Eddine Benbrahim
License: MIT
Repository: https://github.com/CineInfini/master-reference/tree/main/cineinfini_cost_model_param

This module provides a parametric cost model for AI‑generated films (mode AI).
All constants and variables are aligned with the paper version 7.12.
"""

from typing import Dict, Union

# ----------------------------------------------------------------------
# 1. Configuration defaults
# ----------------------------------------------------------------------
CONFIG = {
    "default_scenario": "medium",   # 'low', 'medium', 'high'
    "default_params": None,
}

# ----------------------------------------------------------------------
# 2. Intervals for all constants (low, medium, high)
#    Values updated for version 7.12:
#    - VIDEO_AI_COST_PER_SEC: medium = 0.40 USD/s (cinema quality)
#    - REGENERATION_RATE_VIDEO: range 20-30, default 25
# ----------------------------------------------------------------------
INTERVALS = {
    # Technical constants
    "SHOT_DURATION_SEC": (4.0, 5.0, 8.0),           # [13]
    "DIALOGUE_RATIO": (0.3, 0.4, 0.5),              # [1]
    "SPEECH_RATE_CHAR_PER_SEC": (8, 10, 12),        # [8]
    "MUSIC_RATIO": (0.6, 0.7, 0.8),                 # [9]

    # AI costs (updated: median video cost = 0.40 USD/s)
    "VIDEO_AI_COST_PER_SEC": (0.30, 0.40, 0.50),    # USD/s [21]
    "TTS_COST_PER_CHAR": (0.0001, 0.0003, 0.0005),  # USD/char [8,11]
    "MUSIC_AI_COST_PER_SEC": (0.01, 0.03, 0.05),    # USD/s [10]
    "VFX_AI_COST_PER_SEC": (0.01, 0.05, 0.10),      # USD/s [9]
    "EDITING_AI_COST_PER_SEC": (0.001, 0.005, 0.01),# USD/s [12]
    "GPU_SEC_PER_VIDEO_SEC": (60, 120, 600),        # GPU‑s/s (not used directly)
    "GPU_PRICE_PER_HOUR": (1.5, 3.0, 5.0),          # USD/h [19]
    "TRADITIONAL_VFX_COST_PER_SEC": (10000, 50000, 100000),  # USD/s

    # Human costs (traditional) – kept for completeness
    "ALIST_ACTOR_DAY": (500_000, 1_000_000, 2_000_000),
    "EXTRA_NON_UNION_DAY": (300, 500, 1000),
    "EXTRA_UNION_DAY": (2500, 2500, 2500),
    "SCREENWRITER_FLAT": (100_000, 250_000, 500_000),
    "DIRECTOR_FLAT": (500_000, 2_000_000, 10_000_000),
    "CREW_DAY": (500, 800, 1500),

    # Performance parameter: video regeneration attempts per shot
    "REGENERATION_RATE_VIDEO": (20.0, 25.0, 30.0),   # dimensionless [7]
}

# ----------------------------------------------------------------------
# 3. Default film parameters (user‑adjustable)
# ----------------------------------------------------------------------
DEFAULT_PARAMS = {
    "film_duration_sec": 5400,      # 90 minutes
    "vfx_duration_sec": 1200,       # 20 minutes
    "currency": "USD",              # USD, EUR, GBP
    # Regeneration rates for each component (defaults from paper)
    "regen_video": 25.0,            # attempts per shot (range 20-30)
    "regen_tts": 0.2,               # attempts for TTS (range 0-1)
    "regen_music": 0.2,             # attempts for music (range 0-1)
    "regen_vfx": 0.5,               # attempts for VFX (range 0-2)
    "regen_editing": 0.2,           # attempts for editing (range 0-1)
}

# ----------------------------------------------------------------------
# 4. Scenario to index mapping
# ----------------------------------------------------------------------
SCENARIO_TO_INDEX = {"low": 0, "medium": 1, "high": 2}

def _get_constants_for_scenario(scenario: str) -> Dict:
    """Return a dictionary of constants for the given scenario ('low', 'medium', 'high')."""
    idx = SCENARIO_TO_INDEX[scenario]
    return {key: values[idx] for key, values in INTERVALS.items()}

# ----------------------------------------------------------------------
# 5. Main cost function (mode AI)
# ----------------------------------------------------------------------
def compute_cost_ia(scenario: str = CONFIG["default_scenario"],
                    user_params: Dict = CONFIG["default_params"]) -> Union[float, Dict]:
    """
    Compute the production cost (excluding marketing) for a fully AI‑generated film.

    Parameters
    ----------
    scenario : str, optional
        One of 'low', 'medium', 'high', or 'all'.
        - 'low'   : optimistic (lowest constant values)
        - 'medium': median values
        - 'high'  : pessimistic (highest constant values)
        - 'all'   : return a dict with three keys 'low', 'medium', 'high'
    user_params : dict, optional
        Override default parameters (film_duration_sec, vfx_duration_sec, currency,
        and any regeneration rates).

    Returns
    -------
    float or dict
        Total production cost in the specified currency (default USD).
        If scenario == 'all', returns a dictionary with three entries.
    """
    if scenario == "all":
        return {
            "low": compute_cost_ia("low", user_params),
            "medium": compute_cost_ia("medium", user_params),
            "high": compute_cost_ia("high", user_params)
        }

    # Get constants for the selected scenario
    const = _get_constants_for_scenario(scenario)

    # Merge user parameters with defaults
    params = DEFAULT_PARAMS.copy()
    if user_params:
        params.update(user_params)

    film_duration = params["film_duration_sec"]
    vfx_duration = params["vfx_duration_sec"]
    # Use regeneration rates from params (overridable)
    regen_video = params.get("regen_video", const["REGENERATION_RATE_VIDEO"])
    regen_tts = params.get("regen_tts", 0.2)
    regen_music = params.get("regen_music", 0.2)
    regen_vfx = params.get("regen_vfx", 0.5)
    regen_editing = params.get("regen_editing", 0.2)

    shot_duration = const["SHOT_DURATION_SEC"]
    n_shots = film_duration / shot_duration

    # Video generation cost (per shot, with regenerations)
    video_cost = n_shots * shot_duration * const["VIDEO_AI_COST_PER_SEC"] * (1 + regen_video)

    # Text‑to‑speech (dialogues) – global, with regenerations
    dialogue_sec = film_duration * const["DIALOGUE_RATIO"]
    tts_cost = dialogue_sec * const["SPEECH_RATE_CHAR_PER_SEC"] * const["TTS_COST_PER_CHAR"] * (1 + regen_tts)

    # Music – global, with regenerations
    music_sec = film_duration * const["MUSIC_RATIO"]
    music_cost = music_sec * const["MUSIC_AI_COST_PER_SEC"] * (1 + regen_music)

    # VFX – global, with regenerations
    vfx_cost = vfx_duration * const["VFX_AI_COST_PER_SEC"] * (1 + regen_vfx)

    # Editing – global, with regenerations
    editing_cost = film_duration * const["EDITING_AI_COST_PER_SEC"] * (1 + regen_editing)

    total = video_cost + tts_cost + music_cost + vfx_cost + editing_cost
    return total

# ----------------------------------------------------------------------
# 6. Example usage (when script is run directly)
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("CineInfini Parametric Cost Model (Version 7.12)")
    print("===============================================\n")
    print("Production cost (excluding marketing) for a 90‑minute AI film:\n")

    costs = compute_cost_ia(scenario="all")
    for k, v in costs.items():
        print(f"  {k.capitalize():6s} : {v:.2f} {DEFAULT_PARAMS['currency']}")

    print("\nSensitivity analysis (varying video regeneration rate, medium scenario):")
    for regen in [20, 25, 30]:
        custom_params = {"regen_video": regen}
        cost = compute_cost_ia(scenario="medium", user_params=custom_params)
        print(f"  Video regeneration rate {regen} -> {cost:.2f} USD")
