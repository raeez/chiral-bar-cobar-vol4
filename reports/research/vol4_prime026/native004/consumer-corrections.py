from pathlib import Path
r=Path(__file__).resolve().parents[4]/'research-candidates/vol4_prime026/native004'
a=r/'native-source/chapters/arithmetic'
p=next(a.glob('60_*'));s=p.read_text()
pairs=[
('''domain; HP--Li positivity is reduced on the holomorphic cuspidal
restricted Paley--Wiener class up to the archimedean correction.''','''domain. The finite-prime form has a signed translation representation,
and the full Weil form has the signed zero-evaluation representation
of \\Cref{v4-arith:sc:full-comparison}.'''),
('''\\Cref{v4-arith:w7-d:thm:gauss-ATP} (\\ClaimStatusProvedHere) closes
Gaussian convolution positivity with equality.''','''\\Cref{v4-arith:w7-d:thm:gauss-ATP} determines the exact Gaussian
sign range of the gamma form. The complete Weil value retains the
polar and finite-prime terms.'''),
('''HP--Li restricted class & Conditional & Ch.~57 closes via
Rankin--Selberg isometry \\(\\Upsilon_{F}\\) &
\\textbf{Theorem (unconditional)} &; \\\\''','''Finite-prime restricted pairing & Signed & Explicit positive and
negative lines in $V_b$ & \\textbf{Theorem} &
\\Cref{v4-arith:sc:two-signs} \\\\'''),
('''\\item \\textbf{HPLi (HP--Li positivity).} Closed on the holomorphic
cuspidal restricted class \\(\\mathrm{PW}^{\\mathrm{hol}}_{F}\\) up to
the archimedean correction
(\\Cref{v4-arith:w5-a:thm:hpli-form}). Full HP--Li positivity is''','''\\item \\textbf{HPLi (HP--Li positivity).} The full compact-test form
has the signed representation \\eqref{v4-arith:sc:full-comparison}.
The positive line in \\Cref{v4-arith:sc:two-signs} realizes only the
finite-prime restriction. Full HP--Li positivity is'''),
('''{HP--Li restricted \\\\ \\textbf{Theorem} \\\\ {\\footnotesize Ch.~57}}''','''{Signed Weil pairing \\\\ \\textbf{Theorem} \\\\ {\\footnotesize Ch.~57}}'''),
('''\\item HP--Li restricted closure
(\\Cref{v4-arith:w5-a:thm:hpli-form}) on
\\(\\mathrm{PW}^{\\mathrm{hol}}_{F}\\) up to the archimedean correction.''','''\\item the signed Weil pairing on $\\mathscr A$
(\\Cref{v4-arith:sc:full-comparison}).'''),
('''\\item \\textbf{HP--Li on restricted class} (Conditional \\(\\to\\)
Theorem on \\(\\mathrm{PW}^{\\mathrm{hol}}_{F}\\) up to archimedean) via
Ch.~57.''','''\\item \\textbf{Signed arithmetic comparison.} The complete compact-test
identity and explicit positive and negative finite-prime lines are
\\Cref{v4-arith:sc:full-comparison,v4-arith:sc:two-signs}.'''),
('''\\item HP--Li positivity is reduced on the restricted class
\\(\\mathrm{PW}^{\\mathrm{hol}}_{F}\\) up to the archimedean Tate
distribution via the Mellin--Rankin--Selberg isometry \\(\\Upsilon_{F}\\)
(\\Cref{v4-arith:w5-a:thm:hpli-form}).''','''\\item The complete Weil form has the signed comparison
\\eqref{v4-arith:sc:full-comparison}. The positive finite-prime line
is constructed in \\Cref{v4-arith:sc:two-signs}; extending its norm
identity to the full test algebra is impossible.''')]
for old,new in pairs:
 if old not in s:print('MISSING',old[:85])
 else:s=s.replace(old,new)
p.write_text(s)
# Restore the stronger historical auxiliary HFD condition, without attaching
# the arithmetic gamma sign to it.
p=r/'archimedean-kernel.tex';s=p.read_text();s=s.replace('The auxiliary high-frequency condition is\n\\begin{equation}\n B[f]\\ge A[f].','''Put $M=-g(0)>0$. The auxiliary high-frequency condition is
\\begin{equation}
 2t_*M\\sup_{|u|\\le t_*}|h_f(u)|^2\\le B[f].''');s=s.replace('The positive gamma cone is', '''It implies $A[f]\\le B[f]$, because $-g(u)\\le M$ in the core.
The positive gamma cone is''');s=s.replace('positive for large $v$.','''positive for large $v$. More precisely, $B[b_v]$ grows like
$2\\pi\\|b\\|_2^2\\log v$, whereas the core supremum decays faster
than every power of $v$. This proves the stronger high-frequency
condition as stated.''');p.write_text(s);next(a.glob('61_*')).write_text(s)
print('Consumer assertions and HFD definition corrected.')
