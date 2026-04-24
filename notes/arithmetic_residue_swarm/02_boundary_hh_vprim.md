# Agent 2 Report: Boundary ACS Hochschild Trace versus Vprim

Date: 2026-04-24.

Scope: foundational attack on the comparison
`HH(Boundary_ACS) ~= V^{prim}`. Write scope is this note only.

## Verdict

The full boundary comparison does not close as a source-disjoint proof.

The finite arithmetic Chern--Simons boundary category is constructed in
Chapter 82 as twisted sheaves on a finite arithmetic field groupoid. Its
Hochschild homology has a standard finite-groupoid description: twisted
class functions on the inertia groupoid, with no higher Hochschild
homology over `C` in the finite semisimple case. This is the strongest
local finite-level comparison currently justified.

The passage from this finite boundary category to
`\mathcal V^{\mathrm{prim}}` requires a new independent theorem:
the renormalised profinite ACS boundary category must be Morita
equivalent to the global Iwahori Hecke category, compatibly with the
restricted tensor product and archimedean vacuum. That theorem is not
present in Vol IV or in the source volumes. Chapter 82 currently assumes
this comparison as a compact-generation/local-trace hypothesis.

Claim-status recommendation: keep
`v4-arith:3d-acs:thm:bulk-boundary-Vprim` as `ClaimStatusConditional`.
Do not register it as an HZ-IV source-disjoint verification. Split the
finite groupoid Hochschild trace from the profinite ACS-to-Iwahori
comparison, and name the latter as a separate conjectural Morita
equivalence.

## Exact Target Theorem Attacked

Chapter 82 states the target in the following form:

```tex
\begin{theorem}[bulk-boundary comparison with \(\mathcal V^{\mathrm{prim}}\)]
\label{v4-arith:3d-acs:thm:bulk-boundary-Vprim}
\ClaimStatusConditional \emph{(on the renormalised profinite limit in
\Cref{v4-arith:3d-acs:conj:qu-acs} and on the local Satake/Iwahori
trace identifications of Chapters~\ref{v4-arith:tate-tensor} and
\ref{v4-arith:hochschild-trace})}. Let
\[
\mathcal B_{\infty}^{\mathrm{Ar}}
:=\varprojlim_{N}^{\mathrm{ren}}
\mathcal B_{G_{N},\alpha_{N}}(\{\infty\})
\]
be the renormalised archimedean boundary category of the profinite
ACS tower. If its finite-place compact generators identify with the
local Iwahori Hecke generators and its archimedean vacuum sector
identifies with the rank-\(2\) Heisenberg Kac-Moody vacuum, then
\[
\operatorname{HH}_{\bullet}(\mathcal B_{\infty}^{\mathrm{Ar}})
\simeq \mathcal V^{\mathrm{prim}}.
\]
\end{theorem}
```

File anchor:
`chapters/arithmetic/82_3d_acs_E1_ordered_bar.tex:308`.

In minimal mathematical form, the desired theorem is:

```tex
\operatorname{HH}_{\bullet}
\left(\partial\mathrm{ACS}^{\mathrm{qu}}_{k^{\mathrm{Ar}}}\right)
\simeq
\mathcal V^{\mathrm{prim}}
```

where the left side is the Hochschild trace of the quantum arithmetic
Chern--Simons boundary category and the right side is the primitive
adelic Hochschild trace class
`HH_*(Hk^{Iw}_{GL_2,glob})`.

## First-Principles Construction Attempt

### Finite ACS boundary category

Fix a finite group `G`, an arithmetic boundary `Sigma`, and a finite
level `alpha in H^3(BG,C^x)`. Chapter 82 defines

```tex
\mathcal F_G(\Sigma)
= \operatorname{Map}_{\mathrm{cont}}
(\Pi_1^{\mathrm{et}}(\Sigma),BG)
```

and the boundary category

```tex
\mathcal B_{G,\alpha}(\Sigma)
= \operatorname{Sh}_{\tau_\Sigma(\alpha)}(\mathcal F_G(\Sigma)).
```

File anchors:
`chapters/arithmetic/82_3d_acs_E1_ordered_bar.tex:117` and
`chapters/arithmetic/82_3d_acs_E1_ordered_bar.tex:188`.

