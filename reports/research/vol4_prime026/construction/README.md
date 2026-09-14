# Native Weil carrier and occupation-scattering construction

## Status and authority

The coordinator authorized this construction after the exact prime024 review was recorded. The owned reader sources are `research-candidates/vol4_prime026/weil-pairing.tex` and `occupation-scattering.tex`. Their exact bytes also replace native Chapters57 and 80 in the isolated candidate closure. The original native chapters remain in the immutable review inputs.

Status: **constructed and locally checked; fresh independent mathematical acceptance pending**. The writer does not certify its own source. No complete arithmetic pairing, Hilbert–Pólya construction, or RH proof is claimed. The two-chapter repair does not accept the remaining native book. No staging, commit, push, publication, reader-application opening, or cleanup occurred.

The required configuration is `gpt-6-astra` with `ultra` reasoning. Independently observed metadata remains unavailable and unverified.

## The preserved mathematical question

The original question asks for an arithmetic pairing and trace comparison between occupation/scaling constructions and the full xi zero functional. Correct scalar weights or a positive local state do not answer it.

The construction retains the original entire-function multiplier \(h(\log n)\), where \(h\) is a compact Fourier transform. It separately defines the compact-test multiplier \(f(\log n)\). These maps are not identified. The former remains a holomorphic series whose modularity needs proof. The latter is a finite Fourier polynomial, and its exact modularity obstruction is proved.

For scattering, the input is the actual disjoint-interval occupation embedding already specified in native Chapter80. The construction extends that concrete embedding to the full undamped operator. It then computes the domain, wave limits, trace map, and support obstruction. It makes no claim that an arbitrary embedding is the native arithmetic map.

## Constructed statements and deciding checks

### Weil carrier and gamma sign

The source separates \(\mathscr A=C_c^\infty(\mathbb R)\) from its entire image \(\mathscr P=\mathcal F_+\mathscr A\). The latter has the transported topology. All prime, polar, and zero terms use these exact maps.

The convention \(W=P-W_\infty-W_{\rm fin}\) requires

\[
W_\infty(f)=\frac1{2\pi}\int h(u)
\bigl(\log\pi-\Re\psi_\Gamma(1/4+iu/2)\bigr)du.
\]

For an even positive test supported in \(\pm(a,b)\subset(-\log2,\log2)\) and away from zero, the prime and constant terms vanish. The digamma integral gives a strictly positive \(W_\infty\). This decides the sign without approximate zeros.

The full form \(q_W(f,g)=W(f*g^*)\) is Hermitian. The primary source for its classical positivity criterion is Suzuki, arXiv:2301.00421v3, Introduction, p.1, equations (1.1)–(1.2) and the intervening criterion. The PDF is retained at `primary/suzuki-weil.pdf`, SHA-256 `e4100e529d74cdc4dfa855aa24bcf34a88562d9facebefd70de6e529f9a1ce2e`. Its \(\gamma\) is the negative of the present \(z_\rho\), exactly matching the evaluation convention.

### Polar moments and coefficient maps

The two polar evaluations yield the rank-two Hermitian form
\(a(f)\overline{b(g)}+b(f)\overline{a(g)}\), where \(a,b\) are the two exponential moments. The moment map onto \(\mathbb C^2\) is surjective because the two exponential functions are linearly independent. The form has eigenvalues \(1,-1\). Thus removing the polar term is a specified form change, and does not preserve positivity automatically.

For a compact multiplier, the resulting holomorphic function is a finite polynomial in \(q\). Modularity under \(z\mapsto-1/z\) would make its value at \(iy\) flat at \(y=0\). It is analytic there, so flatness forces the polynomial to vanish. This proves the strongest true modularity statement for that carrier.

The entire multiplier uses \(h(\log n)\) and retains the original question. Polynomial coefficient growth and exponential \(q\)-decay prove convergence on the upper half-plane. Its automorphy is not inferred from convergence.

For an actual cusp form \(G=\sum b_nq^n\), unfolding gives

\[
\int_{\Gamma\backslash\mathbb H}|G|^2y^kE(z,s)\,d\mu
=\frac{\Gamma(s+k-1)}{(4\pi)^{s+k-1}}
\sum_{n\ge1}|b_n|^2n^{-(s+k-1)},\quad s>1.
\]

This replaces the unsupported inserted xi denominators by the actual coefficient calculation. The argument uses nonnegative unfolding, Fourier orthogonality, and the gamma integral. The coefficients belong to \(G\), not automatically to the fixed input form \(F\).

### A negative finite-prime square

Let \(L=\log2\), choose a real nonzero bump \(b\) of sufficiently small support, and set \(f=b-b(\cdot-L)\). Its autocorrelation is

\[
f*f^*=2c-c(\cdot-L)-c(\cdot+L),\qquad c=b*b^*.
\]

The support meets only the prime logarithms \(\pm L\), where the value is \(-\|b\|_2^2\). Therefore

\[
W_{\rm fin}(f*f^*)=-\sqrt2\log2\,\|b\|_2^2<0.
\]

This refutes a positive Hilbert realization of the separate finite-prime form on the full compact test algebra. It does not decide the full Weil form, which has polar and archimedean terms.

The rational Li values \(1-(1-1/\rho)^n\) have leading term \(n/\rho\). Compact Fourier tests decay faster than every inverse power along the zero strip. Infinitely many zeros therefore preclude exact interpolation of these values by one compact Fourier test. Generalized Li tests and approximation in another topology remain separate constructions.

### The full occupation operator

The affected blocks are \(K_m=L^2((m,m+1))\otimes\mathbb C e_0\). On them,

