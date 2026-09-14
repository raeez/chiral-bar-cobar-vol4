from pathlib import Path
import json,sys
import fitz
from PIL import Image,ImageOps,ImageDraw
report=Path(__file__).resolve().parent
tag=sys.argv[1];doc=fitz.open(report/('build-'+tag)/'main.pdf')
out=report/('render-'+tag);out.mkdir(exist_ok=True)
if tag=='reader':pages=list(range(36,62))
else:
 pages=[588,589,598,599,600,639,640,641,743,744,745,747,748,749,789,790,791,864,927,928,929,1005,1006]
 # Ch60 corrected consumers include the table, diagram, and compact criterion.
 needles=['finite-prime restricted pairing','signed arithmetic comparison.','the complete weil form has the signed','signed weil pairing','finite-prime form has a signed translation','isometry is an actual restricted comparison','determines the exact gaussian']
 for i,page in enumerate(doc):
  text=' '.join(page.get_text().lower().split())
  if any(x in text for x in needles):pages.append(i+1)
 pages=sorted(set(pages))
for n in pages:
 pix=doc[n-1].get_pixmap(matrix=fitz.Matrix(1.25,1.25),alpha=False);pix.save(out/f'page-{n:04}.png')
# Small contact sheets aid page-order inspection; full rasters remain available.
for i in range(0,len(pages),4):
 ps=pages[i:i+4];canvas=Image.new('RGB',(1400,1900),'#d5d5d5');draw=ImageDraw.Draw(canvas)
 for j,n in enumerate(ps):
  im=Image.open(out/f'page-{n:04}.png');im.thumbnail((690,900))
  x=(j%2)*700+(700-im.width)//2;y=(j//2)*950+35
  canvas.paste(im,(x,y));draw.text(((j%2)*700+20,(j//2)*950+10),f'{tag} physical page {n}',fill='black')
 canvas.save(out/f'contact-{i//4+1:02}.png')
(report/('render-'+tag+'.json')).write_text(json.dumps({'pages':pages,'page_count':len(doc)},indent=2)+'\n')
print(tag,'pages',pages)