At this level there is no mystery. Let
`X = \mathcal F_G(\Sigma)` and let `tau` be the transgressed twist.
Because `X` is a finite groupoid, choose representatives for its
components and form the finite-dimensional twisted groupoid algebra
`C_tau[X]`. Then

```tex
\mathcal B_{G,\alpha}(\Sigma) \simeq \operatorname{Perf}(C_\tau[X])
```

up to Morita equivalence. Therefore, by categorical Morita invariance,

```tex
\operatorname{HH}_*(\mathcal B_{G,\alpha}(\Sigma))
\cong \operatorname{HH}_*(C_\tau[X]).
```

The cyclic bar complex of a finite groupoid algebra decomposes over the
inertia groupoid `IX`. With the twist included, the coefficient system is
the transgressed line `L_tau` on `IX`. Over `C`, all automorphism groups
are finite and the twisted groupoid algebra is semisimple. Hence

```tex
\operatorname{HH}_0(\mathcal B_{G,\alpha}(\Sigma))
\cong \Gamma(\pi_0 IX,L_\tau),
\qquad
\operatorname{HH}_{n>0}(\mathcal B_{G,\alpha}(\Sigma))=0.
```

For a one-object finite groupoid `BG`, this recovers twisted class
functions on twisted conjugacy classes. This is the finite-level
boundary-Hochschild statement available from first principles.

### Finite bulk-boundary trace

Chapter 82 also constructs the finite bulk-boundary span: a finite
arithmetic cobordism gives an integral transform between the finite
boundary categories, and for a closed `M` the categorical trace is the
finite arithmetic state sum

```tex
Z^{\mathrm{Ar}}_{G,\alpha}(M)
= \sum_{[\rho]\in\pi_0\mathcal F_G(M)}
  \frac{\langle\rho^*\alpha,[M]\rangle}{|\operatorname{Aut}(\rho)|}.
```

File anchors:
`chapters/arithmetic/82_3d_acs_E1_ordered_bar.tex:137`,
`chapters/arithmetic/82_3d_acs_E1_ordered_bar.tex:204`, and
`chapters/arithmetic/82_3d_acs_E1_ordered_bar.tex:225`.

This finite theorem is an arithmetic Dijkgraaf--Witten/Kim state-sum
statement. It produces finite twisted class-function traces. It does not
produce the primitive adelic object `V^{prim}`.

### Required profinite step

For the target theorem, one must pass from finite groups

```tex
G_N = GL_2(\mathbb Z/N\mathbb Z)
```

to a renormalised boundary category

```tex
\mathcal B_{\infty}^{\mathrm{Ar}}
:=\varprojlim_N^{\mathrm{ren}}
\mathcal B_{G_N,\alpha_N}(\{\infty\}).
```

Chapter 82 explicitly marks this as conditional; it lists the
renormalised profinite limit and the boundary comparison with
`V^{prim}` among the remaining residual obligations. File anchors:
`chapters/arithmetic/82_3d_acs_E1_ordered_bar.tex:262`,
`chapters/arithmetic/82_3d_acs_E1_ordered_bar.tex:294`,
`chapters/arithmetic/82_3d_acs_E1_ordered_bar.tex:819`.

Even if the pro-category exists, the proof still needs an independent
Morita equivalence

```tex
\mathcal B_{\infty}^{\mathrm{Ar}}
\simeq_{\mathrm{Morita}}
\mathsf{Hk}^{Iw}_{GL_2,glob}
```

with finite-place factors matching local Iwahori Hecke categories and
the archimedean factor matching the rank-2 Heisenberg/Kac--Moody vacuum.
This is the missing theorem. Without it, taking Hochschild homology of
the ACS boundary produces a trace of a pro-finite local-system category,
not the trace of the global Iwahori Hecke category.

## Source-Disjointness Audit

The finite statement is source-disjoint. It uses Kim/Dijkgraaf--Witten
finite groupoid state sums and ordinary Hochschild homology of finite
groupoid algebras.

