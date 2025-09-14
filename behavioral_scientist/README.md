# Behavioral Scientist Perspective

This folder contains materials for behavioral and AI-based experiments.

- `otree_app.otreezip`: Packaged oTree app for the two-player public goods game.
- `screenshots/`: Screenshots of human play sessions (Rounds 1–3).
- `llm/`: Prompts and transcripts from large language model (LLM) experiments.

## How to Run oTree

- Download otree_app.otreezip.

```bash
pip3 install -U otree
otree zipserver
```

- Requires **oTree 5.x**.
- Open `http://localhost:8000` in a browser to access the game.

## LLM Experiments

- `prompt_oneshot.txt`: Prompt used for the one-shot game.
- `prompt_repeated.txt`: Prompt used for the repeated (10-round) game.
- `transcript.md`: Sample outputs and reasoning by the LLM.
