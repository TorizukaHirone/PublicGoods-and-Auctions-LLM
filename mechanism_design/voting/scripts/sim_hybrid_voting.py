"""
Hybrid Quota–Fund–Matching Simulation (minimal, reproducible)
--------------------------------------------------------------
Generates a small synthetic federation (5–8 states) and a pool of refugees (200–500),
then compares three treatments:
  T0: Mandatory quotas only (no opt-out, no matching by preferences)
  T1: Voluntary + solidarity fund (opt-out allowed), no preference-based matching
  T2: Hybrid (quota + fund + stable matching with preferences)  ← proposed

Outputs (under visualizations/PS3_voting/ and mechanism_design/voting/results/):
  - summary_T3.csv: key metrics per treatment
  - per_state_T*.csv: state-level allocations/payments
  - plots: bar chart (host vs quota), histogram of preference ranks

Run:
  python mechanism_design/voting/scripts/sim_hybrid_voting.py --seed 42 --states 6 --agents 300

Dependencies: numpy, pandas, matplotlib (see requirements.txt)
"""

from __future__ import annotations
import argparse
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import List, Dict, Tuple

# -----------------------------
# Matching (Gale–Shapley variant)
# -----------------------------

def deferred_acceptance(ref_prefs: List[List[int]], state_caps: List[int]) -> Tuple[List[int], Dict[int, List[int]]]:
    """Refugee-proposing deferred acceptance.
    Args:
        ref_prefs: list of length R; each is a list of state indices in strict preference order
        state_caps: list of length S; capacity per state
    Returns:
        assignment: length R with assigned state index or -1 if unassigned
        state_matches: dict state->list of refugee indices
    """
    R = len(ref_prefs)
    S = len(state_caps)
    next_choice = [0]*R
    assignment = [-1]*R
    state_matches: Dict[int, List[int]] = {s: [] for s in range(S)}

    # Precompute inverse rankings for states (here: all refugees ranked by a simple priority = random)
    # In practice, states can have structured priorities; we sample to keep example simple.
    rng = np.random.default_rng(0)
    state_prior = {s: rng.permutation(R).tolist() for s in range(S)}
    prior_rank = {s: {r: i for i, r in enumerate(state_prior[s])} for s in range(S)}

    free = list(range(R))
    while free:
        r = free.pop()
        if next_choice[r] >= S:
            continue  # r has exhausted all states
        s = ref_prefs[r][next_choice[r]]
        next_choice[r] += 1
        # Tentatively accept r
        state_matches[s].append(r)
        # If over capacity, eject worst-priority refugee(s)
        if len(state_matches[s]) > state_caps[s]:
            # sort by state's priority (lower is better)
            state_matches[s].sort(key=lambda rid: prior_rank[s][rid])
            keep = state_matches[s][:state_caps[s]]
            rejected = state_matches[s][state_caps[s]:]
            state_matches[s] = keep
            for rej in rejected:
                free.append(rej)
    # Build assignment
    for s, lst in state_matches.items():
        for r in lst:
            assignment[r] = s
    return assignment, state_matches

# -----------------------------
# Simulation core
# -----------------------------

