# Scientific validation and experiment design

Read before selecting finalists or running computations.

## Adversarial check

For every candidate, answer: Is each premise directly measured? Are the sources independent? Are biological/material contexts compatible? Could a common cause explain both edges? Are units and time scales consistent? Could selection bias, collider bias, reverse causality, or instrumentation create the pattern? Is there a negative or retracted study? Could the effect disappear after controlling for multiple testing or publication bias?

**Reject or defer** unsupported bridges, already-established direct findings (as new discovery claims), unfalsifiable proposals, and candidates contradicted by stronger evidence.

## Ranking (each 1–5, with rationale)

| Criterion | What a 5 means |
|---|---|
| Evidence quality | Independent, well-controlled primary evidence for constituent links |
| Potential novelty | Broad logged prior-art search finds an untested *specific* relationship, still provisional |
| Falsifiability | A realistic, precisely defined result would disprove it |
| Feasibility | Suitable permitted data and bounded, reproducible test |
| Importance | The answer would change an important model or scientific decision |

These numbers are heuristics, **not** calibrated discovery probabilities.

## Pre-experiment contract

Write down *before looking at the target outcome*:

- **Directional hypothesis**, baseline/null model, and a plausible alternative mechanism.
- **Measurements**: units, independent variables, outcome, exposure and inclusion/exclusion criteria.
- **Dataset**: exact identifier/version, license, instruments, expected sample and missingness.
- **Controls**: confounders, negative/positive controls, expected artifacts, sensitivity/power.
- **Statistical rule**: primary endpoint/metric, uncertainty intervals, significance or Bayesian decision rule, multiplicity corrections when testing many ideas.
- **Validation**: independent cohort/replication, held-out split, or prospective data; avoid outcome peeking, test-set tuning and leakage.
- **Falsifier**: an actual observation that would reject or materially weaken the claim.
- **Reproduction**: seeds, commands, dependency versions, code commit, output artifacts, errors and deviations.

For theory and simulation, state the mathematical assumptions, numerical stability checks, and what would require empirical confirmation. Simulation is not a substitute for real-world evidence.

## Status labels

- **proposed:** Literature links suggest a testable hypothesis; direct claim untested.
- **literature-supported:** Relevant primary findings support the mechanism, but not necessarily this extension.
- **computationally tested:** The analysis *ran*; report methods, code, result and limitations.
- **independently replicated:** Independently collected data or method corroborates the prediction.
- **refuted:** A sound test contradicted the prediction.

When tools or datasets are inaccessible, leave `execution: not run` and supply a reproducible plan. Never imply an independent check without one.
