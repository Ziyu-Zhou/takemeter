#!/usr/bin/env python3
"""After your own labels are saved, compare and prepare adjudication.

Requires all 30 by default. Use --allow-partial only for an explicitly partial
report. Never reads the answer key until supplied student labels are valid.
"""
import argparse
import csv
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path


def read_csv(path):
    with path.open(newline='', encoding='utf-8') as stream:
        return list(csv.DictReader(stream))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mine', type=Path, default=Path('my_staff_labels.csv'))
    parser.add_argument('--allow-partial', action='store_true',
                        help='compare only supplied labels and mark the report incomplete')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    mine_path = args.mine.resolve()
    posts = read_csv(root / 'data/staff_posts.csv')
    if not mine_path.exists():
        parser.error('Fill staff_labeling_template.csv yourself and save it as my_staff_labels.csv first.')
    mine = read_csv(mine_path)
    valid = {'analysis', 'hot_take', 'reaction'}
    expected = Counter(row['text'] for row in posts)
    supplied = Counter(row.get('text') for row in mine)
    if args.allow_partial:
        if not 1 <= len(mine) <= len(posts) or any(row.get('label') not in valid for row in mine):
            parser.error('Partial input needs 1–30 valid, nonblank labels. Answer key not opened.')
        if any(count != 1 or text not in expected for text, count in supplied.items()):
            parser.error('Partial input has duplicate or changed post text. Answer key not opened.')
    elif len(mine) != 30 or any(row.get('label') not in valid for row in mine):
        parser.error('All 30 rows need one valid label: analysis, hot_take, reaction. Answer key not opened.')
    if not args.allow_partial and supplied != expected:
        parser.error('Post text must match all 30 original posts exactly. Answer key not opened.')
    key_path = root / 'data/staff_labels.csv'
    if not key_path.exists():
        parser.error('Your labels are complete. Get data/staff_labels.csv from your TF next.')
    key = read_csv(key_path)
    if Counter(row.get('id') for row in key) != Counter(row['id'] for row in posts):
        parser.error('Staff key must contain exactly one entry for every original post ID.')
    for row in key:
        label = next((row.get(col) for col in ('label', 'staff_label', 'my_label', 'your_label')
                      if col in row), None)
        if label not in valid:
            parser.error('Staff key contains a missing or unknown label.')
    subprocess.run([sys.executable, str(root / 'agreement.py'), '--mine', str(mine_path)],
                   cwd=root, check=True)
    result = json.loads((root / 'agreement_results.json').read_text())
    result.update({'partial': len(mine) < len(posts), 'total_staff_posts': len(posts),
                   'student_labels_supplied': len(mine),
                   'remaining_unlabeled': len(posts) - len(mine)})
    (root / 'agreement_results.json').write_text(json.dumps(result, indent=2) + '\n')
    out = root / 'agreement_adjudication.md'
    if out.exists():
        print('Kept existing agreement_adjudication.md; do not overwrite your calls.')
        return
    lines = ['# Personal adjudication — complete every disagreement', '',
             f'Agreement: {result["agreed"]} / {result["compared"]} = {result["agreement_rate"]:.1%}.', '',
             f'Coverage: {len(mine)}/{len(posts)} posts. ' +
             ('PARTIAL: remaining posts excluded, not counted as wrong.' if result['partial'] else 'Complete.'), '',
             'Use data/staff_taxonomy.md. Piles: (a) loose application; (b) rule gap; (c) defensible ambiguity.', '']
    for index, row in enumerate(result['disagreements'], 1):
        lines += [f'## Disagreement {index}', '', row['text'], '',
                  f'Staff: `{row["staff"]}`; mine: `{row["mine"]}`.', '',
                  'My call and rule-based reason: **PENDING MY JUDGMENT**', '',
                  'Pile (a/b/c): **PENDING**', '']
    if not result['disagreements']:
        lines += ['No disagreements. Explain whether the rules felt clear and why.']
    out.write_text('\n'.join(lines) + '\n')
    print('Prepared agreement_adjudication.md. Complete the calls and copy the report into README.md.')


if __name__ == '__main__':
    main()
