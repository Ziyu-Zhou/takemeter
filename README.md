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
dataset is a small exploratory sample; a completed training run is not yet
recorded in this repository.

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

**Run status:** Setup has been run, but the saved notebook contains no
completed split, training, or evaluation outputs. Neither `results.json` nor
`test_split.csv` is present. The settings below describe the planned run,
not a claim that training has finished.

**Base model:** `distilbert-base-uncased`, fine-tuned for two output labels:
`proposal` and `argument`.

**Settings:**

| Setting | Planned value |
|---|---|
| Epochs | 3 |
| Learning rate | `2e-5` |
| Batch size | 16 |
| Maximum input length | 128 tokens per post |
| Seed | 42 |
| Input file | `labels.csv` |
| Split | Stratified 70% train / 15% validation / 15% test |

**Changes from the defaults, and why:** No hyperparameter changes are
planned. Section 2 must use `LABELS = ["proposal", "argument"]` to match my
Minecraft taxonomy instead of the starter's `analysis`, `hot_take`, and
`reaction`. At this documentation update, the saved notebook still contains
the starter label list, so that edit remains necessary before training.

**Device recorded by setup:** `mps` — Apple Silicon GPU (MPS), with
PyTorch `2.14.1`. This comes from the saved section 1 output; the device must
also be checked against `results.json` after training. Device information
matters because the same seed and dataset can produce different results on
different hardware.

**Split sizes:** The earlier 30-row preview is obsolete after expanding the
file to 200 posts. Section 3 must be rerun to report actual label counts for
the new 70/15/15 split before training. No split files were created during
collection. Whole posts remain in the CSV, but the tokenizer will truncate
model inputs longer than 128 tokens.

**Run artifacts:** Pending. After correcting the label map, run notebook
sections 1–5 and retain `results.json` and `test_split.csv` in the repository.
Sections 6–7 and interpretation of the evaluation numbers belong to Unit 6.

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
- *What I changed:* This README now records the required two-label
  configuration. The saved notebook edit is still pending, so I am not
  claiming that the corrected configuration has already been used to train.

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
in `criteria.md`. This README update does not establish that the pending
personal review or independent labeling has happened.

### Unit 5 submission status

- [x] Five numbered numerical criteria and rationales are in `criteria.md`.
- [x] All five required README sections have content, including the hardest
  boundary, three draft hard cases, and AI disclosure.
- [x] `labels.csv` has `text`, `label`, and `note` columns; no label exceeds 70%.
- [x] Reach 200 posts, or at least 150 with the stop-rule explanation.
- [ ] Complete the required 20 unaided cold labels and review every
  AI-prelabeled post.
- [ ] Correct the notebook label map and complete sections 1–5.
- [ ] Generate and commit `results.json` and `test_split.csv`.
- [x] Commit the Milestone 4 dataset, source URLs, and README work.
- [ ] Verify at least four new project commits before submission.
- [ ] Push the completed work and submit my fork's URL.

The sections below are the Unit 6 template and are not required by the pasted
Unit 5 instructions. They remain pending until the corresponding evaluations
and agreement checks have actually been performed.

<!-- ═══════════════════════ UNIT 6 — THE TEST ═══════════════════════

     Don't fill these in during unit 5.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Baseline vs. Trained

<!-- Both models on the same posts. `python baseline.py --trained results.json`
     prints this table for you. -->

| Measure | Baseline | Trained | Difference |
|---|---|---|---|
| Overall accuracy |  |  |  |
| Macro F1 |  |  |  |
| F1 — `label_one` |  |  |  |
| F1 — `label_two` |  |  |  |

**What I predicted before I looked:**
<!-- Milestone 1 asks you to write this BEFORE seeing the trained numbers. A
     prediction made afterwards isn't one. -->

**What the gap actually means:**
<!-- If the baseline matched your trained model, your fine-tuning added
     nothing — and that is a real finding, not a failure. Say it plainly. -->



---

