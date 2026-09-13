from pathlib import Path
import os, subprocess, sys
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
OUT=HERE/'book-build'
OUT.mkdir(exist_ok=True)
ENV=os.environ.copy()
ENV['TEXINPUTS']=str(ROOT)+':/Users/raeez/latex-template//:'+ENV.get('TEXINPUTS','')
PASS=sys.argv[1] if len(sys.argv)>1 else '1'
LOG=OUT/('pass-'+PASS+'.stdout')
COMMAND=['pdflatex','-recorder','-interaction=nonstopmode','-halt-on-error','-output-directory='+str(OUT),str(ROOT/'main.tex')]
with LOG.open('w') as stream:
    result=subprocess.run(COMMAND,cwd=ROOT,env=ENV,stdout=stream,stderr=subprocess.STDOUT)
print({'command':COMMAND,'returncode':result.returncode,'log':str(LOG)})
print('\n'.join(LOG.read_text(errors='replace').splitlines()[-20:]))
sys.exit(result.returncode)
