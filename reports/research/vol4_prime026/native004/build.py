from pathlib import Path
import hashlib,json,os,subprocess,sys
report=Path(__file__).resolve().parent
worktree=report.parents[3]
root=worktree/'research-candidates/vol4_prime026/native004'
tag=sys.argv[1]
assert tag in ('reader','native')
source=root if tag=='reader' else root/'native-source'
output=report/('build-'+tag);output.mkdir(exist_ok=True)
template=root/'standalone' if tag=='reader' else report/'native-template'
env=os.environ.copy();env['TEXINPUTS']=str(template)+':'+str(source)+':'
env['SOURCE_DATE_EPOCH']='1789430400';env['FORCE_SOURCE_DATE']='1'
records=[]
for number in range(1,7):
 cmd=['pdflatex','-no-shell-escape','-recorder','-interaction=nonstopmode','-halt-on-error','-output-directory='+str(output),str(source/'main.tex')]
 with (output/('pass-'+str(number)+'.stdout')).open('w') as stream:
  result=subprocess.run(cmd,cwd=source,env=env,stdout=stream,stderr=subprocess.STDOUT)
 hashes={ext:hashlib.sha256((output/('main.'+ext)).read_bytes()).hexdigest() for ext in ('pdf','aux') if (output/('main.'+ext)).exists()}
 records.append(dict(command=cmd,cwd=str(source),pass_number=number,returncode=result.returncode,hashes=hashes,environment={x:env[x] for x in ('TEXINPUTS','SOURCE_DATE_EPOCH','FORCE_SOURCE_DATE')}))
 (report/('build-'+tag+'.json')).write_text(json.dumps(records,indent=2)+'\n')
 print(tag,number,result.returncode,hashes,flush=True)
 if result.returncode:raise SystemExit(result.returncode)
 if len(records)>1 and records[-2]['hashes']==hashes:break
else:raise RuntimeError('PDF and AUX did not converge')
subprocess.run(['pdftotext','-layout',str(output/'main.pdf'),str(output/'main.txt')],check=True)
inputs=[];outputs=[]
for line in (output/'main.fls').read_text().splitlines():
 if line.startswith('OUTPUT '):
  p=Path(line[7:]);p=p if p.is_absolute() else source/p
  if not p.resolve().is_relative_to(report):raise RuntimeError('Compiler output outside owned report: '+str(p))
  outputs.append(str(p.resolve()))
 if line.startswith('INPUT '):
  p=Path(line[6:]);p=p if p.is_absolute() else source/p
  if p.exists() and p.is_file():inputs.append((str(p.resolve()),hashlib.sha256(p.read_bytes()).hexdigest()))
(report/(tag+'-compiler-inputs.json')).write_text(json.dumps(dict(inputs=sorted(set(inputs)),outputs=sorted(set(outputs))),indent=2)+'\n')
