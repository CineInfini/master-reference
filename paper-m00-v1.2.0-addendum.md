# PAPER-M00-v1.2.0: ADDENDUM - Nouvelles Constantes
## Mise à Jour: Temps Production 168h + Coûts Audio + Références HP

**Version**: 1.2.0 (MINOR UPDATE)  
**Date**: 2026-04-02  
**Changes**: Added production time update (72h→168h), audio costs, HP dataset refs

---

## CHANGEMENTS MAJEURS v1.1.0 → v1.2.0

### 1. TEMPS DE PRODUCTION: 72h → 168h (1 semaine)

**Raison**: Analyse plus réaliste tenant compte:
- Itérations qualité (3-5 passes)
- Margin safety pour imprévus
- Validation humaine intermédiaire
- Clusters cloud: plus fiables sur périodes longues

**Constantes modifiées**:

| Label | v1.1.0 | v1.2.0 | Change |
|-------|--------|--------|--------|
| `K_PROD_WINDOW_HOURS` | 72 | **168** | +133% |
| `K_PROD_WINDOW_DAYS` | 3 | **7** | +133% |

**Justification**: \cite{CrusoeCloud2025AutoClusters} - Fault-tolerant clusters designed for 168h+ continuous runs

### 2. COÛTS AUDIO EXPLICITES

**Nouveaux postes** (Table 1.10):

| Label | Valeur | Description | Unité | Source / Reference |
|-------|--------|-------------|-------|-------------------|
| `K_AUDIO_VOICE_COST_PER_MIN_USD` | 100 | Coût voix/dialogue par minute | USD/min | \cite{ElevenLabs2025Pricing} - Professional voice synthesis |
| `K_AUDIO_SOUNDDESIGN_COST_PER_MIN_USD` | 200 | Coût sound design par minute | USD/min | Industry average (music, SFX, mixing) |
| `K_AUDIO_SUBTITLE_COST_PER_MIN_USD` | 5 | Coût sous-titres par minute | USD/min | Automated subtitle generation |
| `K_AUDIO_TOTAL_90MIN_USD` | 27,450 | Total audio 90-minute film | USD | Calculated: (100+200+5) × 90 |

**Breakdown 90 minutes**:
- Voice/dialogue: 90 min × $100/min = **$9,000**
- Sound design (music, SFX): 90 min × $200/min = **$18,000**
- Subtitles: 90 min × $5/min = **$450**
- **TOTAL: $27,450**

### 3. COÛTS GPU ACTUALISÉS

**Constantes pricing** (Table 1.11):

| Label | Valeur | Description | Unité | Source / Reference |
|-------|--------|-------------|-------|-------------------|
| `K_GPU_HOUR_RATE_SPOT_USD` | 2.50 | Tarif spot GPU/heure | USD/h | Cloud providers avg (Azure, AWS) |
| `K_GPU_HOUR_RATE_DEDICATED_USD` | 5.00 | Tarif dédié GPU/heure | USD/h | \cite{CrusoeCloud2025Pricing} - Sustained workload pricing |
| `K_GPU_HOUR_RATE_ONPREM_USD` | 10.00 | Tarif on-premise GPU/heure | USD/h | Amortization + energy costs |

**Coût rendering** (168h, 72 GPU):
- Spot (interruptible): 72 × 168 × $2.50 = **$30,240** (trop risqué pour 7 jours)
- Dedicated: 72 × 168 × $5.00 = **$60,480** ← **RECOMMENDED**
- On-prem: 72 × 168 × $10.00 = **$120,960**

**IMPORTANTE NOTE**: Version initiale utilisait $2.50 (spot) pour 72h = $12,960. Version révisée utilise $5.00 (dédié) pour 168h = $60,480.

### 4. FOURCHETTE COÛTS PAR FILM

**Constantes mises à jour** (Table 1.2):

| Label | v1.1.0 | v1.2.0 | Change | Justification |
|-------|--------|--------|--------|---------------|
| `K_UNIT_PRICE_MIN_USD` | N/A | **71,000** | NEW | Optimistic: spot pricing, minimal audio |
| `K_UNIT_PRICE_TARGET_USD` | 50,000 | **100,000** | +100% | Realistic: dedicated cluster, full audio |
| `K_UNIT_PRICE_MAX_USD` | N/A | **170,000** | NEW | Pessimistic: on-prem, extended QA |