## Run Log — Before

<!-- Five criteria across three seeds. The notebook's section 6 prints the
     spread table; the Target and Verdict columns are yours. -->

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

### Confusion matrix

<!-- ⚠️ TYPED AS A MARKDOWN TABLE. The notebook prints one ready to paste.
     An image of a matrix earns nothing. -->

| true \ predicted |  |  |  |
|---|---|---|---|
| **** |  |  |  |
| **** |  |  |  |
| **** |  |  |  |

**My biggest off-diagonal number, and what it means:**
<!-- Not "the model made mistakes" — WHICH boundary it didn't learn, and which
     direction. "7 real analysis posts were called hot_take and only 3 went the
     other way" is a direction, not just an error rate. -->



---

## Verdicts and Diagnoses

<!-- MET or MISSED against LAST UNIT's target. The target has to hold across
     all three seeds, not turn up sometimes. -->

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |

**Diagnoses**

<!-- For each miss: the cause, and how you know. The four common causes are:
     too few examples for a label, a boundary you applied inconsistently, a
     genuinely hard label pair, and a task the model can't reach from this
     much data.

     ⚠️ Use your agreement report as evidence. It is the only instrument you
     have that can tell a LABELLING problem from a MODEL problem, and this
     section is graded on whether you used it that way. -->



---

## Agreement Report

<!-- Your rate against the staff set, and every disagreement adjudicated.

     Remember you labelled these 30 under the STAFF taxonomy in
     data/staff_taxonomy.md, not your own — so every argument below is made
     from those definitions and those decision rules. -->

**Agreement rate:** ___ / 30 = ___%

<!-- Nobody grades this number. A 60% who argues every disagreement from the
     stated rules beats a 95% who wrote "staff was right" nine times. Several
     of the 30 were chosen because they're genuinely ambiguous — you should be
     winning some of these. -->

**Disagreements**

<!-- Three lines each: the post, both labels, and who you think is right and
     why — grounded in the staff definitions you were both applying.

     Then sort each into one of three piles:
       (a) the rule covered it and I applied it loosely → a consistency problem
       (b) the rule genuinely doesn't say               → a gap in the definitions
       (c) the rule is ambiguous here and my reading is defensible → argue it.
           This is a legitimate win.

     Pile (a) is the one that matters most for your diagnosis: if you applied a
     written rule two different ways on 30 posts, that is direct evidence about
     what you did across your own 200. -->

**1.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**2.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**What the pattern in my disagreements tells me:**



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Run Log — After

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Did it help, and how do I know:**

<!-- If it didn't, say so. Relabelling that didn't help is a genuinely
     interesting result and earns full credit. -->



---

## What's Still Broken

<!-- For each criterion still missed: what you'd do, and why you stopped. -->



**The gap between what I meant my labels to capture and what the model
learned:**
<!-- Two sentences. Your confusion matrix is the evidence. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 5

       [ ] criteria.md has five numbered criteria, each naming a NUMBER
       [ ] Each has a reason underneath tied to your data or taxonomy
       [ ] labels.csv: at least 150 rows, text/label/note, ONE file not split
       [ ] No label above 70%
       [ ] All five unit 5 sections have real content
       [ ] Label Taxonomy includes the decision rule for your hardest boundary
       [ ] The Dataset includes three hard cases
       [ ] results.json and test_split.csv committed (the notebook does this)
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 6

       [ ] Baseline vs. Trained table, with your prediction written beforehand
       [ ] Run Log — Before, five criteria across three seeds
       [ ] Confusion matrix TYPED AS A MARKDOWN TABLE
       [ ] A verdict on every criterion
       [ ] A diagnosis for every miss, using the agreement report as evidence
       [ ] Agreement Report with every disagreement adjudicated
       [ ] One improvement, with Run Log — After
       [ ] What's Still Broken
       [ ] results_three_seeds_before.json, results_three_seeds_after.json,
           baseline_results.json and
           agreement_results.json committed
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
