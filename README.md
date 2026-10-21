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
TakeMeter will explore differences in how these posts explain opinions and
suggest improvements. Its two starting labels are `proposal` and `argument`.

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

**How I labelled them:** <!-- Cold first? Pre-labelled with AI and corrected?
Say so plainly — the disclosure is required, not penalised. -->

**Counts per label:**

| Label | Count | Share |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |
| **Total** |  | 100% |

**Three hard cases**

<!-- Any post that made you pause: what it was, which two labels it could have
     been, and what you chose. These are worth more than the easy 190. -->

**1.**
> *The post:*
>
> *Could have been:*
>
> *I chose, because:*

**2.**
> *The post:*
>
> *Could have been:*
>
> *I chose, because:*

**3.**
> *The post:*
>
> *Could have been:*
>
> *I chose, because:*

---

## The Training Run

<!-- Your starting model, your settings, and anything you changed and why. -->

**Base model:**

**Settings:** <!-- epochs, learning rate, batch size, seed -->

**Anything I changed from the defaults, and why:**

**Split sizes:** <!-- train / val / test, and per-label counts in the test
split. If a label had fewer than about 8 in test, say so — it explains a lot
of next unit's variance. -->



---

## How I Used AI

<!-- Two specific moments — what you asked, what came back, what you changed.

     ⚠️ Plus disclosure of any pre-labelling. If you had a model pre-label a
     batch and then read and corrected every one, say that. It's an allowed
     workflow and disclosing it costs you nothing. Not disclosing it is the
     problem. -->

**Moment 1**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Pre-labelling disclosure:**

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