The full comparison is not source-disjoint. The current Chapter 82 proof
says that the compact-generation hypothesis is "exactly the assertion"
that the local factors are the Iwahori Hecke categories used in the
definition of `V^{prim}`. File anchor:
`chapters/arithmetic/82_3d_acs_E1_ordered_bar.tex:332`.

Thus the verification source is not independent from the target source.
It assumes the local ACS boundary factors already have the Iwahori
identity needed to identify the result with `V^{prim}`. A valid HZ-IV
realization would need a different verification path, for example:

```tex
finite ACS boundary categories
  -> renormalised profinite boundary category
  -> independent local ACS-to-Iwahori Morita equivalences
  -> restricted tensor product compatibility
  -> Hochschild trace comparison
```

Only the first arrow is currently theorem-grade.

## Exact Obstructions

1. `Boundary_ACS` is not yet a constructed profinite category.
   Chapter 82 constructs finite boundary categories and states the
   profinite quantum ACS theory as conjectural/conditional. File anchor:
   `chapters/arithmetic/82_3d_acs_E1_ordered_bar.tex:262`.

2. The finite ACS boundary category is a twisted sheaf category on a
   finite etale local-system groupoid. The Iwahori Hecke category is a
   convolution category attached to affine flag/Iwahori geometry. The
   finite-level ACS construction does not produce affine Weyl strata,
   affine flag convolution, or Bezrukavnikov's Iwahori category. File
   anchors:
   `chapters/arithmetic/82_3d_acs_E1_ordered_bar.tex:188`,
   `chapters/arithmetic/14_bezrukavnikov_bernstein_langlands.tex:53`.

3. The restricted tensor product formalism closes only the abstract
   infinity-categorical assembly once the local inputs exist. Chapter 29
   proves the restricted tensor product transport but explicitly does not
   prove the mixed-characteristic local Iwahori input. File anchors:
   `chapters/arithmetic/29_infinity_tate_tensor_product.tex:1`,
   `chapters/arithmetic/29_infinity_tate_tensor_product.tex:930`,
   `chapters/arithmetic/29_infinity_tate_tensor_product.tex:1401`.

4. The identification
   `V^{prim}=HH_*(Hk^{Iw}_{GL_2,glob})` is itself conjectural in
   Chapter 14 and is corrected in Chapter 33 by possible wild-prime
   higher Ext contributions at `p=2,3`. File anchors:
   `chapters/arithmetic/14_bezrukavnikov_bernstein_langlands.tex:104`,
   `chapters/arithmetic/33_bzn_loop_convention_and_wild_primes.tex:932`.

5. The arithmetic BZN trace theorem required for the spectral side is
   not available from the inertia-only `B\hat Z` model. Chapter 28
   requires a full Weil/`(\varphi,\Gamma)` parameter stack. File anchors:
   `chapters/arithmetic/28_arithmetic_ben_zvi_nadler.tex:4`,
   `chapters/arithmetic/28_arithmetic_ben_zvi_nadler.tex:17`.

6. The Vol II and Vol III boundary/bulk sources warn against the
   categorical-level mistake. Boundary category, derived center,
   categorical Hochschild trace, and chiral Hochschild cochains are
   distinct operations. In the HT line, the bulk is a derived center of
   the boundary, not the boundary category itself. File anchors:
   `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_core.tex:111`,
   `/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_hochschild_koszul.tex:8`,
   `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/hochschild_calculus.tex:6`,
   `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:23`.

## Strongest Local Result Actually Proved

The strongest honestly proved comparison is finite and local:

```tex
\operatorname{HH}_0(\mathcal B_{G,\alpha}(\Sigma))
\cong \Gamma(\pi_0 I\mathcal F_G(\Sigma),L_{\tau_\Sigma(\alpha)}),
\qquad
\operatorname{HH}_{n>0}(\mathcal B_{G,\alpha}(\Sigma))=0
```

for finite `G`, finite boundary field groupoid
`\mathcal F_G(\Sigma)`, and coefficients over `C`. The right side is the
space of twisted class functions on the inertia groupoid.

Together with Chapter 82's finite bulk-boundary theorem, this proves that
finite ACS boundary traces are finite twisted class-function traces and
that finite closed cobordism traces recover the finite Kim/DW state sum.
It does not prove any Euler product, archimedean gamma factor, global
Iwahori Hecke trace, or primitive adelic `V^{prim}` comparison.

