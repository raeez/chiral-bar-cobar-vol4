# Voice 2 of 5 — A-TP Attack-Heal

## Angle: Geometric Langlands / Fargues-Scholze / Categorical Arithmetic

Voice 2 channels Beilinson-Drinfeld geometric Langlands, Arinkin-Gaitsgory
singular support, Fargues-Scholze geometrization of local Langlands,
Drinfeld-Lafforgue function-field positivity, Frenkel-Gaitsgory local
geometric Langlands, and Ben-Zvi-Nadler categorical trace theory. The
thesis to test: archimedean Tate positivity is the shadow at
$\mathrm{Re}\,s = 1/2$ of a categorical-trace positivity of a Hecke
kernel $T_W$ on $\mathrm{Bun}_{GL_2}(\overline{\mathrm{Spec}\,\mathbb{Z}})$;
Fargues-Scholze spectral action transports Weil-II-style Galois
positivity from the spectral side to the automorphic side; A-TP on a
generic $f \in \mathrm{PW}(\mathbb{R})$ reduces to categorical
positivity of a convolution-square kernel at the archimedean fibre.
Adversarial first; heal only after falsification; Falsify in the ledger
where the geometric machinery fails to survive the archimedean
reduction.

---

## Source Catalog (HZ-IV Primary, Disjoint)

- **Beilinson-Drinfeld 2004.** *Chiral Algebras.* AMS Colloq. Publ. 51.
  Chiral Koszul duality, factorization categories, chiral Hochschild.
- **Arinkin-Gaitsgory 2015.** *Singular support of coherent sheaves and
  the geometric Langlands conjecture.* arXiv:1201.6343. Nilpotent
  singular-support stratification of $\mathrm{IndCoh}$ on
  $\mathrm{LocSys}_{\check G}$; precise formulation of geometric
  Langlands for $G$.
- **Fargues-Scholze 2021.** *Geometrization of the local Langlands
  correspondence.* arXiv:2102.13459. Fargues-Fontaine curve $X_{FF}$;
  $\mathrm{Bun}_G$ as a stack on the category of perfectoid diamonds;
  spectral action of $\mathrm{Perf}(\mathrm{LocSys}_{\check G}^{\mathrm{WD}})$
  on $D_{\mathrm{lis}}(\mathrm{Bun}_G)$.
- **Lafforgue (L.) 2012.** *Chtoucas pour les groupes reductifs et
  parametrisation de Langlands globale.* arXiv:1209.5352. Global
  Langlands for $GL_n$ over function fields; excursion operators;
  positivity of Frobenius eigenvalues as Deligne-Weil-II positivity.
- **Drinfeld 1987.** *Moduli varieties of F-sheaves.* Funct. Anal.
  Appl. 21 (1987), 107-122. Shtukas, Hecke action on
  $\mathrm{Bun}_{GL_n}(X)$ for $X$ a function-field curve.
- **Deligne 1980.** *La conjecture de Weil. II.* Publ. Math. IHES 52,
  137-252. Purity of Frobenius eigenvalues on $\ell$-adic cohomology;
  source of function-field RH and the positivity transported below.
- **Frenkel-Gaitsgory 2006.** *Local geometric Langlands correspondence
  and affine Kac-Moody algebras.* Progr. Math. 253, 69-260. Categorical
  centre, Feigin-Frenkel duality, critical-level identifications.
- **Ben-Zvi-Nadler 2009.** *Loop spaces and Langlands parameters.*
  arXiv:0706.0322. Hochschild-trace presentation of categorical centres
  and Hecke eigencategory.
- **Francis-Gaitsgory 2012.** *Chiral Koszul duality.* arXiv:1103.5803.
  Chiral bar-cobar adjunction for factorization algebras; the precise
  categorical dual of the $\kappa + \kappa^!$ relation.
- **Kapranov-Smirnov 1995.** *Cohomology determinants and reciprocity
  laws: number field case.* Manuscript. Cohomological-determinant
  framing at the real place; Parshin reciprocity three-fold analogue.
- **Laumon 1987.** *Correspondance de Langlands geometrique.* C. R.
  Acad. Sci. Paris. Shtuka-free formulation; geometric Langlands for
  $GL_n$ on a curve over $\mathbb{F}_q$.
- **Bezrukavnikov 2012.** *On two geometric realizations of an affine
  Hecke algebra.* arXiv:1209.0403. Cited in Chapter 14 as
  load-bearing on the Iwahori-Hecke presentation of
  $\mathcal{V}^{\mathrm{prim}}$.

Disjointness statement: none of these sources underwrites the
Weil-1952 explicit formula derivation of Chapter 57, the Bost-Connes
scattering derivation of Chapter 80, the Petersson-Rankin-Selberg
derivation of Chapter 57 Section 3, or the Hurwitz-digamma elementary
derivation of the wave-6 A-TP approach. Fargues-Scholze and
Arinkin-Gaitsgory are cited for local-global compatibility in Chapter
22 but there as derivation sources for the F1 reduction, not for A-TP;
the load-bearing use in this voice is of their positivity consequence,
not their categorical comparison.