\[
A_m=M_\tau,\qquad B_m=A_m+(\log m)|e_m\rangle\langle e_m|.
\]

The bounds \(m\le B_m\le m+1+\log m\) make the maximal direct-sum domain equal to \(\operatorname{Dom}D_0\). The direct sum defines a self-adjoint \(D=D_0+V\), although \(V\) is unbounded and not trace class. Resolvents agree on each finite collection of blocks for all sufficiently large truncations. Their uniform nonreal resolvent bound proves strong resolvent convergence.

Compact spectral cores meet finitely many blocks. Twice integrating their Fourier coefficients by parts gives an integrable Cook bound. The full wave limits therefore exist and are isometries. Completeness is not proved or used.

### Trace-class tests and the support contradiction

Localize a Schwartz test to the spectral interval of \(A_m\) and \(B_m\). Duhamel and Fourier inversion give

\[
\|h(B_m)-h(A_m)\|_1\le C(\log m)
\bigl(\|q_m'\|_2+\|q_m''\|_2\bigr).
\]

Uniform cutoff derivatives bound this by
\(C_N(\log m)\sqrt{3+\log m}(1+m)^{-N}\) times a Schwartz seminorm. Summing with \(N=3\) proves a continuous map \(\mathscr S\to\mathcal S_1(K)\). The trace distribution is tempered and supported in \([1,\infty)\), because every changed block has spectrum there.

If a lower-bounded tempered spectral distribution reproduced \(W\) on every compact Fourier test, then \(W\) would be tempered in the additive variable. The previously proved critical-centering argument would imply RH. Under RH, Fourier density identifies that spectral distribution with the ordinate counting measure. Its negative ordinates are unbounded. This contradicts the lower support bound. Hence the complete occupation model fails the requested arithmetic identity unconditionally.

This is an obstruction for the specified model. It does not exclude an arithmetic construction with another carrier or trace functional. It does not infer RH from an existing object.

## Failed routes retained

The full preceding sources remain under `../inputs/candidate024/native-source/chapters/arithmetic/`. `preserved-chapters.json` records their hashes and the replacement paths. `label-map.json` records old and new anchors. The final patch gives exact before/after bytes.

| Attempted route | Exact failure | Next valid requirement |
|---|---|---|
| Treat PW and compact preimages as one carrier | The second Fourier transform is generally not entire | Keep \(f\) and \(h=\mathcal F_+f\) separate |
| Use \(+\Re\psi+\log\pi\) in a subtracted archimedean term | The compact positive sign test contradicts the explicit formula | Use \(\log\pi-\Re\psi\) with the stated subtraction |
| Remove Tate poles without altering positivity | The polar form has rank two and both signs | Retain its exact two moments or prove a restriction |
| Obtain nonzero modular forms from compact coefficient multipliers | A finite Fourier polynomial cannot satisfy the modular inversion law | Prove automorphy for the distinct entire multiplier |
| Make the full finite-prime form a Petersson norm | The translated-bump square has a strictly negative value | Supply a restricted carrier and an actual comparison |
| Interpolate all Li rational values by one compact test | Rapid Fourier decay contradicts the \(n/\rho\) leading term | Specify a larger test carrier and topology |
| Infer positivity from unitary scattering | Complete identity scattering retains a negative discrete trace difference | Prove the full trace and square-form identity |
| Identify the occupation perturbation trace with the full Weil functional | Its tempered spectral distribution is supported on a half-line | Construct a different spectral carrier or trace |
| Derive unitary phase from reflection symmetry alone | The explicit quotient \((1-t)/(1+t)\) is not unimodular | Use the correctly stated conjugation symmetry |

The inherited Chapter56 determinant-normalization blocker remains outside these two source replacements. Neither the new trace map nor the exact xi constant supplies its missing branch, continuation, and normalization.

## Checks and remaining propagation

The initial build rejected the legacy `rm` math-font command under `memoir`. The source now uses `mathrm`. The failed output and initial source freeze remain in `revision001/`. Explicit carrier and domain definitions were added in the same bounded correction. The current source freeze supersedes that failed candidate.

The final Petersson pullback uses a fixed standard fundamental domain. The weighted measure is defined on that domain. The preceding source and build records remain in `revision002/`. Only the reader's physical page34 and the native physical page598 changed in that raster comparison.

Independent review then refuted a proof sentence asserting that every nonconstant multiplier changes a direct-integral pairing. A nonconstant unimodular multiplier preserves it. The proof now uses the exact rescaling of a nonzero map from I to 2I, which multiplies the pairing by four. The preceding source, freeze, manifest, and build records remain in `revision003/`. This correction changes no theorem statement.

The new reader and native chapters are byte-identical. The full existing dependency closure is included. All external references to the replaced chapters' retained theorem anchors still resolve syntactically. This is not a semantic acceptance of their consumers.

In particular, native Chapter60 still claims a fixed-form prime-positivity closure, and Chapters61, 62, 74, and 79 still use inherited gamma or test-carrier conventions. Chapters62 and 69 also consume the former inserted Rankin–Selberg kernel. They require separate propagation and review. The new negative-square and exact unfolding statements make those obligations explicit.

`checks.py` records finite algebra identities independently: autocorrelation coefficients, the polar eigenvalues, a rational rank-one projector, trace signs, and Li leading coefficients. These checks establish only their finite identities. The manuscript supplies the general smooth-test and operator proofs.

The final manifest records the exact source hashes, full aggregate, native patch, build commands, PDF hashes, render inspection, primary evidence, and outstanding independent review. Only the coordinator may integrate or accept the new source.
