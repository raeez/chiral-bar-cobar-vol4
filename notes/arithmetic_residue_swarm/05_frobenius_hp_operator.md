# Agent 5 Report: Frobenius Flow and Hilbert--Polya Operator

Date: 2026-04-24

Scope: arithmetic Frobenius-flow / Hilbert--Polya operator package for the
arithmetic residue swarm.  This note attacks the cohomology, generator,
determinant, trace formula, and unitarity/positivity claims.  No manuscript
file was edited.

## Verdict

The package is not closed.  The repository contains a theorem-grade
BC/KMS/GNS skeleton and finite-prime Euler/Wilson trace evidence, plus
conditional determinant and trace consequences after a zero-spectrum
Hilbert--Polya twist is assumed.  It does not contain a non-tautological
construction of the middle cohomology carrying a self-adjoint operator whose
spectrum is the ordinates of zeta zeros.

Recommended status:

- BC/KMS zero-mode skeleton and `N_{BC}`: `ProvedHere`.
- finite unramified Wilson/Frobenius traces: theorem-grade only at the
  finite-level unramified locus, with the stated profinite and ramified
  conditionals.
- Deninger cohomology, global Frobenius flow, determinant realization,
  trace formula as an operator trace, and Hilbert--Polya positivity:
  `TheoremWaiting` or `Conditional`.
- Any assertion that a self-adjoint `H_{HP}` has been constructed from the
  existing BC, bar, Wilson, or chiral data must be rejected unless the
  spectral-flow residual below is supplied.

## Exact Target Theorem Statement

The target theorem is the following package.

```tex
\begin{theorem}[Arithmetic Frobenius-flow / Hilbert--Polya package]
There are topological cohomology groups
\[
  H^i_{\mathrm{ar}}(\overline{\operatorname{Spec}\mathbb Z})
  \qquad (i=0,1,2)
\]
and a strongly continuous Frobenius flow
\(\phi^t\) with infinitesimal generator \(\Theta\) such that:
\[
  H^0_{\mathrm{ar}}\simeq \mathbb Q(0),\qquad
  H^2_{\mathrm{ar}}\simeq \mathbb Q(1),
\]
the middle space \(H^1_{\mathrm{ar}}\) has a Hilbert completion
\(\mathcal H_\xi\), and
\[
  \Theta_\xi=\frac{1}{2}I+iH_{HP}
\]
for a self-adjoint operator \(H_{HP}\) on \(\mathcal H_\xi\).  The spectrum
of \(H_{HP}\), with multiplicities, is the multiset of ordinates
\(\gamma\) of non-trivial zeros \(\rho=\frac12+i\gamma\) of \(\xi_{\mathbb R}\).
The regularized determinant and test-function trace satisfy
\[
  \det\nolimits_\infty(sI-\Theta_\xi\mid H^1_{\mathrm{ar}})
    = \xi_{\mathbb R}(s)
\]
up to the Tate-line factors in degrees \(0\) and \(2\), and
\[
  \operatorname{Tr}_{\mathrm{reg}}(h(H_{HP}))
    = \sum_\rho h(\gamma_\rho)
\]
with the right side identified with the Weil--Guinand prime/archimedean
explicit formula.  The Hilbert form is positive, and the induced trace
pairing is positive on the full Weil test cone.
\end{theorem}
```

This is exactly the missing Hilbert--Polya/Deninger package.  It is not a
consequence of the currently proved arithmetic residue material.

## Candidate Cohomology

The surviving cohomological object is only a candidate.  The local file
`chapters/arithmetic/83_deninger_chiral_homology.tex` defines an ordered
incidence/chiral candidate \(H^\bullet_{\Delta,\chi}\), with completed duals
and formal Tate polar lines in degrees \(0\) and \(2\).  Its own status text
says this is not Deninger cohomology: the middle cohomology and trace package
require a spectral-flow hypothesis.

The usable definitions are:

- finite Euler operators \(F_p^{\mathrm{Euler}}=\psi_p\) on the local
  ordered/bar skeleton;
- formal Tate lines \(H^0\simeq \mathbb Q(0)\) and
  \(H^2\simeq \mathbb Q(1)\);
- a middle candidate \(H^1_{\Delta,\chi}\), not yet identified with a
  Hilbert space carrying zeta-zero spectral data.

This is enough for a bookkeeping dictionary, not enough for a Deninger
cohomology theorem.

## Generators

There are three distinct generators, and collapsing them is the main false
move to avoid.

