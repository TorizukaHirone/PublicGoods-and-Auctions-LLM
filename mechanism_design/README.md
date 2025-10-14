# Mechanism Design: Auctions & Voting

This module contains two strands:
1) **Auctions**: testing **winner’s curse** on AI agents (PS2).  
2) **Voting & Institutions**: hybrid mechanism inspired by EU refugee allocation (Reflection 6).

---

## A. Auctions — Winner’s Curse on AI Agents

### A1. Design
- Environment: first-price common-value auction, n=4.
- Signals: pre-generated (seed=42).
- Templates: baseline vs debias (warning about winner’s curse).
- Profit = V - b_win.

### A2. Run
```bash
python scripts/collect_and_score.py
```
- Outputs: summary tables & histograms in `visualizations/`.

### A3. Files
```
mechanism_design/auctions/
├── prompts/
├── data/signals_seed42.csv
├── scripts/collect_and_score.py
└── results/
```

---

## B. Voting & Institutions (Reflection 6)

### B1. Context
EU refugee allocation dilemma (2015–2016).

### B2. Theories
- Arrow: impossibility & cycles.
- Buchanan: majority vs unanimity.
- Hurwicz–Maskin–Myerson: incentive-compatible mechanisms.

### B3. Proposal
- Baseline quota (GDP, population).
- Opt-out with payments to solidarity fund.
- Stable matching for allocation.
- Blockchain smart contracts for transparency.

Files:
```
mechanism_design/voting/
docs/FieldTripReflection.md
```

---

## C. Reproducibility & Ethics
- Fixed seeds, transparent prompts.
- FAIR/CARE principles.