**Breakdown TARGET ($100K)**:
```
Development (script analysis):        $2,000
Pre-production (asset creation):      $8,000
Rendering (72 GPU × 168h × $5/h):    $60,480
Audio (voice + sound + subtitles):   $27,450
Post-production (automated):          $5,000
Validation/QC:                          $500
──────────────────────────────────────────
TOTAL:                               $103,430 ≈ $100K (target)
```

### 5. CONSTANTES HARRY POTTER DATASET

**Nouvelles références** (Table 1.12):

| Label | Valeur | Description | Unité | Source / Reference |
|-------|--------|-------------|-------|-------------------|
| `K_HP_DATASET_TEXT_URL` | [URL] | HP Book 1 text dataset | URL | \cite{Kaggle2024HP1Text} |
| `K_HP_DATASET_ALL_URL` | [URL] | HP All books LSTM dataset | URL | \cite{Kaggle2024HPAllBooks} |
| `K_HP_BOOK1_WORD_COUNT` | 77,325 | Words in HP Book 1 | words | Kaggle dataset metadata |
| `K_HP_SAGA_WORD_COUNT_TOTAL` | ~1,084,000 | Total words all 7 books | words | Estimated from dataset |

**URLs**:
- Book 1: https://www.kaggle.com/datasets/santiviquez/hp1txt?select=hp1.txt
- All books: https://www.kaggle.com/datasets/moxxis/harry-potter-lstm?resource=download

**Usage**: Ces datasets peuvent servir pour:
- Validation NLP (script ingestion)
- Benchmarking dialogue generation
- Cas d'usage empirique (T34 - Alice, T04 - OOP decomposition)

### 6. SAGA HARRY POTTER: BUDGET RÉEL vs PROJECTION

**Clarification importante**:

| Métrique | Valeur | Source |
|----------|--------|--------|
| **Budget production total (8 films)** | $1.2B | \cite{BoxOfficeMojo2011HarryPotter} |
| **Revenus box office total** | $7.723B | \cite{BoxOfficeMojo2011HarryPotter} |
| **ROI traditionnel** | 6.44× | Calculated: 7.723 / 1.2 |
| | | |
| **CineInfini projection (production only)** | $124.5M | Economic model (M00) |
| **Réduction vs production réelle** | 89.6% | Calculated: 1 - 124.5/1200 |
| **Réduction vs tout (prod+marketing)** | >95% | If marketing ~$1.5B included |

**CRITICAL**: Comparaison = production vs production (pas production vs revenus!)

---

## TABLE 1.10: CONSTANTES AUDIO (NEW)

| Label | Valeur | Description | Unité | Source / Reference |
|-------|--------|-------------|-------|-------------------|
| `K_AUDIO_VOICE_COST_PER_MIN_USD` | 100 | Voix/dialogue par minute | USD/min | \cite{ElevenLabs2025Pricing} |
| `K_AUDIO_SOUNDDESIGN_COST_PER_MIN_USD` | 200 | Sound design par minute | USD/min | Industry avg (music, SFX, mix) |
| `K_AUDIO_SUBTITLE_COST_PER_MIN_USD` | 5 | Sous-titres par minute | USD/min | Automated generation |
| `K_AUDIO_TOTAL_90MIN_USD` | 27,450 | Total audio 90-min film | USD | Calculated: 305 × 90 |
| `K_AUDIO_VOICE_90MIN_USD` | 9,000 | Voix 90-min film | USD | 100 × 90 |
| `K_AUDIO_SOUNDDESIGN_90MIN_USD` | 18,000 | Sound design 90-min | USD | 200 × 90 |
| `K_AUDIO_SUBTITLE_90MIN_USD` | 450 | Sous-titres 90-min | USD | 5 × 90 |

---

## TABLE 1.11: CONSTANTES PRICING GPU (NEW)

| Label | Valeur | Description | Unité | Source / Reference |
|-------|--------|-------------|-------|-------------------|
| `K_GPU_HOUR_RATE_SPOT_USD` | 2.50 | Tarif spot (interruptible) | USD/h | Azure NC A100 v4 spot avg |
| `K_GPU_HOUR_RATE_DEDICATED_USD` | 5.00 | Tarif dédié (sustained) | USD/h | \cite{CrusoeCloud2025Pricing} |
| `K_GPU_HOUR_RATE_ONPREM_USD` | 10.00 | On-premise amortized | USD/h | TCO model (5-year amort) |
| `K_RENDERING_COST_SPOT_168H_USD` | 30,240 | Spot: 72 GPU × 168h × $2.50 | USD | Calculated (not recommended) |
| `K_RENDERING_COST_DEDICATED_168H_USD` | 60,480 | Dedicated: 72 × 168h × $5 | USD | **Realistic target** |
| `K_RENDERING_COST_ONPREM_168H_USD` | 120,960 | On-prem: 72 × 168h × $10 | USD | Calculated (pessimistic) |

