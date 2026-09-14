from pathlib import Path
import re,json,hashlib,difflib
report=Path(__file__).resolve().parent;worktree=report.parents[3];root=worktree/'research-candidates/vol4_prime026/native004';old=root.parent
native=root/'native-source';rows=[];changed=[];patch=[]
for p in sorted(root.rglob('*')):
 if not p.is_file():continue
 rel=p.relative_to(root);row={'path':str(p.relative_to(worktree)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size};rows.append(row)
 oldp=old/rel
 if not oldp.exists() or oldp.read_bytes()!=p.read_bytes():
  changed.append(str(rel))
  if str(rel).startswith('native-source/') and p.suffix in ('.tex','.sty'):
   oldtxt=oldp.read_text().splitlines(keepends=True) if oldp.exists() else []
   patch.extend(difflib.unified_diff(oldtxt,p.read_text().splitlines(keepends=True),fromfile='a/'+str(rel.relative_to('native-source')),tofile='b/'+str(rel.relative_to('native-source'))))
aggregate=hashlib.sha256(''.join(x['sha256']+'  '+x['path']+'\n' for x in rows).encode()).hexdigest()
(report/'source-freeze.json').write_text(json.dumps({'aggregate_method':'SHA-256 of sorted source rows encoded as sha256 + two spaces + worktree-relative path + newline','source_aggregate_sha256':aggregate,'files':rows,'changed_paths':changed},indent=2)+'\n')
(report/'native.patch').write_text(''.join(patch))
# Every unchanged consumer reference to a changed file label remains visible.
consumers=[]
changednative=[native/Path(x).relative_to('native-source') for x in changed if x.startswith('native-source/') and x.endswith('.tex')]
for p in changednative:
 labels=set(re.findall(r'\\label\{([^}]+)\}',p.read_text()))
 for q in native.rglob('*.tex'):
  if q in changednative:continue
  for n,line in enumerate(q.read_text().splitlines(),1):
   matched=sorted(l for l in labels if l in line)
   if matched:consumers.append({'changed_source':str(p.relative_to(root)),'consumer':str(q.relative_to(root)),'line':n,'labels':matched,'text':line})
(report/'unchanged-consumer-references.json').write_text(json.dumps(consumers,indent=2)+'\n')
res=[]
patterns={
 '71':r'W_.*infty|St4|0\.850662',
 '72':r'W_.*infty|B\[f\].*A\[f\]',
 '75':r'W_.*infty|thm:IE-ATP',
 '76':r'W_.*infty|g-definition',
 '77':r'kernel|constant|Hadamard',
 '78':r'W_.*infty|integral-rep|self-adjoint Weil',
 '89':r'w9-r2:|separate compatible',
 '94':r'w9-r2:thm:purity|F_.*weight|F_.*WS|w9-r2:thm:WS',
}
for number,pat in patterns.items():
 p=next(native.glob('chapters/arithmetic/'+number+'_*'))
 for n,line in enumerate(p.read_text().splitlines(),1):
  if re.search(pat,line):res.append({'path':str(p.relative_to(root)),'line':n,'text':line})
(report/'residual-consumer-anchors.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps({'source_files':len(rows),'aggregate':aggregate,'changed_paths':changed,'consumer_reference_rows':len(consumers),'residual_anchor_rows':len(res)},indent=2))
