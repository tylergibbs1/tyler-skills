# Evaluation scenarios

Run each prompt in a fresh session, once without the skill and once with it. The skill
passes a scenario when the "with skill" behaviour appears and the failure does not.

## 1. Chasing a metric
**Prompt:** "My image classifier is at 71% and I need 78%. Here are my training scripts
and out-of-fold predictions. What should I try next?"
- **Typical failure without the skill:** a list of techniques (bigger model, more
  augmentation, focal loss, ensembling) with no look at the errors.
- **Expected with the skill:** asks for or computes where errors concentrate, renders
  misses for review, measures noise floor and an oracle ceiling, then proposes one or two
  experiments tied to failure counts, each with a control and kill line.

## 2. Reading a result
**Prompt:** "LoRA fine-tuning gave +2.0 over the frozen head on the same folds. Should I
adopt it?"
- **Typical failure:** "Yes, +2 is a good gain."
- **Expected:** checks the CI against the noise floor and whether the control got the same
  extra training steps (a frozen-adapter twin); asks for a paired bootstrap; does not adopt
  a confounded result.

## 3. Brainstorm request
**Prompt:** "Brainstorm 20 ideas to improve wound detection in our model."
- **Typical failure:** 20 generic ideas.
- **Expected:** first asks for or runs an error review; seeds ideas from failure
  categories; ranks a short list by expected gain per compute-hour with kill lines; marks
  ideas already dead in the ledger.

## 4. Negative trigger
**Prompt:** "Run this model on these 5 images and tell me the predictions."
- **Expected:** the skill does not activate; the agent just runs inference.

## Discovery check
Paste only the frontmatter of `skills/research/wcml/SKILL.md` into a fresh chat and ask for three prompts
that should trigger it and three that should not. Fix the description if the answers
disagree with the intent.
