# Constants, variables and parameters for the CineInfini cost model

See [`Bibliography/Bibliography.md`](../Bibliography/Bibliography.md) for full citations.

---

## Table 1 – Core constants (medium values)

| Constant | Description | Medium value | Unit | Reference |
|----------|-------------|--------------|------|-----------|
| `SHOT_DURATION_SEC` | Shot duration | 5 | s | [13] |
| `DIALOGUE_RATIO` | Dialogue proportion | 0.4 | – | [1] |
| `SPEECH_RATE_CHAR_PER_SEC` | Speech rate | 10 | char/s | [8] |
| `MUSIC_RATIO` | Music proportion | 0.7 | – | [9] |
| `VIDEO_AI_COST_PER_SEC` | AI video cost | 0.40 | USD/s | [21] |
| `TTS_COST_PER_CHAR` | TTS cost per character | 0.0003 | USD/char | [8,11] |
| `MUSIC_AI_COST_PER_SEC` | AI music cost | 0.03 | USD/s | [10] |
| `VFX_AI_COST_PER_SEC` | AI VFX cost | 0.01 | USD/s | [9] |
| `EDITING_AI_COST_PER_SEC` | AI editing cost | 0.005 | USD/s | [12] |
| `GPU_PRICE_PER_HOUR` | GPU rental (H100 spot) | 3.0 | USD/h | [19] |

---

## Table 2 – User‑adjustable variables

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
