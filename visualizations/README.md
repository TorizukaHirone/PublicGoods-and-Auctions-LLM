# Visualizations

This folder collects all figures used across PS1, PS2, PS3 (Reflection/Voting), and the Final Research Proposal. Images are grouped by component for clarity and reproducibility.

---

## 📘 PS1 — Theory (Economist & Computational Scientist)

| File | Description | Report Section |
|------|-------------|----------------|
| `colab_output.png` | Solver output from NashPy (grid discretization of contributions). | PS1 Part 2a (Normal Form & Computation) |
| `equilibrium_output.png` | Nash equilibrium computation confirming (0,0). | PS1 Part 2a |
| `gte_solution.png` | Screenshot of GTE solution panel. | PS1 Part 2b (Extensive Form & SPNE) |
| `gte_tree.png` | Extensive-form tree of the public goods game. | PS1 Part 2b |
| `payoff_matrices.png` | Payoff table for corner contributions. | PS1 Part 1.3 (Analytical Solution) |
| `welfare_table.png` | Social welfare table (maximized at full contributions). | PS1 Part 1.3 (Analytical Solution) |

---

## 👥 PS1 — Behavior (Behavioral Scientist)

| File | Description | Report Section |
|------|-------------|----------------|
| `otree_round1.png` | oTree session: Player 1 contributed 100, Player 2 free-rode. | PS1 Part 3a (Observed Play) |
| `otree_round2.png` | oTree session: Both contributed 0. | PS1 Part 3a |
| `otree_round3.png` | oTree session: Partial contributions (10 and 50). | PS1 Part 3a |
| `llm_one_shot.png` | LLM one-shot contribution (≈50, fairness reasoning). | PS1 Part 3b (LLM Session) |
| `llm_repeated.png` | LLM repeated game strategy: early cooperation, final defection. | PS1 Part 3b |

---

## 🛠️ PS2 — Auctions (Mechanism Design)

| File | Description | Report Section |
|------|-------------|----------------|
| `b_minus_V_win_dist.png` | Distribution of (bid − true value) across winners; shows overbidding baseline. | PS2 Part 2.2 (Results & Analysis) |
| `profit_by_treatment.png` | Profit distributions across baseline vs debias prompts, by model. | PS2 Part 2.2 |

---

## 🗳️ PS3 — Voting & Institutions (Reflection 6)

| File | Description | Report Section |
|------|-------------|----------------|
| `quota_vs_hosted_*.png` | Quota vs hosted comparison for T2 hybrid treatment. | Reflection/Part 3 (Mechanism Evaluation) |
| `rank_hist_*.png` | Distribution of assigned preference ranks under stable matching. | Reflection/Part 3 (Preference Satisfaction) |

---

## 🗂️ Usage Notes
- **File naming** is consistent with report sections; update if you regenerate plots.
- **README cross-links**: Root `README.md` references selected figures directly from these subfolders.
- **FAIR principles**: Figures are derived from scripts in `computational_scientist/`, `mechanism_design/auctions/scripts/`, and `mechanism_design/voting/scripts/`; reproduction steps are in each subfolder README.

---
