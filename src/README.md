# CineInfini Parametric Cost Model

This repository contains the parametric cost model for AI‑generated films, as described in the paper *"A Parametric Cost Model for Film Production..."*.

## Files

- `src/cineinfini_cost_model_param.py` – main Python script.
- `constants/Constants.md` – all constants with low/medium/high intervals.
- `bibliography/Bibliography.md` – full references.
- `sensitivity_analysis.ipynb` – Jupyter notebook for interactive exploration.

## Usage

```python
from src.cineinfini_cost_model_param import compute_cost_ia

# Get low, medium, high costs
costs = compute_cost_ia(scenario='all')
print(costs)
