"""Freeze exact source, compiler inputs, evidence, renders and the book PDF."""
from pathlib import Path
from datetime import datetime, timezone
import difflib
import hashlib
import json
import re
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
FREEZE = HERE / 'candidate-003'
BASE = '10157885d7d9df587df8bf43804acabcbb7ad850'
SOURCES = [
    'chapters/arithmetic/05_connes_soibelman_bost_connes.tex',
    'chapters/arithmetic/15_kontsevich_soibelman_formality.tex',
    'chapters/arithmetic/15a_integral_centre_formality.tex',
    'chapters/arithmetic/15b_coha_euler_comparison.tex',
    'appendices/arithmetic/A_primary_source_catalog.tex',
    'appendices/arithmetic/B_source_families_index.tex',
]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
old = HERE.parent / 'candidate-001'
assert sha(old / 'manifest.json') == '4834e1085a080bafd862fa82444c92993595f50fe619599547d30e85b1684112'
old_manifest = json.loads((old / 'manifest.json').read_text())
for row in old_manifest['source_files']:
    assert sha(Path(row['frozen_path'])) == row['sha256']
assert sha(old / 'arithmetic-centres-vol4.pdf') == 'dc9987a1e45b84fb4b8f26d9a642d90e18e31ee5bac5c342e71fe1fc7e9c7088'
assert sha(Path(old_manifest['source_patch'])) == old_manifest['aggregate_source_diff_sha256']
assert sha(Path(old_manifest['build_input_manifest'])) == old_manifest['build_input_manifest_sha256']
for row in old_manifest['evidence']:
    assert sha(Path(row['path'])) == row['sha256']

assert sha(ROOT / SOURCES[2]) == '9c57bf1d83209384e78acac350f17d36935610272087cba27de066c0bd7d3189'
prior002 = HERE.parent / 'coha-euler-002' / 'candidate-002'
assert sha(prior002 / 'manifest.json') == '0d70738d8408567b24f528f616a88eee179d41893a50c8a7df0df003979d0667'
prior002_manifest = json.loads((prior002 / 'manifest.json').read_text())
for row in prior002_manifest['source_files'] + prior002_manifest['renders'] + prior002_manifest['evidence']:
    assert sha(Path(row['frozen_path'])) == row['sha256']
assert sha(Path(prior002_manifest['pdf']['path'])) == prior002_manifest['pdf']['sha256']
for key in ('phase002_patch', 'full_source_patch', 'full_source_inputs', 'compiler_inputs'):
    assert sha(Path(prior002_manifest[key]['path'])) == prior002_manifest[key]['sha256']

assert subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip() == BASE
subprocess.run(['git', 'diff', '--check'], cwd=ROOT, check=True)
PASS = sys.argv[1]
build = HERE / 'book-build'
logfile = build / ('pass-' + PASS + '.stdout')
log = logfile.read_text(errors='replace')
assert 'Output written on' in log and 'Fatal error' not in log
assert 'undefined' not in log and 'Rerun' not in log
render_manifest = json.loads((HERE / 'final-render-manifest.json').read_text())
assert render_manifest['pdf_sha256'] == sha(build / 'main.pdf')
FREEZE.mkdir(exist_ok=False)
files = []
phase_patch = []
for name in SOURCES:
    p = ROOT / name
    q = FREEZE / 'source' / name
    q.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(p, q)
    previous = HERE / 'pre-edit' / name
    pre = previous.read_text() if previous.exists() else ''
    if pre != p.read_text():
        phase_patch.extend(difflib.unified_diff(pre.splitlines(keepends=True),
                          p.read_text().splitlines(keepends=True),
                          fromfile='a/' + name if previous.exists() else '/dev/null',
                          tofile='b/' + name))
    files.append({'path': name, 'sha256': sha(p), 'frozen_path': str(q),
                  'pre_edit_sha256': sha(previous) if previous.exists() else None,
                  'changed_in_phase003': pre != p.read_text()})
(FREEZE / 'phase003.patch').write_text(''.join(phase_patch))
patch = subprocess.check_output(['git', 'diff', '--binary', '--'] + SOURCES, cwd=ROOT)
for name in SOURCES:
    tracked = subprocess.run(['git', 'ls-files', '--error-unmatch', name],
                             cwd=ROOT, capture_output=True)
    if tracked.returncode:
        addition = subprocess.run(['git', 'diff', '--no-index', '--binary', '--',
                                  '/dev/null', name], cwd=ROOT, capture_output=True)
        assert addition.returncode == 1
        patch += addition.stdout
(FREEZE / 'full-source.patch').write_bytes(patch)

# All repository TeX/bibliography/style sources, including owned new inputs.
tracked = subprocess.check_output(['git', 'ls-files', '-z'], cwd=ROOT).decode().split('\0')
source_inputs = []
for name in sorted(set(tracked + SOURCES)):
    p = ROOT / name
    if p.is_file() and p.suffix in ('.tex', '.sty', '.bib'):
        source_inputs.append({'path': name, 'resolved_path': str(p.resolve()), 'sha256': sha(p)})
(FREEZE / 'full-source-inputs.json').write_text(json.dumps(source_inputs, indent=2) + '\n')

