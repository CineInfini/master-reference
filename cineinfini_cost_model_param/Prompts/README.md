# Prompts for figures generation (Gemini)

This document contains the exact prompts provided by Gemini (Google Imagen) that were used to generate the figures in the paper. The prompts are kept as originally received, without modification.

---

## Figure 1 – Pipeline diagram

**Image:** [`../Figures/figure1.png`](https://github.com/CineInfini/master-reference/blob/main/cineinfini_cost_model_param/Figures/figure1.png)

**Prompt (Gemini):**
> A precise, high-resolution professional flow diagram against a clean white background. The diagram consists of six rectangular boxes with slightly rounded corners, presented in a minimalist, flat vector style with subtle drop shadows for depth. All boxes are a uniform light blue color with thin grey borders. The boxes are arranged in two clean rows of three and connected by thin grey solid arrows. The top row of boxes contains the following text in a clear sans-serif font: 'Script analysis', 'Shot generation', and 'Human oversight'. The bottom row of boxes, precisely aligned below the top row, contains: 'Editing', 'Quality assurance', and 'Final film'. The solid grey arrows establish a clear sequential flow between these steps. A dashed grey arrow loops directly back from the bottom-left edge of the 'Quality assurance' box to the top-right edge of the 'Shot generation' box in the row above. Near this dashed loop arrow, clear, dark grey text in a clear font reads 'Regeneration (ex: 20–30 attempts)', with the text and arrow clearly separated. The alignment is clean and precise, with all six specific labels present. There are no other text labels, headers, footers, or extra decorative elements on the diagram.

---

## Figure 2 – Sensitivity line chart

**Image:** [`../Figures/figure2.png`](https://github.com/CineInfini/master-reference/blob/main/cineinfini_cost_model_param/Figures/figure2.png)

**Prompt (Gemini):**
> A professional, minimalist line chart on a solid white background. The X-axis is labeled 'Video regeneration attempts per shot' with a scale from 20 to 30. The Y-axis is labeled 'Technical rendering cost (USD)' with a scale from 30,000 to 90,000. A smooth, solid blue line connects three specific data points: (20, 34,200), (25, 56,360), and (30, 83,900). Each point is marked with a small blue dot and its value is clearly labeled. No grid lines, no background patterns, no title. High resolution, flat vector style, clean black text for labels.

---

## Figure 3 – Sobol sensitivity bar chart

**Image:** [`../Figures/figure3.png`](https://github.com/CineInfini/master-reference/blob/main/cineinfini_cost_model_param/Figures/figure3.png)

**Prompt (Gemini):**
> A professional bar chart on a solid white background. The Y-axis is labeled 'Sobol index (first-order)' with a scale from 0 to 0.7. The X-axis features five categories: 'Video cost', 'Video regeneration rate', 'Film duration', 'VFX duration', and 'VFX regeneration rate'. The bars are light blue with thin grey outlines. The bar heights correspond to these values: 0.65 (Video cost), 0.25 (Video regeneration rate), 0.05 (Film duration), 0.04 (VFX duration), and 0.01 (VFX regeneration rate). Minimalist flat vector style, no grid lines, no title, clean sans-serif typography, high resolution.

---

## Notes

- All images are stored in the [`../Figures/`](../Figures/) folder.
- The prompts above are the exact outputs from Gemini (Google Imagen) as received on April 7, 2026.
- For the dark‑theme, high‑tech versions (with titles and glowing effects), see the supplementary material (not included in the paper submission).
