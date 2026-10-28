# TakeMeter

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first** — setup, the
> notebook, the baseline, and what to do when something breaks.
>
> Once `python test.py` passes:
>
> ```bash
> head -5 data/practice_labels.csv     # the shape your labels.csv needs
> ```
>
> Then open `takemeter.ipynb` **in this folder** — in VS Code, or with
> `jupyter notebook` if you prefer. Pick the kernel: the `.venv` inside this
> project. Run section 1, which reports the hardware you'll be training on.
> Everything else waits until you have data.
>
> Nothing to upload, nothing to connect, no accounts and no keys. The notebook
> runs on your machine and writes next to your code.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     HOW TO USE THIS FILE

     Unit 5 asks for the first five sections. Unit 6 adds the five below them.

     Everything is pasted as TEXT. No screenshots, no images.

     ⚠️ The confusion matrix especially. The notebook prints one as a markdown
     table, ready to copy. A screenshot of a matrix earns nothing. Paste the
     table.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 5 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- Your community, and what your classifier sorts posts into. Three or four
     sentences. -->

My community is [r/Minecraft](https://www.reddit.com/r/Minecraft/), focusing
on public text discussions about game mechanics and proposed changes.
TakeMeter is intended to classify each submission's title and body as either
`proposal`, an endorsed specific change, or `argument`, a supported position
without an endorsed specific change. The goal is to distinguish suggestions
from explanations even when both discuss the same mechanic. The current
dataset is a small exploratory sample; training and evaluation are recorded
below, while personal label review remains incomplete.

### Candidate Distinctions — Milestone 1

Starting examples:
[The elytra should not be nerfed](https://www.reddit.com/r/Minecraft/comments/1rigtgg/the_elytra_should_not_be_nerfed/)
and
[How would you fix the inventory problem?](https://www.reddit.com/r/Minecraft/comments/1ukeodx/how_would_you_fix_the_inventory_problem/).

1. **Explaining an opinion versus only stating a preference.** The elytra
   post supports its position by explaining that slower travel would make
   crossing long distances tedious.
2. **Defending an existing mechanic versus proposing a specific change.**
   The elytra post argues for keeping its current strength. The inventory
   post proposes new storage options, including a backpack.
3. **Naming a tradeoff versus focusing on benefits.** The inventory post
   explains that its backpack would take the chest equipment slot, forcing
   a choice between extra storage, armor, and elytra. The elytra post focuses
   on the convenience of fast travel.



---

## Label Taxonomy

<!-- Each label: a one-sentence definition and two real examples from your
     reading. Then your decision rule for the hardest boundary.

     The decision rule is worth a point on its own and it's the thing most
     people leave out. Every taxonomy has a hardest boundary. Name yours. -->

The unit being labeled is one submission's title and body together, without
its comments. Include text that makes sense without attachments and expresses
an opinion or suggested change about Minecraft. Exclude standalone help
requests, questions without a position, unsupported reactions, advertisements,
and posts whose meaning depends on an image or video.

### `proposal`

**Definition:** The author endorses a specific change to Minecraft's current
mechanics or behavior, identifying what should change and how.

**Example 1:** [How would you fix the inventory problem?](https://www.reddit.com/r/Minecraft/comments/1ukeodx/how_would_you_fix_the_inventory_problem/)
proposes a backpack that adds storage while occupying the chest equipment slot.

**Example 2:** [Why does repairing take more materials than crafting AND experience?](https://www.reddit.com/r/Minecraft/comments/1vihgnf/why_does_repairing_take_more_materials_than/)
proposes charging experience only for enchanted repairs and limiting material
costs relative to crafting a replacement.

### `argument`

**Definition:** The author supports a position about Minecraft with an explicit
reason, example, or gameplay consequence, without endorsing a specific change
to the game's current mechanics or behavior.

**Example 1:** [The elytra should not be nerfed](https://www.reddit.com/r/Minecraft/comments/1rigtgg/the_elytra_should_not_be_nerfed/)
defends its current strength by explaining how slower travel would make long
journeys tedious.

**Example 2 — additional post to review:** [The elytra is end-game content, not mid-game](https://www.reddit.com/r/Minecraft/comments/1g53qtg/hot_take_the_elytra_is_endgame_content_not_midgame/)
argues that its strength is justified by when a relaxed player obtains it,
using the author's own progression as support.

### The hardest boundary

**Which two labels:** `proposal` and `argument`.

**Borderline post:** The repair-cost post above. It argues that repairing is
too expensive and also specifies how the costs should change.

**Case for `argument`:** It compares repairing with crafting a replacement
to support a criticism of the existing mechanic.

**Case for `proposal`:** It specifies a different rule for experience costs
and a limit on material costs.

**Decision rule to apply every time:** Read the title and body together.
If the author endorses at least one specific change to current game behavior,
use `proposal`, even when most of the post explains or argues for that change.
Otherwise, use `argument` only if a position has an explicit supporting reason,
example, or consequence. A change is specific when both its target and the
intended behavior are identifiable; exact numbers or implementation details
are not required. Defending an existing mechanic against a suggested change,
or quoting another person's suggestion only to reject it, does not itself
count as a proposal. A vague wish such as "make it better" is insufficient.
Exclude a post if it meets neither definition.

**Borderline decision under this rule:** `proposal` for the repair-cost post.

### AI boundary stress test

The following eight posts are AI-generated examples, not real Reddit posts
or training data. The labels and explanations are an AI-assisted first pass;
personal classification and group discussion or the independent AI discussion
check are still pending.

| # | Generated post | Draft label | Reason |
|---|---|---|---|
| 1 | "The inventory is cramped because each block variant needs another slot. Add a backpack that uses the chest slot." | `proposal` | A supported complaint also endorses a specific storage change. |
| 2 | "The inventory feels cramped because a detailed roof needs stairs, slabs, and full blocks in several materials." | `argument` | Supplies a reason for the criticism without specifying a change. |
| 3 | "People suggest removing rocket boosting, but I disagree: long trips would become tedious." | `argument` | Mentions a change only to reject it. |
| 4 | "Elytra is fine. Make minecarts faster so railways are worth building." | `proposal` | Endorses a change to minecart speed; an exact speed is unnecessary. |
| 5 | "Repairing is frustrating because a new tool can cost fewer materials. Mojang should make repairs better." | `argument` | Gives a reason, but the requested improvement has no specific behavior. |
| 6 | "Could unenchanted repairs cost zero XP? That would make maintaining early tools worthwhile." | `proposal` | A question can endorse a specific change. |
| 7 | "Mending is useful because it lets me keep building instead of repeatedly replacing my pickaxe." | `argument` | Describes an existing mechanic's benefit without asking to change it. |
| 8 | "I'm not sure whether this would be balanced, but I would like a keep-inventory option that saves tools while dropping all XP." | `proposal` | Tentative language still expresses endorsement of a specific new option. |

The draft rule distinguishes an author's own suggestion from a rejected quote,
a specific change from a vague wish, and question wording from a genuine help
request. These cases need personal review before treating the taxonomy as final.

---

## The Dataset

<!-- Where you collected from, how you labelled, your counts, and three hard
     cases. -->

**Where the posts came from:**

r/Minecraft public submissions about game mechanics, balance, progression,
and suggested changes. **200 posts** are in `labels.csv`, meeting the collection
target. Each row contains the title and complete rendered post body, without
comments; media and Reddit interface markup were removed while keeping the
author's text. The original 30 rows were preserved, and 170 more posts were
appended; `data/post_sources.csv` maps data rows to their
original URLs. Posts were found through topic searches, so this is a targeted
sample rather than a random sample of the subreddit. Direct bulk retrieval
was blocked; the collected text came from readable public pages, not search
snippets. Text that depended on attachments, removed bodies, help-only posts,
and duplicates was excluded during screening.

**How I labelled them:** <!-- Cold first? Pre-labelled with AI and corrected?
Say so plainly — the disclosure is required, not penalised. -->

The exported file contained **9 unaided labels**, marked `cold`. AI
normalized capitalization only, preserving those label choices, and pre-labeled
the other **191 posts**. Their notes explicitly say
`ai-prelabeled; pending human review`. The student has not yet confirmed those
AI labels. Because of time limits, the student chose to proceed with
fewer than the required 20 cold labels. Collection is now complete, but the
20-cold-label requirement and personal review of the AI labels remain unmet;
this is not a fully completed Milestone 4 submission.

**Counts per label (including unreviewed AI labels):**

| Label | Count | Share |
|---|---|---|
| `proposal` | 90 | 45.0% |
| `argument` | 110 | 55.0% |
| **Total** | **200** | **100%** |

**Data checks:** The file has the required `text`, `label`, and `note`
columns, with no empty text or labels and no exact duplicate post texts.
Neither label exceeds the assignment's 70% cap; both also meet my stricter
40–60% balance target in `criteria.md`. The file remains one unsplit dataset;
the notebook creates the train, validation, and test splits.

**Remaining labeling work:** Only 9 of the required 20 cold labels are
recorded. The 191 AI-prelabeled posts still need to be read and corrected
individually by me before their pending-review notes can be changed. AI
assistance cannot substitute for either requirement. The original nine cold
labels and the first 30 rows were preserved during expansion.

**Three hard cases — AI-assisted drafts, pending student review**

**1. [Repair costs](https://www.reddit.com/r/Minecraft/comments/1vihgnf/why_does_repairing_take_more_materials_than/)**

- *Could have been:* `argument` or `proposal`.
- *AI draft decision:* `proposal`, because the post both criticizes repair
  costs and endorses specific rules for experience and material costs.

**2. [Mending is healthy for the game](https://www.reddit.com/r/Minecraft/comments/1x9uanb/mending_is_healthy_for_the_game_actually/)**

- *Could have been:* `argument` or `proposal`.
- *AI draft decision:* `argument`. Most of the post defends Mending with
  gameplay consequences. Its final wish to make villager enchanting easier
  does not specify how the mechanic should behave differently, so it does
  not meet the specific-change rule.

**3. [Community is wrong about latest updates](https://www.reddit.com/r/Minecraft/comments/1rbgfol/community_is_wrong_about_latest_updates/)**

- *Could have been:* `argument` or `proposal`.
- *AI draft decision:* `proposal`. Although most of the post argues for the
  current update approach, the author also explicitly endorses implementing
  the Illusioner. Under the decision rule, one specific endorsed change takes
  priority over the surrounding argument.

---

## The Training Run

<!-- Your starting model, your settings, and anything you changed and why. -->

**Run status:** The existing Unit 5 run produced `results.json` and
`test_split.csv`. The notebook uses `LABELS = ["proposal", "argument"]`.
Unit 6 repeated the original setup on three seeds and tested one input-length
change on the same splits. `labels.csv` was unchanged throughout evaluation.

| Setting | Before | After |
|---|---|---|
| Base model | `distilbert-base-uncased` | same |
| Epochs | 3 | same |
| Learning rate | `2e-5` | same |
| Batch size | 16 | same |
| Maximum input length | 128 tokens | 256 tokens |
| Seeds | 42, 7, 2024 | same |
| Rows | 200 | same |

**Device:** The preserved Unit 5 `results.json` records Apple Silicon GPU
(`mps`), PyTorch `2.14.1`. All six new before/after training runs used **CPU**,
PyTorch `2.14.1`, because MPS was unavailable in the execution sandbox. The
before/after comparison therefore uses the same device. Original MPS and
repeated CPU seed-42 accuracy, F1, and confusion counts agree; confidence
values differ slightly. No cross-device numerical reproducibility is assumed.

**Actual split sizes:** 139 train / 31 validation / 30 test, stratified.
The notebook intends 70/15/15, but scikit-learn rounds the fractional validation
size up to 31 in this implementation. Each test split has 14 `proposal` and
16 `argument` posts. The saved Unit 5 test file exactly matches the notebook's
seed-42 selection, in order and labels.

**Execution and evidence:** `run_experiment.py` executes section 1 setup,
sections 2–3, section 6's entire three-seed cell, and section 7. It imports the
training/evaluation function definitions directly from notebook sections 4–5
without overwriting the original Unit 5 artifacts. Logs, settings, file hashes,
per-post predictions, and per-seed test files are in `evaluation/`. It retains
each completed seed in a separate partial file if interrupted. Completed
three-seed results are `results_three_seeds_before.json` and
`results_three_seeds_after.json`.

Reproduce in a fresh checkout without existing three-seed result files:

```bash
.venv/bin/python run_experiment.py --label before
.venv/bin/python run_experiment.py --label after --max-length 256
```

The runner refuses to overwrite completed three-seed files. It requires the
Unit 5 base model to be cached. The notebook itself retains its original
128-token settings and `RUN_LABEL = "before"`; the runner explicitly sets
`RUN_LABEL = "after"` and the one input-length override for the improvement.

---

## How I Used AI

<!-- Two specific moments — what you asked, what came back, what you changed.

     ⚠️ Plus disclosure of any pre-labelling. If you had a model pre-label a
     batch and then read and corrected every one, say that. It's an allowed
     workflow and disclosing it costs you nothing. Not disclosing it is the
     problem. -->

**Moment 1 — understanding the notebook's label map**

- *What I asked for:* Why the notebook only used the default labels and
  whether I was supposed to edit them.
- *What came back:* AI inspected the notebook and CSV, explained that
  `LABELS` is hardcoded, and identified the correct list as
  `["proposal", "argument"]`.
- *What I changed:* The saved notebook now uses the two-label configuration,
  and the recorded training results use that map.

**Moment 2 — collecting and pre-labeling the dataset**

- *What I asked for:* Gather r/Minecraft posts and finish the remaining
  Milestone 4 work after proceeding with my unaided labels because of time.
- *What came back:* AI collected complete public post text, screened out
  unsuitable posts, applied the written definitions, and expanded the CSV
  from 30 to 200 posts. It supplied source URLs, counts, and three draft hard
  cases, and marked every AI label as pending human review.
- *What I changed:* I supplied nine unaided labels. The original choices
  remain intact; I have not yet confirmed or corrected the AI labels.

**Pre-labelling disclosure:** AI pre-labeled 191 of 200 collected posts;
those labels still await student review. The other 9 labels were supplied
unaided by the student, with capitalization normalized afterward. This
collection uses targeted topic searches rather than random subreddit sampling,
so its label balance does not estimate the community's natural distribution.

Earlier AI assistance is also documented in the taxonomy's generated boundary
examples and the three draft hard-case explanations. Those generated examples
are not training posts. The acceptance criteria were AI-assisted, as disclosed
in `criteria.md`. The recorded evaluation does not establish that the pending
personal review or independent labeling has happened.

**Moment 3 — Unit 6 evaluation and interpretation**

- *What I asked for:* Follow the evaluation milestones and identify the work
  requiring my decisions later.
- *What came back:* AI inspected the actual notebook and saved split, recorded
  an AI-assisted prediction before reading scores, ran both zero-shot prompts,
  and ran the notebook's training functions across three before and three
  after seeds. It audited training-input lengths, selected the single
  128-to-256-token intervention, verified metrics from saved predictions, and
  drafted the tables, verdicts, and bounded diagnoses below.
- *What I changed:* The repository now contains measured evaluation artifacts
  and an AI-assisted draft write-up. I have not yet personally confirmed the
  interpretations or completed the blank personal labeling templates. AI later extracted my 19 entered labels from Numbers and computed partial
  staff agreement at my request. It drafted rule-based recommendations for
  five disagreements, clearly marked as drafts rather than my final calls.
  It did not invent student labels or a delayed personal agreement rate.

### Unit 5 submission status

- [x] Five numbered numerical criteria and rationales are in `criteria.md`.
- [x] All five required README sections have content, including the hardest
  boundary, three draft hard cases, and AI disclosure.
- [x] `labels.csv` has `text`, `label`, and `note` columns; no label exceeds 70%.
- [x] Reach 200 posts, or at least 150 with the stop-rule explanation.
- [ ] Complete the required 20 unaided cold labels and review every
  AI-prelabeled post.
- [x] Correct the notebook label map and complete sections 1–5.
- [x] Generate and commit `results.json` and `test_split.csv`.
- [x] Commit the Milestone 4 dataset, source URLs, and README work.
- [x] Verify at least four new project commits before submission.
- [ ] Push the completed work and submit my fork's URL.

The sections below record Unit 6 measurements and partial staff agreement
from 19 student labels. Eleven staff labels, final personal adjudications, and
the delayed consistency check remain incomplete; see
[PERSONAL_REVIEW.md](PERSONAL_REVIEW.md).

<!-- UNIT 6 — THE TEST -->

---

## Baseline vs. Trained

**What I predicted before I looked:**

AI-assisted prediction, recorded before inspecting the existing scores or running either baseline: the fine-tuned model will outperform the zero-shot baseline on `proposal` F1 because Minecraft-specific wording can distinguish an endorsed change from a defended or rejected suggestion. This prediction still needs my personal confirmation.

This was committed in `ace568b` before the AI read `results.json` or ran a
baseline. It is an AI-assisted prediction, not a claim that I independently
made it before seeing results. The interpretations below are AI-assisted drafts
for my review.

Both models were scored on **all 30 posts in `test_split.csv`**, the original
seed-42 held-out set. There was no random-sample fallback and no sample cap.
The baseline is `facebook/bart-large-mnli` using the two definition sentences
copied from this README into `label_definitions.txt`. The file's comments are
ignored; examples and the longer boundary discussion are not part of its prompt.
The baseline and preserved Unit 5 trained run both used MPS.

| Measure | Baseline | Trained | Difference |
|---|---|---|---|
| Overall accuracy | 0.633 | 0.533 | -0.100 |
| Macro F1 | 0.576 | 0.348 | -0.229 |
| F1 — `argument` | 0.732 | 0.696 | -0.036 |
| F1 — `proposal` | 0.421 | 0.000 | -0.421 |

Difference means trained minus baseline. The prediction was wrong: fine-tuning
lost 0.421 proposal F1 and 10 percentage points of accuracy on these posts.
This experiment supplies no evidence of added accuracy from fine-tuning.
The baseline is a larger model with a longer input window; this comparison
measures these two systems, not the isolated causal effect of fine-tuning.

### What the definitions were worth

| Prompt | Accuracy | Macro F1 | Proposal F1 | Argument F1 |
|---|---|---|---|---|
| Definitions — main baseline | 0.633 | 0.576 | 0.421 | 0.732 |
| Bare names — ablation | 0.667 | 0.665 | 0.643 | 0.688 |

Definitions minus bare names is **−0.033 accuracy**: 19 rather than 20 correct
posts. The definitions did not improve this run. One post on a 30-post test
set does not establish that definitions are generally harmful. I keep the
specified definitions baseline as the main result rather than selecting the
better prompt after seeing its score. Both runs used the same model, MPS
device, and held-out posts. Predictions are saved in `baseline_results.json`
and `baseline_bare_names_results.json`.

```bash
HF_HOME=.cache/huggingface .venv/bin/python baseline.py --trained results.json
HF_HOME=.cache/huggingface .venv/bin/python baseline.py \
  --definitions evaluation/intentionally_missing_definitions.txt \
  --out baseline_bare_names_results.json --trained results.json
```

The missing definitions path is deliberate; the real definitions file was
retained. Default pipeline tokenization and hypothesis construction were used
for both baseline runs. Model revision, prompt, device, and input hashes are
recorded in `evaluation/baseline_provenance.json`.

---

## Run Log — Before

Seeds **42, 7, 2024**, CPU, PyTorch `2.14.1`; 128 input tokens. Criteria and
thresholds are unchanged from `criteria.md`. Criteria 1–3 must pass on every
seed using unrounded values. Criteria 4–5 are measured once; their repeated
cells show that they do not vary with seed.

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1. Overall accuracy | ≥ 0.75 | 0.533 | 0.533 | 0.533 | MISSED |
| 2. Proposal F1 | ≥ 0.70 | 0.000 | 0.000 | 0.000 | MISSED |
| 3. Argument F1 | ≥ 0.70 | 0.696 | 0.696 | 0.696 | MISSED |
| 4. Dataset balance | Each label 40–60% | 45% / 55% | 45% / 55% | 45% / 55% | MET |
| 5. Unaided repeat-label agreement | ≥ 27/30 after ≥ 48 hours | Not tested | Not tested | Not tested | MISSED (unverified) |

All three runs have macro F1 **0.348**. Accuracy spread is **0.000**.
This apparent stability comes from predicting `argument` for every post,
not from consistently distinguishing the labels. Every split has 16 argument
posts out of 30, so the all-argument majority guesser also scores 0.533.
There are only 14 proposal test examples per seed; one recovered proposal
moves accuracy by 3.3 percentage points. Seeds change both split membership
and initialization; their held-out sets can overlap and are not independent
samples of a new population.

### Confusion matrix — Before, seed 42

| true \ predicted | proposal | argument |
|---|---|---|
| **proposal** | 0 | 14 |
| **argument** | 0 | 16 |

**Biggest confusion:** 14 reference `proposal` posts were called `argument`,
while zero `argument` posts were called `proposal`. Seeds 7 and 2024 have the
same counts on their own held-out posts. These reference labels include
unreviewed AI labels; they are not independently verified human ground truth.

---

## Verdicts and Diagnoses

| # | Criterion | Verdict before | Verdict after | How I decided |
|---|---|---|---|---|
| 1 | Accuracy ≥ 0.75 on every seed | MISSED | MISSED | Before: 0.533 throughout; after: best seed 0.667, below 0.75. |
| 2 | Proposal F1 ≥ 0.70 on every seed | MISSED | MISSED | Before: 0 throughout; after: 0, 0.444, 0.133. |
| 3 | Argument F1 ≥ 0.70 on every seed | MISSED | MISSED | Seed 42 remains 0.695652, below 0.70; two passing after-seeds do not rescue it. |
| 4 | Each label 40–60% of deduplicated data | MET | MET | 90 proposal / 110 argument = 45% / 55%; dataset unchanged. |
| 5 | ≥ 90% unaided repeat agreement after ≥ 48 hours | MISSED (unverified) | MISSED (unverified) | The required personal repeat-label record does not exist. No rate was inferred from another test. |

MISSED (unverified) means the required evidence is absent; it does not mean a
measured personal agreement rate was below 90%. No original target was revised.

**1. Accuracy miss — failure to distinguish proposals.** All 42 proposal
reference instances across the three before runs are missed; no argument
reference instances are missed. This explains the low accuracy directly.
It does not establish why the model collapsed. The training partitions have
62–63 proposals and 76–77 arguments, so a severely missing training class is
not the immediate explanation. Small data and short training remain plausible.

**2. Proposal F1 miss — lost context is a testable contributor.** In the
three training partitions, **89, 90, and 86 of 139 posts** exceed 128 tokens.
The label rule gives priority to any endorsed specific change anywhere in the
post, which may occur beyond the visible prefix. This motivated the one
input-length intervention. There has been no span-level audit proving where
each decisive suggestion occurs, so this is a supported hypothesis rather
than a demonstrated explanation of every error. Even at 256 tokens, 48, 55,
and 48 training posts remain truncated.

**3. Argument F1 miss — biased predictions create false positives.** Argument
recall is 1.0 before, but precision is only 16/30 = 0.533 because every proposal
is also assigned argument. Its F1 is therefore 0.695652, just below 0.70.
Rounding it to 0.70 would conceal a miss. The improvement reduces this problem
on two seeds, but leaves seed 42 unchanged.

**5. Consistency criterion miss — missing personal procedure.** The data notes
record only 9 cold labels and 191 AI-prelabeled labels pending review. No
unaided second labeling with a documented 48-hour gap has been completed.
That is a missing measurement, not evidence of a model limitation. The prepared
blind sample in `relabel_review.csv` is not a completed experiment.

**Agreement evidence and the limit on these diagnoses:** On the 19 posts I
completed, 14 match staff and 5 disagree. Three staff-analysis posts were
labeled hot_take, one staff-analysis post was labeled reaction, and one
staff-hot_take post was labeled reaction. This points to difficulty recognizing
when a checkable comparison is carrying an argument and separating a general
claim from a personal response. The AI draft recommends pile (a) for each,
with individual reasons below; I have not yet adopted those calls. This is
direct evidence of rule-application differences on the completed staff subset,
and a reason to audit boundary decisions in my Minecraft data. It does not
prove which of the 191 pending AI labels is wrong, or that labeling caused the
trained model's collapse. The subset was chosen by completion rather than
random sampling, so 73.7% must not be treated as a full-set consistency estimate.
Staff agreement is also not a replacement for criterion 5 under a different
taxonomy and a delayed, unaided procedure.

**AI adversarial verdict check, for my review:** The strongest case for marking
criterion 3 MET is that two improved seeds pass and the third rounds to 0.70.
I reject that reading: the written target applies to every seed and its raw
seed-42 F1 is below 0.70. This was an AI-assisted check, not a claim of an
independent breakout or Claude discussion.

---

## Agreement Report

**Partial agreement: 14 / 19 = 73.7%.** The student completed **19 of 30**
posts in `staff_labeling_template.numbers` and explicitly requested proceeding
with that subset. The 19 labels were exported unchanged to
`my_staff_labels.csv` and saved before inspecting the key. The other **11**
posts were excluded, not counted as wrong and not filled by AI. All 19 texts
match the original posts exactly. Source hash and completed/remaining IDs are
recorded in `evaluation/staff_labeling_progress.json`.

The comparison uses the supplied TF key in `data/staff_labels.csv` and the
provided agreement script, with an explicit partial-report mode:

```bash
.venv/bin/python finish_agreement.py --allow-partial
```

`agreement_results.json` records the denominator, five disagreements, partial
status, and eleven remaining posts. The default helper still requires all 30.
Only the completed posts' staff labels are presented in the write-up. This is
partial evidence and does not fulfill the assignment's full 30-post exercise.

### Disagreements — AI-assisted drafts for personal review

Each full post, both labels, the strongest case for the student's original
label, and an AI recommendation are in
[agreement_adjudication.md](agreement_adjudication.md). The student's final
calls and pile choices remain pending. All five tentative recommendations favor
the staff label because of the specific rules below; no ambiguous case was
invented to force a mix of outcomes.

**1. Post:** The club championship scoring changed in 2019 from top-6 to top-10. Since then our B team has finished above the A team twice. That's not depth improving, it's the scoring rewarding turnout.

**Staff / mine:** `analysis` / `hot_take`.

**AI draft call:** `analysis`. The change from top-6 to top-10 in 2019 and the B team beating the A team twice are the evidence for a scoring-system explanation. They carry the argument rather than decorating it (rule 1). Suggested pile **(a)**; personal final call and reason pending.

**2. Post:** Everyone blames the hill at 18 miles. I split the field into people who ran the first half under 1:45 and over, and the slowdown after 18 was almost identical for both groups. If the hill were the problem the fast starters would fall apart harder.

**Staff / mine:** `analysis` / `hot_take`.

**AI draft call:** `analysis`. The under/over-1:45 grouping and similar slowdown after mile 18 form a checkable comparison used to challenge the hill explanation. The inference can be debated, but the comparison does argumentative work (rule 1). Suggested pile **(a)**; personal final call and reason pending.

**3. Post:** Ran the same loop in 4C and in 24C within a fortnight, same effort by heart rate. 90 seconds slower in the heat over six miles. People keep saying heat costs you 'a bit' and it's more than that.

**Staff / mine:** `analysis` / `hot_take`.

**AI draft call:** `analysis`. The same loop, matched heart-rate effort, 4C versus 24C, and 90-second difference support the claim that heat costs more than a little. The numbers are central evidence, so analysis fits rule 1. Suggested pile **(a)**; personal final call and reason pending.

**4. Post:** Three of us ran the same session on the same day, different shoes, within 10 seconds of each other over 5 miles. I'm not saying shoes do nothing, but whatever they do was smaller than the noise between three people.

**Staff / mine:** `analysis` / `reaction`.

**AI draft call:** `analysis`. Different shoes, the same session/day, and a spread of 10 seconds over 5 miles directly support the argument that the observed shoe effect was smaller than variation between runners. First-person experience does not override load-bearing evidence (rule 3). Suggested pile **(a)**; personal final call and reason pending.

**5. Post:** The club needs to stop pretending the Tuesday session is for everyone. It isn't and it never has been.

**Staff / mine:** `hot_take` / `reaction`.

**AI draft call:** `hot_take`. The claim that the Tuesday session is not for everyone is a general assertion about the club, with no supporting fact and no account of an immediate personal event. Rule 2 therefore favors hot_take. Suggested pile **(a)**; personal final call and reason pending.

**Pattern:** Four disagreements concern posts that offer checkable comparisons
as support, despite first-person wording or a confident conclusion. The fifth
concerns a general unsupported assertion that was labeled as a personal
reaction. These are useful boundary-review targets, but the incomplete staff
set and the different taxonomy limit what they establish about my own dataset.

For the discussion exercise, disagreement 4 is a concrete starting point: the
case for reaction is its personal-experience framing, while the case for
analysis is its quantified comparison and explicit inference about shoes.
Both cases are developed in the linked draft; the final personal judgment has
not been made.

---

## The Improvement

**One change:** increase `MAX_LENGTH` from **128 to 256 tokens**. No label rows
were changed. Epochs, learning rate, batch size, base model, device, seed list,
and train/validation/test membership per seed stayed fixed. The plan was
recorded in `evaluation/improvement_plan.json` before running the improvement.
The runner explicitly sets `RUN_LABEL = "after"`, preserving the before file.

**Diagnosis:** the original model read truncated prefixes of most training
posts despite a taxonomy requiring it to notice an endorsed change anywhere.
The intervention tests that input constraint; it does not test label cleanup
or longer training.

### Run Log — After

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1. Overall accuracy | ≥ 0.75 | 0.533 | 0.667 | 0.567 | MISSED |
| 2. Proposal F1 | ≥ 0.70 | 0.000 | 0.444 | 0.133 | MISSED |
| 3. Argument F1 | ≥ 0.70 | 0.696 | 0.762 | 0.711 | MISSED |
| 4. Dataset balance | Each label 40–60% | 45% / 55% | 45% / 55% | 45% / 55% | MET |
| 5. Unaided repeat-label agreement | ≥ 27/30 after ≥ 48 hours | Not tested | Not tested | Not tested | MISSED (unverified) |

| Measure | Seed 42 | Seed 7 | Seed 2024 |
|---|---|---|---|
| Accuracy change | +0.000 | +0.133 | +0.033 |
| Macro F1 | 0.348 | 0.603 | 0.422 |
| Proposal recall | 0.000 | 0.286 | 0.071 |

**Did it help?** It improved mean accuracy from **0.533 to 0.589** (+5.6
percentage points) and recovered 4 proposals on seed 7 and 1 on seed 2024,
but seed 42 did not improve and no previously missed criterion became MET.
After accuracy spread is **0.133**, above the assignment's ten-point warning;
the improvement is sensitive to split/initialization and is not a stable
solution. Training took roughly 50 seconds per seed after versus 21 seconds
before on CPU. Only this one intervention was tested.

### Confusion matrices — After

Seed 42:

| true \ predicted | proposal | argument |
|---|---|---|
| **proposal** | 0 | 14 |
| **argument** | 0 | 16 |

Seed 7:

| true \ predicted | proposal | argument |
|---|---|---|
| **proposal** | 4 | 10 |
| **argument** | 0 | 16 |

Seed 2024:

| true \ predicted | proposal | argument |
|---|---|---|
| **proposal** | 1 | 13 |
| **argument** | 0 | 16 |

All after runs still make errors only from proposal to argument. The largest
off-diagonal after count is 14 on seed 42; on seed 7 it falls to 10, with zero
errors in the reverse direction. The saved zero-shot baseline is compared
only with seed 42, its matching split; its 0.633 score cannot be compared
fairly with seed 7's 0.667 on different posts.

---

## What's Still Broken

- **Criterion 1 — accuracy:** audit reviewed training labels and validation
  learning curves, then test a single further training intervention. I stopped
  after the one planned change to preserve an interpretable before/after
  comparison; the current model remains close to a majority guesser.
- **Criterion 2 — proposal F1:** review the specific-change boundary and locate
  decisive proposal clauses in training posts. Truncation is still possible
  after the change. Personal label review and a completed adjudication of the partial staff
  agreement evidence are needed before attributing this to label inconsistency.
- **Criterion 3 — argument F1:** reduce proposals incorrectly called argument
  rather than trying to raise argument recall, which is already 1.0. I stopped
  because this experiment did not fix that bias across every seed, and further
  model selection against these test sets would overfit the evaluation.
- **Criterion 5 — consistency:** complete personal initial review, document
  timing, and carry out the blind repeat-label check at least 48 hours later.
  Automation cannot supply unaided student labels or an elapsed personal
  labeling procedure. Staff agreement now covers 19/30 posts; personal adjudication remains pending.

**The gap between what I meant my labels to capture and what the model learned:**
I intended the labels to distinguish an endorsed specific Minecraft change
from a supported position without one. The original confusion matrix instead
shows a model assigning every post to argument, and the longer-input runs
recover only 0–4 of 14 proposals per seed while still assigning all 16 arguments
correctly.

### Submission status

- [x] Prediction recorded before AI inspected scores; AI authorship disclosed.
- [x] Definitions baseline and bare-name ablation on the saved held-out posts.
- [x] Three before and three after seeds, device, five-row run logs, and typed matrices.
- [x] Strict verdicts, evidence-limited diagnoses, one intervention, and remaining issues.
- [x] Results, prediction files, logs, and provenance retained in this repository.
- [x] Supplied TF key and partial agreement computed from 19 unchanged student labels.
- [ ] Remaining 11 staff labels and final personal calls on the five current disagreements.
- [ ] Personal label review and criterion 5's documented delayed consistency check.
- [ ] Student review of AI-assisted interpretation and completion of the discussion exercises.
- [ ] Push completed work and submit the same URL: https://github.com/Ziyu-Zhou/takemeter.

See [PERSONAL_REVIEW.md](PERSONAL_REVIEW.md) for the exact remaining steps.
Numerical artifact checks are recorded in `evaluation/verification.json`.

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
