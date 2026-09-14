# Volume IV prime-distribution review

## Verdict and custody

**Bounded mathematical PASS:** the new prime-distribution chapter and the changed normalization and compact-trace passages are correct on their stated domains.

**Native consumer closure FAIL:** the full source closure still contains contradictory archimedean signs, an unsupported determinant normalization, and an invalid scattering implication. These inherited statements do not invalidate the new prime-distribution proofs. They prevent acceptance of the entire native closure or any claim that its arithmetic comparison is complete.

This review concerns the exact snapshot in `inputs/candidate024/`. Its source aggregate is:

`8fd836044e90f22dc5a7a37331c2bd99517c3bbc17daff0a47ab5d79fbfaf9c8`

The aggregate hashes sorted original relative paths, a NUL, the file SHA-256, and a newline. `review-freeze.json` records all 119 files. Its SHA-256 is `4a778872fa402b0e7c7b86eef26b876f9be5e4675b479bc6936601411c95889a`.

Both worktrees have base commit `10157885d7d9df587df8bf43804acabcbb7ad850`. The review branch is `intake/frontier-vol4-prime-026-20260914`. No manuscript source was edited. No staging, commit, push, publication, or cleanup occurred.

The previously supplied source freeze had aggregate `0bc7313bfc82222be022b242290d4070c9ccbba36c95fe6af19ec708b0747efc`. At capture, 118 rows matched. Chapter56 differed: expected `9d84b17d05fd5952dd5e8f71087295cd4ca2f4acdaef524f65870e0f85f9603e`, observed `d22cbfd50cf7baaabfca301517efdd4b862ed0ddb3c5ed586d63722de0314d69`. Therefore the old freeze cannot certify this complete snapshot. No public final PASS for identical candidate024 bytes was found in the routed return directories.

The required mathematical configuration is `gpt-6-astra` with `ultra` reasoning. Independently observed runtime metadata was unavailable and remains unverified. The review does not attribute mathematical validity to a runtime configuration.

## Exact reviewed boundaries

| Source | SHA-256 | Reviewed boundary |
|---|---|---|
| `prime-carriers.tex` | `e14b2587ae93064ad10cb3d60da1afc9cf27736764de7851655eab8c92b93668` | All 406 lines |
| `native-source/chapters/arithmetic/87c_prime_distributions.tex` | `6023420dc3a535383989dd072041dc5eb1a7cca7f9f56770a4fa1011140b02ee` | Exact native projection of the prime chapter |
| `native-source/chapters/arithmetic/87_HPAr_spectral_flow.tex` | `07a113a71fb82c1a166a0b771629a37a7a0990479e9397f224a7e1c3e0b81f16` | Changed normalization and distribution passages, lines 234–355 |
| `native-source/chapters/arithmetic/56_hp_ar_operator_construction.tex` | `d22cbfd50cf7baaabfca301517efdd4b862ed0ddb3c5ed586d63722de0314d69` | Changed constant and Dirichlet-series domain, lines 418–432; conditional trace and square class, lines 561–632 |
| `arithmetic-reader.tex` | `1c9c168e6f1aeab13102bfd5e85169d7bcf064e01cb3acafa9a0ac5ee730793d` | Theta integral and normalization dependency, lines 85–176 |
| `comparisons.tex` | `056c295e70365f59635a00e2f218d183a5720b38e799fef735204c8b3119d78d` | Fourier convention and involution dependency |

The native023-to-snapshot delta changes only Chapters56, 87, and 87c. `native023-to-frozen026.patch` has SHA-256 `288aa88572d1b26c218b3127c72e3a12630c3473438a20cbfa98d75886aa8d1e`.

The old occupation, jet, Hilbert transport, and general scattering results were not re-certified in this review. Their unchanged bytes were checked against the preceding candidate. The prime chapter introduces no use of a native positive pairing or occupation intertwiner.

## Mathematical reconstruction

### Ambient spaces and conventions

All distributions are complex-linear. The initial carrier is the LF test space \(\mathscr A=C_c^\infty(\mathbb R)\). Temperedness means continuous extension to \(\mathscr S(\mathbb R)\). Dirac masses use additive Lebesgue coordinates. The Fourier conventions are

