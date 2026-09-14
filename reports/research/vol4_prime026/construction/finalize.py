from pathlib import Path
import hashlib
import json
import re
import subprocess
import tarfile

report = Path(__file__).resolve().parent
worktree = report.parents[3]
source = worktree / 'research-candidates/vol4_prime026'
freeze = json.loads((report / 'source-freeze.json').read_text())
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
for row in freeze['files']:
    assert sha(worktree / row['path']) == row['sha256'], row['path']
old = report.parent / 'inputs/candidate024'
unchanged = []
for p in old.rglob('*'):
    if p.is_file():
        relative = p.relative_to(old)
        if str(relative) in ['main.tex', 'native-source/chapters/arithmetic/57_hp_li_positivity_closure.tex',
                             'native-source/chapters/arithmetic/80_ATP_adelic_scattering.tex']:
            continue
        assert sha(p) == sha(source / relative), relative
        unchanged.append(str(relative))
for a, b in [('weil-pairing.tex', '57_hp_li_positivity_closure.tex'),
             ('occupation-scattering.tex', '80_ATP_adelic_scattering.tex')]:
    assert (source / a).read_bytes() == (source / 'native-source/chapters/arithmetic' / b).read_bytes()
forbidden = re.compile(r'\b(?:agent|reviewer|worktree|workflow|manifest|audit|checklist|TODO|codex|GPT|prompt|acceptance)\b|/Users/', re.I)
checks = {}
for tag in ['reader', 'native']:
    build = report / ('build-' + tag)
    text = (build / 'main.txt').read_text()
    pages = text.split('\f')[:-1]
    log = (build / 'main.log').read_text(errors='replace')
    records = json.loads((report / ('build-' + tag + '.json')).read_text())
    assert records[-1]['returncode'] == 0
    assert records[-1]['hashes'] == records[-2]['hashes']
    assert records[-1]['hashes']['pdf'] == sha(build / 'main.pdf')
    undefined = re.findall(r'.*(?:Reference|Citation).*undefined.*', log)
    assert not undefined and 'multiply defined' not in log
    selected = list(range(31, 42)) if tag == 'reader' else list(range(595, 601)) + list(range(819, 824))
    hits = [{'page': number, 'match': m.group()} for number in selected
            for m in forbidden.finditer(pages[number-1])]
    assert not hits
    checks[tag] = {'pages': len(pages), 'pdf_sha256': sha(build / 'main.pdf'),
                   'aux_sha256': sha(build / 'main.aux'), 'undefined': undefined,
                   'duplicate_labels': 0, 'overfull_hbox': log.count('Overfull \\hbox'),
                   'overfull_vbox': log.count('Overfull \\vbox'),
                   'underfull_hbox': log.count('Underfull \\hbox'),
                   'selected_pages': selected, 'selected_text_firewall_hits': hits}
    if tag == 'reader':
        assert checks[tag]['overfull_hbox'] == checks[tag]['overfull_vbox'] == 0
    inputs = {}
    cwd = source if tag == 'reader' else source / 'native-source'
    for line in (build / 'main.fls').read_text(errors='replace').splitlines():
        if line.startswith('INPUT '):
            p = Path(line[6:]); p = p if p.is_absolute() else cwd / p; p = p.resolve()
            if p.is_file():
                inputs[str(p)] = {'path': str(p), 'sha256': sha(p), 'bytes': p.stat().st_size,
                                  'generated': p.parent == build}
    (report / (tag + '-compiler-inputs.json')).write_text(json.dumps(list(inputs.values()), indent=2)+'\n')
(report / 'build-checks.json').write_text(json.dumps(checks, indent=2)+'\n')
(report / 'preservation-check.json').write_text(json.dumps({'unchanged_predecessor_files': unchanged,
    'reader_native_copies_exact': True}, indent=2)+'\n')

archive = report / 'source-closure.tar'
with tarfile.open(archive, 'w') as tar:
    for p in sorted(source.rglob('*')):
        if p.is_file():
            info = tar.gettarinfo(str(p), arcname=str(p.relative_to(source)))
            info.uid = info.gid = 0; info.uname = info.gname = ''; info.mtime = 1789344000
            with p.open('rb') as stream:
                tar.addfile(info, stream)
artifacts = ['README.md', 'source-freeze.json', 'native.patch', 'preserved-chapters.json',
             'label-map.json', 'build.py', 'build-reader.json', 'build-native.json', 'build-checks.json',
             'reader-compiler-inputs.json', 'native-compiler-inputs.json', 'checks.py',
             'calculation-results.json', 'primary/source.json', 'primary/suzuki-weil.pdf',
             'preservation-check.json', 'source-closure.tar', 'render-review.json',
             'consumer-propagation.json', 'raster-comparison.json',
             'raster-comparison-latest.json', 'finalize.py']
manifest = {'task': 'vol4_prime026 native Weil and occupation-scattering construction',
            'status': 'Constructed; independent mathematical acceptance pending',
            'base_commit': freeze['base_head'], 'branch': subprocess.check_output(['git', 'branch', '--show-current'], cwd=worktree, text=True).strip(),
            'source_aggregate_sha256': freeze['source_aggregate_sha256'],
            'source_files': freeze['files'], 'native_patch_sha256': sha(report / 'native.patch'),
            'checks': checks, 'evidence': [{'path': name, 'sha256': sha(report / name)} for name in artifacts],
            'residuals': ['Fresh independent exact review', 'Native arithmetic pairing and trace comparison',
                          'Unchanged Chapter56 determinant normalization', 'Downstream Chapters60,61,62,69,74,79 and further consumers'],
            'observed_controls': 'unverified', 'integration_authority': 'root only'}
(report / 'manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
print(json.dumps({'manifest_sha256': sha(report / 'manifest.json'), 'source_aggregate_sha256': freeze['source_aggregate_sha256'],
                  'native_patch_sha256': sha(report / 'native.patch'), 'checks': checks}, indent=2))
