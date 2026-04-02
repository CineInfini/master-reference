# PAPER-M00-v1.2.0: Master Constants for CineInfini Research

**Version**: 1.2.0  
**Date**: 2026-04-02  
**Status**: Canonical reference for all CineInfini publications

---

## Technical & Economic Constants

All values are referenced in research papers by their label (e.g., `K_GPU_COUNT_TARGET_INT`).

### 1. GPU Cluster Configuration

| Label | Value | Unit | Description |
|-------|-------|------|-------------|
| `K_GPU_COUNT_TARGET_INT` | 72 | GPUs | Target cluster size (NVIDIA H100/H200) |
| `K_GPU_VRAM_GB` | 80 | GB | VRAM per GPU (H100 SXM) |
| `K_GPU_HOUR_RATE_DEDICATED_USD` | 5 | USD/hour | Dedicated GPU hourly cost |
| `K_GPU_HOUR_RATE_SPOT_USD` | 2 | USD/hour | Spot instance hourly cost |

### 2. Production Parameters

| Label | Value | Unit | Description |
|-------|-------|------|-------------|
| `K_PROD_WINDOW_HOURS` | 168 | hours | Production time (1 week) |
| `K_PROD_WINDOW_DAYS` | 7 | days | Production time (1 week) |
| `K_MAX_FRAMES_OUTPUT_INT` | 129,600 | frames | 90 min @ 24 fps |
| `K_FILM_DURATION_MINUTES` | 90 | minutes | Standard feature film length |
| `K_FRAMERATE_FPS` | 24 | fps | Standard cinema framerate |

### 3. Audio Production Costs

| Label | Value | Unit | Description |
|-------|-------|------|-------------|
| `K_AUDIO_VOICE_COST_PER_MIN_USD` | 100 | USD/min | Voice/dialogue synthesis |
| `K_AUDIO_SOUNDDESIGN_COST_PER_MIN_USD` | 200 | USD/min | Music, SFX, mixing |
| `K_AUDIO_SUBTITLE_COST_PER_MIN_USD` | 5 | USD/min | Subtitle generation |
| `K_AUDIO_TOTAL_90MIN_USD` | 27,450 | USD | Total audio (90 min film) |

### 4. Quality Metrics

| Label | Value | Unit | Description |
|-------|-------|------|-------------|
| `K_BDS_TARGET` | 0.0012 | % | Target Biometric Drift Score |
| `K_BDS_THRESHOLD_MAX` | 0.005 | % | Maximum acceptable BDS |
| `K_AGENT_QUORUM` | 5 | agents | Minimum validation quorum |

### 5. Cost Projections

| Label | Value | Unit | Description |
|-------|-------|------|-------------|
| `K_UNIT_PRICE_MIN_USD` | 71,000 | USD | Minimum cost estimate (90 min) |
| `K_UNIT_PRICE_TARGET_USD` | 100,000 | USD | Target cost (90 min) |
| `K_UNIT_PRICE_MAX_USD` | 170,000 | USD | Maximum cost estimate (90 min) |
| `K_HP_CINEINFINI_PROJECTION_USD` | 450,000 | USD | HP saga (8 films) projection |

### 6. Industry Baselines

| Label | Value | Unit | Description |
|-------|-------|------|-------------|
| `K_LEGACY_BLOCKBUSTER_COST_USD` | 200,000,000 | USD | Average Hollywood blockbuster |
| `K_LEGACY_PROD_TIME_MONTHS_MIN` | 18 | months | Minimum traditional production |
| `K_LEGACY_PROD_TIME_MONTHS_MAX` | 36 | months | Maximum traditional production |
| `K_HP_PRODUCTION_BUDGET_TOTAL_USD` | 1,200,000,000 | USD | HP saga actual production budget |

### 7. Energy & Compute

| Label | Value | Unit | Description |
|-------|-------|------|-------------|
| `K_ENERGY_BUDGET_KWH` | 60,480 | kWh | Total energy (168h × 72 GPUs) |
| `K_CARBON_KG_CO2` | 18,144 | kg CO2 | Carbon footprint estimate |

---

## Usage

Reference constants in papers using their label:

**Example**:
```markdown
The system processes K_MAX_FRAMES_OUTPUT_INT frames over K_PROD_WINDOW_HOURS 
hours on a cluster of K_GPU_COUNT_TARGET_INT GPUs.
```

---

## Sources

All values are sourced from:
- NVIDIA official pricing (GPU costs)
- ElevenLabs pricing (audio synthesis)
- Box Office Mojo (Harry Potter budget data)
- Industry averages (production timelines)
- Analytical modeling (CineInfini projections)

---

**Last Updated**: 2026-04-02  
**Maintained by**: Dr. Salah-Eddine Benbrahim  
**Repository**: https://github.com/CineInfini/master-reference
