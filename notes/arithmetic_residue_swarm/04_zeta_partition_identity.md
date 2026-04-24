# Agent 4 Report: Zeta Partition Identity for Arithmetic Chern-Simons

## Verdict

The arithmetic Chern-Simons zeta partition identity does not close as a
first-principles theorem beyond finite-level TQFT trace formalism.

The theorem-grade content is:

1. finite arithmetic Chern-Simons state sums over finite field groupoids;
2. the Bost-Connes KMS partition function `Z_BC(beta)=zeta(beta)` for
   `Re beta > 1`, with meromorphic continuation inherited from zeta;
3. the finite-place primitive character
   `prod_p (1-p^{-s})^{-1}=zeta(s)`;
4. the completed primitive character
   `Gamma_R(s) zeta(s)=xi(s)`.

What is not theorem-grade is the promotion of these character identities
to the scalar partition function of a renormalised profinite arithmetic
Chern-Simons theory on `overline{Spec Z}`.

Claim-status recommendation: keep the arithmetic Chern-Simons partition
identity at `ClaimStatusConjectured` or `ClaimStatusConditional`. Do not
mark it `ClaimStatusProvedHere`.

## Exact Target Theorem Attacked

The target theorem would need the following form.

Let `M=overline{Spec Z}` be the arithmetic three-space. Let
`G_N=GL_2(Z/NZ)`, and let `alpha_N` be a compatible finite-level
arithmetic Chern-Simons cocycle system. For each `N`, define the finite
state sum

```text
Z^{Ar}_{G_N,alpha_N}(M)
  = sum_[rho in F_{G_N}(M)] <rho^* alpha_N,[M]> / |Aut(rho)|.
```

The claimed zeta partition identity asserts that there is a canonical
renormalised profinite limit and a scalar partition function

```text
Z_ACS^qu(M;s) = lim_N^ren Z^{Ar}_{G_N,alpha_N}(M;s)
```

such that

```text
Z_ACS^qu(overline{Spec Z};s) = xi(s),
```

where the Vol IV primitive-character notation is
`xi(s)=Gamma_R(s) zeta(s)`. If the Deninger determinant form is meant,
the target is instead the entire completed function
`xi_R(s)=1/2 s(s-1) Gamma_R(s) zeta(s)`. These two normalisations must
not be interchanged.

A finite-place weakening would assert only

```text
Z_ACS,fin^qu(s) = zeta(s).
```

This weaker identity also does not follow from finite arithmetic
Chern-Simons state sums. It is proved for Bost-Connes zero modes and for
the primitive finite-place character, not for an arithmetic
Chern-Simons bulk partition.

## First-Principles Partition Construction

Kim's arithmetic Chern-Simons input gives a finite-level construction.
For a finite group `G`, an arithmetic three-space `M`, and a cocycle
`alpha`, the field object is the finite groupoid

```text
F_G(M) = Map(pi_1(M),G)//G.
```

The arithmetic action is the transgressed class

```text
S_alpha^{Ar}(rho) = <rho^* alpha,[M]>.
```

The finite groupoid integral is

```text
Z^{Ar}_{G,alpha}(M)
  = integral_{F_G(M)} S_alpha^{Ar}
  = sum_[rho] <rho^* alpha,[M]> / |Aut(rho)|.
```

This construction is honest and local at finite level. It is a finite
sum over representations, with the automorphism denominator coming from
groupoid cardinality. Gluing follows from finite groupoid Fubini under
the etale descent hypotheses imposed in Chapter 82.

This construction by itself has no Euler product over primes, no
archimedean Gaussian factor, and no polar Tate factor. Those enter
through Bost-Connes zero modes, the primitive zeta character, and Tate
normalisation, not through the finite state sum formula.

## What Actually Closes

### Finite Arithmetic Chern-Simons

Chapter 82 proves the closed finite-level state sum:

```text
Z^{Ar}_{G,alpha}(M)
  = sum_[rho] <rho^* alpha,[M]> / |Aut(rho)|.
```

This is a finite arithmetic TQFT trace identity when the finite
cobordism category and descent hypotheses are fixed. It is not a zeta
identity.

### Bost-Connes and KMS Euler Product

The Bost-Connes Hamiltonian has eigenvalues `log n` on the standard
representation. Hence

```text
Tr(e^{-beta H}) = sum_{n>=1} n^{-beta} = zeta(beta),
Re beta > 1.
```

Equivalently, in the prime zero-mode factorisation,

```text
Tr(e^{-s N_BC} | A_fin)
  = prod_p sum_{r>=0} p^{-rs}
  = prod_p (1-p^{-s})^{-1}
  = zeta(s).
```

This is a KMS and Euler-product theorem. It is not a construction of a
profinite arithmetic Chern-Simons partition function.

### Primitive Zeta Character

The primitive finite-place character closes as

```text
ch_fin V_prim(s) = prod_p (1-p^{-s})^{-1} = zeta(s).
```

The archimedean Gaussian primary sector closes as

```text
ch_infty V_prim(s) = Gamma_R(s).
```

Together they give the theorem-grade character identity