\[
\mathcal F_+f(z)=\int f(t)e^{izt}\,dt,
\qquad
\mathcal F_-f(u)=\int f(t)e^{-iut}\,dt,
\qquad
f(t)=\frac1{2\pi}\int\mathcal F_+f(u)e^{-iut}\,du.
\]

The entire Fourier image carries the transported topology of \(\mathscr A\). The zero multiset includes multiplicity. For \(\rho=\beta+i\gamma_\rho\), the evaluation point is \(z_\rho=-i(\rho-1/2)\), not its real part.

### Growth, zeros, and the Hadamard constant

The theta proof supplies

\[
\xi(s)=\frac12+\frac{s(s-1)}2
\int_1^\infty\sum_{n\ge1}e^{-\pi n^2x}
\bigl(x^{s/2}+x^{(1-s)/2}\bigr)\frac{dx}{x}.
\]

Periodization of the Gaussian proves the theta relation used here. Exponential decay permits all complex derivatives locally uniformly. Thus \(\xi\) is entire, \(\xi(0)=1/2\), and \(\xi(s)=\xi(1-s)=\overline{\xi(\bar s)}\).

For \(|s|\le R\), bound the powers by \(2x^{(R+1)/2}\). Split the exponential as \(e^{-\pi x/2}e^{-\pi x/2}\). Maximizing \(x^Ae^{-\pi x/2}\) gives the claimed \(CR\log(R+2)\) bound for the logarithmic maximum. Jensen's formula at radius \(2R\) then gives \(N(R)=O(R\log(R+2))\), since \(\xi(0)\ne0\). Dyadic summation proves \(\sum|\rho|^{-2}<\infty\).

If there were finitely many zeros, the finite-order factorization theorem would give \(e^{a+bs}P(s)\). The gamma integral on \([s/2,s/2+1]\) gives \(\log\xi(s)\ge(s/2)\log s-Cs\) for real \(s\ge2\). This excludes that factorization. Euler-product nonvanishing and reflection place all zeros in \(0\le\Re s\le1\). No zero-free boundary theorem or RH assumption enters.

Removing the apparent singularity at zero yields

\[
\xi(s)=(s-1)\Gamma(1+s/2)\pi^{-s/2}\zeta(s).
\]

Differentiation gives

\[
B=-1-\frac\gamma2-\frac12\log\pi+\log(2\pi)
=-1-\frac\gamma2+\frac12\log(4\pi).
\]

The three special values are correctly identified in DLMF 25.6.1, 25.6.11, and 5.4.11. For each canonical factor, \(\log((1-s/\rho)e^{s/\rho})=O_K(|\rho|^{-2})\). Its logarithmic derivative is \(s/[\rho(s-\rho)]\). Normal convergence and differentiation at zero therefore establish the exact product and the constant \(B\). Separating \(\sum1/\rho\) would require another summation convention.

### Chebyshev bound and the sharp weight threshold

For every prime \(p\),

\[
v_p\binom{2n}{n}=\sum_{k\ge1}
\left(\left\lfloor\frac{2n}{p^k}\right\rfloor
-2\left\lfloor\frac n{p^k}\right\rfloor\right).
\]

Each summand is zero or one. Hence \(\binom{2n}{n}\) divides \(\operatorname{lcm}(1,\ldots,2n)\), whose logarithm is \(\psi(2n)\). The largest-binomial bound proves

\[
\psi(2n)\ge2n\log2-\log(2n+1).
\]

Taking \(n=\lfloor x/2\rfloor\) yields \(\psi(x)\ge cx\) for sufficiently large \(x\). The upper bound \(\psi(x)\le x\log x\) follows termwise. These estimates require no prime-number asymptotic.

For \(\mu_\sigma=\sum_{m\ge2}\Lambda(m)m^{-\sigma}\delta_{\log m}\), local finiteness gives continuity on every fixed compact test carrier. When \(\sigma\ge1\),

\[
|\mu_\sigma(\varphi)|\le
\sup_t(1+|t|)^3|\varphi(t)|
\sum_{m\ge2}\frac{\log m}{m(1+\log m)^3}.
\]

