# PublicGoods-and-Auctions-LLM

Interdisciplinary study linking **strategic games** (PS1) → **mechanism design & auctions** (PS2) → **voting & institutions** (Reflection 6), aligned with COMSCI/ECON 206 Final Research Proposal.

> This repository supports the final research proposal submitted to **COMSCI/ECON 206: Computational Microeconomics**, instructed by Prof. Luyao Zhang at Duke Kunshan University in Autumn 2025.

---

## 1. Abstract
We investigate a two-player **Public Goods Game** (E=100, m=1.5) to contrast theoretical predictions with **human** and **LLM** behaviors (PS1). We extend to **mechanism design** with **first-price common-value auctions** to test the **winner’s curse** on AI agents and prompt-based de-biasing (PS2). Finally, we propose a **hybrid voting/institutional design** that balances fairness, efficiency, and legitimacy, inspired by EU refugee allocation and informed by Arrow/Buchanan/Hurwicz-Maskin-Myerson (Reflection 6).

**SDG contributions**: SDG 16 (Institutions), SDG 11 (Sustainable Cities), SDG 10 (Reduced Inequalities), SDG 9 (Innovation).

---

## 2. Repository Structure
```
├── economist/                # Theory & welfare analysis (PS1)
├── computational_scientist/  # NashPy notebooks, GTE assets (PS1)
├── behavioral_scientist/     # oTree app, human session data, LLM transcripts (PS1/PS2)
├── mechanism_design/         # Auctions (winner’s curse) & Voting (Reflection 6)
│   ├── auctions/
│   └── voting/
├── visualizations/           # Figures exported from notebooks/otree/scripts
└── docs/
    ├── Report.pdf            # Final Research Proposal (to be added)
    ├── Poster.pdf            # Symposium poster (to be added)
    └── FieldTripReflection.md# Field trip & institutional reflection
```

---

## 3. Quick Start (Reproducibility)

### 3.1 Environment
- Python >= 3.10
- Install:
```bash
pip install -r requirements.txt
```
Minimal requirements:
```
nashpy
numpy
scipy
pandas
matplotlib
jupyter
tqdm
otree
```

### 3.2 Reproduce PS1 (Strategic Game)
- **Normal-form grid & Nash**:
  - `computational_scientist/notebooks/public_goods_nashpy.ipynb`
- **Extensive-form & SPNE**:
  - `computational_scientist/gte/`
- **Figures** exported to `visualizations/`.

### 3.3 Reproduce PS2 (Auctions & Winner’s Curse)
```bash
python scripts/collect_and_score.py
```
- Outputs: summary tables & histograms (saved under `visualizations/`).

### 3.4 Voting & Institutions (Reflection 6)
- Proposal & notes: `mechanism_design/voting/`
- Field trip reflection: `docs/FieldTripReflection.md`

---

## 4. Navigation Guide
- **Economist**: `economist/`
- **Computational Scientist**: `computational_scientist/`
- **Behavioral Scientist**: `behavioral_scientist/`
- **Mechanism Design**: `mechanism_design/`
- **Docs**: `docs/`

---

## 5. Roles
- **Economist**: theoretical modeling, welfare & fairness analysis.
- **Computational Scientist**: Nash equilibrium computation, GTE/SPNE.
- **Behavioral Scientist**: oTree deployment, human vs LLM comparative analysis.
- **Mechanism Designer**: auction design, winner’s curse tests, voting/institution proposal.

---

## 6. Acknowledgments
Professor Luyao Zhang (feedback on reconciling Colab/GTE, documenting oTree adaptations, integrating figures/citations). Peer review improved coherence and readability (VCM clarity, GitHub ToC). Tools: NashPy, GTE, oTree.

---

## 7. Statement of Growth
From PS1 to PS2 to institutional design, we improved research design, reproducibility, and critical evaluation across theory–computation–behavior. We also practiced transparent coding and FAIR/CARE-aligned data sharing.

---

## 8. License
MIT (unless otherwise noted).
