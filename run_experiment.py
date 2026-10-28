#!/usr/bin/env python3
"""Run notebook sections 1–3 and 6–7 without requiring a Jupyter kernel.

Uses the notebook's training/evaluation functions verbatim. Keeps the original
results.json and test_split.csv intact; checkpoints each completed seed.
"""
import argparse
import ast
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--label', choices=['before', 'after'], required=True)
    parser.add_argument('--max-length', type=int)
    parser.add_argument('--epochs', type=int)
    args = parser.parse_args()
    if args.max_length and args.epochs:
        parser.error('Change only one training setting per experiment.')
    root = Path(__file__).resolve().parent
    os.chdir(root)
    out = root / f'results_three_seeds_{args.label}.json'
    if out.exists():
        parser.error(f'{out.name} already exists; preserve it before another run.')
    evaluation = root / 'evaluation'
    evaluation.mkdir(exist_ok=True)
    # Downloads are unnecessary: Unit 5 already cached the training model.
    os.environ.setdefault('HF_HUB_OFFLINE', '1')
    os.environ.setdefault('HF_DATASETS_CACHE', str(root / '.cache/datasets'))
    os.environ.setdefault('TOKENIZERS_PARALLELISM', 'false')
    notebook = json.loads((root / 'takemeter.ipynb').read_text())
    ns = {'__name__': '__notebook__'}
    executed = []

    def source(index):
        return ''.join(notebook['cells'][index]['source'])

    def run(index, code=None):
        print(f'\nNotebook cell {index}', flush=True)
        exec(compile(code or source(index), f'takemeter.ipynb:cell{index}', 'exec'), ns)
        executed.append(index)

    for index in [2, 4, 6, 8, 10, 12]:
        run(index)
    if ns['problems']:
        raise ValueError(ns['problems'])
    # Import definitions from sections 4 and 5, without repeating Unit 5 or
    # overwriting its artifacts. No training/evaluation implementation is copied.
    for index in [14, 16]:
        tree = ast.parse(source(index))
        tree.body = [node for node in tree.body if isinstance(
            node, (ast.Import, ast.ImportFrom, ast.FunctionDef))]
        exec(compile(tree, f'takemeter.ipynb:cell{index}', 'exec'), ns)
    if args.max_length:
        ns['MAX_LENGTH'] = args.max_length
    if args.epochs:
        ns['EPOCHS'] = args.epochs
    settings = {key: ns[key] for key in [
        'LABELS', 'BASE_MODEL', 'EPOCHS', 'LEARNING_RATE', 'BATCH_SIZE',
        'MAX_LENGTH', 'DEVICE', 'DEVICE_NAME']}
    settings.update({
        'run_label': args.label,
        'started_at_utc': datetime.now(timezone.utc).isoformat(),
        'labels_sha256': hashlib.sha256((root / 'labels.csv').read_bytes()).hexdigest(),
        'notebook_sha256': hashlib.sha256((root / 'takemeter.ipynb').read_bytes()).hexdigest(),
        'torch_version': ns['torch'].__version__,
        'execution': 'Notebook code cells executed directly by run_experiment.py',
    })
    meta = evaluation / f'run_{args.label}.json'
    meta.write_text(json.dumps(settings, indent=2) + '\n')

    def save_seed(result, frame, trainer, tokenizer):
        seed = result['seed']
        result.update({
            'device': ns['DEVICE'], 'device_name': ns['DEVICE_NAME'],
            'torch_version': ns['torch'].__version__,
            'max_length': ns['MAX_LENGTH'],
        })
        frame.to_csv(evaluation / f'test_seed_{seed}.csv', index=False)
        tokenized = tokenizer(frame['text'].tolist(), truncation=True,
                              padding='max_length', max_length=ns['MAX_LENGTH'],
                              return_tensors='pt')
        model = trainer.model
        model.eval()
        predictions = []
        confidence = []
        torch = ns['torch']
        with torch.no_grad():
            for start in range(0, len(frame), ns['BATCH_SIZE']):
                batch = {key: val[start:start+ns['BATCH_SIZE']].to(model.device)
                         for key, val in tokenized.items()}
                probs = model(**batch).logits.softmax(-1)
                predictions.extend(probs.argmax(-1).cpu().tolist())
                confidence.extend(probs.max(-1).values.cpu().tolist())
        rows = [{'text': text, 'gold': gold, 'predicted': ns['LABELS'][pred],
                 'confidence': conf}
                for text, gold, pred, conf in zip(
                    frame.text, frame.label, predictions, confidence)]
        (evaluation / f'predictions_{args.label}_{seed}.json').write_text(
            json.dumps(rows, indent=2) + '\n')
        # A partial file survives an interrupted session; never impersonates
        # the completed three-seed artifact.
        (evaluation / f'partial_{args.label}.json').write_text(
            json.dumps(ns['all_results'] + [result], indent=2) + '\n')

    ns['save_seed'] = save_seed
    code = source(19).replace('RUN_LABEL = "before"', f'RUN_LABEL = "{args.label}"')
    code = code.replace('    all_results.append(r)',
                        '    save_seed(r, te, t, tok)\n    all_results.append(r)')
    # Release each trained model before constructing the next one, keeping
    # training settings identical while avoiding double GPU allocation.
    code = code.replace('    print(f"  accuracy',
                        '    del t, tok\n    print(f"  accuracy')
    run(19, code)
    run(21)
    run(23)
    settings['completed_at_utc'] = datetime.now(timezone.utc).isoformat()
    settings['executed_cells'] = executed
    meta.write_text(json.dumps(settings, indent=2) + '\n')


if __name__ == '__main__':
    main()