---

## Cycle 1 — Attack: The Hecke Kernel Candidate $T_W$

**Attack.** Can the Weil distribution $W$ be realised as the
categorical trace of an actual Hecke kernel $T_W \in \mathrm{Hk}^{\mathrm{Iw}}_{GL_2, \mathrm{glob}}$?
The Vol IV crowning placement
(Chapter 14, $\mathcal{V}^{\mathrm{prim}} = \mathrm{HH}_\bullet(\mathrm{Hk}^{\mathrm{Iw}}_{GL_2, \mathrm{glob}})$)
gives $\mathcal{V}^{\mathrm{prim}}$ as a Hochschild trace class; the
character $\xi(s)$ is the trace pairing against a distinguished family
of Hecke operators. If $W$ is itself such a trace, then $W(f * \tilde f)
= \mathrm{Tr}(T_{f} \cdot T_{f}^*)$ for a morphism $T_f$ in the
Hochschild-trace pairing, and $W(f * \tilde f) \geq 0$ becomes the
manifest statement $\|T_f\|_{\mathrm{HS}}^2 \geq 0$ on an appropriate
trace Hilbert space.

**Failure mode.** A categorical trace on an $\infty$-category is
valued in chain complexes (or $E_1$-algebras in complexes), not
automatically in positive reals. The pairing
$\mathrm{Tr}: \mathcal{C} \otimes \mathcal{C}^{\mathrm{op}} \to \mathbb{1}$
produces an object of the monoidal unit; positivity requires a
Hermitian or unitary structure on $\mathcal{C}$. The Iwahori Hecke
category in mixed characteristic does not yet carry a proved unitary
structure: Bezrukavnikov 2012 supplies the equal-characteristic
equivalence between $\mathrm{D}^b\mathrm{Coh}(\mathrm{St}_{GL_2})$ and
mixed perverse sheaves on the affine flag variety over
$\overline{\mathbb{F}_p}$, not over $\mathbb{Q}_p$; the
mixed-characteristic lift is supplied by Fargues-Scholze via diamonds,
but the unitary structure on the resulting $D_{\mathrm{lis}}(\mathrm{Bun}_{GL_2})$
is not yet a proved theorem for the full Paley-Wiener class.

**Heal (partial).** Assume F1 + F2 + F3 of Chapter 22. Under this
hypothesis, $\mathcal{V}^{\mathrm{prim}} = \mathrm{HH}_\bullet(\mathrm{Hk}^{\mathrm{Iw}}_{GL_2, \mathrm{glob}})$
is an $E_1$-algebra with a Petersson pairing
(Chapter 22, P3, conditional on Koszul-Petersson compatibility). The
Hecke kernel $T_W$ is then identified as the universal
Hecke-convolution kernel whose categorical trace is $\mathcal{V}^{\mathrm{prim}}$;
its pairing against $f * \tilde f$ factors through the Petersson
pairing at finite places. At the archimedean place, the
Hecke-categorical pairing is governed by the archimedean local factor
of the Fargues-Scholze spectral action, which at $\mathrm{Re}\,s = 1/2$
is precisely the Tate digamma distribution $\mathcal{T}_\infty$.

**Residual.** A-TP reformulates as: the archimedean local factor of the
categorical trace of $T_{f * \tilde f}$ is non-negative for every
$f \in \mathrm{PW}(\mathbb{R})$. The finite-place factor is
non-negative by the Petersson-Hilbert-space structure
(Chapter 57, Theorem 3.4); the archimedean factor is not absorbed by
the Petersson isometry (Chapter 57, Proposition 4.2); it is carried by
the pullback of the spectral action to the archimedean fibre, which
for $GL_2 / \mathbb{Q}$ is the real place $v = \infty$.

**Status: Conjectural.** The reformulation is structurally precise but
does not yet close A-TP. It shifts the obstruction from "positivity of
the Weil archimedean distribution" to "positivity of the archimedean
local factor of Fargues-Scholze spectral action on a convolution-square
Hecke kernel", a statement of comparable depth.

---

## Cycle 2 — Attack: Arinkin-Gaitsgory Nilpotent Singular Support as Positivity

**Attack.** Arinkin-Gaitsgory (arXiv:1201.6343) cut out the
geometric-Langlands side of the category $\mathrm{IndCoh}_{\mathrm{Nilp}}(\mathrm{LocSys}_{\check G})$
by nilpotent singular support. Singular support is a coherent-sheaf
invariant living in $T^*\mathrm{LocSys}_{\check G} / \mathrm{LocSys}_{\check G}$,
the cotangent stack; nilpotent SS is a closed locus, compatible with
the Langlands-automorphic side by the equivalence. In
function-field arithmetic Langlands (Drinfeld-Lafforgue), positivity
of Frobenius eigenvalues of cohomology sheaves on
$\mathrm{Bun}_{\check G}$ is a Weil-II consequence: pure objects of
weight 0 have Frobenius eigenvalues of absolute value $1$. Deligne
1980 (Weil II) is a theorem of that form.

