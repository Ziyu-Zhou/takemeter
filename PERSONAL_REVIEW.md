# Work that needs you

The evaluation can run automatically. These steps require your labels or
judgment. Blank templates are preparation, not completed evidence.

1. Read `data/staff_taxonomy.md`. Label all 30 posts in
   `staff_labeling_template.csv` yourself using `analysis`, `hot_take`, or
   `reaction`. Keep the text unchanged. Save as `my_staff_labels.csv`.
   Do this before opening any staff answer key.
2. After saving your labels, obtain `data/staff_labels.csv` from your TF.
   In this directory run `.venv/bin/python finish_agreement.py`.
   It validates all 30 personal labels before reading the key, runs the
   provided `agreement.py`, and creates `agreement_adjudication.md`.
3. For every disagreement, make your own call using the written staff rules
   and select pile (a), (b), or (c). Add the completed report to the README.
   For the discussion exercise, choose one defensible disagreement; an AI can
   make both cases, but the final call and reason need to be yours.
4. Review the existing 191 AI-prelabeled Minecraft posts in `labels.csv`.
   Their notes still truthfully say `pending human review`. The previous
   unit also required 20 unaided cold labels; only 9 are recorded. Existing
   AI labels cannot be retroactively called cold labels.
5. Criterion 5 is a separate, personal consistency experiment under your
   Minecraft taxonomy. `relabel_review.csv` contains a shuffled blind sample
   of 30 posts (15 per original label, seed 42), with original CSV row numbers
   recorded in `evaluation/relabel_selection.json`. Its label column is blank.
   Before treating it as a test of your own repeatability, establish which
   original labels you personally supplied/reviewed and when. Relabel without
   AI, original labels, notes, or predictions, at least 48 hours after that
   initial personal labeling. If original labels change during review,
   regenerate and record the balanced sample from that reviewed dataset.
   Do not claim a 48-hour personal experiment based on the old AI labels.
6. Read and adopt or edit the AI-assisted prediction and interpretations in
   README.md. The prediction was committed before AI inspected the scores;
   confirming it now does not make it a prior personal prediction.
7. After those evidence gaps are resolved, push the commits and submit the
   same repository URL: https://github.com/Ziyu-Zhou/takemeter.

No accuracy/F1 target has been lowered. Criterion 5 remains MISSED
(unverified), rather than receiving a made-up agreement rate. The staff
agreement report is also pending; no answer key or personal judgments were
invented.