```text
ch V_prim(s) = Gamma_R(s) zeta(s) = xi(s).
```

This is a character theorem for the primitive sector. It does not become
an arithmetic Chern-Simons partition theorem until a boundary comparison
and a scalar regularised character map are constructed.

## What Does Not Close

The following conversion is the missing step:

```text
finite ACS state sums
  -> renormalised profinite ACS theory
  -> boundary theory identified with V_prim
  -> regularised scalar character
  -> xi(s).
```

Each arrow contains an open mathematical obligation.

1. The tower `G_N=GL_2(Z/NZ)` has no canonical renormalised inverse-limit
   partition measure in the current text.
2. The finite arithmetic boundary categories have not been promoted to a
   profinite quantum arithmetic Chern-Simons boundary theory.
3. The boundary object has not been identified with `V^{prim}` by a
   local trace comparison.
4. The ordered incidence bar model has not been identified with
   Beilinson-Drinfeld or Costello-Gwilliam chiral homology in the
   required arithmetic setting.
5. The map from the homology object to a scalar partition function is
   still a regularised character hypothesis.
6. The archimedean `Gamma_R(s)` and polar Tate lines do not arise from
   the finite state sum.
7. The Deninger zero-side determinant requires an `R_+^x` spectral flow
   whose regularised determinant is `xi_R(s)`. The Bost-Connes heat flow
   gives prime lengths and the Euler product, not the zero spectrum.

## Exact Renormalisation Gap

The gap is not a minor normalisation issue. A proof would need to specify
all of the following data and verify compatibility:

```text
(a) a profinite measure or counterterm system on the tower G_N;
(b) compatibility of the Kim cocycles alpha_N under level change;
(c) convergence or determinant-class renormalisation of the resulting trace;
(d) boundary gluing identifying the limit boundary category with V^{prim};
(e) a scalar character map from arithmetic chiral homology to C;
(f) Tate archimedean and polar normalisations;
(g) compatibility with the Weil-Guinand or Deninger trace formula.
```

Without `(a)-(g)`, the expression `Z_ACS^qu=xi(s)` is a conditional
synthesis statement. The proved identities are KMS, Euler-product, and
primitive-character identities living on adjacent structures.

## Finite-Level and Euler-Product Identities Isolated

The strongest honestly proved statements are the following.

```text
Finite ACS:
Z^{Ar}_{G,alpha}(M)
  = sum_[rho] <rho^* alpha,[M]> / |Aut(rho)|.
```

```text
Finite BC/KMS:
Z_BC(beta)
  = Tr(e^{-beta H})
  = sum_{n>=1} n^{-beta}
  = zeta(beta),
  Re beta > 1.
```

```text
Prime skeleton:
Tr(e^{-s N_BC} | A_fin)
  = prod_p (1-p^{-s})^{-1}
  = zeta(s),
  Re s > 1.
```

```text
Primitive completed character:
ch V_prim(s)
  = Gamma_R(s) zeta(s)
  = xi(s).
```

These can be cited as proved components. They should not be cited as a
proof of the arithmetic Chern-Simons partition identity.

## Primary-Source Anchors

Primary mathematical sources used by the local text:

1. M. Kim, "Arithmetic Chern-Simons Theory I", arXiv:1510.05818.
   Source of the arithmetic Chern-Simons action and finite classical
   partition formalism.
2. J.-B. Bost and A. Connes, "Hecke algebras, type III factors and phase
   transitions with spontaneous symmetry breaking in number theory",
   Selecta Mathematica 1 (1995), 411-457. Source of the Bost-Connes
   system and `zeta(beta)` KMS partition.
3. B. Julia, "Statistical theory of numbers", source for the primon gas
   interpretation of `zeta(beta)`.
4. J. Tate, "Fourier Analysis in Number Fields and Hecke's Zeta
   Functions", source of `Gamma_R(s)`, adelic Poisson summation, and the
   completed zeta functional equation.
5. A. Connes, C. Consani, and C. Deninger sources as catalogued in
   Vol IV, for the spectral-flow and trace-formula obstruction. These do
   not supply an unconditional Hilbert-Polya operator.

## Local File Anchors

Main Vol IV anchors:

1. `chapters/arithmetic/82_3d_acs_E1_ordered_bar.tex:51-62`: Kim
   classical arithmetic Chern-Simons action and partition sum.
2. `chapters/arithmetic/82_3d_acs_E1_ordered_bar.tex:137-186`:
   theorem-grade finite arithmetic state sum.
3. `chapters/arithmetic/82_3d_acs_E1_ordered_bar.tex:262-292`:
   conjectural profinite quantum ACS package and `Z=xi(k^Ar)` axiom.
4. `chapters/arithmetic/82_3d_acs_E1_ordered_bar.tex:494-514`:
   conditional ordered-bar partition corollary and missing scalar
   character conversion.
5. `chapters/arithmetic/82_3d_acs_E1_ordered_bar.tex:598-626`:
   proved BC prime-side Euler product `zeta(s)`.
6. `chapters/arithmetic/82_3d_acs_E1_ordered_bar.tex:628-638`:
   trace-formula normalisation warning.
