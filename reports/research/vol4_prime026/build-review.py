from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys

report = Path(__file__).resolve().parent
tag = sys.argv[1]
root = report / 'inputs' / 'candidate024'
source = root if tag == 'reader' else root / 'native-source'
output = report / ('build-' + tag)
output.mkdir(exist_ok=True)
environment = os.environ.copy()
template = root / 'standalone' if tag == 'reader' else report / 'inputs' / 'native-template'
environment['TEXINPUTS'] = str(template) + ':' + str(source) + ':'
environment['SOURCE_DATE_EPOCH'] = '1789344000'
environment['FORCE_SOURCE_DATE'] = '1'
records = []
for number in range(1, 6):
    command = ['pdflatex', '-no-shell-escape', '-recorder', '-interaction=nonstopmode',
               '-halt-on-error', '-output-directory=' + str(output), str(source / 'main.tex')]
    with (output / ('pass-' + str(number) + '.stdout')).open('w') as stream:
        result = subprocess.run(command, cwd=source, env=environment, stdout=stream, stderr=subprocess.STDOUT)
    hashes = {suffix: hashlib.sha256((output / ('main.' + suffix)).read_bytes()).hexdigest()
              for suffix in ['pdf', 'aux'] if (output / ('main.' + suffix)).exists()}
    records.append({'command': command, 'cwd': str(source), 'pass': number,
                    'environment': {key: environment[key] for key in ['TEXINPUTS', 'SOURCE_DATE_EPOCH', 'FORCE_SOURCE_DATE']},
                    'returncode': result.returncode, 'hashes': hashes})
    (report / ('build-' + tag + '.json')).write_text(json.dumps(records, indent=2) + '\n')
    print(tag, number, result.returncode, hashes, flush=True)
    if result.returncode:
        raise SystemExit(result.returncode)
    if len(records) > 1 and records[-2]['hashes'] == hashes:
        break
else:
    raise RuntimeError('PDF and AUX did not converge')
subprocess.run(['pdftotext', '-layout', str(output / 'main.pdf'), str(output / 'main.txt')], check=True)
