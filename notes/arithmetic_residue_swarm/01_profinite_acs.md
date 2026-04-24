# Agent 1 Report: Profinite Arithmetic Chern--Simons

## Target Under Attack

Target theorem, as stated by Chapter 82:

Let \(G_N=GL_2(\mathbb Z/N\mathbb Z)\). Let
\(\alpha_N\in H^3(BG_N,\mathbb C^\times)\) be a compatible tower of
finite levels whose inverse-limit class is the arithmetic level
\(k^{\mathrm{Ar}}=\kappa^{\mathrm{Ar}}_{\mathsf G}\). The finite
arithmetic Chern--Simons theories
\[
Z^{\mathrm{Ar}}_{G_N,\alpha_N}
\]
admit a renormalised profinite limit
\[
\mathrm{ACS}^{\mathrm{qu}}_{k^{\mathrm{Ar}}}
:=\varprojlim_N^{\mathrm{ren}}Z^{\mathrm{Ar}}_{G_N,\alpha_N}
\]
on \(\overline{\mathrm{Spec}\,\mathbb Z}\), with:

1. boundary factorization algebra \(\partial\mathrm{ACS}^{\mathrm{qu}}_{k^{\mathrm{Ar}}}
   =\mathcal V^{\mathrm{prim}}\);
2. partition function
   \(Z_{\mathrm{ACS}^{\mathrm{qu}}}(\overline{\mathrm{Spec}\,\mathbb Z};k^{\mathrm{Ar}})
   =\xi(k^{\mathrm{Ar}})\);
3. Wilson loop identity
   \(\langle W_\rho(K_p)\rangle=\operatorname{tr}\rho(\mathrm{Frob}_p)\).

File anchor: `chapters/arithmetic/82_3d_acs_E1_ordered_bar.tex:262`.

## First-Principles Construction Attempt

Fix \(N\). Put \(G_N=GL_2(\mathbb Z/N\mathbb Z)\). The finite field
groupoid over an arithmetic 3-space \(M\) is
\[
\mathcal F_N(M)=\operatorname{Map}_{\mathrm{cont}}
(\Pi_1^{\mathrm{et}}(M),BG_N).
\]
For \(\alpha_N\in H^3(BG_N,\mathbb C^\times)\), Kim/Dijkgraaf--Witten
integration gives
\[
Z_N(M)=\sum_{[\rho]\in\pi_0\mathcal F_N(M)}
\frac{\langle\rho^*\alpha_N,[M]\rangle}{|\operatorname{Aut}(\rho)|}
\]
when \(\mathcal F_N(M)\) is finite. This is exactly the finite-level
state sum of Chapter 82. File anchor:
`chapters/arithmetic/82_3d_acs_E1_ordered_bar.tex:137`.

For \(M=\overline{\mathrm{Spec}\,\mathbb Z}\), the closed global
finite-etale fundamental group has no prime-indexed degrees of
freedom. By Hermite--Minkowski, a finite extension of \(\mathbb Q\)
unramified at every finite prime has discriminant \(1\), hence is
\(\mathbb Q\). Thus
\[
\Pi_1^{\mathrm{et}}(\mathrm{Spec}\,\mathbb Z)=1
\]
for finite-etale covers. Therefore
\[
\mathcal F_N(\overline{\mathrm{Spec}\,\mathbb Z})\simeq BG_N.
\]
The pulled-back degree-3 action is trivial on \(B1\), and the
groupoid-cardinality partition sum is
\[
Z_N(\overline{\mathrm{Spec}\,\mathbb Z})=\frac{1}{|G_N|}
=\frac{1}{N^4\prod_{\ell\mid N}(1-\ell^{-1})(1-\ell^{-2})}.
\]
After the canonical finite-gauge normalization by \(|G_N|\), this is
the constant \(1\). Without that normalization it tends to \(0\) along
cofinal \(N\). In neither convention does it produce a nonconstant
function of \(k^{\mathrm{Ar}}\), let alone \(\xi(k^{\mathrm{Ar}})\).

If one punctures at a finite set \(S\) of primes, replacing
\(\mathrm{Spec}\,\mathbb Z\) by \(\mathrm{Spec}\,\mathbb Z[1/S]\), the
field groupoids become nontrivial and finite-level Kim/DW theory
applies. That is a theory of ramified arithmetic link complements and
Wilson defects. It is not the closed profinite partition function of
the target theorem. Taking \(S\nearrow\mathbb P\) introduces a second
limit, a choice of local measures, and analytic weights \(p^{-s}\).
Those data are not present in the finite topological state sum.

## Proof Closure

The complete profinite theorem does not close.

The finite-level theory closes. The formal pro-object
\(\{Z^{\mathrm{Ar}}_{G_N,\alpha_N}\}_N\) exists after choosing
compatible finite levels and reduction maps. What does not exist from
the cited inputs is a canonical scalar renormalisation
\[
\varprojlim_N^{\mathrm{ren}} Z_N
\]
whose value is \(\xi(k^{\mathrm{Ar}})\), or a canonical boundary
category whose Hochschild trace is \(\mathcal V^{\mathrm{prim}}\).