The final series converges. If a positive measure on the half-line is tempered, apply its finite seminorm bound to \(\chi(t/T)\). Choose \(\chi\ge0\), compactly supported, and equal to one on \([0,1]\). Its seminorms grow at most polynomially in \(T\), so the mass of \([0,T]\) must grow polynomially. For \(0\le\sigma<1\), that mass is at least \(ce^{(1-\sigma)T}\). For \(\sigma<0\), comparison with \(\mu_0\) suffices. This proves both failure directions.

Absolute summation gives finite total mass for \(\sigma>1\). Partial summation gives

\[
\sum_{m\le X}\frac{\Lambda(m)}m
=\frac{\psi(X)}X+\int_1^X\frac{\psi(x)}{x^2}\,dx\longrightarrow\infty.
\]

Thus \(\sigma=1\) is tempered but not finite. All smaller exponents are non-tempered and cannot be finite. In particular, critical weighting does not give a tempered positive measure, even under RH.

### Laplace and Fourier domains

The Euler product and local absolute convergence give
\(\int e^{-st}d\mu_0=-\zeta'(s)/\zeta(s)\) only for \(\Re s>1\). For \(\sigma>1\), Fourier integration against the finite measure gives the displayed value at \(\sigma+iu\). Dominated convergence in the preceding seminorm bound proves \(\mu_{1+\varepsilon}\to\mu_1\) weakly in \(\mathscr S'\). Fourier continuity proves the boundary statement. Meromorphic continuation does not enlarge the domain of the original positive-measure integral.

### Compact-test explicit formula

For a fixed compact support and every \(N\), integration by parts gives
\(|h(u+iv)|\le C_{K,N}(1+|u|)^{-N}\) uniformly for \(|v|\le1/2\). The zero count therefore gives absolute convergence of \(\sum_\rho h(z_\rho)\), including multiple zeros, and continuity in the compact-test topology.

Set \(H(s)=\int f(t)e^{(s-1/2)t}dt\). Use the rectangle bounded by \(\Re s=a\) and \(\Re s=1-a\), where \(a>1\). One can choose heights \(T_j\in[j,j+1]\) at distance at least \(j^{-2}\) from all zero ordinates. The excluded intervals have total length \(O(\log j/j)\), even using only the global zero bound. Conjugation gives the same separation at the negative height.

The canonical logarithmic derivative is polynomially bounded on the horizontal sides. Split zeros at \(|\rho|=2T_j\), use ordinate separation for the finite part, and use \(C T_j/|\rho|^2\) for the tail. The rapid decrease of \(H\) makes the horizontal integrals vanish. Functional-equation substitution on the left side gives

