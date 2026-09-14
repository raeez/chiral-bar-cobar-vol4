from pathlib import Path
r=Path(__file__).resolve().parents[4]/'research-candidates/vol4_prime026/native004/native-source'
p=next(r.glob('chapters/arithmetic/98_*'));s=p.read_text();start=s.index('The quantum arithmetic Chern--Simons bulk construction');end=s.index('\\section{The RH-Equivalent Obstruction}',start)
s=s[:start]+'''The complete Weil form is defined on the compact convolution algebra
$\\mathscr A$. A geometric Hilbert-space construction and a comparison
with this arithmetic form are separate data.

\\begin{theorem}[Weil positivity and an additional descent]
\\label{v4-arith:w10-final:thm:cs-descent-atp-rh}
For $\\mathscr A=C_c^\\infty(\\mathbb R)$, positivity
$W(f*f^*)\\ge0$ for every $f\\in\\mathscr A$ is equivalent to RH.
The same positivity together with a condensed-Hilbert descent therefore
implies RH. The descent is not needed for this analytic equivalence.
\\end{theorem}
\\begin{proof}
The explicit signed comparison \\eqref{v4-arith:sc:full-comparison}
identifies the complete arithmetic form, with its two polar moments.
Weil's criterion proves the equivalence. Adding a further hypothesis
preserves the implication to RH.
\\end{proof}

\\begin{remark}[continuous and arithmetic purity]
\\label{v4-arith:w10-final:rem:w10-a-shape}
Continuous scaling satisfies $|F_\\infty|=e^{-1/2}1$ without RH.
The arithmetic zero operator satisfies $|F_Z|=e^{-1/2}1$ exactly
under RH, by Theorem~\\ref{v4-arith:w9-r2:thm:purity-ATP-RH}.
A descent to the continuous carrier does not supply an intertwiner
with $F_Z$. That comparison must be specified and proved separately.
\\end{remark}

'''+s[end:]
start=s.index('\\begin{proof}',s.index('\\label{v4-arith:w10-final:prop:tier1}'));end=s.index('\\end{proof}',start)+len('\\end{proof}')
s=s[:start]+'''\\begin{proof}
The Fourier map is an algebra isomorphism from convolution on
$\\mathscr A$ to multiplication on $\\mathscr P$ and respects the
stated involutions. Thus the displayed inequality is exactly Weil's
compact-test criterion. The additional comparison inputs do not enter
that equivalence.
\\end{proof}'''+s[end:];p.write_text(s)
print('Corrected the Ch98 purity carrier and direct Weil proof.')