The obstruction is structural, not computational.

## Exact Obstruction

1. Closed \(\overline{\mathrm{Spec}\,\mathbb Z}\) has trivial
   finite-etale local-system content. The finite closed state sum sees
   \(BG_N\), not the prime-indexed Euler factors. The zeta Euler product
   requires either local Wilson defects at every prime or a
   Bost--Connes/Hecke coefficient system. It is not produced by the
   closed Kim state sum.

2. The phrase "compatible tower of finite levels whose inverse-limit
   class is \(k^{\mathrm{Ar}}\)" is not yet a construction. Finite
   \(H^3(BG_N,\mathbb C^\times)\) classes are Dijkgraaf--Witten torsion
   levels. The arithmetic level \(k^{\mathrm{Ar}}\) is a Koszul/derived
   center scalar and a complex evaluation variable in the displayed
   \(\xi(k^{\mathrm{Ar}})\). No source constructs a map from that scalar
   to a continuous class in
   \(H^3_{\mathrm{cont}}(BGL_2(\widehat{\mathbb Z}),\mathbb C^\times)\).

3. A renormalisation that returns \(\xi(s)\) would have to insert the
   analytic weights \(p^{-s}\), the archimedean \(\Gamma_{\mathbb R}\)
   factor, and the polar terms. Chapter 82 already supplies these
   through the ordered-bar/Bost--Connes/Deninger package, not through
   the finite ACS state sum. File anchors:
   `chapters/arithmetic/82_3d_acs_E1_ordered_bar.tex:598`,
   `chapters/arithmetic/82_3d_acs_E1_ordered_bar.tex:640`,
   `chapters/arithmetic/82_3d_acs_E1_ordered_bar.tex:703`.

4. The boundary statement
   \(\operatorname{HH}_\bullet(\mathcal B_\infty^{\mathrm{Ar}})
   \simeq\mathcal V^{\mathrm{prim}}\) is exactly the local
   Satake/Iwahori trace comparison and profinite boundary
   renormalisation. It is not a consequence of finite groupoid
   cardinality. File anchor:
   `chapters/arithmetic/82_3d_acs_E1_ordered_bar.tex:308`.

5. The Wilson--Frobenius identity is proved only at finite level and on
   the unramified finite/abelian locus, then transported conditionally
   to the profinite limit. This supports the finite-prime trace
   component. It does not construct the global profinite measure. File
   anchor: `chapters/arithmetic/85_Wilson_line_Frobenius.tex:325`.

## Strongest Partial Theorem Proved

**Theorem.** For each \(N\) and each finite arithmetic link complement
whose \(G_N\)-field groupoid is finite, the Kim/Dijkgraaf--Witten
arithmetic Chern--Simons state sum and the boundary span construction
exist at finite level. If the levels \(\alpha_N\) are compatible under
reduction, these finite theories form a pro-object in finite
arithmetic DW theories. On the closed base
\(\overline{\mathrm{Spec}\,\mathbb Z}\), this pro-object has scalar
value \(1/|G_N|\) before finite-gauge normalization and scalar value
\(1\) after normalization. Hence the finite-level tower alone does not
produce \(\xi(s)\). For finitely many unramified Wilson defects, the
finite-level expectation is a finite class-function average whose
specialized level-zero value recovers the Frobenius trace.

This theorem is proved by finite groupoid cardinality, Hermite--Minkowski,
and the finite arithmetic DW construction. It is the honest surviving
statement beyond the manuscript's finite-level theorem.

## Primary-Source Anchors

- Kim, *Arithmetic Chern--Simons Theory I*, arXiv:1510.05818. The
  abstract states that the first three sections define classical
  Chern--Simons functionals on spaces of Galois representations, while
  the L-function comparison in Section 5 is speculative. The p-adic
  section treats a \(p\)-adic Lie group such as \(GL_n(\mathbb Z_p)\)
  with extra cyclotomic structure, not an adelic
  \(GL_2(\widehat{\mathbb Z})\) quantum measure. In Section 6 Kim says
  the desired comparison between Chern--Simons torsors and determinant
  line bundles is unavailable and is a major unsolved problem.
  Source link: https://arxiv.org/abs/1510.05818.

- Hirano--Kim--Morishita, *On arithmetic Dijkgraaf--Witten theory*,
  arXiv:2106.02308. They construct arithmetic analogues of the
  prequantization bundle, quantum Hilbert space, Dijkgraaf--Witten
  partition function, functoriality, decomposition, and gluing for
  finite gauge group and finite prime set \(S\). They explicitly use
  arithmetic Chern--Simons theory with finite gauge group. Source link:
  https://arxiv.org/abs/2106.02308.

- Chung--Kim--Kim--Pappas--Park--Yoo, *Abelian arithmetic
  Chern--Simons theory and arithmetic linking numbers*,
  arXiv:1706.03336. This is the abelian linking-number refinement. It
  supports finite abelian Wilson/linking calculations, not the
  profinite \(GL_2(\widehat{\mathbb Z})\) bulk measure. Source link:
  https://arxiv.org/abs/1706.03336.

## File Anchors