# Recorder inputs include the actual template, packages, fonts, format and aux state.
compiler_inputs = []
seen = set()
for line in (build / 'main.fls').read_text(errors='replace').splitlines():
    if not line.startswith('INPUT '):
        continue
    p = Path(line[6:])
    p = (ROOT / p).resolve() if not p.is_absolute() else p.resolve()
    if str(p) in seen:
        continue
    seen.add(str(p))
    row = {'path': str(p), 'exists': p.is_file()}
    if p.is_file():
        row['sha256'] = sha(p)
        if build in p.parents:
            row['role'] = 'generated bibliography/reference state'
            q = FREEZE / 'build-state' / p.name
            q.parent.mkdir(exist_ok=True)
            shutil.copyfile(p, q)
            row['frozen_path'] = str(q)
        else:
            row['role'] = 'source or compiler resource'
    compiler_inputs.append(row)
assert all(row['exists'] for row in compiler_inputs)
(FREEZE / 'compiler-inputs.json').write_text(json.dumps(compiler_inputs, indent=2) + '\n')

pdf = FREEZE / 'arithmetic-euler-coha-vol4.pdf'
shutil.copyfile(build / 'main.pdf', pdf)
for name in ('main.fls', 'main.log', 'main.aux', 'main.toc', 'main.out'):
    if (build / name).exists():
        q = FREEZE / 'build-state' / name
        q.parent.mkdir(exist_ok=True)
        shutil.copyfile(build / name, q)
shutil.copyfile(logfile, FREEZE / 'build.stdout')
info = subprocess.check_output(['pdfinfo', str(pdf)], text=True)
(FREEZE / 'pdfinfo.txt').write_text(info)
renders = []
for row in render_manifest['pages']:
    p = Path(row['path'])
    assert sha(p) == row['sha256']
    q = FREEZE / 'render' / p.name
    q.parent.mkdir(exist_ok=True)
    shutil.copyfile(p, q)
    renders.append(dict(row, frozen_path=str(q)))
evidence = []
for name in ('README.md', 'mining-dispositions.json', 'protected-identities.json',
             'build_vol4.py', 'freeze_candidate.py', 'source-firewall.json',
             'render-review.json', 'final-render-manifest.json'):
    p = HERE / name
    q = FREEZE / 'evidence' / name
    q.parent.mkdir(exist_ok=True)
    shutil.copyfile(p, q)
    evidence.append({'path': str(p), 'sha256': sha(p), 'frozen_path': str(q)})
manifest = {
    'candidate_id': 'vol4-euler-coha-003',
    'status': 'unaccepted frozen candidate for independent review',
    'created_utc': datetime.now(timezone.utc).isoformat(),
    'worktree': str(ROOT), 'base_head': BASE,
    'branch': subprocess.check_output(['git', 'branch', '--show-current'], cwd=ROOT, text=True).strip(),
    'protected_candidate001_manifest_sha256': sha(old / 'manifest.json'),
    'protected_candidate002': {'manifest': str(prior002 / 'manifest.json'), 'manifest_sha256': sha(prior002 / 'manifest.json'), 'pdf_sha256': prior002_manifest['pdf']['sha256']},
    'protected_integral_centre_source_sha256': sha(ROOT / SOURCES[2]),
    'source_files': files,
    'phase003_patch': {'path': str(FREEZE / 'phase003.patch'), 'sha256': sha(FREEZE / 'phase003.patch')},
    'full_source_patch': {'path': str(FREEZE / 'full-source.patch'), 'sha256': sha(FREEZE / 'full-source.patch')},
    'full_source_inputs': {'path': str(FREEZE / 'full-source-inputs.json'), 'sha256': sha(FREEZE / 'full-source-inputs.json'), 'count': len(source_inputs)},
    'compiler_inputs': {'path': str(FREEZE / 'compiler-inputs.json'), 'sha256': sha(FREEZE / 'compiler-inputs.json'), 'count': len(compiler_inputs)},
    'pdf': {'path': str(pdf), 'sha256': sha(pdf), 'pages': int(re.search(r'Pages:\s+(\d+)', info).group(1))},
    'build': {'command': 'python3 reports/research/MINING-2026-09-13/coha-euler-003/build_vol4.py ' + PASS,
              'pdflatex_version': subprocess.check_output(['pdflatex', '--version'], text=True).splitlines()[0],
              'log': str(FREEZE / 'build.stdout'), 'log_sha256': sha(FREEZE / 'build.stdout'),
              'undefined_references': 0, 'rerun_required': False, 'whole_book_overfull_boxes': log.count('Overfull'),
              'changed_regions_overfull_boxes': 0},
    'renders': renders, 'evidence': evidence,
    'scope': 'Two statement repairs to candidate002: exclude only nonempty edgeless prime quivers and treat the empty case explicitly; require both supercommutation and evenness for the ordinary polynomial PBW conclusion. The immediate final scope sentence is repaired. All other manuscript sources and accepted15a are unchanged. Candidate002 mathematics and primary evidence are inherited with their exact frozen hashes. The arithmetic Hochschild-trace-to-BPS realization remains open; no whole-book acceptance.',
    'publication': 'None. No staging, commit, push, or accepted PDF replacement.'
}
(FREEZE / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
print(json.dumps({'manifest': str(FREEZE / 'manifest.json'), 'manifest_sha256': sha(FREEZE / 'manifest.json'),
                  'pdf': manifest['pdf'], 'phase_patch_sha256': manifest['phase003_patch']['sha256']}, indent=2))
