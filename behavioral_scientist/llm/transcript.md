# LLM Public Goods Game Transcript

This document records the outputs of a large language model (LLM) playing the two-player public goods game.

---

## One-Shot Game

**Prompt:**
```
You are Player 1 in a two-player public goods game. 
Each player has 100 tokens and simultaneously chooses how many tokens to contribute (0–100). 
The multiplier is 1.5 and the group size is 2, so MPCR = 0.75. 
Your payoff is: 100 - g1 + 0.75*(g1+g2). 
The other player follows the same rule. 
Choose your contribution g1 (an integer between 0 and 100). 
Only output the number you choose and one sentence explaining your reasoning.
```

**LLM Output:**
```
I will contribute 50. 
This balances my personal payoff with the collective benefit, avoiding pure free-riding.
```

---

## Repeated Game (10 Rounds)

**Prompt:**
```
You are Player 1 in a repeated (10-round) two-player public goods game. 
Each round, both players have 100 tokens. 
You and Player 2 simultaneously choose contributions (0–100). 
Multiplier = 1.5, group size = 2 (MPCR = 0.75). 
Your payoff in each round: 100 - g1 + 0.75*(g1+g2). 
You can condition your strategy on previous rounds. 
Play for 10 rounds. For each round, state your contribution (0–100) and a short explanation.
```

**LLM Output (excerpt):**
```
Round 1: Contribute 100 (to signal cooperation).
Round 2: Contribute the same as opponent's previous move.
Round 3–9: Continue mirroring opponent's previous contribution.
Round 10: Contribute 0 (final round defection).
```

**Explanation:**
The LLM adopted a conditional cooperation strategy — starting with full contribution, reciprocating in the middle rounds, and defecting in the last round. This mirrors common human behavior in repeated public goods experiments.
