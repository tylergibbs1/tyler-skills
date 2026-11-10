# Experiment: <short question>

- **Failure category targeted:** <category> (<N> misses, <share>% of errors)
- **Hypothesis:** <why this change should fix that category>
- **Ceiling:** <oracle result, or "not measured" with reason>
- **The one change:** <exact flag/config difference>
- **Control:** <baseline file and config; how extra steps/data are matched>
- **Comparison:** `<baseline predictions>` vs `<candidate predictions>`, same folds and seeds
- **Proxy run:** <seeds, folds, epochs, est. compute>
- **Kill line:** dead if delta < <x> or CI lower bound < <y> or <mechanism metric> rises < <z>
- **Result:** delta <+/-d> (95% CI <lo>..<hi>), macro <+/-m>, <class> recall <before> -> <after>
- **Status:** adopted | promising | dead | running | info
- **Why:** <one line>