The nearby unconditional character statement is different: Chapter 45
proves the primitive zeta-character

```tex
\operatorname{ch}(\mathcal V^{\mathrm{prim}})(s)
= \Gamma_{\mathbb R}(s)\zeta(s)=\xi(s)
```

after defining the primary subspace as a restricted tensor product of
one archimedean Gaussian line and one finite single-oscillator primary
per prime. File anchors:
`chapters/arithmetic/45_primitive_zeta_character.tex:32`,
`chapters/arithmetic/45_primitive_zeta_character.tex:430`,
`chapters/arithmetic/45_primitive_zeta_character.tex:507`,
`chapters/arithmetic/45_primitive_zeta_character.tex:556`.

That character theorem is not an ACS boundary-Hochschild theorem.

## Primary-Source Anchors

- Kim 2015 supplies the foundational arithmetic Chern--Simons definition.
  Source catalog anchor:
  `appendices/arithmetic/A_primary_source_catalog.tex:308`.
- Chung--Kim--Kim--Pappas--Park--Yoo 2017 supplies the abelian arithmetic
  CS/linking setting used by the Gaiotto chapter. Source catalog anchor:
  `appendices/arithmetic/A_primary_source_catalog.tex:310`.
- Morishita 2009 supplies the primes/knots and number rings/3-manifolds
  dictionary. Source catalog anchor:
  `appendices/arithmetic/A_primary_source_catalog.tex:313`.
- Costello--Gwilliam and Costello--Gaiotto are the relevant
  factorization/boundary field-theory sources. Source catalog anchors:
  `appendices/arithmetic/A_primary_source_catalog.tex:181` and
  `appendices/arithmetic/A_primary_source_catalog.tex:189`.
- Bezrukavnikov 2016 is the Iwahori Hecke-category source. Source catalog
  anchor:
  `appendices/arithmetic/A_primary_source_catalog.tex:211`.
- Ben-Zvi--Nadler 2009 is the complex-group Hochschild trace/character
  theory source, not an arithmetic proof over `Spec Z`. Source catalog
  anchor:
  `appendices/arithmetic/A_primary_source_catalog.tex:215`.

## File Anchors

- Finite field groupoid and finite ACS state sum:
  `chapters/arithmetic/82_3d_acs_E1_ordered_bar.tex:117`,
  `chapters/arithmetic/82_3d_acs_E1_ordered_bar.tex:137`.
- Finite boundary category and finite bulk-boundary theorem:
  `chapters/arithmetic/82_3d_acs_E1_ordered_bar.tex:188`,
  `chapters/arithmetic/82_3d_acs_E1_ordered_bar.tex:204`.
- Profinite ACS conjecture and boundary comparison:
  `chapters/arithmetic/82_3d_acs_E1_ordered_bar.tex:262`,
  `chapters/arithmetic/82_3d_acs_E1_ordered_bar.tex:308`.
- Residual obligations:
  `chapters/arithmetic/82_3d_acs_E1_ordered_bar.tex:819`.
- Early ACS/`V^{prim}` caution:
  `chapters/arithmetic/13_gaiotto_arithmetic_CS.tex:4`,
  `chapters/arithmetic/13_gaiotto_arithmetic_CS.tex:99`.
- Iwahori/`V^{prim}` definition:
  `chapters/arithmetic/14_bezrukavnikov_bernstein_langlands.tex:65`,
  `chapters/arithmetic/14_bezrukavnikov_bernstein_langlands.tex:104`.
- Arithmetic BZN obstruction:
  `chapters/arithmetic/28_arithmetic_ben_zvi_nadler.tex:4`,
  `chapters/arithmetic/28_arithmetic_ben_zvi_nadler.tex:17`.
- Restricted tensor product theorem and remaining local input:
  `chapters/arithmetic/29_infinity_tate_tensor_product.tex:84`,
  `chapters/arithmetic/29_infinity_tate_tensor_product.tex:930`.
- Wild-prime correction:
  `chapters/arithmetic/33_bzn_loop_convention_and_wild_primes.tex:932`.