def simulate(seed=42, n_states=6, n_agents=300, alpha=0.6, base_quota_ratio=1.0, p=1.0, c=1.0):
    """Simulate three treatments (T0/T1/T2). Returns (summary_df, per_state_dict)."""
    rng = np.random.default_rng(seed)

    # Synthetic state stats (GDP, population) normalized
    gdp = rng.lognormal(mean=0.0, sigma=0.5, size=n_states)
    pop = rng.lognormal(mean=0.0, sigma=0.5, size=n_states)
    gdp_share = gdp/ gdp.sum()
    pop_share = pop/ pop.sum()

    # Baseline quota by fair-share formula
    weights = alpha * gdp_share + (1-alpha) * pop_share
    total_refugees = int(n_agents * base_quota_ratio)
    quota = np.rint(total_refugees * weights).astype(int)

    # Declared capacities (around quota with noise)
    cap = np.maximum(0, (quota * rng.uniform(0.8, 1.2, size=n_states)).astype(int))

    # Refugee preferences over states (iid ranks with mild correlation to GDP/pop)
    # Build a utility score = 0.5*GDP_rank + 0.5*Pop_rank + small noise, then sort
    util = 0.5 * (gdp_share/ gdp_share.max()) + 0.5 * (pop_share/ pop_share.max())
    prefs = []
    for _ in range(n_agents):
        noise = rng.normal(0, 0.15, size=n_states)
        scores = util + noise
        prefs.append(np.argsort(-scores).tolist())

    # T0: Mandatory quotas only → host = min(quota, cap). No matching or preferences.
    host_T0 = np.minimum(quota, cap)
    pay_T0 = np.zeros(n_states)
    unassigned_T0 = int(max(0, total_refugees - host_T0.sum()))
    avg_rank_T0 = np.nan  # not applicable

    # T1: Voluntary + Fund (no matching). States can opt-out proportion k~U[0,0.5]; pay for shortfall.
    optout_k = rng.uniform(0.0, 0.5, size=n_states)
    target_T1 = (quota * (1.0 - optout_k)).astype(int)
    host_T1 = np.minimum(cap, target_T1)
    shortfall_T1 = np.maximum(0, quota - host_T1)
    pay_T1 = p * shortfall_T1
    unassigned_T1 = int(max(0, total_refugees - host_T1.sum()))
    avg_rank_T1 = np.nan

    # T2: Hybrid (quota + fund + stable matching). Effective capacity = cap; fund for (quota - host)^+ ex post.
    assign_T2, state_matches_T2 = deferred_acceptance(prefs, cap.tolist())
    host_counts_T2 = np.zeros(n_states, dtype=int)
    for s, lst in state_matches_T2.items():
        host_counts_T2[s] = len(lst)
    host_T2 = host_counts_T2
    shortfall_T2 = np.maximum(0, quota - host_T2)
    pay_T2 = p * shortfall_T2
    # Preference satisfaction (rank): lower is better
    ranks = []
    for r, s in enumerate(assign_T2):
        if s == -1:
            continue
        ranks.append(prefs[r].index(s))
    avg_rank_T2 = float(np.mean(ranks)) if ranks else np.nan
    unassigned_T2 = int((np.array(assign_T2) == -1).sum())

    # Budget disbursement to receivers (simple linear per hosted)
    transfer_T2 = c * host_T2

    # Metrics
    def fairness_deviation(host, pay):
        # convert pay back to hosted-equivalent units by dividing by p (avoid div0)
        p_eff = p if p>0 else 1.0
        eq = host + (pay / p_eff)
        return float(np.mean(np.abs(eq - quota)))

    summary = []
    summary.append({
        'treatment': 'T0_mandatory',
        'unassigned': unassigned_T0,
        'avg_rank_assigned': avg_rank_T0,
        'fairness_deviation': fairness_deviation(host_T0, pay_T0),
        'total_hosted': int(host_T0.sum()),
        'total_payments': float(pay_T0.sum()),
    })
    summary.append({
        'treatment': 'T1_voluntary_fund',
        'unassigned': unassigned_T1,
        'avg_rank_assigned': avg_rank_T1,
        'fairness_deviation': fairness_deviation(host_T1, pay_T1),
        'total_hosted': int(host_T1.sum()),
        'total_payments': float(pay_T1.sum()),
    })
    summary.append({
        'treatment': 'T2_hybrid_matching',
        'unassigned': unassigned_T2,
        'avg_rank_assigned': avg_rank_T2,
        'fairness_deviation': fairness_deviation(host_T2, pay_T2),
        'total_hosted': int(host_T2.sum()),
        'total_payments': float(pay_T2.sum()),
    })

    summary_df = pd.DataFrame(summary)

    per_state = pd.DataFrame({
        'state': np.arange(n_states),
        'gdp_share': gdp_share,
        'pop_share': pop_share,
        'quota': quota,
        'capacity': cap,
        'host_T0': host_T0,
        'pay_T0': pay_T0,
        'host_T1': host_T1,
        'pay_T1': pay_T1,
        'host_T2': host_T2,
        'pay_T2': pay_T2,
        'transfer_T2': transfer_T2,
    })

    res = {
        'summary': summary_df,
        'per_state': per_state,
        'assign_T2': assign_T2,
        'prefs': prefs,
    }
    return res

# -----------------------------
# Plot helpers
# -----------------------------

def ensure_dirs():
    os.makedirs('visualizations/PS3_voting', exist_ok=True)
    os.makedirs('mechanism_design/voting/results', exist_ok=True)


def plot_host_vs_quota(per_state: pd.DataFrame, tag: str):
    fig = plt.figure(figsize=(8,4))
    idx = np.arange(len(per_state))
    width = 0.35
    plt.bar(idx - width/2, per_state['quota'], width, label='quota')
    plt.bar(idx + width/2, per_state['host_T2'], width, label='host_T2')
    plt.xticks(idx, per_state['state'])
    plt.ylabel('Count')
    plt.title('Quota vs Hosted (T2)')
    plt.legend()
    out = f'visualizations/PS3_voting/quota_vs_hosted_{tag}.png'
    plt.tight_layout()
    plt.savefig(out, dpi=150)
    plt.close(fig)


def plot_rank_hist(assign_T2: List[int], prefs: List[List[int]], tag: str):
    ranks = []
    for r, s in enumerate(assign_T2):
        if s == -1:
            continue
        ranks.append(prefs[r].index(s))
    if not ranks:
        return
    fig = plt.figure(figsize=(6,4))
    plt.hist(ranks, bins=np.arange(-0.5, max(ranks)+1.5, 1.0))
    plt.xlabel('Assigned preference rank (0=top choice)')
    plt.ylabel('Frequency')
    plt.title('Preference Satisfaction (T2)')
    out = f'visualizations/PS3_voting/rank_hist_{tag}.png'
    plt.tight_layout()
    plt.savefig(out, dpi=150)
    plt.close(fig)

# -----------------------------
# CLI
# -----------------------------

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--states', type=int, default=6)
    parser.add_argument('--agents', type=int, default=300)
    parser.add_argument('--alpha', type=float, default=0.6)
    parser.add_argument('--p', type=float, default=1.0, help='per-capita payment rate for shortfall')
    parser.add_argument('--c', type=float, default=1.0, help='transfer per hosted in T2')
    args = parser.parse_args()

    ensure_dirs()

    res = simulate(seed=args.seed, n_states=args.states, n_agents=args.agents,
                   alpha=args.alpha, p=args.p, c=args.c)

    # Save CSVs
    res['summary'].to_csv('mechanism_design/voting/results/summary_T3.csv', index=False)
    res['per_state'].to_csv('mechanism_design/voting/results/per_state_T3.csv', index=False)

    # Plots
    plot_host_vs_quota(res['per_state'], tag=f's{args.states}_a{args.agents}_seed{args.seed}')
    plot_rank_hist(res['assign_T2'], res['prefs'], tag=f's{args.states}_a{args.agents}_seed{args.seed}')

    print('Done. Results in:')
    print('  - mechanism_design/voting/results/summary_T3.csv')
    print('  - mechanism_design/voting/results/per_state_T3.csv')
    print('  - visualizations/PS3_voting/*.png')


if __name__ == '__main__':
    main()
