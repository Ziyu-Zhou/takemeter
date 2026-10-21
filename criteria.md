# Acceptance criteria — TakeMeter

Five criteria that say what "working" means for this classifier, written in
unit 5 **before** anything was trained.

**Target status:** These targets and rationales were suggested with AI assistance
at my request, then reviewed and accepted before training.
They are targets, not measured results. The planned dataset has 200 posts;
its actual size and label counts are not known yet.

**All five are yours this time.** None are given. You've had two projects of
practice.

An acceptance criterion names a number. *"The model is accurate"* is an
opinion. *"Every label has an F1 of at least 0.60 on the held-out set"* is a
criterion.

Under each, write a sentence or two on **why that number**. A reason that says
something about your data or your taxonomy earns credit — *"I picked 0.60 F1
for `reaction` because it's my smallest label and I only have about 50
examples of it"*. A reason that could be attached to any project does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

Not numbers that sound impressive. Three labels means a coin-flip guesser gets
about 33%, so a target of 0.40 is barely a target. Your number should sit
somewhere you'd honestly call useful.

**Cover at least three of these five areas.** They're here as prompts, not as a
form to fill in — a criterion that fits none of them is fine if it names a
number.

| Area | A question it could answer |
|---|---|
| Overall accuracy | How often does it need to be right to be worth using? |
| Per-label performance | Is one label allowed to be much worse than the others? |
| Balance | How lopsided can your label counts get before it's a problem? |
| Consistency | If someone else labelled the same posts, how often should you agree? |
| Confidence | Should a confident prediction be right more often than an unsure one? |

Two things worth knowing before you pick numbers, because both will affect
whether you hit them:

- **Your smallest label will have the jumpiest score.** If a label has 50
  examples, about 8 land in the test split. An F1 computed on 8 examples moves
  a lot between seeds. A target for that label should be looser than one for
  your biggest label, and saying so is a good reason.
- **Unit 6 tests across three seeds, and the target has to hold across all
  three.** A target of 0.65 against results of 0.71, 0.62, 0.68 is a **miss**.
  Pick with that in mind — it is stricter than it first sounds.

---

## 1. Overall accuracy of at least 75%

The classifier must achieve **accuracy >= 0.75** on the notebook's held-out
test set in each of the three training runs: seeds **42, 7, and 2024**.

**Why this target:** With two labels and the 40–60% balance target below,
always predicting the larger label would achieve at most 60% on the full
dataset. A 75% target asks the model to distinguish specific proposed changes
from supported positions well enough to get at least three out of four unseen
posts right. This is a target, not a claim of improvement over the next unit's
measured baseline.

---

## 2. Proposal F1 of at least 0.70

The classifier must achieve **F1 >= 0.70 for `proposal`** on the held-out
test set in each run with seeds **42, 7, and 2024**.

**Why this target:** Posts like the repair-cost example both argue and propose
a change. The model needs to find the endorsed change without treating every
criticism as a proposal. F1 accounts for both missed proposals and incorrect
proposal predictions. A 0.70 target asks for useful performance while allowing
some errors on this overlapping boundary in a small test set.

---

## 3. Argument F1 of at least 0.70

The classifier must achieve **F1 >= 0.70 for `argument`** on the held-out
test set in each run with seeds **42, 7, and 2024**.

**Why this target:** The elytra example mentions a possible nerf only to reject
it, so merely spotting change-related words is not enough. This target checks
whether the model recognizes supported positions without an endorsed change.
The same 0.70 minimum for both labels prevents acceptable overall accuracy
from hiding a weak label, especially before the actual class counts are known.

---

## 4. Each label represents 40–60% of the dataset

In the final deduplicated `labels.csv`, **each label must account for at least
40% and at most 60% of all rows**. Check the counts before training; this
criterion concerns the dataset and does not vary with the training seed.

**Why this target:** Both labels concern Minecraft opinions, but proposals may
be easier to find through searches for suggested changes. Keeping both within
40–60% limits that collection bias and is stricter than the assignment's 70%
cap. With the planned 200 posts, each label would have at least 80 examples,
giving roughly 12 or more examples per label in a stratified 15% test split.
Collect more eligible examples if needed rather than changing correct labels
to hit the target.

---

## 5. At least 90% agreement when labeling again

After initial labeling, randomly select **30 posts, 15 per label, using seed
42**, and record their original CSV row numbers. **At least 48 hours later**,
label those same posts again using the same definitions, without AI help and
without seeing the original labels, notes, or model predictions. At least
**27 of the 30 labels must match the original labels (90%)**. Save both sets
of labels and report the agreement and disagreements in the README. This
criterion does not vary with the training seed.

**Why this target:** The main boundary is whether the author actually endorses
a specific change; the repair-cost and elytra posts show how arguments and
mentions of changes can overlap. Sampling both labels equally checks
consistency on both sides. Allowing at most three disagreements leaves room
for difficult cases while requiring consistent decisions on most posts. This
measures repeatability under this project's taxonomy; it is separate from
next unit's staff agreement check under the staff taxonomy.

**How the targets will be judged:** Criteria 1–3 must meet their minimums in
all three runs, not just on average. Criteria 4–5 are checked once against the
dataset and the relabeling record. No measurements have been made yet.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 6 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Every label performs acceptably

         The model performs well on all labels.

         **Why this target:** ...

         > **Revised in unit 6:** Every label has an F1 of at least 0.60 on
         > the held-out set.
         >
         > **Why revised:** "performs well" gave me nothing to check. I
         > couldn't produce a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "Overall accuracy of at least 0.65" → "at least 0.55", because
            0.65 turned out to be optimistic for 200 examples.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