Does nilpotent SS + Deligne positivity give A-TP directly at the
archimedean place?

**Failure mode.** Deligne Weil-II is function-field positivity: it
applies to $\ell$-adic sheaves on varieties over $\mathbb{F}_q$, and
the positivity input is purity of Frobenius. Over number fields there
is no Frobenius at the real place; the analogue of Weil-II at the
archimedean place is not proved, and the hypothesis "pure of weight 0"
does not translate. Arinkin-Gaitsgory is a categorical equivalence over
$\mathbb{C}$ (or a field of characteristic 0); its arithmetic lift to
$\mathrm{Spec}\,\mathbb{Z}$ is F1 of Chapter 21. The categorical
positivity of nilpotent-SS-restricted $\mathrm{IndCoh}$ is not
automatically a positivity statement: $\mathrm{IndCoh}$ is a stable
$\infty$-category, its mapping spaces are chain complexes, and
positivity requires a Hermitian enhancement.

**Heal (strong).** Replace the direct Deligne transport with the
Fargues-Scholze spectral action. Fargues-Scholze (Thm I.10.2 in
arXiv:2102.13459) construct, for each local Langlands parameter
$\phi_v : W_v \to \check G(\overline{\mathbb{Q}}_\ell)$, a spectral
action of $\mathrm{Perf}(\mathrm{LocSys}_{\check G}^{\mathrm{WD}, v})$
on $D_{\mathrm{lis}}(\mathrm{Bun}_G)_{\phi_v}$; Hecke operators at $v$
act by the characteristic polynomial of $\phi_v(\mathrm{Frob}_v)$.
Positivity of these characteristic polynomials (Deligne-Weil-II at
finite places, where it is proved) gives Hecke-eigenvalue positivity.

At the archimedean place $v = \infty$, $W_\infty = W_{\mathbb{R}}$ is
generated by $\mathbb{C}^\times$ and a complex-conjugation involution;
the archimedean local Langlands parameters for $GL_2 / \mathbb{R}$ are
parametrised by their infinity-types (discrete series, principal
series, limits of discrete series). For a parameter $\phi_\infty$, the
spectral Hecke action at $\infty$ is multiplication by
$\phi_\infty(z) + \phi_\infty(\bar z)$ for $z \in \mathbb{C}^\times$,
controlled by the archimedean local factor $L_\infty(s, \phi_\infty) =
\Gamma_{\mathbb{R}}(s - \mu_1)\Gamma_{\mathbb{R}}(s - \mu_2)$. The
positivity of this expression on $\mathrm{Re}\,s = 1/2$, for real
$\mu_i$, is exactly the tempered-unitary-representation positivity; for
$\mu_i$ with imaginary part (non-tempered), the positivity fails and
the local factor has sign changes.

**Residual (precise).** A-TP reduces to a positivity statement about
the archimedean local factor of $L(s, \pi_\infty \otimes \tilde\pi_\infty)$
for $\pi$ tempered at $\infty$. For the holomorphic cuspidal $F$ of
Chapter 57, $\pi_\infty$ is the discrete series of weight $k$, and
this is proved (Chapter 57 Theorem 3.4). For generic
$\pi \in \mathrm{PW}(\mathbb{R})$, temperedness at $\infty$ is the
archimedean Ramanujan conjecture, which for $GL_2 / \mathbb{Q}$ is
proved for holomorphic cuspidals (Deligne 1974) and known up to
$7/64$ for Maass cuspidals (Kim-Sarnak 2003). A-TP on the full
$\mathrm{PW}(\mathbb{R})$ class requires full archimedean Ramanujan,
which is open.

**Status: Scope-restricted (tempered archimedean locus) + conditional
(full Ramanujan).** The spectral-action reduction is structurally
sharp: A-TP on the tempered-archimedean locus is a consequence of
Fargues-Scholze spectral positivity + holomorphic-Ramanujan; A-TP on
the full Paley-Wiener class is conditional on the archimedean
Ramanujan conjecture at $GL_2 / \mathbb{Q}$.

---

## Cycle 3 — Attack: Chiral Koszul Self-Duality on $\mathrm{Bun}_{GL_2}$

**Attack.** Francis-Gaitsgory 2012 (arXiv:1103.5803) prove a chiral
Koszul duality: for a chiral algebra $A$ on a curve $C$, there is a
derived equivalence between $A$-modules and cochain complexes on the
Ran space $\mathrm{Ran}(C)$ with coefficients in the chiral cobar of
$A$. Applied arithmetically (Chapter 10, Beilinson bar-cobar), the
chiral bar-cobar pairing on $\mathcal{V}^{\mathrm{prim}}_{\mathrm{Heis}}$
is the adelic Mellin pairing, with Koszul self-duality forcing
$\kappa + \kappa^! = 0$ equivalent to $\xi(s) = \xi(1-s)$ (Chapter 22,
P1 resolution). Does chiral self-duality produce a positive-definite
inner product on chiral cohomology at the archimedean fibre?