\[
\sum_\rho H(\rho)=\frac1{2\pi i}\int_{\Re s=a}
(H(s)+H(1-s))\frac{\xi'(s)}{\xi(s)}\,ds.
\]

On the right line,

\[
\frac{\xi'}\xi=\frac1s+\frac1{s-1}-\frac12\log\pi
+\frac12\psi_\Gamma(s/2)+\frac{\zeta'}\zeta.
\]

For the Dirichlet term, Fourier inversion gives
\(m^{-1/2}f(\log m)\) from \(H(s)\), and \(m^{-1/2}f(-\log m)\) from \(H(1-s)\). Its sign is negative. Move the remaining terms to \(\Re s=1/2\). The pole at one contributes \(H(1)+H(0)=h(-i/2)+h(i/2)\). The rational part is odd in the vertical variable and integrates to zero against the even combined test. Reflection of half the gamma integral gives

\[
\mathcal A_\infty(h)=\frac1{2\pi}\int h(u)
\bigl(\Re\psi_\Gamma(1/4+iu/2)-\log\pi\bigr)du.
\]

The digamma series proves logarithmic growth on this line. Every integral converges absolutely. This establishes the formula for non-even complex tests as well as even ones. Odd tests give zero on every term, which independently checks the reflection conventions.

### Critical centering and the converse

Define \(\nu_\sigma=\mu_\sigma-\mathbf1_{[0,\infty)}e^{(1-\sigma)t}dt\) on compact tests. For \(\sigma=1\), the removed density has Fourier transform

\[
\lim_{\varepsilon\downarrow0}(\varepsilon+iu)^{-1}
=\pi\delta_0-i\operatorname{pv}(1/u).
\]

For \(f\in C_c^\infty(0,\infty)\), DLMF 5.9.16 and Fourier inversion give

\[
\mathcal A_\infty(h)=-\int_0^\infty
\frac{e^{-t/2}}{1-e^{-2t}}f(t)dt.
\]

To justify the interchange, truncate the digamma integral first. Near zero, the subtracted numerator is bounded by \(Cv(1+|u|)\). Integrability follows from the rapid decay of \(h\). At infinity the denominator is bounded away from zero and the exponential factors decay. The constant terms vanish because \(f(0)=0\). The substitution \(v=2t\) produces exactly the stated coefficient.

Subtracting the main half-line density and cancelling \(h(i/2)\) yields

\[
\nu_{1/2}(f)=-\sum_\rho\int f(t)e^{(\rho-1/2)t}dt
-\int_0^\infty\frac{e^{-t/2}}{e^{2t}-1}f(t)dt.
\]

Under RH, the zero term is the tempered distribution \(f\mapsto\mu_{\rm ord}(\mathcal F_+f)\). Choose a smooth cutoff equal to zero on \(( -\infty,1/2]\) and one on \([1,\infty)\). Its multiplication preserves \(\mathscr S'\). The remaining density decays exponentially after that cutoff. The discrepancy with \(\nu_{1/2}\) is a compactly supported distribution. This proves temperedness under RH, including the otherwise singular neighborhood of zero.

Conversely, suppose \(\nu_{1/2}\in\mathscr S'\). Its support lies in \([0,\infty)\). Choose a smooth \(\eta\) equal to one there and zero on \(( -\infty,-1]\). For \(\Re s>0\), \(\eta(t)e^{-st}\) and all parameter derivatives are Schwartz functions, locally uniformly in \(s\). Thus \(L(s)=\nu_{1/2}(\eta e^{-st})\) is holomorphic. On \(\Re s>1/2\), truncation of these Schwartz tests and absolute convergence prove

\[
L(s)=-\frac{\zeta'(s+1/2)}{\zeta(s+1/2)}-\frac1{s-1/2}.
\]

Meromorphic uniqueness extends the identity. The pole from \(\zeta\) at one cancels. A zero of order \(r\) with \(\Re\rho>1/2\) would leave residue \(-r\) at \(s=\rho-1/2\), contradicting holomorphy. Reflection excludes zeros on the other side. This proves the stated equivalence, without assuming its conclusion.

The same argument excludes temperedness of \(\nu_0\). Infinitely many xi zeros and reflection guarantee a zero with positive real part. Equality of the full zero functional with the ordinate measure on every compact Fourier test implies critical temperedness by the same cutoff proof. Hence the final shadow criterion is also valid. None of these criteria constructs an arithmetic positive pairing.

## Native trace passages

Chapter56 now explicitly assumes a complete orthonormal eigenbasis with actual zero multiplicities and real ordinates. Compact Fourier tests decrease faster than every power on the real line. The zero count gives \(\sum|h(\gamma_\rho)|<\infty\). Diagonal functional calculus therefore makes \(h(H_{\rm HP})\) trace-class. The stipulated actual-divisor identity permits application of the new explicit formula. A regularized trace can share this value only under the stated compatibility assumption.

For \(g^*(t)=\overline{g(-t)}\), Fubini gives
\(\mathcal F_+(g*g^*)=\phi(z)\overline{\phi(\bar z)}\). On the real spectrum the terms are \(|\phi(\gamma_\rho)|^2\). Positivity follows under the realization hypothesis, which already imposes critical-line zero placement. The text does not infer the hypothesis from positivity of an unrelated Petersson cone. Chapter60, lines 254–260, preserves that conditional boundary.

Chapter87's new even-test formula is the exact restriction of the proved compact-test formula. Its two polar evaluations are separate from the digamma density. The unweighted and critical prime measures retain their correct carriers.

## Native blockers and deciding models

### N1. The inherited archimedean sign and test carrier

Chapter57, lines 65–110, uses the right-hand side
\(P(h)-W_\infty(f)-W_{\rm fin}(f)\), with

\[
W_\infty(f)=\frac1{2\pi}\int h(u)
\bigl(\Re\psi_\Gamma(1/4+iu/2)+\log\pi\bigr)du.
\]

This contradicts the new formula's digamma sign. The issue is not resolved by calling one term a contribution with a different sign.

Choose \(0<a<b<\log2\) and a nonzero even nonnegative \(f\in C_c^\infty\) supported in \((-b,-a)\cup(a,b)\). Its prime term and \(f(0)\) vanish. The integral representation above gives

\[
\mathcal A_\infty(h)=-2\int_a^b
\frac{e^{-t/2}}{1-e^{-2t}}f(t)dt<0.
\]

The correct zero functional is \(P(h)+\mathcal A_\infty(h)\). The inherited formula gives \(P(h)-\mathcal A_\infty(h)\). Their difference is strictly positive. This is an exact compact-test counterexample to the normalization, with no numerical zero computation.

There is also a logically prior carrier defect. Chapter57 defines PW as the entire Fourier image of compact smooth functions, then takes another Fourier transform and evaluates it at complex zeros. That second transform is generally only a compactly supported smooth function on the real line. It has no stated entire continuation. Repair must name the Fourier preimage and the entire image separately. Even after that natural carrier correction, the sign counterexample above remains.

Chapter74's density and Chapter79's claimed constant-shift comparison inherit these incompatible conventions. They require a fresh normalization comparison. No blanket acceptance of their Weil or RH consequences is licensed here.

### N2. Scattering unitarity does not give trace positivity

Chapter80, lines 340–407, claims a Weil spectral-shift identification and then states that positivity becomes scattering unitarity. Its reference to the corrected Chapter56 trace theorem supplies no map to its different carrier.

An explicit self-adjoint scattering pair refutes that general implication. Let

\[
K=L^2(\mathbb R,dx)\oplus\mathbb C,\quad
H_0=M_x\oplus0,\quad H_1=M_x\oplus1,
\]

with common domain
\(\{v\in L^2:xv\in L^2\}\oplus\mathbb C\). Their bounded difference is the rank-one projection onto \(\mathbb C\). Both absolutely continuous subspaces are \(L^2(\mathbb R)\oplus0\).

For every real \(t\),

\[
e^{itH_1}e^{-itH_0}P_{\rm ac}(H_0)=P_{\rm ac}(H_0).
\]

The wave operators therefore exist exactly and have full absolutely continuous range. Their scattering operator is the identity on that subspace. No existence theorem for wave operators is needed.

Take any nonzero nonnegative \(g\in C_c^\infty(\mathbb R)\), set \(\phi=\mathcal F_+g\), and put \(h(z)=\phi(z)\overline{\phi(\bar z)}\). Then

\[
h(H_1)-h(H_0)=0\oplus(h(1)-h(0)),
\qquad
\operatorname{Tr}(h(H_1)-h(H_0))=|\phi(1)|^2-|\phi(0)|^2<0.
\]

Strictness follows from the equality condition in the triangle inequality. A nonzero smooth nonnegative function is positive on an interval, where \(e^{it}\) is not constant. The spectral-shift formula also holds directly with \(\xi_{\rm shift}=\mathbf1_{(0,1)}\), since \(\int_0^1h'=h(1)-h(0)\). Its exponential \(e^{-2\pi i\xi_{\rm shift}}\) is one almost everywhere. Thus scattering can lose the integer bound-state contribution even when a trace formula is valid.

This model refutes the proposed generic bridge. It neither identifies the native arithmetic pair with this example nor refutes a separately proved arithmetic identity. The remaining requirement is an actual arithmetic realization and a comparison retaining all spectral contributions and the specified test carrier.

### N3. Divisor data do not fix the determinant normalization

Chapter56, lines 482–538, still asserts that an unspecified zeta-regularized prescription yields exactly \(\xi(s)\). Its proof invokes normalization compatibility that is not in the displayed hypothesis. Correcting \(B\) does not supply the missing prescription.

For example, \(D_c(s)=e^{cs}\xi(s)\), for arbitrary \(c\in\mathbb C\), has exactly the same divisor and order bound. A nonzero scalar multiple has the same properties. The divisor therefore cannot determine the scalar or exponential factor. A spectral zeta construction additionally needs a complex-power branch, an initial trace-class domain, continuation regular at zero, and proved normalization values. An entire-function Hadamard product alone is insufficient.

This blocker is inherited outside the compact-trace delta. The new trace theorem expressly does not claim that determinant normalization constructs its trace comparison.

## Evidence and verification limits

The independent integer calculation checks \(n=1,\ldots,512\). Every central binomial divides the corresponding least common multiple and satisfies its mean bound. The general proof above carries the unbounded conclusion. A separate theta-integral calculation gives

\[
B=-0.0230957089661210338143102479064952916219321271520507595\ldots.
\]

It agrees with the closed constant to the recorded 70-digit working precision. Quadrature error is not certified. These numerics are diagnostics, not proof evidence for a zero-location statement. `calculations.py` and `calculation-results.json` retain commands, versions, inputs, and scope.

Both source snapshots were independently compiled with `pdflatex -no-shell-escape -recorder -interaction=nonstopmode -halt-on-error`. The reader stabilized on passes 3–4. The native PDF and AUX stabilized on passes 4–5. `build-review.py`, `build-reader.json`, and `build-native.json` retain exact commands and environments. All build writes stayed within this report directory.

The reader has 31 pages, no undefined references, no duplicate labels, no overfull boxes, and two underfull horizontal boxes. The native PDF has 1,074 pages, no undefined references, and no duplicate labels. It retains 148 horizontal and three vertical overfull boxes outside this bounded layout verdict.

The reader PDF hash is `0d11924282de4f0864b5842bf0fea10380d15e1e0f8f632e031a3ac749cd62a9`. The native PDF hash is `fc65a494a80ddbedf95855a94bb94da7dc92fd77494275f3872db6caca2feb9e`.

Reader physical pages 25–30 and native physical pages 589–592 and 890–896 were individually inspected as PNGs. The new formulas and hypotheses are legible, with no clipping, overlap, or missing symbols. The new prime chapter and changed trace passages contain mathematical exposition. Inherited bibliography-production prose elsewhere is not accepted by this review. No standalone PDF was opened in a reader application.

DLMF browser retrieval verified the special values and digamma integral at their exact equation locators. Direct downloads of the TeX endpoints returned HTTP 403. The failure is retained in `primary-evidence.json`. Access to the original von Mangoldt article failed with HTTP 403 at EuDML and HTTP 405 at the publisher. The inherited pointwise explicit-formula citation was therefore not newly certified. It is not used in the compact-test proof.

The first calculation command used system Python, which lacked `mpmath`. The installed Homebrew Python 3.14.6 with `mpmath` 1.3.0 ran the calculation successfully. An initial log read assumed UTF-8 and failed on a legacy byte. A repeated read with replacement decoding produced the recorded diagnostics. Neither failure was suppressed as a passing check.

## Handoff and remaining obligation

For a reader that already includes the earlier occupation and comparison sources, the new include is `prime-carriers.tex`. It depends on `mo:xi-integral` from `arithmetic-reader.tex` and `v4-arith:mc:test-algebra` from `comparisons.tex`. The native include is `chapters/arithmetic/87c_prime_distributions.tex`, with the native theta label `v4-arith:mo:xi-integral`. Native Chapter87 supplies the include call. The current candidate reader `main.tex` supplies the complete existing dependency closure.

The corrected prime chapter is eligible for integration within this bounded verdict. A new integration candidate requires its own byte freeze and checks. Root retains acceptance and integration authority. The entire native closure remains unaccepted until the inherited carrier, normalization, determinant, and scattering obligations are repaired. The actual arithmetic pairing, completed scaling action, and trace comparison remain unconstructed. No RH conclusion follows from this review.