- Vol II/III categorical-level discipline:
  `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_core.tex:111`,
  `/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/sc_chtop_heptagon.tex:87`,
  `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/hochschild_calculus.tex:32`,
  `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:103`.

## TeX-Ready Repair Text

Recommended insertion after the finite boundary category definition:

```tex
\begin{proposition}[finite boundary Hochschild trace]
\label{v4-arith:3d-acs:prop:finite-boundary-HH}
\ClaimStatusProvedElsewhere. Let \(G\) be finite, let
\(\alpha\in H^3(BG,\mathbb C^\times)\), and let
\(\Sigma\) be an arithmetic boundary for which
\(\mathcal F_G(\Sigma)\) is a finite groupoid. Put
\[
\mathcal B_{G,\alpha}(\Sigma)
=\operatorname{Sh}_{\tau_\Sigma(\alpha)}(\mathcal F_G(\Sigma)).
\]
Let \(I\mathcal F_G(\Sigma)\) be the inertia groupoid and let
\(L_{\tau_\Sigma(\alpha)}\) be the transgressed twisting line on it.
Then, over \(\mathbb C\),
\[
\operatorname{HH}_0(\mathcal B_{G,\alpha}(\Sigma))
\cong
\Gamma(\pi_0 I\mathcal F_G(\Sigma),L_{\tau_\Sigma(\alpha)}),
\qquad
\operatorname{HH}_{n>0}(\mathcal B_{G,\alpha}(\Sigma))=0.
\]
\end{proposition}

\begin{proof}
Choose a finite twisted groupoid algebra representing
\(\operatorname{Sh}_{\tau_\Sigma(\alpha)}(\mathcal F_G(\Sigma))\).
Categorical Hochschild homology is Morita invariant. The cyclic bar
complex of a finite twisted groupoid algebra is the homology of the
inertia groupoid with coefficients in the transgressed twisting line.
Since the automorphism groups are finite and the ground field is
\(\mathbb C\), the algebra is semisimple and the higher homology
vanishes.
\end{proof}
```

Recommended replacement for the current proof paragraph of
`v4-arith:3d-acs:thm:bulk-boundary-Vprim`:

```tex
\begin{proof}
The finite boundary categories of
\Cref{v4-arith:3d-acs:def:finite-boundary-category} have Hochschild
traces described by twisted inertia class functions; by themselves they
do not identify with local Iwahori Hecke traces. The displayed
equivalence therefore follows only after imposing an independent
Morita equivalence
\[
\mathcal B_{\infty}^{\mathrm{Ar}}
\simeq_{\mathrm{Morita}}
\mathsf{Hk}^{Iw}_{GL_2,\mathrm{glob}},
\]
compatible with the restricted tensor product, spherical units, and the
archimedean vacuum. Under this added hypothesis, Morita invariance of
Hochschild homology and the restricted tensor product theorem of
Chapter~\ref{v4-arith:tate-tensor} identify
\(\operatorname{HH}_\bullet(\mathcal B_\infty^{\mathrm{Ar}})\) with
\(\operatorname{HH}_\bullet(\mathsf{Hk}^{Iw}_{GL_2,\mathrm{glob}})\).
The latter is the defining Hochschild-trace candidate for
\(\mathcal V^{\mathrm{prim}}\), subject to the arithmetic BZN and
wild-prime hypotheses recorded in
Chapters~\ref{v4-arith:hochschild-trace},
\ref{v4-arith:arithmetic-bzn}, and
\ref{v4-arith:bzn-loop-convention-wild-primes}. This proves only the
conditional implication, not the ACS-to-Iwahori comparison itself.
\end{proof}
```

## Files Changed

- Created this report:
  `notes/arithmetic_residue_swarm/02_boundary_hh_vprim.md`.

No manuscript files were edited.

## Commands and Tests

Commands run for source loading and verification included `sed`, `nl`,
`rg`, `find`, `ls`, and `git status --short` over the Vol IV files,
the inherited ecosystem instructions, and the relevant Vol I/II/III
source chapters.

No TeX build, Python tests, or compute tests were run. This was a
note-only edit.