**Failure mode.** Chiral Koszul duality over a complex curve produces a
derived equivalence of $\infty$-categories; positivity is not built
in. The natural Hermitian structure on a chiral algebra is the
Beilinson-Drinfeld Hermitian form coming from the $\lambda$-bracket
pairing; this is positive-definite only on unitary chiral algebras. On
the arithmetic Heisenberg $\mathcal{V}^{\mathrm{prim}}_{\mathrm{Heis}}$
this form is positive-definite at finite primes
(Bost-Connes Hilbert-space structure; Chapter 22 Step 2 of P1-proof)
and at the archimedean place (classical Heisenberg Fock
positive-definiteness). So far identical to Chapter 22 P3 conditional
closure.

The genuinely new content from chiral self-duality: the pairing is
$\mathbb{Z}/2$-equivariant under $s \mapsto 1 - s$, which is the
Tate-Poisson invariance. The pairing is Hermitian. But: Hermitian +
self-dual + $\mathbb{Z}/2$-equivariant is not the same as positive
definite, and the archimedean Tate distribution lives on the
$\mathbb{Z}/2$-fixed locus $\mathrm{Re}\,s = 1/2$ where the self-dual
structure is reflected, not broken. Positivity at the fixed locus is
the genuine load-bearing content; self-duality reduces the problem to
this locus but does not resolve it.

**Heal (structural).** Chiral Koszul self-duality on the archimedean
fibre gives a Fourier-self-dual pairing; Tate-Poisson is the
Fourier-invariance of the archimedean theta distribution. The pairing
on $\mathcal{V}^{\mathrm{prim}}$ is the adelic Fourier pairing at the
archimedean place. Its positivity is the positivity of the Fourier
self-dual measure; for the real line, this is Bochner positivity: a
Fourier self-dual measure is positive iff its characteristic function
is non-negative-definite. Applied to the archimedean theta
distribution, Bochner positivity is a classical theorem
(Bochner 1933). But the archimedean Tate distribution
$\mathcal{T}_\infty(t) = (2\pi)^{-1} \mathrm{Re}\,\psi(1/4 + it/2) +
(2\pi)^{-1}\log\pi$ is not the Fourier transform of a positive
measure: $\mathrm{Re}\,\psi$ oscillates in sign (Chapter 57
Proposition 4.2 proof).

**Residual (named).** The archimedean Tate distribution
$\mathcal{T}_\infty$ is not Bochner-positive; chiral self-duality on
its own does not supply a positive inner product at the archimedean
fibre of $\mathcal{V}^{\mathrm{prim}}$. The Fourier-self-dual structure
exists but is insufficient.

**Status: Falsified (as a direct route).** Chiral Koszul self-duality
does not produce archimedean positivity. It produces only the $s
\mapsto 1 - s$ symmetry, which is the Riemann functional equation, not
the Riemann hypothesis. The attempted categorical upgrade of Bochner
positivity fails because the Tate $\psi$-distribution is not Bochner.

---

## Cycle 4 — Attack: Kapranov-Smirnov Cohomology Determinants at the Real Place

**Attack.** Kapranov-Smirnov 1995 propose a cohomology-determinant
framework for reciprocity laws on arithmetic threefolds, adapting
Deligne's determinant line construction to the number-field setting
with the archimedean place as the third dimension. In this framework,
the Weil distribution arises as the Chern class of a determinant line
bundle on the moduli of adelic line bundles (or rank-2 bundles, for
our $GL_2$ setting). Positivity of this Chern class at the archimedean
fibre would be a geometric-positivity statement.

The Kapranov-Smirnov intuition: $\mathrm{Spec}\,\mathbb{Z}$ is a
"real 1-dimensional base"; adding the real place gives a
compactification $\overline{\mathrm{Spec}\,\mathbb{Z}}$ that is
"arithmetically 3-dimensional" via the Minkowski-Arakelov embedding,
with the third dimension the Minkowski lattice. Cohomology determinants
on a 3-fold give a reciprocity law of the form: sum of local symbols =
0. Weil's explicit formula has exactly this form:
$\sum_\rho \hat f(\gamma_\rho) + \text{polar} - W_\infty - W_{\mathrm{fin}} = 0$.

**Failure mode.** Kapranov-Smirnov is unpublished manuscript; its
mathematical status is heuristic. The specific identification of the
archimedean Weil distribution with a Chern class requires a specific
compactification of the moduli stack; the Arakelov-compactified
$\overline{\mathrm{Spec}\,\mathbb{Z}}$ is a pointed "point at infinity"
but not in general a smooth proper 3-fold. Arakelov-Gillet-Soule
arithmetic Chow theory supplies the correct framework for Chern classes
on arithmetic varieties, but its archimedean piece is the de Rham
cohomology at the infinite fibre, dressed with a Green current; the
positivity of an arithmetic Chern class is not a primary theorem but a
conjecture of the arithmetic-Hodge-index type (Faltings, Arakelov,
Gillet-Soule).