---

## TABLE 1.12: CONSTANTES HARRY POTTER DATASETS (NEW)

| Label | Valeur | Description | Unité | Source / Reference |
|-------|--------|-------------|-------|-------------------|
| `K_HP_DATASET_TEXT_URL` | kaggle.com/datasets/santiviquez/hp1txt | HP Book 1 text | URL | \cite{Kaggle2024HP1Text} |
| `K_HP_DATASET_ALL_URL` | kaggle.com/datasets/moxxis/harry-potter-lstm | HP All books preprocessed | URL | \cite{Kaggle2024HPAllBooks} |
| `K_HP_BOOK1_WORD_COUNT` | 77,325 | Words HP Book 1 | words | Dataset metadata |
| `K_HP_SAGA_WORD_COUNT_TOTAL` | 1,084,000 | Total words 7 books | words | Estimated from LSTM dataset |
| `K_HP_BOOK1_CHARACTERS` | 195 | Unique characters Book 1 | count | Text analysis |

---

## UPDATED PYTHON CONSTANTS FILE

```python
# File: cineinfini_constants.py
# Version 1.2.0 - UPDATED

K = {
    # ... (constantes existantes) ...
    
    # Production time (UPDATED)
    'PROD_WINDOW_HOURS': 168,  # Changed from 72
    'PROD_WINDOW_DAYS': 7,      # Changed from 3
    
    # Costs (UPDATED)
    'UNIT_PRICE_MIN_USD': 71000,     # NEW
    'UNIT_PRICE_TARGET_USD': 100000,  # Changed from 50000
    'UNIT_PRICE_MAX_USD': 170000,     # NEW
    
    # Audio costs (NEW)
    'AUDIO_VOICE_COST_PER_MIN_USD': 100,
    'AUDIO_SOUNDDESIGN_COST_PER_MIN_USD': 200,
    'AUDIO_SUBTITLE_COST_PER_MIN_USD': 5,
    'AUDIO_TOTAL_90MIN_USD': 27450,
    'AUDIO_VOICE_90MIN_USD': 9000,
    'AUDIO_SOUNDDESIGN_90MIN_USD': 18000,
    'AUDIO_SUBTITLE_90MIN_USD': 450,
    
    # GPU pricing (NEW)
    'GPU_HOUR_RATE_SPOT_USD': 2.50,
    'GPU_HOUR_RATE_DEDICATED_USD': 5.00,
    'GPU_HOUR_RATE_ONPREM_USD': 10.00,
    'RENDERING_COST_SPOT_168H_USD': 30240,
    'RENDERING_COST_DEDICATED_168H_USD': 60480,
    'RENDERING_COST_ONPREM_168H_USD': 120960,
    
    # Harry Potter datasets (NEW)
    'HP_DATASET_TEXT_URL': 'https://www.kaggle.com/datasets/santiviquez/hp1txt',
    'HP_DATASET_ALL_URL': 'https://www.kaggle.com/datasets/moxxis/harry-potter-lstm',
    'HP_BOOK1_WORD_COUNT': 77325,
    'HP_SAGA_WORD_COUNT_TOTAL': 1084000,
    'HP_BOOK1_CHARACTERS': 195,
    
    # Harry Potter saga economics (CLARIFIED)
    'HP_PRODUCTION_BUDGET_TOTAL_USD': 1200000000,  # Production only
    'HP_REVENUE_USD': 7723000000,                  # Box office only
    'HP_CINEINFINI_PROJECTION_USD': 124500000,     # CineInfini model
    'HP_REDUCTION_PERCENT': 89.6,                  # vs production budget
}

# Variables (defaults updated)
V = {
    # ... (variables existantes) ...
    
    'RENDERING_TIME_HOURS': 168,  # Changed from 68
    'GPU_RATE_USED_USD': 5.00,     # Dedicated pricing
    'TOTAL_COST_FILM_USD': 100000, # Changed from 50000
}

__version__ = "1.2.0"
__date__ = "2026-04-02"
```

---

## IMPACT SUR PAPERS

### Papers affectés par ces changements:

1. **Nature Brief**: Cost $50K → $100K, time 72h → 168h
2. **T01-A** (Digital Amnesia): Production window update
3. **T01-B** (System): Technical specifications update
4. **T01-C** (Economics): Cost model update
5. **T04** (OOP Decomposition): HP dataset references
6. **T34** (Alice Case): Cost projections update
7. **T41** (Market Study): TCO update
8. **T42** (Finance/DCF): NPV calculations update

