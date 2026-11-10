# Error analysis by eye

## Contents
- Single-person review
- Category list
- Parallel review for large error sets
- Turning counts into experiments
- What it typically finds

## Single-person review
1. Export the misses of the current best out-of-fold predictions: item path, group, true
   label, prediction, any teacher or second-model answer, any boxes.
2. Count misses per group and per class. Report the share held by the worst group and the
   worst five groups; errors are usually concentrated.
3. Build contact sheets (`scripts/contact_sheet.py`) and view them. Put misses next to
   similar items the model gets right: the contrast reveals the cue the model relies on.
4. Tag each miss with one category from the list below and count.
5. Verify suspected pipeline faults numerically (e.g. crop overlap with a reference box,
   input tensor orientation) before acting on them.

## Category list
Start from task-neutral categories and extend with task-specific ones:
- small_distant: the evidence is visible but tiny at the input resolution
- occluded: hidden by pose, objects, people or the frame edge
- atypical_appearance: the class looks unlike its usual training examples
- absent_evidence: the class is signalled by something missing (a missing part)
- context_confusion: the cue is present nearby but not on the target (wrong region)
- orientation_or_pipeline: rotation, aspect ratio, crop or preprocessing fault
- label_doubt: a careful human cannot see the labelled class
- confusable_class: mixed up with a neighbouring class (severity, laterality)
- other: describe

## Parallel review for large error sets
When there are more than about 100 misses, split the contact sheets across 4-8 reviewers
(agents or people). Give every reviewer the same legend (what each colour and caption
field means), the same category list and the same output schema: sheets read, counts per
category, total misses seen, 6-12 examples with what is visible, and recurring patterns.
Then have one synthesizer:
1. Sum counts into one table with shares; merge equivalent "other" tags.
2. Flag disagreements between reviewers about the same item or group.
3. Estimate the fixable ceiling (all misses minus label doubt and invisible ones).
4. Map each category to the planned experiments and list categories nothing addresses.
5. Propose at most three new one-change experiments for the unaddressed categories, each
   with a cheap decisive test and a kill line.

## Turning counts into experiments
Rank experiments by (misses in the categories they address) x (chance they work) / compute.
An experiment that cannot plausibly move a large category is deprioritised even if it is
fashionable. Re-run the review after each adopted change: the category mix shifts.

## What it typically finds
- One or a few groups holding a third or more of all errors.
- A shortcut cue: the model keys on colour, background, camera or collection rather than
  the object itself. It shows up only when misses and hits are viewed side by side.
- A small number of pipeline faults (orientation, cropping) that no metric revealed.
- A label-noise floor that caps the achievable score.
