# CineInfini Parametric Cost Model

This repository contains the parametric cost model for AI‑generated films (mode AI), as described in the paper  
*"A Parametric Cost Model for AI‑Driven Film Production: Realistic Estimates and Sensitivity Analysis"* (submitted).

The model estimates the **technical rendering cost** (video, audio, VFX, AI editing) of a 90‑minute feature film generated entirely by AI.  
All constants are defined with low/medium/high intervals, and the user can adjust film duration, VFX duration, regeneration rates for each component, and currency.

**Key assumptions:**  
- Cinema‑quality video cost: **$0.40 per second** (median)  
- Video regeneration attempts per shot: **25** (range 20–30)  
- Lower regeneration rates for TTS (0.2), music (0.2), VFX (0.5), editing (0.2)  
- 90‑min film ≈ 1,200 shots (5 seconds each)  

---

## Repository Structure

| File / Folder | Description |
|---------------|-------------|
| [`src/cineinfini_cost_model_param.py`](src/cineinfini_cost_model_param.py) | Main Python script with the cost model |
| [`constants/Constants.md`](Constants/Constants.md) | All constants, variables, and parameters with intervals and references |
| [`bibliography/Bibliography.md`](Bibliography/Bibliography.md) | Full list of references (academic, industry, legal) |
| [`examples/`](examples/) | Example scripts (sensitivity analysis, calibration, etc.) |
| [`sensitivity_analysis.ipynb`](sensitivity_analysis.ipynb) | Jupyter notebook for interactive sensitivity analysis (optional) |
| `README.md` | This file |

**Direct links:** [constants](Constants/Constants.md) · [source code](src/cineinfini_cost_model_param.py) · [examples](examples/) · [bibliography](Bibliography/Bibliography.md)

---

## Constants and Parameters (Full Tables)

Full references are available in [`bibliography/Bibliography.md`](bibliography/Bibliography.md).

### Table 1 – Core constants (medium values)

| Constant | Description | Medium value | Unit | Reference |
|----------|-------------|--------------|------|-----------|
| `SHOT_DURATION_SEC` | Shot duration | 5 | s | [13] |
| `DIALOGUE_RATIO` | Dialogue proportion | 0.4 | – | [1] |
| `SPEECH_RATE_CHAR_PER_SEC` | Speech rate | 10 | char/s | [8] |
| `MUSIC_RATIO` | Music proportion | 0.7 | – | [9] |
| `VIDEO_AI_COST_PER_SEC` | AI video cost | 0.40 | USD/s | [21] |
| `TTS_COST_PER_CHAR` | TTS cost per char | 0.0003 | USD/char | [8,11] |
| `MUSIC_AI_COST_PER_SEC` | AI music cost | 0.03 | USD/s | [10] |
| `VFX_AI_COST_PER_SEC` | AI VFX cost | 0.01 | USD/s | [9] |
| `EDITING_AI_COST_PER_SEC` | AI editing cost | 0.005 | USD/s | [12] |
| `GPU_PRICE_PER_HOUR` | GPU rental (H100 spot) | 3.0 | USD/h | [19] |

### Table 2 – User‑adjustable variables

| Variable | Description | Default | Range | Unit | References |
|----------|-------------|---------|-------|------|-------------|
| `film_duration_sec` | Film duration | 5400 | 3600–7200 | s | [20] |
| `vfx_duration_sec` | VFX duration | 1200 | 600–2400 | s | Industry estimate |
| `regen_video` | Video regeneration attempts per shot | 25 | 20–30 | – | [7] |
| `regen_tts` | TTS regeneration attempts | 0.2 | 0–1 | – | [8,11] |
| `regen_music` | Music regeneration attempts | 0.2 | 0–1 | – | [10] |
| `regen_vfx` | VFX regeneration attempts | 0.5 | 0–2 | – | [9] |
| `regen_editing` | Editing regeneration attempts | 0.2 | 0–1 | – | [12] |
| `currency` | Currency | USD | – | – | User preference |

These regeneration rates are derived from reported high success rates of AI‑assisted audio, music, and post‑production tools, which typically require significantly fewer iterations than video generation [8,11,12].

---

## Quick Start

```python
from src.cineinfini_cost_model_param import compute_cost_ia

# Get low, medium, high costs for a standard 90‑minute film
costs = compute_cost_ia(scenario='all')
print(costs)
```

**Expected output (default parameters):**

```
{'low': 34220.00, 'medium': 56360.00, 'high': 83900.00}
```

> *Note: These are **technical rendering costs** only. They exclude human labour, marketing, licensing, and quality assurance.*

---

## Usage Examples

### 1. Single scenario (medium, default parameters)

```python
cost = compute_cost_ia(scenario='medium')
print(f"Median technical rendering cost: {cost:.2f} USD")
```

### 2. Custom film duration (e.g., 120 minutes)

```python
custom = {"film_duration_sec": 7200, "vfx_duration_sec": 1800}
cost = compute_cost_ia(scenario='medium', user_params=custom)
print(f"120 min film cost: {cost:.2f} USD")
```

### 3. Sensitivity analysis – vary video regeneration rate

```python
for regen in [20, 25, 30]:
    params = {"regen_video": regen}
    cost = compute_cost_ia(scenario="medium", user_params=params)
    print(f"Video regeneration rate {regen}: {cost:.2f} USD")
```

### 4. Visualisation (requires matplotlib)

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

---

## Dependencies

- **Python 3.8+** (no external libraries required for basic computation)
- Optional: `pandas`, `matplotlib` for advanced analysis and plotting.

---

## License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## Citation

If you use this code or data in your research, please cite:

> Benbrahim, S.-E. (2026). CineInfini Master Reference – constants, parameters, and code. GitHub.  
> https://github.com/CineInfini/master-reference/tree/main/cineinfini_cost_model_param

And the associated paper (submitted to ACM AI Letters).

---

## Notes on Reproducibility

All numerical values are exposed as parameters. You can reproduce the results in the paper by running the default configuration. To explore alternative scenarios (different video costs, regeneration rates, film lengths), simply modify the corresponding parameters as shown in the examples above.

For a complete sensitivity analysis (Sobol indices), refer to the Jupyter notebook `sensitivity_analysis.ipynb` and the script [`examples/example_sobol_sensitivity.py`](examples/example_sobol_sensitivity.py).
```

Vous pouvez copier ce contenu dans votre fichier `README.md`. Les liens sont actifs et pointent vers les bons emplacements (supposant que votre dépôt a la structure décrite).