- `chapters/arithmetic/82_3d_acs_E1_ordered_bar.tex:7`: finite ACS is
  theorem-grade; profinite \(GL_2(\widehat{\mathbb Z})\), boundary
  comparison, and zeta partition function remain conditional.
- `chapters/arithmetic/82_3d_acs_E1_ordered_bar.tex:137`: finite-level
  arithmetic state sum and gluing theorem.
- `chapters/arithmetic/82_3d_acs_E1_ordered_bar.tex:262`: target
  profinite conjecture.
- `chapters/arithmetic/82_3d_acs_E1_ordered_bar.tex:294`: status
  remark naming profinite renormalisation and boundary comparison as
  residual.
- `chapters/arithmetic/82_3d_acs_E1_ordered_bar.tex:831`: residual
  obligation for profinite ACS renormalisation.
- `chapters/arithmetic/13_gaiotto_arithmetic_CS.tex:102`: boundary
  shadow is conjectural.
- `chapters/arithmetic/13_gaiotto_arithmetic_CS.tex:120`: Kim is
  classical; quantum boundary category is not constructed there.
- `chapters/arithmetic/11_witten_tqft_triangle.tex:180`: no rigorous
  TQFT bulk for \(\mathcal V^{\mathrm{prim}}\) in the 2026 snapshot.
- `chapters/arithmetic/83_deninger_chiral_homology.tex:165`: no
  unconditional triple identification among Deninger cohomology,
  ordered chiral candidate, and ACS boundary homology.
- `chapters/arithmetic/85_Wilson_line_Frobenius.tex:325`: finite-level
  Wilson--Frobenius identity is unconditional, profinite transport is
  conditional on Chapter 82.

## Claim-Status Recommendation

Do not upgrade
`v4-arith:3d-acs:conj:qu-acs`.

Keep it `Conjectured`. Add, if the manuscript is repaired, a
`ProvedHere` obstruction/partial theorem immediately after the status
remark: finite closed \(GL_2(\mathbb Z/N\mathbb Z)\) ACS over
\(\overline{\mathrm{Spec}\,\mathbb Z}\) is scalar and cannot itself
produce \(\xi(s)\). The profinite ACS theorem must be split into:

1. finite DW/Kim state sums: proved;
2. compatible pro-object over \(N\): formal/proved after level
   compatibility is specified;
3. scalar renormalisation to \(\xi(s)\): conjectural;
4. boundary trace comparison with \(\mathcal V^{\mathrm{prim}}\):
   conditional;
5. Wilson--Frobenius at finite level: proved on the unramified locus;
6. Wilson--Frobenius in the profinite theory: conditional on (3).

## TeX-Ready Repair Text

```tex
\begin{proposition}[finite closed ACS does not produce the zeta character]
\label{v4-arith:3d-acs:prop:closed-finite-tower-obstruction}
\ClaimStatusProvedHere.
Let \(G_N=GL_2(\mathbb Z/N\mathbb Z)\) and let
\(\alpha_N\in H^3(BG_N,\mathbb C^\times)\). For the closed arithmetic
3-space \(M=\overline{\mathrm{Spec}\,\mathbb Z}\), the finite etale
local-system groupoid \(\mathcal F_{G_N}(M)\) is equivalent to \(BG_N\).
Consequently the Kim/Dijkgraaf--Witten finite state sum is
\[
Z^{\mathrm{Ar}}_{G_N,\alpha_N}(M)=|G_N|^{-1}
\]
with the groupoid-cardinality convention, and becomes \(1\) after the
standard finite-gauge normalization. Thus the closed finite-level tower
does not by itself produce a non-constant function of a complex level,
and in particular does not produce \(\xi(s)\). Any zeta-valued
renormalisation must add the prime-indexed Wilson/Hecke data,
the archimedean Tate--Gamma factor, and the polar terms separately.
\end{proposition}

\begin{proof}
By Hermite--Minkowski, a finite extension of \(\mathbb Q\) unramified at
all finite primes has discriminant \(1\), hence is \(\mathbb Q\).
Therefore the finite etale fundamental group of
\(\mathrm{Spec}\,\mathbb Z\) is trivial. A map from the trivial
fundamental group to \(BG_N\) is the trivial \(G_N\)-local system, whose
automorphism group is \(G_N\). The pullback of \(\alpha_N\) to \(B1\)
is trivial, so the action equals \(1\). Groupoid cardinality gives
\(|G_N|^{-1}\). Since this scalar contains no prime-indexed spectral
parameter and no archimedean factor, no canonical inverse limit of these
closed finite sums equals \(\xi(s)\).
\end{proof}
```

## Files Changed

- Created `notes/arithmetic_residue_swarm/01_profinite_acs.md`.

## Commands and Checks Run

- Read `CLAUDE.md` and the inherited invariants/harness instructions.
- Read Chapter 82 and context chapters 11, 13, 81, 83, 85, 88, 90.
- Queried source anchors for Kim 2015, Hirano--Kim--Morishita 2022,
  and Chung--Kim--Kim--Pappas--Park--Yoo 2017.
- No manuscript build run. Assigned output is a standalone markdown
  report and no TeX source was edited.