1. `N_{BC}`.  The BC/KMS/GNS construction gives a canonical positive
   self-adjoint number operator
   \[
     N_{BC}=-\frac12\log\Delta_1,
     \qquad N_{BC}\delta_m=(\log m)\delta_m,
   \]
   with spectrum \(\{\log m:m\in\mathbb N^\times\}\).  This is a theorem-grade
   logarithmic prime/power skeleton, not a zeta-zero operator.

2. Archimedean scaling.  The archimedean Wilson-surface chapter constructs
   an Arakelov scaling generator \(\widehat D=-i\partial_\lambda|_{\lambda=1}\)
   and \(F_\infty=\exp(-\widehat D)\).  Mellin conjugacy to multiplication by
   \(s-\frac12\), and any identification with a primary Virasoro generator,
   are conditional on the stated quantum ACS and primary-Virasoro hypotheses.

3. `Theta_xi`.  The target zero generator is
   \[
     \Theta_\xi=\frac12I+iH_{HP}.
   \]
   A formal diagonal operator on a vector space indexed by zeros is tautological.
   A valid theorem needs an independently constructed Hilbert space, a dense
   invariant core, self-adjointness of \(H_{HP}\), and spectral equality with
   the zero ordinates.

The present corpus proves (1), gives conditional structure for (2), and leaves
(3) as the Hilbert--Polya input.

## Determinant Attempt

The determinant identity is conditional.  If one assumes a Hilbert space
\(\mathcal H_\xi\), a self-adjoint \(H_{HP}\), and
\(\operatorname{Spec}(H_{HP})=\{\gamma_\rho\}\) with multiplicities, then
Hadamard factorization gives
\[
  \det\nolimits_\infty(sI-\Theta_\xi)=\xi_{\mathbb R}(s)
\]
after the standard regularization and Tate-line accounting.  This is a
consequence of the assumed spectrum, not a construction of it.

The determinant notes explicitly warn that a Deninger determinant formula
requires all of: a cohomological space, a densely defined operator, spectral
theory, a regularized determinant, and a trace formula.  The current arithmetic
branch has the BC log-modular operator but not the middle zero operator.

## Trace Formula Attempt

There are two trace formulas in play.

The classical Weil--Guinand explicit formula gives a distributional equality
between a zero sum and the prime plus archimedean side.  The repository
records this formula and uses it as the target trace identity.

The operator trace formula
\[
  \operatorname{Tr}_{\mathrm{reg}}(h(H_{HP}))
    =\sum_\rho h(\gamma_\rho)
\]
is conditional on the same Hilbert--Polya operator.  Connes--Meyer style
formulations give distributional trace realizations, but the local chapters
do not produce a positive Hilbert-space operator with this spectrum from the
BC/bar/Wilson skeleton.  The spectral-flow chapter identifies the missing step
as an operatorial lift of the Mellin-Hadamard distributional duality.

## Unitarity and Positivity

The KMS/GNS Hilbert space is positive and the modular operator is positive
self-adjoint.  This proves positivity for the BC skeleton, not for the zero
side.

Prime-side positivity is proved only in restricted or conditional forms:
the Petersson/Rankin--Selberg argument controls the tempered cuspidal prime
side, and some Tate-Mellin subclasses close.  The full archimedean term is not
absorbed by the positive form.  The arithmetic Tate-positivity condition
(A-TP), full HP-Li positivity, scattering unitarity on the full positive cone,
and Weil positivity are recorded in the local chapters as RH-equivalent
within the framework.

Thus unitarity/positivity is not an independent proof of RH here.  It is the
same residual content in another language.

## Exact Obstruction

The obstruction is not notation.  It is the construction of a non-formal
spectral-flow operator package:
\[
  (\mathcal H_\xi,\mathcal D,H_{HP},A)
\]
where \(\mathcal H_\xi\) is a Hilbert completion of the middle arithmetic
cohomology, \(\mathcal D\) is a dense invariant core, \(H_{HP}\) is
self-adjoint, and \(A\) is a closed intertwiner from the BC/logarithmic
skeleton to the zero side satisfying the required determinant and trace
identities.  The formal Mellin-Hadamard transform is not an operator without
domain, codomain, and closability.  The atomic BC Hilbert space does not
automatically embed by Mellin transform into the zero-side \(L^2\) space.
The formal symmetric intertwining construction assumes critical-line zeros
if used as a self-adjoint multiplication model.

The sharp repair route already isolated in the corpus is the Dirac two-test:
construct the residual symmetric ordinate core \(H_0\), prove
\[
  \ker(H_0^*-i)=\ker(H_0^*+i)=0,
\]
then prove the determinant identity for the self-adjoint closure.  Until those
two tests are passed, the Frobenius-flow / Hilbert--Polya package remains
open.

## Primary-Source and File Anchors

Primary-source catalog:

