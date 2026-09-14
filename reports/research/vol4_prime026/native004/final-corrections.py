from pathlib import Path
r=Path(__file__).resolve().parents[4]/'research-candidates/vol4_prime026/native004';a=r/'native-source/chapters/arithmetic'
p=r/'archimedean-kernel.tex';s=p.read_text();s=s.replace('They satisfy the auxiliary high-frequency condition for large $v$.','''They satisfy the auxiliary high-frequency condition for large $v$.
For $u_0\\in(t_*,u_*)$, the functions
$g_L(t)=L^{-1}b(t/L)e^{-iu_0t}$ have both
$Q_g(g_L)>0$ and $W_\\infty(g_L*g_L^*)>0$ for large $L$.''');s=s.replace('condition as stated.\n\\end{proof}','''condition as stated. Finally,
$h_{g_L}(u)=h_b(L(u-u_0))$. The same dominated convergence gives
$LQ_g(g_L)\\to g(u_0)\\|b\\|_2^2>0$ and
$LW_\\infty(g_L*g_L^*)\\to k(u_0)\\|b\\|_2^2>0$.
\\end{proof}''');p.write_text(s);next(a.glob('61_*')).write_text(s)
p=r/'debranges-comparison.tex';s=p.read_text().replace('\\label{v4-arith:w7-c:chapter}','\\label{v4-arith:w7-c:chapter}\n\n\\section{The model space}')
s=s.replace('\\Cref{v4-arith:sc:two-signs}', 'Proposition~\\ref{v4-arith:sc:two-signs}');p.write_text(s);next(a.glob('73_*')).write_text(s)
p=next(a.glob('60_*'));s=p.read_text().replace(r'\mathrm{PW}(\mathbb{R})',r'\mathscr A').replace(r'\widetilde{f}',r'f^*')
s=s.replace('\\label{v4-arith:w5-synth:chapter}','\\label{v4-arith:w5-synth:chapter}\n\nHere $\\mathscr A=C_c^\\infty(\\mathbb R)$, $f^*(t)=\\overline{f(-t)}$,\nand $\\widehat f(z)=\\int f(t)e^{izt}dt$.')
p.write_text(s)
print('Corrected auxiliary positive example, de Branges headings, and Ch60 compact carrier.')
