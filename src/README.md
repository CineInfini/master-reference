# CineInfini Parametric Cost Model

This repository contains the parametric cost model for AI‑generated films (mode IA), as described in the paper *"A Parametric Cost Model for Film Production: Unifying Human, Hybrid, and Generative AI Modes"*.

The model provides a reproducible, parameterisable way to estimate the production cost (excluding marketing) of a 90‑minute feature film generated entirely by AI. All constants are defined with low/medium/high intervals, and the user can adjust film duration, VFX duration, and other parameters.

---

## Repository Structure

| File / Folder | Description |
|---------------|-------------|
| `src/cineinfini_cost_model_param.py` | Main Python script with the cost model |
| `constants/Constants.md` | All constants, variables, and parameters with intervals and references |
| `bibliography/Bibliography.md` | Full list of references (academic, industry, legal) |
| `sensitivity_analysis.ipynb` | Jupyter notebook for interactive sensitivity analysis (optional) |
| `README.md` | This file |

---

## Quick Start

```python
from cineinfini_cost_model_param import compute_cost_ia

# Get low, medium, high costs for a standard 90‑minute film
costs = compute_cost_ia(scenario='all')
print(costs)
Output example:

text
{'low': 1198.00, 'medium': 2621.00, 'high': 9450.00}
Usage Examples
1. Single scenario (medium, default parameters)
python
cost = compute_cost_ia(scenario='medium')
print(f"Median cost: {cost:.2f} USD")
2. Custom film duration (e.g., 120 minutes)
python
custom = {"film_duration_sec": 7200, "vfx_duration_sec": 1800}
cost = compute_cost_ia(scenario='medium', user_params=custom)
print(f"120 min film cost: {cost:.2f} USD")
3. Compare all three scenarios
python
costs = compute_cost_ia(scenario='all')
for k, v in costs.items():
    print(f"{k.capitalize():6s} : {v:.2f} USD")
4. Sensitivity analysis – vary rejection rate
Note: To change a constant like REJECTION_RATE, you need to create a custom constants dictionary. This example shows how to override constants by creating a modified copy of the intervals.

python
from cineinfini_cost_model_param import INTERVALS, _get_constants_for_scenario, compute_cost_ia

def compute_with_rejection_rate(rej):
    # Create a custom intervals dict with a new rejection rate
    custom_intervals = INTERVALS.copy()
    custom_intervals["REJECTION_RATE"] = (rej, rej, rej)  # low=mid=high=rej
    # Temporarily replace INTERVALS (for advanced use)
    import cineinfini_cost_model_param as cm
    original = cm.INTERVALS
    cm.INTERVALS = custom_intervals
    cost = compute_cost_ia(scenario='medium')
    cm.INTERVALS = original
    return cost

for rej in [0.2, 0.5, 1.0, 2.0]:
    cost = compute_with_rejection_rate(rej)
    print(f"Rejection rate {rej}: {cost:.2f} USD")
5. Visualisation (requires matplotlib)
python
import matplotlib.pyplot as plt
costs = compute_cost_ia(scenario='all')
scenarios = list(costs.keys())
values = list(costs.values())
plt.bar(scenarios, values, color=['green', 'orange', 'red'])
plt.ylabel('Production cost (USD)')
plt.title('CineInfini cost estimates (90 min AI film)')
plt.show()
Constants and Parameters
All constants (shot duration, dialogue ratio, AI costs, human costs, etc.) are defined with low, medium, and high values. They are documented in:

constants/Constants.md – human‑readable tables with references.

src/cineinfini_cost_model_param.py – the INTERVALS dictionary.

User‑adjustable parameters (film duration, VFX duration, rejection rate, GPU price, currency) are in DEFAULT_PARAMS and can be overridden via user_params.

Dependencies
Python 3.8+ (no external libraries required for basic computation)

Optional: pandas, matplotlib for advanced analysis and plotting.

License
This project is licensed under the MIT License – see the LICENSE file for details.

Citation
If you use this code or data in your research, please cite:

Benbrahim, S.-E. (2026). CineInfini Master Reference – constants, parameters, and code. GitHub. https://github.com/CineInfini/master-reference

And the associated paper (preprint on arXiv, DOI pending).
