#!/usr/bin/env python3
"""After your own 30 labels are saved, compare and prepare adjudication.

Never reads the answer key until all student labels pass validation.
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
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    mine_path = args.mine.resolve()
    posts = read_csv(root / 'data/staff_posts.csv')
    if not mine_path.exists():
        parser.error('Fill staff_labeling_template.csv yourself and save it as my_staff_labels.csv first.')
    mine = read_csv(mine_path)
    valid = {'analysis', 'hot_take', 'reaction'}
    if len(mine) != 30 or any(row.get('label') not in valid for row in mine):
        parser.error('All 30 rows need one valid label: analysis, hot_take, reaction. Answer key not opened.')
    if Counter(row.get('text') for row in mine) != Counter(row['text'] for row in posts):
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
    out = root / 'agreement_adjudication.md'
    if out.exists():
        print('Kept existing agreement_adjudication.md; do not overwrite your calls.')
        return
    lines = ['# Personal adjudication — complete every disagreement', '',
             f'Agreement: {result["agreed"]} / {result["compared"]} = {result["agreement_rate"]:.1%}.', '',
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
