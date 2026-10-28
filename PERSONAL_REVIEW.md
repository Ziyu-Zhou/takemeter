# Work that needs you

The evaluation can run automatically. These steps require your labels or
judgment. Blank templates are preparation, not completed evidence.

1. **Partial labeling accepted for the current report:** your saved Numbers
   file contains 19 labels. They were exported unchanged to
   `my_staff_labels.csv`; agreement is **14/19 = 73.7%**. You asked to work
   with these entries, so the remaining 11 are excluded and left unlabeled.
   The full assignment still calls for 30 posts.
2. The TF key is present and the partial comparison is saved. Reproduce it
   with `.venv/bin/python finish_agreement.py --allow-partial`. Without that
   explicit flag, the helper still requires all 30 labels. If you complete the
   rest later, update the student CSV and rerun the full comparison. Keep the
   remaining labels independent of the answer key.
3. Your five final labels and short reasons are now recorded in
   `agreement_adjudication.md` and the README. AI preserved your exact words,
   added rule-specific explanations, and inferred pile (a) for each from your
   reasons. Those pile letters were not explicit selections by you and remain
   editable. The original 14/19 agreement score and original labels are intact.
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
agreement report is explicitly partial; no missing student labels or final
personal judgments were invented.
