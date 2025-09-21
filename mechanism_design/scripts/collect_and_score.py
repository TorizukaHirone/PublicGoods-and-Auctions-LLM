import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re

BASE = os.path.dirname(__file__)
DATA = os.path.join(BASE, "data", "T2_seed42_R30.csv")
RESULTS = os.path.join(BASE, "results")

R = 30
BIDDERS = [1,2,3,4]
MODELS = ["GPT-5", "DeepSeek"]    # Change labels if you like
TEMPLATES = ["baseline", "debias"]

def read_bids(model, template, bidder):
    path = os.path.join(RESULTS, f"{model}_{template}_bidder{bidder}.txt")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Missing: {path}")
    with open(path, "r", encoding="utf-8") as f:
        lines = [ln.strip() for ln in f.readlines() if ln.strip()!=""]
    bids = []
    for ln in lines:
        m = re.match(r"^\d+$", ln)
        if not m:
            raise ValueError(f"Non-integer line in {path}: '{ln}'")
        bids.append(int(ln))
    if len(bids) != R:
        raise ValueError(f"Expected {R} lines in {path}, got {len(bids)}")
    return np.array(bids, dtype=int)

def main():
    df = pd.read_csv(DATA)
    if len(df) != R:
        raise ValueError(f"Data CSV has {len(df)} rows, expected {R}")
    all_rows = []
    for model in MODELS:
        for template in TEMPLATES:
            bids = np.zeros((R, 4), dtype=int)
            for j, b in enumerate(BIDDERS):
                bids[:, j] = read_bids(model, template, b)
            rnd = np.random.default_rng(42)
            winners = []
            win_bids = []
            for k in range(R):
                row = bids[k, :]
                maxb = row.max()
                idxs = np.where(row == maxb)[0]
                if len(idxs) == 1:
                    win_idx = idxs[0]
                else:
                    win_idx = rnd.choice(idxs)
                winners.append(win_idx+1)
                win_bids.append(int(maxb))
            V = df["V"].to_numpy()
            profits = V - np.array(win_bids, dtype=float)
            tidy = pd.DataFrame({
                "round": np.arange(1, R+1),
                "model": model,
                "template": template,
                "winner_bidder": winners,
                "V": V,
                "b_win": win_bids,
                "profit": profits
            })
            all_rows.append(tidy)
    big = pd.concat(all_rows, ignore_index=True)
    big_path = os.path.join(RESULTS, "bids_scored_T2.csv")
    big.to_csv(big_path, index=False)
    print(f"Saved: {big_path}")

    def loss_rate(x): 
        return (x[x<0].count()/x.count())*100.0
    summary = big.groupby(["model","template"]).agg(
        mean_profit=("profit","mean"),
        sd_profit=("profit","std"),
        loss_rate=("profit", loss_rate),
        mean_b_win=("b_win","mean"),
        sd_b_win=("b_win","std")
    ).reset_index()
    sum_path = os.path.join(RESULTS, "summary_T2.csv")
    summary.to_csv(sum_path, index=False)
    print(f"Saved: {sum_path}")
    print(summary)

    # Plot 1
    plt.figure()
    for (model, template), g in big.groupby(["model","template"]):
        plt.hist(g["profit"], bins=20, alpha=0.5, label=f"{model}-{template}")
    plt.xlabel("Profit")
    plt.ylabel("Count")
    plt.title("Profit distribution (T2)")
    plt.legend()
    fig1 = os.path.join(RESULTS, "profit_by_treatment.png")
    plt.savefig(fig1, dpi=160, bbox_inches="tight")
    plt.close()
    print(f"Saved: {fig1}")

    # Plot 2
    plt.figure()
    for (model, template), g in big.groupby(["model","template"]):
        plt.hist(g["b_win"] - g["V"], bins=20, alpha=0.5, label=f"{model}-{template}")
    plt.xlabel("b_win - V (overbid if > 0)")
    plt.ylabel("Count")
    plt.title("Overbid when winning (T2)")
    plt.legend()
    fig2 = os.path.join(RESULTS, "b_minus_V_win_dist.png")
    plt.savefig(fig2, dpi=160, bbox_inches="tight")
    plt.close()
    print(f"Saved: {fig2}")

if __name__ == "__main__":
    main()
