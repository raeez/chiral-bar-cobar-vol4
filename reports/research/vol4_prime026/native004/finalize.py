from pathlib import Path
import re,json,hashlib,subprocess
import fitz
report=Path(__file__).resolve().parent;worktree=report.parents[3];source=worktree/'research-candidates/vol4_prime026/native004'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
freeze=json.loads((report/'source-freeze.json').read_text());assert all(sha(worktree/r['path'])==r['sha256'] for r in freeze['files'])
checks={}
for tag in ('reader','native'):
 out=report/('build-'+tag);log=(out/'main.log').read_text(encoding='latin1');pdf=fitz.open(out/'main.pdf')
 inp=json.loads((report/(tag+'-compiler-inputs.json')).read_text())
 drift=[p for p,h in inp['inputs'] if Path(p).is_file() and sha(Path(p))!=h]
 assert not drift,drift
 checks[tag]={'pages':len(pdf),'pdf_sha256':sha(out/'main.pdf'),'pdf_path':str((out/'main.pdf').relative_to(worktree)),'aux_sha256':sha(out/'main.aux'),'undefined_references_or_citations':len(re.findall(r'(?:Reference|Citation) [^\n]*(?:\n[^\n]*)?undefined',log)),'duplicate_labels':len(re.findall(r'multiply defined',log)),'overfull_hbox':len(re.findall(r'Overfull \\hbox',log)),'overfull_vbox':len(re.findall(r'Overfull \\vbox',log)),'underfull_hbox':len(re.findall(r'Underfull \\hbox',log)),'compiler_input_drift':drift,'rendered_pages':json.loads((report/('render-'+tag+'.json')).read_text())['pages']}
 assert checks[tag]['undefined_references_or_citations']==0 and checks[tag]['duplicate_labels']==0
 checks[tag]['pdf_metadata']=pdf.metadata
# New mathematical prose has no process narration. Existing native material
# is recorded separately and is not covered by this bounded check.
process=re.compile(r'\b(?:agent|reviewer|worktree|workflow|manifest|audit|checklist|TODO|codex|GPT|prompt|acceptance|repair)\b|/Users/',re.I)
new_source_hits=[]
for p in source.glob('*.tex'):
 if p.name in ('main.tex','references.tex','arithmetic-reader.tex','comparisons.tex','prime-carriers.tex','weil-pairing.tex','occupation-scattering.tex'):continue
 for n,line in enumerate(p.read_text().splitlines(),1):
  if process.search(line):new_source_hits.append({'path':str(p.relative_to(worktree)),'line':n,'text':line})
assert not new_source_hits,new_source_hits
preserved=[]
for number,expected in [('57','959caa71b54ef6d6041f98caeb8ff6193f46d4646afcc07fb293244db36a2422'),('80','a223804ab1fc543234f72a7c0eee4e35a1b51f22c72fd3d061e38238f205c058')]:
 p=next((source/'native-source/chapters/arithmetic').glob(number+'_*'));assert sha(p)==expected;preserved.append({'path':str(p.relative_to(worktree)),'sha256':expected})
base=json.loads((report/'base-manifest.json').read_text());assert all(sha(worktree/r['path'])==r['sha256'] for r in base['source_files'])
validation={'checks':checks,'source_freeze_unchanged':True,'prior_121_source_files_unchanged':True,'new_mathematical_prose_firewall_hits':new_source_hits,'private_source_hits':json.loads((report/'private-source-scan.json').read_text()),'preserved_bounded_pass':preserved,'render_assessment':'The 26 selected reader pages and 30 selected native pages were inspected through full-resolution page rasters and ordered contact sheets. New formulas and their continuations are legible, with no clipping or overlap. Existing native production-style tables and global overflows prevent a whole-book layout/firewall verdict.','mathematical_acceptance':'Fresh exact-candidate independent review remains required. The constructive derivation and self-inspection do not constitute acceptance.'}
(report/'validation.json').write_text(json.dumps(validation,indent=2)+'\n')
manifest={'task':'Vol IV native arithmetic consumer construction','status':'Constructed, frozen, built and visually inspected; fresh review pending; whole-native closure incomplete','base_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=worktree,text=True).strip(),'branch':subprocess.check_output(['git','branch','--show-current'],cwd=worktree,text=True).strip(),'source_root':str(source.relative_to(worktree)),'source_aggregate_sha256':freeze['source_aggregate_sha256'],'source_freeze_sha256':sha(report/'source-freeze.json'),'source_files':freeze['files'],'changed_paths':freeze['changed_paths'],'native_patch_sha256':sha(report/'native.patch'),'validation_sha256':sha(report/'validation.json'),'checks':checks,'whole_native_closed':False,'remaining_consumers':['Ch71','Ch72','Ch75','Ch76','Ch77','Ch78','Ch89','Ch94'],'remaining_constructions':['Arithmetic-primary comparison to the actual signed test form','Positive comparison on any separately claimed modular restricted carrier','Whole-native proof, carrier, firewall, and render review'],'runtime_requirement':'gpt-6-astra / ultra','observed_runtime_metadata':'unavailable; unverified; no observed mismatch','integration_authority':'Root only; no staging, commit, push, central PDF write, or application opening.'}
(report/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'manifest_sha256':sha(report/'manifest.json'),'source_freeze_sha256':sha(report/'source-freeze.json'),'aggregate':freeze['source_aggregate_sha256'],'native_patch_sha256':manifest['native_patch_sha256'],'checks':checks},indent=2))