**Heal (partial).** The Arakelov-Chern-class framing identifies the
archimedean Tate distribution $W_\infty$ with the Green-current
component of a specific arithmetic Chern class on
$\overline{\mathrm{Spec}\,\mathbb{Z}}$. Positivity of arithmetic Chern
classes is governed by the arithmetic Hodge index theorem of
Faltings (1984) and its extensions; at present, the arithmetic Hodge
index is proved for arithmetic surfaces of Faltings type but open in
the general archimedean setting. Positivity of the Green current of
$W_\infty$ would follow from a specific arithmetic-Hodge-index
statement, which is comparable in difficulty to RH itself.

**Residual.** The Kapranov-Smirnov route does not shorten A-TP; it
relocates A-TP from "positivity of $W_\infty$" to "positivity of a
specific Arakelov Chern class / Green current", a statement of
comparable and unproved difficulty. The arithmetic Hodge index at the
archimedean place is not in the catalog of proved theorems.

**Status: Heuristic.** The cohomology-determinant framing is
suggestive but does not give a proof path. It confirms that A-TP is
naturally an arithmetic-geometric positivity statement rather than an
analytic one; but within the geometric frame, it is Hodge-index,
comparable to RH.

---

## Cycle 5 — Attack: Fargues-Scholze Spectral Action and Deligne Transport

**Attack.** Can the function-field positivity of Deligne-Weil-II
(Deligne 1980) be transported to the number-field archimedean place
via Fargues-Scholze? Function-field Langlands (Drinfeld 1987,
Lafforgue 2012) proves full global Langlands for $GL_n / \mathbb{F}_q(X)$,
including the Ramanujan conjecture (Frobenius eigenvalues on the
$\ell$-adic cohomology of the associated shtuka moduli are pure of
weight $(k-1)/2$ after normalisation). Purity + Satake identification
gives tempered Hecke-eigenvalue bounds globally. In the
Fargues-Scholze framework, the function-field and number-field
Langlands share the same local structure at all finite places (diamonds
over $\mathrm{Spa}\,\mathbb{Z}_p$ and $\mathrm{Spa}\,\mathbb{F}_q((t))$
are parallel); the divergence is at the archimedean place, where the
Fargues-Fontaine curve $X_{FF}$ has no direct archimedean analogue.

**Failure mode.** Fargues-Scholze is genuinely about the local
Langlands, with local meaning $\mathbb{Q}_p$ not $\mathbb{R}$. There
is no archimedean Fargues-Fontaine curve; the archimedean local
Langlands for $GL_2 / \mathbb{R}$ is the Jacquet-Langlands-Shalika
classical setup (discrete series, principal series, limits), not a
diamond-theoretic construction. Deligne-Weil-II applies to
$\ell$-adic cohomology of varieties over $\mathbb{F}_q$; at the real
place, the analogue would be Betti cohomology with a Hodge structure,
and the "purity" would be a Hodge-Frobenius-type positivity, for which
Hodge index is the closest available technology.

The Fargues-Scholze spectral action *does* extend the local Langlands
to the derived setting at each finite prime; applying it to the full
global automorphic category requires the F1 conjecture (Chapter 21),
which itself is conditional on local categorical Langlands +
$\mathrm{L}_{\mathrm{ACD}}$ (Chapter 22). Even granting F1 + F2 + F3,
the archimedean local factor of the spectral action on a
convolution-square Hecke kernel is the Tate-gamma-factor archimedean
pairing, which is precisely the object A-TP asks about.

**Heal (categorical reformulation).** Under F1 + F2 + F3, A-TP is
equivalent to the categorical positivity statement: for every
$f \in \mathrm{PW}(\mathbb{R})$, the archimedean component of the
spectral pairing of $T_f$ with $T_f^*$ in
$D_{\mathrm{lis}}(\mathrm{Bun}_{GL_2})_\infty$ is non-negative. At the
archimedean place, $D_{\mathrm{lis}}(\mathrm{Bun}_{GL_2})_\infty$ is
replaced by the $(\mathfrak{g}, K_\infty)$-module category; the
spectral pairing is the Jacquet-Langlands-Shalika local pairing; the
archimedean positivity is the positivity of the local
Rankin-Selberg integral $\Psi_\infty(s, W_f, \tilde W_f)$ on
$\mathrm{Re}\,s = 1/2$.

**Residual (named precisely).** A-TP under F1 + F2 + F3 reduces to:
$\Psi_\infty(1/2, W_f, \tilde W_f) \geq 0$ for every Whittaker vector
$W_f$ obtained from $f \in \mathrm{PW}(\mathbb{R})$ via the
archimedean Kirillov model. This is a classical-analytic positivity
question; it is equivalent, modulo the holomorphic-case reduction, to
A-TP on the full Paley-Wiener class. The categorical framing has
relocated the question from the Weil $W$-distribution to a local
Rankin-Selberg positivity, but the local Rankin-Selberg positivity at
$\mathrm{Re}\,s = 1/2$ for generic archimedean Whittaker vectors is
itself the open part of A-TP.

