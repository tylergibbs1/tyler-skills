# Generating bets

Use this when the obvious levers are exhausted or the user wants a step change.

## Start from measured facts

Keep an observations file of measured facts only, each with its source. Every
brainstorm starts from it and must explain those facts. Ideas that contradict a
measured fact are dropped or must first explain the fact away.

## Discovery moves from past breakthroughs

Each move maps to a cheap kill test. Tag every bet with the move it uses.

| Move | Example | Cheap kill test |
|---|---|---|
| Diagnose the bottleneck | Attention fixed the fixed-length encoder vector; residual connections fixed training error rising with depth | Oracle swaps: replace one part at a time with the truth and see which recovers the gap |
| Delete an assumed-necessary part | The Transformer dropped recurrence (the paper cites parallel training) | Run the system without the part, plus whatever the deletion frees up |
| Simple objective plus scale, then look inside | Next-character prediction produced a unit that tracked sentiment, which led to scaling next-token prediction | Train at 3-4 small sizes, probe for capabilities nobody trained for |
| Measure slopes small, predict large | Scaling laws (Kaplan et al., 2020) | Fit success or loss against log compute with CIs; compare slopes, not points |
| Chase anomalies, run long | Grokking: delayed generalisation after long training | Keep one run going well past convergence and watch held-out curves |
| Data first | ImageNet before AlexNet | Build the unseen, varied test and training data before the model |
| Generate your own experience | Self-play (AlphaZero) | Replace demonstrations with play or self-generated goals at equal or lower data |

Emergence shows as a qualitative jump with scale, not a smooth gain. Only a multi-size
run can show it; one size cannot.

## Cross-field analogies

Distant fields (navigation, control engineering, epidemiology, immunology, ecology,
sports science) often already solved a structural twin of the problem. Keep an analogy
only if it predicts something the current understanding does not and that prediction
has a cheap test. Drop analogies that are only poetic.

## Scoring candidates

Score each on ceiling (what an oracle says it could buy), probability, cost of the
cheapest decisive test, and practicality. Run the cheapest decisive test of the
highest-ceiling bet first, and fund low-probability, high-information bets (scale
ladders) for the trend they reveal, not their odds.

## Novelty check

Before claiming something new, search papers, code and issues for the exact claim.
Report "known", "partly known" (and which part is new), or "not found", with what was
searched.
