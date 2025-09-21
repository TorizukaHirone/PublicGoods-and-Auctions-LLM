# PublicGoods-and-Auctions-LLM

Two parallel LLM-based experiments for **COMSCI/ECON 206** at Duke Kunshan University:

1. **Public Goods (PS1)** — 2‑player game with endowment 100 and multiplier 1.5.
2. **Auctions (PS2)** — winner’s curse test in first‑price common‑value auctions with LLM bidders.

---

## Repository Structure

* `economist/` — Theoretical background, references, and supporting materials.
* `computational_scientist/` — Jupyter notebook implementing Nash equilibrium computation with NashPy, plus GTE screenshots.
* `behavioral_scientist/` — oTree application (zip), session screenshots, and large language model (LLM) transcripts.
* `mechanism_design/` — **PS2**: Winner’s Curse with LLM bidders (data, prompts, scoring script, figures, results).

---

## How to Reproduce

### Project A — Public Goods (PS1)

1. **Theory (Economist)**
   See `economist/README.md` and the references in `economist/refs/`.

2. **Computational Scientist**
   Open `computational_scientist/notebook.ipynb` in Google Colab or Jupyter.
   Requirements: Python 3.10+, NashPy ≥ 0.0.38, NumPy, Matplotlib.
   Run all cells to reproduce payoff matrices, equilibrium computation, and the welfare table.

3. **Behavioral Scientist**
   Unzip `behavioral_scientist/otree_app.zip`.
   Run locally with oTree 5.x:

   ```bash
   otree devserver
   ```

   Navigate to [http://localhost:8000](http://localhost:8000) to play the public goods game.
   See screenshots in `behavioral_scientist/screenshots/` for session results.
   See `behavioral_scientist/llm/` for prompts and transcripts of the LLM sessions.

### Project B — Auctions / Winner’s Curse (PS2)

Go to `mechanism_design/` and follow its README. In short:

1. Use `prompts/` to obtain **30‑line integer** bids for each **model × template × bidder**.
2. Save outputs to `mechanism_design/results/<Model>_<template>_bidderK.txt` (K∈{1,2,3,4}).
3. Score and visualize:

   ```bash
   python mechanism_design/scripts/collect_and_score.py
   ```
4. Figures (`profit_by_treatment.png`, `b_minus_V_win_dist.png`) and summary tables will be written to `mechanism_design/results/`.

---

## Software and Tools

* [NashPy](https://doi.org/10.21105/joss.03778) — equilibria in 2‑player games.
* [Game Theory Explorer](http://www.gametheoryexplorer.org/) — extensive‑form modeling.
* [oTree](https://www.otreehub.com/) — behavioral experiments.
* **PS2 analysis**: Python 3.10+, NumPy, Pandas, Matplotlib (see `mechanism_design/README.md`).
