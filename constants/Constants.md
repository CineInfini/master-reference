# Constants, variables and parameters for the CineInfini cost model

See [Bibliography.md](../bibliography/Bibliography.md) for full citations.

---

## 1. Fixed constants (from literature)

| Constant | Description | Low | Medium | High | Unit | Reference |
|----------|-------------|-----|--------|------|------|-----------|
| DUREE_PLAN | Duration of a shot | 4 | 5 | 8 | s | [Vogel2020] |
| RATIO_DIALOGUES | Proportion of dialogue | 0.3 | 0.4 | 0.5 | | [Vogel2020] |
| CARACTERES_PAR_SEC | Speech rate | 8 | 10 | 12 | char/s | [ElevenLabs2026] |
| DUREE_MUSIQUE_RATIO | Proportion of music | 0.6 | 0.7 | 0.8 | | [MuseSteamer2025] |
| VIDEO_IA_PAR_SEC | AI video generation cost | 0.10 | 0.30 | 0.50 | USD/s | [Brooks2025] |
| TTS_COUT_PAR_CARACTERE | TTS cost per character | 0.0001 | 0.0003 | 0.0005 | USD/char | [ElevenLabs2026] |
| MUSIQUE_IA_PAR_SEC | AI music generation cost | 0.01 | 0.03 | 0.05 | USD/s | [MuseSteamer2025] |
| VFX_IA_PAR_SEC | AI VFX cost | 0.01 | 0.05 | 0.10 | USD/s | [MuseSteamer2025] |
| MONTAGE_IA_PAR_SEC | AI editing cost | 0.001 | 0.005 | 0.01 | USD/s | [Runway2025] |
| VIDEO_IA_GPU_PAR_SEC | GPU seconds per video second | 60 | 120 | 600 | GPU‑s/s | [MovieGen2024] |
| PRIX_GPU_HEURE | GPU rental price (H100 spot) | 1.5 | 3.0 | 5.0 | USD/h | [MovieGen2024] |
| VFX_TRADITIONNEL_PAR_SEC | Traditional VFX cost | 10 000 | 50 000 | 100 000 | USD/s | [MuseSteamer2025] |
| ACTEUR_VEDETTE_JOUR | A‑list actor per day | 500 000 | 1 000 000 | 2 000 000 | USD/day | [Vogel2020][MPA2025] |
| FIGURANT_JOUR | Non‑union extra per day | 300 | 500 | 1 000 | USD/day | [SAGindie2023] |
| FIGURANT_SYNDIQUE_JOUR | Union extra per day | 2 500 | 2 500 | 2 500 | USD/day | [SAGindie2023] |
| SCENARISTE_FORFAIT | Screenwriter per script | 100 000 | 250 000 | 500 000 | USD/script | [WGA] |
| REALISATEUR_FORFAIT | Director per film | 500 000 | 2 000 000 | 10 000 000 | USD/film | [DGA] |
| TECHNICIEN_JOUR | Crew member per day | 500 | 800 | 1 500 | USD/day | [Vogel2020] |

---

## 2. Percentage allocations (top‑down method)

| Constant | Description | Low | Medium | High | Reference |
|----------|-------------|-----|--------|------|-----------|
| DEV_PCT | Development | 5% | 7.5% | 10% | [Vogel2020] |
| ABOVE_PCT | Above‑the‑line | 20% | 25% | 30% | [Vogel2020] |
| BELOW_PCT | Below‑the‑line | 30% | 35% | 40% | [Vogel2020] |
| POST_PCT | Post‑production | 10% | 12.5% | 15% | [Vogel2020] |
| MARKETING_PCT | Marketing | 10% | 15% | 20% | [Vogel2020] |

---

## 3. User‑adjustable parameters

| Parameter | Description | Low | Medium | High | Default | Unit | Justification / Reference |
|-----------|-------------|-----|--------|------|---------|------|---------------------------|
| duree_film_sec | Film duration | 5400 | 5400 | 5400 | 5400 | s | 90 minutes fixed |
| duree_vfx_sec | VFX duration | 600 | 1200 | 2400 | 1200 | s | [MuseSteamer2025] |
| taux_rejet | Plan regeneration rate | 0.2 | 0.5 | 2.0 | 0.5 | | [Brooks2025] (estimated) |
| prix_gpu_hour | Effective GPU price | 1.5 | 3.0 | 5.0 | 3.0 | USD/h | [MovieGen2024] |
| devise | Currency | USD | USD | USD | USD | | User preference |

---

## 4. Notes

- All monetary values are in USD (default), but the `devise` parameter can be changed to EUR, GBP, etc.
- The `taux_rejet` (rejection rate) accounts for multiple regeneration attempts per shot. A value of 0.5 means 50% additional renders.
- The `prix_gpu_hour` reflects spot market prices for H100 GPUs; actual costs may vary.
- For a full explanation of the parametric model, please refer to the associated paper (preprint on arXiv, DOI pending).
