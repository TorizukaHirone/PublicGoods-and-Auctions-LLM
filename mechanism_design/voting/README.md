# Voting & Institutions — Hybrid Incentive-Compatible Mechanism

This module extends the repo from strategic games (PS1) and auctions (PS2) to **collective choice and institutional design**. We prototype a **hybrid quota–fund–matching mechanism** inspired by the EU refugee allocation dilemma. The goal is to balance **fairness**, **efficiency**, and **legitimacy** by aligning incentives and enabling transparent implementation.

---

## 1) Problem Framing
- **Setting**: A union of member states with heterogeneous preferences and capacities for hosting refugees.
- **Pain points**: majority rule may alienate veto players; unanimity can block action; quotas without incentives face non-compliance; pure voluntarism under-provides.
- **Design target**: A mechanism that guarantees contribution (hosting *or* funding), reduces preference cycles in practice, and respects capacity/sovereignty constraints.

---

## 2) Mechanism Sketch (High Level)

### 2.1 Baseline Quota (Fair Share)
- Compute each state’s **baseline share** using a weighted formula, e.g. `w = α·GDP_share + (1−α)·Population_share`.
- This defines the **reference obligation** (number of refugees or equivalent monetary contribution).

### 2.2 Partial Opt-Out with Solidarity Fund
- States can **partially opt out** of hosting by contributing to a **solidarity fund** at per-capita rate `p`.
- Fund is earmarked to support **overburdened border states** and reception costs (housing, schooling, integration services).
- Payment caps & discount factors prevent corner solutions (e.g., small states simply opting out completely without limit).

### 2.3 Stable Matching with Preferences
- Refugees submit (or are inferred) **ranked preferences** over states; states declare **capacities** and priority criteria.
- Use a **stable matching** procedure (e.g., Gale–Shapley variant) to assign refugees to willing states, respecting capacities and improving legitimacy (matching reduces mismatches and reallocation).

### 2.4 Smart-Contract–Backed Transfers (Optional)
- **Escrow & disbursement** rules for the solidarity fund are encoded as smart contracts for transparency.
- Periodic audits verify hosting numbers and trigger conditional disbursements to receiving states.

---

## 3) Formal Components (Proto)

### 3.1 Allocation Formula
```
quota_i = total_refugees * (α * GDP_i/GDP_total + (1-α) * Pop_i/Pop_total)
```
- Parameters: `α ∈ [0,1]` controls GDP vs population weight.
- Soft bounds ensure quotas do not exceed capacity `Cap_i` and maintain floor `min_i`.

### 3.2 Budget Balance
- Solidarity fund `F = Σ_i pay_i`, where `pay_i = p * (quota_i - host_i)+`.
- Disbursement: `transfer_j = c * hosted_j` for eligible receivers; calibrate `p, c` to ensure **approximate budget balance** over a fiscal period.

### 3.3 Matching Procedure (Sketch)
1. Collect states’ capacities and minimal service guarantees.
2. Collect refugees’ preferences (or inferred signals: language ties, family links).
3. Run a **deferred acceptance** variant that honors capacities; treat funded opt-outs as reduced capacities for those states.
4. Post-process for **stability** and **equity constraints** (e.g., diversity metrics, max travel distance).

---

## 4) Simulation Plan
- **Inputs**: synthetic/aggregated GDP, population, declared capacities, preference draws.
- **Treatments**:
  - T0: Mandatory quotas only
  - T1: Voluntary + fund (opt-outs) without matching
  - T2: Hybrid (quota + fund + stable matching) ← proposed
- **Metrics**:
  - *Fairness*: deviation from fair-share (`|host_i + pay_i/p − quota_i|`)
  - *Efficiency*: total unassigned; reallocation rate; average wait time
  - *Legitimacy*: preference satisfaction (rank hit), dispersion measures
  - *Stability*: blocking pairs in matching; compliance rate over periods
- **Outputs**: tables & plots saved under `visualizations/PS3_voting/` (create folder when used).

---

## 5) Reproducibility
```
mechanism_design/voting/
├── README.md                 # this file
├── prototype.md              # optional: notes, math details, parameter sweeps
├── data/                     # (optional) synthetic inputs for simulations
└── scripts/                  # (optional) simulation scripts
```
- Use fixed seeds for stochastic components.
- Document parameters (`α, p, c, Cap_i`) in script headers and commit configs.

---

## 6) Ethics & Data
- Use **aggregated** or **synthetic** state-level metrics for public repos.
- Do not include personally identifiable information (PII).
- Provide plain-language descriptions of how preferences are collected/inferred and how privacy is protected.

---

## 7) How This Connects to the Report
- **Body Part 3**: Present the policy context, the trilemma (fairness–efficiency–legitimacy), and the proposed mechanism.
- Include a small **illustrative simulation** (e.g., 5–8 states, 200–500 agents) to demonstrate feasibility.
- Discuss limitations and potential failure modes (strategic misreporting of capacities, unilateral free-riding, cross-border leakage) and how audits/penalties/transfer schedules mitigate them.

---

### TODO Checklist
- [ ] Add `PS3_voting/` under `visualizations/` for figures.
- [ ] Add a toy simulation script and upload sample outputs.
- [ ] Write a short evaluation section comparing T0/T1/T2 on the metrics above.
- [ ] Link to this folder from the root `README.md` Navigation Guide.
