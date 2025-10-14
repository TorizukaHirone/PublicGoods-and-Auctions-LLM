# PublicGoods-and-Auctions-LLM

Interdisciplinary study linking **strategic games** (PS1) → **mechanism design & auctions** (PS2) → **voting & institutions** (PS3 / Reflection 6), aligned with COMSCI/ECON 206 Final Research Proposal.

> This repository supports the final research proposal submitted to **COMSCI/ECON 206: Computational Microeconomics**, instructed by Prof. Luyao Zhang at Duke Kunshan University in Autumn 2025.

---

## 1. Abstract
We investigate a two-player **Public Goods Game** (E=100, m=1.5) to contrast theoretical predictions with **human** and **LLM** behaviors (PS1). We extend to **mechanism design** with **first-price common-value auctions** to test the **winner’s curse** on AI agents and prompt-based de-biasing (PS2). Finally, we propose and simulate a **hybrid voting/institutional design** (PS3) that balances fairness, efficiency, and legitimacy, inspired by EU refugee allocation and informed by Arrow/Buchanan/Hurwicz-Maskin-Myerson.

**SDG contributions**: SDG 16 (Institutions), SDG 11 (Sustainable Cities), SDG 10 (Reduced Inequalities), SDG 9 (Innovation).

---

## 2. Repository Structure
```
├── economist/                # Theory & welfare analysis (PS1)
├── computational_scientist/  # NashPy notebooks, GTE assets (PS1)
├── behavioral_scientist/     # oTree app, human session data, LLM transcripts (PS1/PS2)
├── mechanism_design/         # Auctions (PS2) & Voting (PS3)
│   ├── auctions/
│   └── voting/
├── visualizations/           # Figures for PS1, PS2, PS3
│   ├── PS1_theory/
│   ├── PS1_behavior/
│   ├── PS2_auctions/
│   └── PS3_voting/
└── docs/
    ├── Report.pdf
    ├── Poster.pdf
    └── FieldTripReflection.md
```

---

## 3. Quick Start (Reproducibility)

### 3.1 Environment
```bash
pip install -r requirements.txt
```

### 3.2 Reproduce PS1 (Strategic Game)
- `computational_scientist/notebooks/public_goods_nashpy.ipynb`
- Figures exported under `visualizations/PS1_theory/`

### 3.3 Reproduce PS2 (Auctions & Winner’s Curse)
```bash
python mechanism_design/auctions/scripts/collect_and_score.py
```
- Figures in `visualizations/PS2_auctions/`

### 3.4 Reproduce PS3 (Voting & Institutions)
```bash
python mechanism_design/voting/scripts/sim_hybrid_voting.py --seed 42 --states 6 --agents 300
```
- Figures in `visualizations/PS3_voting/`
- Key outputs: `quota_vs_hosted_*.png`, `rank_hist_*.png`

---

## 4. Navigation Guide
- **Economist**: `economist/`
- **Computational Scientist**: `computational_scientist/`
- **Behavioral Scientist**: `behavioral_scientist/`
- **Mechanism Design**:
  - Auctions: `mechanism_design/auctions/`
  - Voting & Institutions: `mechanism_design/voting/`
- **Visualizations**:
  - PS1 Theory: `visualizations/PS1_theory/`
  - PS1 Behavior: `visualizations/PS1_behavior/`
  - PS2 Auctions: `visualizations/PS2_auctions/`
  - PS3 Voting: `visualizations/PS3_voting/`
- **Docs**: `docs/`

---

## 5. Roles
- **Economist**: theoretical modeling, welfare & fairness analysis.
- **Computational Scientist**: Nash equilibrium computation, GTE/SPNE.
- **Behavioral Scientist**: oTree deployment, human vs LLM comparative analysis.
- **Mechanism Designer**: auction design, winner’s curse tests, voting/institution proposal.

---

## 6. Acknowledgments
Professor Luyao Zhang (guidance on methodology and integration). Peers (feedback on coherence, repo structure). Tools: NashPy, GTE, oTree.

---

## 7. Statement of Growth
Progressed from PS1 → PS2 → PS3, gaining skills in research design, reproducibility, and institutional analysis. Improved ability to align **theory, computation, and behavior** with SDG-relevant mechanisms.

---

## 8. License
MIT (unless otherwise noted).