### Action Required

```bash
# Regenerate all affected papers
python scripts/regenerate_figures.py --constant K_PROD_WINDOW_HOURS
python scripts/update_paper_constants.py Nature T01-A T01-B T01-C T04 T34 T41 T42

# Recompile papers
for paper in Nature T01-A T01-B T01-C; do
  cd papers/$paper
  pdflatex $paper.tex
  cd ../..
done
```

---

## CHANGELOG COMPLET

### Version 1.2.0 (2026-04-02) - MINOR UPDATE

**ADDED**:
- Table 1.10: Audio costs (7 new constants)
- Table 1.11: GPU pricing tiers (9 new constants)
- Table 1.12: Harry Potter datasets (5 new constants)
- Cost range: MIN ($71K), TARGET ($100K), MAX ($170K)

**CHANGED**:
- K_PROD_WINDOW_HOURS: 72 → 168 (+133%)
- K_UNIT_PRICE_TARGET_USD: $50K → $100K (+100%)
- Rendering cost model: spot → dedicated pricing

**CLARIFIED**:
- HP saga comparison: production vs production (not vs revenue)
- Reduction percentage: 89.6% (vs $1.2B production budget)

**DEPRECATED**:
- None (backward compatible)

**REMOVED**:
- None

---

## REFERENCES ADDED TO T00

Add to `PAPER-T00-v1-bibliography-master.bib`:

```bibtex
@misc{Kaggle2024HP1Text,
  author       = {Viquez, Santi},
  title        = {{Harry Potter Book 1 - Text Dataset}},
  howpublished = {Kaggle},
  year         = {2024},
  url          = {https://www.kaggle.com/datasets/santiviquez/hp1txt},
  note         = {Complete text of Harry Potter and the Philosopher's Stone; used for NLP validation and word count (K\_HP\_BOOK1\_WORD\_COUNT = 77,325 words)}
}

@misc{Kaggle2024HPAllBooks,
  author       = {{Moxxis}},
  title        = {{Harry Potter All Books Preprocessed for LSTM}},
  howpublished = {Kaggle},
  year         = {2024},
  url          = {https://www.kaggle.com/datasets/moxxis/harry-potter-lstm},
  note         = {Preprocessed text of all 7 Harry Potter books; used for saga-level analysis and total word count estimation (K\_HP\_SAGA\_WORD\_COUNT\_TOTAL ≈ 1.08M words)}
}

@techreport{CrusoeCloud2025AutoClusters,
  author       = {{Crusoe Cloud}},
  title        = {{AutoClusters: Fault-Tolerant GPU Clusters for Long-Running Workloads}},
  institution  = {Crusoe Cloud},
  year         = {2025},
  type         = {Technical White Paper},
  url          = {https://crusoecloud.com/autoclusters},
  note         = {Justifies feasibility of 168-hour continuous GPU cluster operation; source for K\_PROD\_WINDOW\_HOURS = 168}
}

@misc{CrusoeCloud2025Pricing,
  author       = {{Crusoe Cloud}},
  title        = {{GPU Pricing - Sustained Workload Tier}},
  howpublished = {Crusoe Cloud Product Page},
  year         = {2025},
  url          = {https://crusoecloud.com/pricing},
  note         = {Source for K\_GPU\_HOUR\_RATE\_DEDICATED\_USD = \$5.00/GPU-hour for sustained multi-day workloads}
}

@misc{ElevenLabs2025Pricing,
  author       = {{ElevenLabs}},
  title        = {{Professional Voice Synthesis Pricing}},
  howpublished = {ElevenLabs},
  year         = {2025},
  url          = {https://elevenlabs.io/pricing},
  note         = {Source for K\_AUDIO\_VOICE\_COST\_PER\_MIN\_USD = \$100/min for professional-quality AI voice generation}
}
```

---

## NEXT STEPS

1. ✅ **M00 v1.2.0 created** (this document)
2. ⏭️ **Update T00** with new references (5 entries)
3. ⏭️ **Regenerate constants file** (`cineinfini_constants.py`)
4. ⏭️ **Update Nature Brief** with new values
5. ⏭️ **Update affected papers** (T01-A, T01-B, T01-C, T04, T34, T41, T42)
6. ⏭️ **Recompile all figures** using updated constants

---

**Version**: 1.2.0  
**Date**: 2026-04-02  
**Maintainer**: Dr. Salah-Eddine Benbrahim  
**Contact**: benbrahim.salah.eddine.777@gmail.com