- `appendices/arithmetic/A_primary_source_catalog.tex:71`: Bost--Connes and
  Connes--Marcolli references for the BC system.
- `appendices/arithmetic/A_primary_source_catalog.tex:442`: Deninger on
  motivic \(L\)-functions and regularized determinants.
- `appendices/arithmetic/A_primary_source_catalog.tex:531`: Riemann,
  von Mangoldt, Weil, and Li references.
- `appendices/arithmetic/A_primary_source_catalog.tex:607`: operator-theory
  sources and the warning that zero spectral matching is genuine
  Hilbert--Polya content.

Local file anchors:

- `chapters/arithmetic/05_connes_soibelman_bost_connes.tex:16`: BC algebra
  generators and relations.
- `chapters/arithmetic/05_connes_soibelman_bost_connes.tex:41`: BC partition
  function \(Z_{BC}(\beta)=\zeta(\beta)\).
- `chapters/arithmetic/05_connes_soibelman_bost_connes.tex:80`: zero-mode
  lattice \(\ell^2(\mathbb N^\times)\).
- `chapters/arithmetic/23_rh_reformulation.tex:111`: H-P\({}^{Ar}\)
  hypothesis and \(\Theta_\xi=\frac12I+iH_{HP}\).
- `chapters/arithmetic/23_rh_reformulation.tex:146`: H-P\({}^{Ar}\) is
  independent input, not derived from P1--P3.
- `chapters/arithmetic/36_HPAr_and_VBstar_converse.tex:49`: earlier
  moment/operator errors and domain warning.
- `chapters/arithmetic/36_HPAr_and_VBstar_converse.tex:292`: necessary and
  sufficient spectral realization condition.
- `chapters/arithmetic/36_HPAr_and_VBstar_converse.tex:1360`: residual
  conditions for BC trace compatibility, Connes absorption, Deninger spectrum,
  and determinacy.
- `chapters/arithmetic/45_primitive_zeta_character.tex:32`: primitive
  zeta-character theorem at character level.
- `chapters/arithmetic/45_primitive_zeta_character.tex:582`: adelic
  primary character \(\xi(s)\).
- `chapters/arithmetic/46_KMS_GNS_full_sector.tex:347`: GNS modular operator
  and its positive self-adjointness.
- `chapters/arithmetic/56_hp_ar_operator_construction.tex:122`: BC GNS
  Hilbert space.
- `chapters/arithmetic/56_hp_ar_operator_construction.tex:169`: definition
  of \(N_{BC}\).
- `chapters/arithmetic/56_hp_ar_operator_construction.tex:380`: H-P\({}^{Ar}\)
  twist hypothesis.
- `chapters/arithmetic/56_hp_ar_operator_construction.tex:417`: determinant
  identity conditional on the twist.
- `chapters/arithmetic/56_hp_ar_operator_construction.tex:489`: trace
  identity conditional on the twist.
- `chapters/arithmetic/56_hp_ar_operator_construction.tex:600`: precise
  obstruction theorem.
- `chapters/arithmetic/57_hp_li_positivity_closure.tex:440`: archimedean
  Weil/Tate positivity obstruction.
- `chapters/arithmetic/57_hp_li_positivity_closure.tex:639`: A-TP equivalent
  to Weil positivity and RH inside the framework.
- `chapters/arithmetic/80_ATP_adelic_scattering.tex:373`: scattering
  unitarity equivalent to A-TP on the positive cone.
- `chapters/arithmetic/83_deninger_chiral_homology.tex:16`: Deninger wish
  list.
- `chapters/arithmetic/83_deninger_chiral_homology.tex:90`: chiral candidate
  cohomology.
- `chapters/arithmetic/83_deninger_chiral_homology.tex:323`: middle
  cohomology and Hilbert--Polya operator are precisely the missing part.
- `chapters/arithmetic/84_trace_formula_equivalence_gutzwiller.tex:16`:
  Weil--Guinand target trace formula.
- `chapters/arithmetic/84_trace_formula_equivalence_gutzwiller.tex:154`:
  no independent zero locator or self-adjoint operator from the bar skeleton.
- `chapters/arithmetic/85_Wilson_line_Frobenius.tex:325`: finite-level
  Wilson line equals Frobenius trace on the unramified locus.
- `chapters/arithmetic/85_Wilson_line_Frobenius.tex:657`: global Deninger
  flow and zero-side operator remain residual.
- `chapters/arithmetic/87_HPAr_spectral_flow.tex:32`: BC operator
  \(N_{BC}\) has log-prime/power spectrum.
- `chapters/arithmetic/87_HPAr_spectral_flow.tex:70`: formal diagonal
  zero operator is tautological.
