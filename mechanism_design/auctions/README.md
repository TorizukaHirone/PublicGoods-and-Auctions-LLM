# Mechanism Design — Winner’s Curse with LLM Bidders

This package reproduces **Problem Set 2 (PS2)** for COMSCI/ECON 206: a first‑price **common‑value** auction where LLMs act as bidders. We evaluate a neutral **baseline** prompt versus a **debias** prompt (winner’s‑curse reminder) under **T2 only**.

* Condition: `n = 4` bidders, noise `σ = 20`, bid range `0–200`
* Rounds: `R = 30` (fixed), seed `= 42`
* Outcome: highest bid wins (ties random); `profit = V − b_win`

---

## Folder Layout

```
mechanism_design/
  data/         # fixed V and signals (seed=42, R=30)
  prompts/      # ready-to-paste SYSTEM/USER texts (per bidder × template)
  results/      # save model outputs here; scoring & figures are written here
  figs/         # optional: copy figures here for the paper
  scripts/      # scoring + plotting script
  README.md     # this file
```

**Key Files**

* `data/T2_seed42_R30.csv` — 30 draws of `V` and 4 bidders’ signals (truncated N(100, 20²)).
* `prompts/T2_seed42_R30_bidderK_{baseline|debias}_{SYSTEM|USER}.txt` — K ∈ {1,2,3,4}.
* `scripts/collect_and_score.py` — reads outputs, computes winners/profits, writes figures and tables.

---

## How to Run (Two Models × Two Templates)

You will produce **16 text files** total (8 per model): `baseline/ debias × bidder1..4`. Each file must contain **exactly 30 lines**, each line a single integer bid in `[0, 200]`.

1. **Query the model**
   For each model (e.g., `GPT-5`, `DeepSeek`) and each template:

* Open a new chat.
* Paste the corresponding `*_SYSTEM.txt` into the system role.
* Paste the matching `*_USER.txt` into the user message.
* Parameters: `temperature 0–0.3`, `top_p = 1`, `max_tokens ≈ 100`.
* Send. Ensure the reply is exactly 30 lines of integers (no extra text).

2. **Save outputs**
   Save the 30 lines to:

```
mechanism_design/results/<Model>_<template>_bidderK.txt
# e.g., results/GPT-5_baseline_bidder1.txt
```

Repeat for `bidder2/3/4`, and for `debias`.

3. **Score and plot**

```bash
python mechanism_design/scripts/collect_and_score.py
```

This writes:

* `results/bids_scored_T2.csv`
* `results/summary_T2.csv`
* `results/profit_by_treatment.png`
* `results/b_minus_V_win_dist.png`

> The script **auto-detects model names** from your file prefixes (e.g., `GPT-5_...`), so the figure legends match your labels.

---

## File Naming Rules (strict)

* Prefix must be the **model label** you want to appear in figures (e.g., `GPT-5`, `DeepSeek`).
* Template must be either `baseline` or `debias`.
* Suffix must be `bidder1` .. `bidder4`.

Examples:

```
results/DeepSeek_baseline_bidder3.txt
results/GPT-5_debias_bidder2.txt
```

---

## Data Dictionary

**`data/T2_seed42_R30.csv`**

* `round` — 1..30
* `V` — common value (truncated N(100,20²))
* `s1..s4` — real-valued signals for bidders 1..4
* `s1_int..s4_int` — integer-rounded signals (shown in prompts)

**`results/bids_scored_T2.csv`** (generated)

* `round, model, template, winner_bidder, V, b_win, profit`

**`results/summary_T2.csv`** (generated)

* `mean_profit, sd_profit, loss_rate, mean_b_win, sd_b_win, E_b_minus_V_win, sd_overbid` (grouped by model × template)

---

## Troubleshooting

* **Extra words/blank lines in replies** → resend: `Return EXACTLY 30 lines, each a single integer in [0,200]. No other text.`
* **Out-of-range numbers** → add: `Bid must be between 0 and 200.`
* **Figures not updating** → rerun the script; confirm the PNG timestamps changed; clear LaTeX aux files and recompile.

---

## Environment

* Python 3.10+
* Packages: `numpy`, `pandas`, `matplotlib`

```bash
pip install numpy pandas matplotlib
```

---

## Notes

* This PS2 release includes **T2 only**. Extending to C0/T1 follows the same format (new `data/` file + `prompts/` set).
* Figures and tables in the paper reference the files generated in `results/`. You may copy final images into `figs/` for the LaTeX build if desired.
