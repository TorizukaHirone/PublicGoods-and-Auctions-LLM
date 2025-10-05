# -*- coding: utf-8 -*-
# === Environment ===
# pip install matplotlib pandas numpy

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

plt.rcParams['font.family'] = 'Arial'
plt.rcParams['axes.unicode_minus'] = False

OUTDIR = "outputs_en"
os.makedirs(OUTDIR, exist_ok=True)

# =========================================================
# 1) Efficiency Comparison (Bar Chart)
# =========================================================
efficiency_df = pd.DataFrame({
    "Auction Mechanism": ["First-price", "Second-price", "AI-enhanced"],
    "Total Welfare Index": [70, 80, 95]
})

plt.figure(figsize=(8, 6))
x = np.arange(len(efficiency_df["Auction Mechanism"]))
plt.bar(x, efficiency_df["Total Welfare Index"], color=['#4c72b0','#55a868','#c44e52'])
plt.xticks(x, efficiency_df["Auction Mechanism"])
plt.ylabel("Total Welfare Index (relative)")
plt.title("Efficiency Comparison: Total Welfare under Different Mechanisms")
plt.tight_layout()
plt.savefig(os.path.join(OUTDIR, "efficiency_comparison_en.png"), dpi=300, bbox_inches="tight")
plt.savefig(os.path.join(OUTDIR, "efficiency_comparison_en.pdf"), bbox_inches="tight")
plt.close()

# =========================================================
# 2) Fairness Comparison (Gini Coefficient, lower = fairer)
# =========================================================
fairness_df = pd.DataFrame({
    "Auction Mechanism": ["First-price", "Second-price", "AI-enhanced"],
    "Gini Coefficient": [0.45, 0.38, 0.25]
})

plt.figure(figsize=(8, 6))
x = np.arange(len(fairness_df["Auction Mechanism"]))
plt.bar(x, fairness_df["Gini Coefficient"], color=['#4c72b0','#55a868','#c44e52'])
plt.xticks(x, fairness_df["Auction Mechanism"])
plt.ylabel("Gini Coefficient (lower = fairer)")
plt.title("Fairness Comparison: Inequality in Allocation")
plt.tight_layout()
plt.savefig(os.path.join(OUTDIR, "fairness_comparison_en.png"), dpi=300, bbox_inches="tight")
plt.savefig(os.path.join(OUTDIR, "fairness_comparison_en.pdf"), bbox_inches="tight")
plt.close()

# =========================================================
# 3) Transparency / Manipulation Resistance (Radar Chart)
# =========================================================
indicators = ["Transparency", "Auditability", "Resistance to Manipulation", "Trust"]
traditional_scores = [50, 40, 45, 55]
ai_scores = [90, 85, 88, 92]

N = len(indicators)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles_loop = angles + angles[:1]
trad = traditional_scores + traditional_scores[:1]
ai = ai_scores + ai_scores[:1]

plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)
ax.plot(angles_loop, trad, linewidth=2, label="Traditional Auction")
ax.fill(angles_loop, trad, alpha=0.1)
ax.plot(angles_loop, ai, linewidth=2, label="AI-enhanced Auction")
ax.fill(angles_loop, ai, alpha=0.1)
ax.set_thetagrids(np.degrees(angles), indicators)
ax.set_rlim(0, 100)
ax.set_title("Transparency & Resistance to Manipulation (Radar Chart)", va='bottom')
ax.legend(loc="upper right", bbox_to_anchor=(1.2, 1.1))
plt.tight_layout()
plt.savefig(os.path.join(OUTDIR, "transparency_radar_en.png"), dpi=300, bbox_inches="tight")
plt.savefig(os.path.join(OUTDIR, "transparency_radar_en.pdf"), bbox_inches="tight")
plt.close()

print("English version charts exported to:", OUTDIR)