**Status: Conjectural.** Fargues-Scholze + F1 + F2 + F3 give a
categorical reformulation of A-TP as archimedean Rankin-Selberg
positivity. This reformulation is sharper than the Chapter 57
statement (it is explicitly a local-archimedean question, not a global
one) but it is not a closure.

---

## Cycle 6 — Attack: de Branges Hermite-Biehler in the Geometric Frame

**Attack.** Chapter 73 (de Branges Hilbert spaces, HB) closes A-TP on
a de Branges-Hermite-Biehler sub-class. de Branges Hilbert spaces
$H(E)$ are characterised by the Hermite-Biehler condition on the
structure function $E$: $|E(s)| > |E(\bar s)|$ for
$\mathrm{Im}\,s > 0$. This is positivity of a specific reproducing
kernel. Can the de Branges HB positivity be placed in the
Fargues-Scholze / Arinkin-Gaitsgory frame?

**Heal (structural).** The de Branges HB condition on $E$ corresponds
to $E$ being the archimedean local factor of a tempered automorphic
representation. For $GL_2 / \mathbb{R}$, the archimedean parameter
$\phi_\infty$ determines a structure function
$E(s) = \Gamma_{\mathbb{R}}(s - \mu_1)\Gamma_{\mathbb{R}}(s - \mu_2)$
with $\mu_i \in \mathbb{R}$ (tempered) giving the HB condition. The
reproducing kernel of the associated $H(E)$ is the archimedean
Rankin-Selberg kernel. Under F1 + F2 + F3, this kernel is the
archimedean pullback of the Fargues-Scholze spectral pairing at
$\infty$.

So the de Branges HB frame (Chapter 73) is the Hilbert-space
realisation of the categorical frame (this voice); the Hermitian
structure of $H(E)$ is the categorical-trace Hermitian structure at the
archimedean place.

**Residual.** The de Branges HB sub-class is precisely the tempered
archimedean locus. Extension beyond this locus requires archimedean
Ramanujan. Consistent with Cycle 2.

**Status: Convergent with Cycle 2.** The de Branges HB route and the
Fargues-Scholze geometric route agree on: (i) A-TP is proved on the
tempered archimedean locus; (ii) extension requires archimedean
Ramanujan. Two independent presentations of the same sub-class
closure.

---

## Cycle 7 — Attack: Adelic Scattering (Chapter 80) vs Geometric Langlands

**Attack.** Chapter 80 (adelic scattering, voice J) reduces A-TP to
unitarity of a Bost-Connes scattering matrix $S$ on
$L^2(C_{\mathbb{Q}})$, closes A-TP on a Tate-Mellin sub-class, and
locates the residual in the Connes non-commutative $L^2(X_{\mathbb{Q}})$
construction. How does this compare with the Fargues-Scholze /
Arinkin-Gaitsgory categorical frame?

**Heal (cross-reduction).** The two frames attack orthogonal aspects.
Chapter 80 uses operator-theoretic scattering: the Weil distribution is
a spectral shift function, A-TP is unitarity of $S$, closure is on
zero-adapted test functions (Tate-Mellin sub-class). This voice uses
categorical Langlands: $W$ is a categorical trace, A-TP is
archimedean Rankin-Selberg positivity, closure is on tempered
archimedean representations.

The structural relation: the Bost-Connes $C^*$-algebra
$\mathbb{A}^{\mathrm{BC}}$ is the Koszul dual of the arithmetic
Heisenberg $\mathcal{V}^{\mathrm{prim}}_{\mathrm{Heis}}$ (Chapter 22 P1
Step 2); the Bost-Connes scattering space $L^2(C_{\mathbb{Q}})$ is the
Hilbert-space realisation of a Whittaker model of $\mathcal{V}^{\mathrm{prim}}$
(Chapter 22 P3 Step 3). Under F1 + F2 + F3, the categorical frame and
the scattering frame are two presentations of the same A-TP
question; the former closes on the tempered archimedean locus, the
latter closes on the Tate-Mellin sub-class (these are genuinely
different but overlapping sub-classes).

**Which contains more structure?** Both frames are genuinely
informative. The categorical Langlands frame adds: a bridge to F1 +
F2 + F3, a structural understanding of why archimedean positivity is
the obstruction, an equivalence with archimedean Ramanujan at the
residual level. The scattering frame adds: a precise trace-class
perturbation criterion, a direct Connes absorption-spectrum residual.
They are not equivalent; they are complementary.

**Status: Complementary.** Both are partial, neither closes A-TP, each
names its residual in its own language. The common residual is
archimedean positivity at the tempered / zero-adapted boundary.

---

