# CineInfini Parametric Cost Model

This repository contains the parametric cost model for AI‑generated films (mode AI), as described in the paper  
*"A Parametric Cost Model for AI‑Driven Film Production: Realistic Estimates and Sensitivity Analysis"*.

The model estimates the **technical rendering cost** (video, audio, VFX, AI editing) of a 90‑minute feature film generated entirely by AI.  
All constants are defined with low/medium/high intervals, and the user can adjust film duration, VFX duration, regeneration rates for each component, and currency.

**Key assumptions (version 6.2):**  
- Cinema‑quality video cost: **$0.40 per second** (median)  
- Video regeneration attempts per shot: **25** (range 20–30)  
- Lower regeneration rates for TTS (0.2), music (0.2), VFX (0.5), editing (0.2)  
- 90‑min film ≈ 1,200 shots (5 seconds each)  

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
```

**Expected output:**

```
{'low': 34000.00, 'medium': 56000.00, 'high': 84000.00}
```

> *Note: These are **technical rendering costs** only. They exclude human labour, marketing, licensing, and quality assurance.*

---

## Usage Examples

### 1. Single scenario (medium, default parameters)

```python
cost = compute_cost_ia(scenario='medium')
print(f"Median technical rendering cost: {cost:.2f} USD")
```

**Expected output:**

```
Median technical rendering cost: 56000.00 USD
```

### 2. Custom film duration (e.g., 120 minutes)

```python
custom = {"film_duration_sec": 7200, "vfx_duration_sec": 1800}
cost = compute_cost_ia(scenario='medium', user_params=custom)
print(f"120 min film cost: {cost:.2f} USD")
```

**Expected output (approximate):**

```
120 min film cost: 74700.00 USD
```

### 3. Compare all three scenarios

```python
costs = compute_cost_ia(scenario='all')
for k, v in costs.items():
    print(f"{k.capitalize():6s} : {v:.2f} USD")
```

**Expected output:**

```
Low    : 34000.00 USD
Medium : 56000.00 USD
High   : 84000.00 USD
```

### 4. Sensitivity analysis – vary video regeneration rate

The regeneration rate (attempts per shot) strongly influences total cost. You can override it directly in `user_params`:

```python
for regen in [20, 25, 30]:
    params = {"regen_video": regen}
    cost = compute_cost_ia(scenario="medium", user_params=params)
    print(f"Video regeneration rate {regen}: {cost:.2f} USD")
```

**Expected output (linear scaling):**

```
Video regeneration rate 20: 46700.00 USD
Video regeneration rate 25: 56000.00 USD
Video regeneration rate 30: 65300.00 USD
```

### 5. Sensitivity analysis – vary video cost per second

```python
for vc in [0.30, 0.40, 0.50]:
    # Temporarily override the constant in INTERVALS (advanced)
    import cineinfini_cost_model_param as cm
    original = cm.INTERVALS["VIDEO_AI_COST_PER_SEC"]
    cm.INTERVALS["VIDEO_AI_COST_PER_SEC"] = (vc, vc, vc)
    cost = compute_cost_ia(scenario="medium")
    cm.INTERVALS["VIDEO_AI_COST_PER_SEC"] = original
    print(f"Video cost ${vc}/s: {cost:.2f} USD")
```

**Expected output (linear scaling):**

```
Video cost $0.30/s: 42000.00 USD
Video cost $0.40/s: 56000.00 USD
Video cost $0.50/s: 70000.00 USD
```

### 6. Adjust regeneration rates for other components

```python
params = {"regen_tts": 0.5, "regen_music": 0.5, "regen_vfx": 1.0, "regen_editing": 0.5}
cost = compute_cost_ia(scenario="medium", user_params=params)
print(f"Cost with higher non‑video regeneration: {cost:.2f} USD")
```

### 7. Visualisation (requires matplotlib)

```python
import matplotlib.pyplot as plt

costs = compute_cost_ia(scenario='all')
scenarios = list(costs.keys())
values = list(costs.values())

plt.bar(scenarios, values, color=['green', 'orange', 'red'])
plt.ylabel('Technical rendering cost (USD)')
plt.title('CineInfini cost estimates (90 min AI film)')
plt.show()
```

**Expected output:** A bar chart with three bars labelled low (≈34k), medium (≈56k), high (≈84k).

---

## Constants and Parameters

All constants (shot duration, dialogue ratio, AI costs, human costs, etc.) are defined with **low, medium, and high** values. They are documented in:

- **`constants/Constants.md`** – human‑readable tables with references.
- **`src/cineinfini_cost_model_param.py`** – the `INTERVALS` dictionary.

User‑adjustable parameters (film duration, VFX duration, regeneration rates, currency) are in `DEFAULT_PARAMS` and can be overridden via `user_params`.

| Variable | Description | Default | Range | Unit |
|----------|-------------|---------|-------|------|
| `film_duration_sec` | Film duration | 5400 | 3600–7200 | s |
| `vfx_duration_sec` | VFX duration | 1200 | 600–2400 | s |
| `regen_video` | Video regeneration attempts per shot | 25 | 20–30 | – |
| `regen_tts` | TTS regeneration attempts | 0.2 | 0–1 | – |
| `regen_music` | Music regeneration attempts | 0.2 | 0–1 | – |
| `regen_vfx` | VFX regeneration attempts | 0.5 | 0–2 | – |
| `regen_editing` | Editing regeneration attempts | 0.2 | 0–1 | – |
| `currency` | Currency | USD | – | – |

---

## Dependencies

- **Python 3.8+** (no external libraries required for basic computation)
- Optional: `pandas`, `matplotlib` for advanced analysis and plotting.

---

## License

This project is licensed under the **MIT License** – see the [LICENSE](../LICENSE) file for details.

---

## Citation

If you use this code or data in your research, please cite:

> Benbrahim, S.-E. (2026). CineInfini Master Reference – constants, parameters, and code. GitHub.  
> https://github.com/CineInfini/master-reference/tree/main/cineinfini_cost_model_param

And the associated paper (submitted to ACM AI Letters).

---

## Notes on Reproducibility

All numerical values are exposed as parameters. You can reproduce the results in the paper by running the default configuration. To explore alternative scenarios (different video costs, regeneration rates, film lengths), simply modify the corresponding parameters as shown in the examples above.

For a complete sensitivity analysis (Sobol indices), refer to the Jupyter notebook `sensitivity_analysis.ipynb`.
