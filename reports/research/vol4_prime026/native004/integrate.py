from pathlib import Path
r=Path(__file__).resolve().parents[4]/'research-candidates/vol4_prime026/native004'
a=r/'native-source/chapters/arithmetic'
p=next(a.glob('56_*'));s=p.read_text();start=s.index('Assuming the twist of',s.index('\\section{Determinant Identity'));end=s.index('\\begin{remark}[comparison with Berry--Keating]',start)
d=(r/'determinant-normalization.tex').read_text().replace('\\section{The normalized genus-one determinant}','\\subsection{The normalized genus-one determinant}')
d=d.replace('\\label{v4-arith:sc:normalized-det}','\\label{v4-arith:sc:normalized-det}\n\\label{v4-arith:w5-b:prop:det-formal}')
d=d.replace('\\label{v4-arith:sc:normalized-det-formula}','\\label{v4-arith:sc:normalized-det-formula}\n\\label{v4-arith:w5-b:eq:det-identity}')
d+='''
\\begin{remark}[operator comparison and determinant normalization]
\\label{v4-arith:w5-b:rem:det-does-not-buy}
For a normal operator with a complete orthonormal eigenbasis indexed
by the same zeros, use the prescription
$\\det_{\\infty}(s-\\Theta)=\\tfrac12e^{Bs}\\det_2(1-s\\Theta^{-1})$.
The unitary eigenbasis map proves equality with $\\Delta_Z$.
This fixes the determinant notation in the determinant-trace
hypothesis. The construction of such an operator from an arithmetic
primary sector requires an additional domain-preserving comparison.
The diagonal operator $\\Theta_Z$ itself uses the zero divisor as input.
\\end{remark}

'''
p.write_text(s[:start]+d+s[end:])
(a/'signed_arithmetic_comparison.tex').write_text((r/'signed-comparison.tex').read_text())
p=r/'native-source/main.tex';s=p.read_text();line='\\input{chapters/arithmetic/57_hp_li_positivity_closure}'
assert s.count(line)==1;p.write_text(s.replace(line,line+'\n\\input{chapters/arithmetic/signed_arithmetic_comparison}'))
p=r/'main.tex';s=p.read_text();s=s.replace('\\input{weil-pairing}','\\input{weil-pairing}\n\\input{signed-comparison}\n\\input{determinant-normalization}');p.write_text(s)
p=next(a.glob('60_*'));s=p.read_text();start=s.index('\\Cref{v4-arith:w5-a:thm:RS-integral}',s.index('\\label{v4-arith:w5-synth:ch57}'));end=s.index('\\subsection{Chapter 58:',start)
s=s[:start]+'''For an actual cusp form, \\Cref{v4-arith:w5-a:thm:RS-integral}
computes the Rankin--Selberg integral from its own Fourier coefficients.
The finite-prime form on $\\mathscr A=C_c^\\infty(\\mathbb R)$ has the
signed translation representation \\eqref{v4-arith:sc:prime-comparison}.
On the two-dimensional space $V_b$, \\Cref{v4-arith:sc:two-signs}
constructs explicit positive and negative lines. Its positive-line
isometry is an actual restricted comparison. The negative line excludes
an extension as a positive Hilbert norm on the full test algebra.
For the complete arithmetic form, \\eqref{v4-arith:sc:full-comparison}
gives a signed zero-evaluation representation, with the finite-prime,
polar, and gamma terms unchanged. Positivity on all tests is equivalent
to RH by \\Cref{v4-arith:sc:positivity-boundary}.
The Rankin--Selberg norm supplies no equality with these prime weights.

'''+s[end:];p.write_text(s)
p=next(a.glob('87_*'));s=p.read_text();old='''\\item \\(\\mathcal{H}_{\\xi}^{\\mathrm{adele}}=L^{2}(X_{\\mathbb{Q}})\\) the
adele-class space with non-commutative-geometric \\(L^{2}\\)-structure
via \\(C^{*}(\\mathbb{A}/\\mathbb{Q}^{\\times})\\)
(\\Cref{v4-arith:w7-j:def:connes-ac-space});'''
new='''\\item $K_Z=\\ell^2(Z)$ with the signed form $\\langle u,Jv\\rangle$
and test map $E$ of \\Cref{v4-arith:sc:zero-representation}.
This is a constructed zero-evaluation carrier. It has no specified
identification with an adele-class quotient. Such an identification
requires a separate measure or representation and a domain-preserving
map, as in \\Cref{v4-arith:w7-j:def:connes-ac-space};'''
assert old in s;s=s.replace(old,new);p.write_text(s)
p=next(a.glob('98_*'));s=p.read_text();start=s.index('W(f \\ast \\widetilde{f})');end=s.index('It is\ndenoted A-TP throughout.',start)+len('It is\ndenoted A-TP throughout.')
s=s[:start]+'''W(f*f^*)\\ge0\\qquad(f\\in\\mathscr A=C_c^\\infty(\\mathbb R)).
\\end{equation}
Here $f^*(t)=\\overline{f(-t)}$ and multiplication in $\\mathscr A$
is additive convolution. Equivalently, on
$\\mathscr P=\\mathcal F_+\\mathscr A$, the inequality is
$\\mathcal W(hh^\\sharp)\\ge0$, where
$\\mathcal W(h)=W(\\mathcal F_+^{-1}h)$ and
$h^\\sharp(z)=\\overline{h(\\bar z)}$.
Fubini gives $\\mathcal F_+(f*f^*)=h h^\\sharp$, so this is an
exact change of test algebra. The functional includes its two polar
moments, the signed gamma density, and the weights
$\\Lambda(n)/\\sqrt n$. \\Cref{v4-arith:sc:full-comparison} constructs
its signed pairing. Weil's criterion makes positivity for every test
equivalent to RH. It is denoted A-TP throughout.'''+s[end:];p.write_text(s)
print('Integrated determinant, signed comparison, and first consumer corrections.')