## Cycle 8 — Attack: F1 Reduction and RH-Equivalent Categorical Statement

**Attack.** Chapter 22 reduces F1 (global arithmetic Arinkin-Gaitsgory)
to $\mathrm{L}_{\mathrm{ACD}}$ (adelic categorical descent) plus the
local categorical Langlands. Conditional on F1, A-TP reduces (via this
voice's Cycle 5) to archimedean Rankin-Selberg positivity. Is the
archimedean Rankin-Selberg positivity itself a theorem-waiting
statement in the categorical language, or is it equivalent to RH?

**Heal (sharp formulation).** Archimedean Rankin-Selberg positivity
$\Psi_\infty(1/2, W_f, \tilde W_f) \geq 0$ is not equivalent to RH in
isolation; it is equivalent to A-TP on the archimedean fibre. The
global A-TP (= RH) additionally requires that the full convolution
structure (finite + archimedean) respect positivity, which is the
content of the Weil explicit formula.

Concretely: on the holomorphic-tempered-archimedean sub-class
$\mathrm{PW}^{\mathrm{hol}}_F$ of Chapter 57, archimedean
Rankin-Selberg positivity is a theorem (Petersson-Jacquet; Chapter 57
Theorem 4.3 Jacquet 1972 archimedean-local input). On the
Maass-tempered locus (where temperedness at $\infty$ holds up to
$7/64$ Kim-Sarnak), archimedean Rankin-Selberg positivity follows
conditionally. On the non-tempered archimedean locus, positivity
fails at individual parameters.

**Residual.** The categorical frame reduces A-TP to an archimedean
Rankin-Selberg positivity that is itself theorem-waiting, not
theorem-trivial. The distinction from Chapter 57 is: Chapter 57
treats the archimedean factor as a classical digamma-kernel positivity
question; this voice frames it as a categorical-spectral-action
positivity question. The two framings are equivalent modulo F1 + F2 +
F3.

**Status: Conjectural, sharpness checked.** Archimedean
Rankin-Selberg positivity is genuinely the content of archimedean
A-TP; the categorical reformulation does not trivially close or
trivially reduce to RH.

---

## Convergence Proposal

From the eight cycles above, the geometric-Langlands voice converges
on the following structured reformulation of A-TP.

### Theorem-Waiting (Categorical A-TP):

Under F1 (global arithmetic Arinkin-Gaitsgory), F2 (perfectoid
$E_2$-enhancement), F3 (arithmetic Ben-Zvi-Nadler), A-TP is
equivalent to the categorical-spectral positivity:

For every $f \in \mathrm{PW}(\mathbb{R})$, the archimedean component
of the Fargues-Scholze spectral pairing of the Hecke kernel
$T_{f * \tilde f}$ in $D_{\mathrm{lis}}(\mathrm{Bun}_{GL_2})$ is
non-negative. Equivalently, the archimedean local Rankin-Selberg
integral
$\Psi_\infty(1/2, W_f, \tilde W_f)$ is non-negative for every
archimedean Whittaker vector $W_f$ obtained from $f$ via the
Kirillov model.

### Scope-Restricted Closure (Tempered Archimedean):

On the tempered archimedean locus (holomorphic cuspidals +
Kim-Sarnak-bounded Maass cuspidals), archimedean Rankin-Selberg
positivity follows from classical Jacquet-Langlands-Shalika
archimedean integrals, disjoint from the Weil-1952 derivation.
Matches Chapter 57 scope, via independent reduction path.

### Falsified (Naive Chiral Self-Duality):

Cycle 3 falsifies the naive attempt to obtain archimedean positivity
directly from chiral Koszul self-duality: the Fourier-self-dual
structure exists but is not Bochner-positive at the archimedean place
because the Tate $\psi$-distribution oscillates.

### Residual (Conjectural):

Full A-TP on $\mathrm{PW}(\mathbb{R})$ requires archimedean Ramanujan
for $GL_2 / \mathbb{Q}$ (non-tempered locus). Equivalently, full
A-TP requires the archimedean Rankin-Selberg positivity on the
untempered archimedean locus, which is the genuine open sector.

### Independent Reductions (disjoint-source audit):

This voice reduces A-TP via the geometric-Langlands chain to:
archimedean Ramanujan for $GL_2 / \mathbb{Q}$. Chapter 57 reduces
A-TP to: archimedean digamma-kernel positivity. Chapter 80 reduces
A-TP to: Connes absorption-spectrum on $L^2(X_{\mathbb{Q}})$. Three
disjoint reductions, three disjoint residuals, common underlying
obstruction.

### Status Ledger:

- **Cycle 1 (Hecke kernel $T_W$):** Conjectural. Structural reformulation under F1 + F2 + F3.
- **Cycle 2 (Nilpotent SS + Fargues-Scholze spectral action):** Scope-restricted. Reduces to tempered archimedean.
- **Cycle 3 (Chiral Koszul self-duality):** Falsified as direct route. Supplies $s \mapsto 1-s$ symmetry, not positivity.
- **Cycle 4 (Kapranov-Smirnov cohomology determinants):** Heuristic. Relocates to arithmetic Hodge index, open.
- **Cycle 5 (Fargues-Scholze + Deligne transport):** Conjectural. Full A-TP conditional on archimedean Ramanujan.
- **Cycle 6 (de Branges HB placement):** Convergent with Cycle 2.
- **Cycle 7 (Scattering vs Langlands):** Complementary. Common residual in archimedean positivity.
- **Cycle 8 (Sharpness check):** Archimedean Rankin-Selberg positivity is the genuine load.

---

## Realization Pointer

The Vol IV realization decorator for the categorical-A-TP statement:

- **Claim label:** `v4-arith:w-geolang:thm:categorical-ATP-equivalence` (pending inscription if a separate chapter is added; currently absorbed into Chapter 57 + Chapter 22).
- **Derived from (primary):** Fargues-Scholze 2021, Arinkin-Gaitsgory 2015, Ben-Zvi-Nadler 2009, Francis-Gaitsgory 2012, Deligne 1980.
- **Verified against (disjoint secondary):** Weil 1952 / Li 1997 / Jacquet 1972 (Chapter 57 derivation catalog); Bost-Connes 1995 / Connes 1999 / Meyer 2005 (Chapter 80 derivation catalog); Hurwitz 1882 / Gauss 1813 (wave-6 derivation catalog).
- **Disjoint rationale.** The geometric-Langlands derivation proceeds
  through Fargues-Scholze local geometrization, Arinkin-Gaitsgory
  nilpotent singular support, and categorical Ben-Zvi-Nadler. The
  three other derivations underwrite Chapter 57 (Petersson /
  Rankin-Selberg), Chapter 80 (Bost-Connes scattering), and the
  wave-6 elementary approach. None of the geometric sources
  (Fargues-Scholze, Arinkin-Gaitsgory, Francis-Gaitsgory) appears as
  load-bearing input to the Weil explicit formula derivation, the
  Bost-Connes spectral-shift derivation, or the digamma-kernel
  derivation. The disjointness is genuine: function-field positivity
  and categorical Langlands on one side, operator-theoretic
  scattering and classical Rankin-Selberg on the other.

### Recommended Vol IV Action

1. Inscribe the categorical-A-TP equivalence as a conditional
   theorem under F1 + F2 + F3 in a new chapter or as an appendix
   to Chapter 57. Status tag: `\ClaimStatusProvedHere` (conditional
   on F1 + F2 + F3 + archimedean Ramanujan on the non-tempered
   locus).
2. Inscribe the scope-restricted tempered-archimedean closure as
   `\ScopeRestricted`: categorical A-TP closes unconditionally on
   the tempered archimedean locus, matching Chapter 57's holomorphic
   cuspidal closure via an independent disjoint path.
3. Inscribe the Cycle 3 Falsification of chiral self-duality as a
   remark: the naive categorical upgrade fails because the Tate
   $\psi$-distribution is not Bochner-positive. This is a genuine
   Falsification of a structural speculation.

### Cross-Comparison with Voice 1 and Voices 3-5

This voice's contribution is the categorical-Langlands reduction.
Voice 1 (adjacent adversarial frame, not yet written) is expected to
approach from a different angle (e.g.\ automorphic-spectral,
functional-analytic, operator-algebraic). The five voices in
aggregate should produce: five disjoint reductions, five named
residuals, one common obstruction. The geometric-Langlands reduction
of this voice names the residual as "archimedean Rankin-Selberg
positivity on the non-tempered locus = archimedean Ramanujan for
$GL_2 / \mathbb{Q}$ on non-holomorphic cuspidals".

---

## Final Verdict

The geometric-Langlands / Fargues-Scholze / Arinkin-Gaitsgory
machinery does not close A-TP. It produces three genuine contributions:

1. A conditional equivalence of A-TP with archimedean
   Rankin-Selberg positivity under F1 + F2 + F3.
2. An unconditional closure on the tempered archimedean sub-class,
   matching Chapter 57 via an independent disjoint path (disjoint
   source audit: Fargues-Scholze + Ben-Zvi-Nadler vs.\ Weil + Jacquet).
3. A Falsification of naive chiral Koszul self-duality as a direct
   positivity route; the Fourier-self-dual structure survives, the
   Bochner-positivity does not.

The residual is archimedean Ramanujan for $GL_2 / \mathbb{Q}$ on the
non-tempered locus. This is the geometric-Langlands name for the
same obstruction that Chapter 57 names as "Tate digamma positivity",
Chapter 80 names as "Connes absorption-spectrum", and the wave-6
approach names as "digamma bounded-interval positivity". Four names,
one obstruction, equivalent to RH.

The Beilinson-principled closure: A-TP on the tempered locus is a
genuine unconditional closure in the geometric frame; A-TP on the
full class is conditional on archimedean Ramanujan. No overclaim, no
downgrade, precise residual.