- `chapters/arithmetic/87_HPAr_spectral_flow.tex:130`: spectral-flow
  problem.
- `chapters/arithmetic/87_HPAr_spectral_flow.tex:301`: symbolic
  Mellin-Hadamard intertwiner is not an operator.
- `chapters/arithmetic/87_HPAr_spectral_flow.tex:1081`: H-P\({}^{Ar}\),
  Connes absorption, Meyer spectral matching, A-TP, and Deninger spectral-flow
  are equivalent residuals within the framework.
- `chapters/arithmetic/87_HPAr_spectral_flow.tex:1449`: Dirac two-test.
- `chapters/arithmetic/90_archimedean_Wilson_surface.tex:291`:
  archimedean Frobenius \(F_\infty=\exp(-\widehat D)\).
- `chapters/arithmetic/90_archimedean_Wilson_surface.tex:533`: the
  archimedean generator, Virasoro generator, and Hilbert--Polya generator
  remain distinct.
- `determinant_of_an_operator.tex:851`: determinant identity warning.
- `determinant_of_an_operator.tex:1168`: Deninger-type determinant target.
- `determinant_of_an_operator.tex:1455`: required data for an arithmetic
  determinant formula.

Adjacent-file check:

- `../igusa-cusp-form/standalone/determinant_of_an_operator.tex` and
  `../topological-strings/standalone/determinant_of_an_operator.tex` contain
  the same determinant warnings at the corresponding standalone anchors.

## TeX-Ready Repair Text

The following replacement text is safe to use where a closed Frobenius-flow
or Hilbert--Polya theorem is currently too strong.

```tex
\begin{theorem}[Arithmetic Frobenius-flow package: honest status]
\label{v4-arith:hp-frobenius-flow-status}
The BC/KMS/GNS construction supplies a positive Hilbert space and a
canonical self-adjoint logarithmic operator
\[
  N_{BC}=-\frac12\log\Delta_1,\qquad
  \operatorname{Spec}(N_{BC})=\{\log m:m\in\mathbb N^\times\}.
\]
The finite unramified Wilson-line construction supplies the corresponding
finite-prime Frobenius traces.  These operators do not construct the
Hilbert--Polya generator for \(\xi_{\mathbb R}\).

The determinant identity
\[
  \det\nolimits_\infty(sI-\Theta_\xi)=\xi_{\mathbb R}(s),
  \qquad
  \Theta_\xi=\frac12I+iH_{HP},
\]
and the trace identity
\[
  \operatorname{Tr}_{\mathrm{reg}}(h(H_{HP}))
    =\sum_\rho h(\gamma_\rho)
\]
are conditional on an independent Hilbert--Polya spectral-flow input:
a Hilbert completion of the middle arithmetic cohomology, a dense invariant
core, a self-adjoint operator \(H_{HP}\), and spectral equality with the
non-trivial zero ordinates.  The existing BC, ordered-bar, Wilson-line, and
archimedean scaling constructions do not provide this input.
\end{theorem}

\begin{proof}
The BC/KMS/GNS part gives \(N_{BC}\) by the modular operator of the KMS state,
hence a self-adjoint operator with logarithmic integer spectrum.  The finite
Wilson trace identifies finite unramified Frobenius traces, not a global
middle cohomology operator.  The Weil--Guinand formula gives the desired
zero/prime distributional trace, but an operator trace requires a positive
Hilbert space and self-adjoint generator with the zero ordinates as spectrum.
Constructing that generator is precisely the Hilbert--Polya spectral-flow
residual.  Therefore the determinant and trace formulas are conditional on
that residual and cannot be recorded as unconditional realization data.
\end{proof}
```

## Files Changed

- Created `notes/arithmetic_residue_swarm/05_frobenius_hp_operator.md`.

## Commands and Tests Run

- `mkdir -p notes/arithmetic_residue_swarm`.
- `sed -n ...` / `rg -n ...` over `CLAUDE.md`, `AGENTS.md`,
  `~/ecosystem/INVARIANTS.md`, `~/ecosystem/AGENTS-HARNESS.md`,
  `chapters/arithmetic/*.tex`, `appendices/arithmetic/*.tex`, and adjacent
  determinant standalone files.
- `rg -n` style-sentinel scan over
  `notes/arithmetic_residue_swarm/05_frobenius_hp_operator.md`.
- `git status --short -- notes/arithmetic_residue_swarm/05_frobenius_hp_operator.md \
  notes/arithmetic_residue_swarm`.
- `git diff --no-index -- /dev/null \
  notes/arithmetic_residue_swarm/05_frobenius_hp_operator.md`.
- No `pdflatex` or `pytest` run: this was a notes-only report and did not edit
  manuscript or compute files.