7. `chapters/arithmetic/82_3d_acs_E1_ordered_bar.tex:640-675`:
   Deninger spectral-flow hypothesis.
8. `chapters/arithmetic/82_3d_acs_E1_ordered_bar.tex:703-728`:
   proved Deninger gap proposition.
9. `chapters/arithmetic/82_3d_acs_E1_ordered_bar.tex:819-870`:
   residual obligations and summary of closed components.

Adjacent Vol IV anchors:

1. `chapters/arithmetic/05_connes_soibelman_bost_connes.tex:41-53`:
   Bost-Connes KMS partition `zeta(beta)`.
2. `chapters/arithmetic/11_witten_tqft_triangle.tex:73-100` and
   `180-189`: no finite-level CS boundary construction currently
   delivers `V^{prim}` as a rigorous arithmetic TQFT boundary.
3. `chapters/arithmetic/13_gaiotto_arithmetic_CS.tex:102-139`:
   conjectural arithmetic CS boundary character statements.
4. `chapters/arithmetic/45_primitive_zeta_character.tex:507-609`:
   finite-place, archimedean, and completed primitive zeta character
   theorems.
5. `chapters/arithmetic/45_primitive_zeta_character.tex:650-677`:
   BC partition on the primitive sector.
6. `chapters/arithmetic/46_KMS_GNS_full_sector.tex:381-525`:
   KMS1/GNS identification.
7. `chapters/arithmetic/46_KMS_GNS_full_sector.tex:968-1030`:
   Eisenstein continuum mismatch, showing another place where scalar
   character comparison is not automatic.
8. `chapters/arithmetic/68_compute_engine_verification.tex:332-349`:
   compute verification coverage, not including ACS partition equality.
9. `compute/tests/test_wave5_verification.py`: numerical constant
   checks only; no ACS zeta partition decorator.
10. `appendices/arithmetic/A_primary_source_catalog.tex:71-86`,
   `304-330`, `390-397`, `535-540`, `636-646`: BC, Kim, Julia, Tate,
   Riemann, Connes-Deninger source catalogue entries.

Home-volume anchors:

1. `../chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:172-190`:
   spectral zeta and eta-function shadows, not an ACS partition proof.
2. `../chiral-bar-cobar/compute/lib/chern_simons_barcobar.py`: ordinary
   finite-level Chern-Simons/WZW computations, not arithmetic ACS.
3. `../chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:75-96`:
   ordinary CS and 3D gravity trace formalism, not an arithmetic zeta
   partition construction.

## TeX-Ready Repair Text

```tex
\begin{remark}[Status of the arithmetic Chern--Simons zeta partition]
The finite arithmetic Chern--Simons construction gives an honest
finite groupoid state sum
\[
  Z^{\mathrm{Ar}}_{G,\alpha}(M)
  =
  \sum_{[\rho]\in \pi_0\mathcal F_G(M)}
  \frac{\langle \rho^*\alpha,[M]\rangle}{|\operatorname{Aut}(\rho)|}.
\]
This theorem does not identify the finite state sum, or a tower of such
state sums, with an Euler product. The Euler product
\[
  \prod_p (1-p^{-s})^{-1}=\zeta(s)
\]
is proved on the Bost--Connes zero-mode side and on the finite-place
primitive character side. The completed identity
\[
  \Gamma_{\mathbb R}(s)\zeta(s)=\xi(s)
\]
is proved as the primitive zeta-character identity after adjoining the
Tate archimedean factor.

Promoting these character identities to the scalar partition function
of a quantum arithmetic Chern--Simons theory on
\(\overline{\operatorname{Spec}\mathbb Z}\) remains conditional. It
requires a renormalised profinite limit of the finite
\(GL_2(\mathbb Z/N\mathbb Z)\) state sums, a boundary comparison with
\(\mathcal V^{\mathrm{prim}}\), the ordered-bar to chiral-homology
comparison, a regularised scalar character map, and the Tate polar and
archimedean normalisations. If the Deninger determinant
\(\xi_{\mathbb R}(s)\) is intended, one also needs the independent
\(\mathbb R_+^\times\)-spectral-flow package whose determinant and
trace formula produce the zeta-zero side.
\end{remark}
```

## Files Changed

Created:

```text
notes/arithmetic_residue_swarm/04_zeta_partition_identity.md
```

No manuscript files were edited.

## Commands and Tests Run

Context commands:

```text
sed / nl reads of CLAUDE.md, AGENTS.md, ecosystem invariants and harness
rg searches over arithmetic ACS, Bost-Connes, KMS, primitive zeta, Kim,
chapter 82, compute verification, and source-volume trace material
nl reads of the local file anchors listed above
web source checks for Kim arXiv:1510.05818 and Bost-Connes arXiv:hep-th/9411174
mkdir -p notes/arithmetic_residue_swarm
apply_patch add/update of this report only
rg hygiene scan for banned prose tokens, attribution tokens, dash characters, and typo guards
wc -l and git status check on this report
```

Tests:

```text
No pytest or pdflatex run. This was a note-only attack report with no
compute, registry, or manuscript edits.
```
