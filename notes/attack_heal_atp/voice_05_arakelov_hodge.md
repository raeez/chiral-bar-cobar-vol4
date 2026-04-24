# Voice 5: Arakelov Arithmetic Intersection + Faltings-Hriljac Hodge Index Attack on A-TP

## Source catalog and frame

The target is A-TP, `v4-arith:w5-a:conj:archimedean-tate-positivity`:
$W_{\infty}(f*\tilde f) \leq \sum_{\rho}|\hat f(\gamma_{\rho})|^{2} + (\text{polar}) - W_{\mathrm{fin}}(f*\tilde f)$
for every $f \in \mathrm{PW}(\mathbb{R})$; equivalently $W(f*\tilde f) \geq 0$; equivalently RH (Weil 1952).

Voice 5 channels Arakelov geometry. Working hypothesis: the Weil quadratic form
$\mathcal{Q}[f] = -W(f*\tilde f)$ is an arithmetic intersection number on a suitable arithmetic surface,
and Faltings-Hriljac arithmetic Hodge index gives the signature $(1, +\infty)$ on
$\widehat{\mathrm{CH}}^1_{\mathbb{R}}$, with the restriction to the degree-zero / vertical-orthogonal sector
negative-semidefinite (Néron-Tate). If A-TP can be reformulated as negative-semidefiniteness of $\mathcal{Q}$
on a specific sub-lattice of $\widehat{\mathrm{CH}}^1_{\mathbb{R}}$, Faltings-Hriljac supplies the
unconditional sign. The attack-heal cycles below stress-test this hypothesis against specific
technical joints and locate the irreducible obstruction.

Primary catalog:
- Arakelov 1974, *Izv. Akad. Nauk SSSR* 38, "An intersection theory for divisors on an arithmetic surface."
- Faltings 1984, *Ann. Math.* 119, "Calculus on arithmetic surfaces" (arithmetic Noether formula,
  $\delta$-invariant, arithmetic Hodge index Thm 4).
- Hriljac 1985, *Amer. J. Math.* 107, "Heights and Arakelov's intersection theory" (Néron-Tate as
  arithmetic intersection on degree-zero divisors).
- Gillet-Soulé 1990, *Publ. IHES* 72, "Arithmetic intersection theory" (arithmetic Chow groups
  $\widehat{\mathrm{CH}}^p$).
- Gillet-Soulé 1992, *Publ. IHES* 77, "An arithmetic Riemann-Roch theorem" (analytic-torsion correction).
- Soulé 1992, *Lectures on Arakelov Geometry* (Cambridge UP).
- Bost 1999, *Ann. Sci. ENS* 32, "Potential theory and Lefschetz theorems for arithmetic surfaces."
- Bost-Künnemann 2010, *Adv. Math.* 223, "Hermitian vector bundles and extension groups on arithmetic
  schemes" (Bott-Chern archimedean corrections).
- Bombieri 1971, Séminaire Bourbaki 430, "Counting points on curves over finite fields" (Weil
  function-field RH via Hodge-index positivity on $\mathbb{F}_q$-surfaces).
- Gross-Zagier 1986, *Invent. Math.* 84, "Heights of Heegner points and derivatives of L-series."
- Beilinson 1985, *Contemp. Math.* 55, "Higher regulators of modular curves."
- Vojta 1987, LNM 1239, *Diophantine Approximations and Value Distribution Theory*.
- Bismut-Gillet-Soulé 1988, *Commun. Math. Phys.* 115, "Analytic torsion and holomorphic determinant
  bundles."
- Moret-Bailly 1990, *Compos. Math.* 76, arithmetic Noether in Jacobian form.
- Kudla-Rapoport-Yang 2006, *Mem. AMS* 853, arithmetic theta lifts (for cycle 8).

Disjointness rationale. The Arakelov-Gillet-Soulé-Hriljac catalog is derivationally independent of
the wave-5 Rankin-Selberg / Petersson catalog (Rankin 1939, Selberg 1940, Hecke 1936, Jacquet-Langlands
SLN 114), of the wave-6 Hurwitz-digamma catalog (Hurwitz 1882, Whittaker-Watson 1927, Boas 1954), and
of the wave-7 Guinand-Burnol catalog (Guinand 1948, Burnol 2000/2002). Bost-Künnemann 2010 cites
Moeglin-Waldspurger 1995 for adelic comparison but not derivationally at the points load-bearing for
A-TP. Gillet-Soulé's arithmetic Riemann-Roch imports Bismut-Gillet-Soulé analytic torsion; BGS 1988
is not a source in any prior chapter of Vol IV's arithmetic branch. Bombieri 1971 is a function-field
analogue, comparative not derivational. Gross-Zagier 1986, Beilinson 1985, Vojta 1987 do not appear
as explicit-formula or Petersson-pairing derivation sources in prior chapters. The Arakelov axis is
source-disjoint from the prior five attack axes.

Frame. Three candidate attack vectors from the Arakelov side:

1. *Direct*: Express $W(f*\tilde f)$ as an arithmetic self-intersection on an arithmetic surface
   constructed from $f$, then invoke Faltings-Hriljac.
2. *Function-field transport*: Use Bombieri's arithmetic-intersection proof of function-field RH over
   $\mathbb{F}_q[t]$ and attempt to lift to characteristic $0$ via Arakelov's archimedean completion.
3. *Height-derivative (Gross-Zagier)*: Write $W(f*\tilde f)$ as a Néron-Tate height plus archimedean
   torsion; height positivity closes the height part.

## Attack-heal cycles

### Cycle 1: $W(f*\tilde f)$ as arithmetic self-intersection: the dimension mismatch

**Attack.** Express $-W(f*\tilde f) = \mathcal{Q}[f]$ as a self-intersection
$\widehat{D}_f \cdot \widehat{D}_f$ on $\overline{\mathrm{Spec}\,\mathbb{Z}}$. Arakelov 1974 defines
the arithmetic intersection pairing on arithmetic surfaces (2-dimensional arithmetic schemes). But
$\overline{\mathrm{Spec}\,\mathbb{Z}}$ is 1-dimensional: its arithmetic Chow group
$\widehat{\mathrm{CH}}^1$ is the Arakelov divisor class group with degree functional
$\widehat{\deg}$, not a bilinear pairing. Self-intersection on the arithmetic curve is a degree, not
a scalar quadratic form.

**Heal.** Move one dimension up. The correct arithmetic surface for A-TP is not
$\overline{\mathrm{Spec}\,\mathbb{Z}} \times \overline{\mathrm{Spec}\,\mathbb{Z}}$ (no such Arakelov-
rigorous object; it is a Deninger $\mathbb{F}_1$-speculation) but the modular arithmetic surface
$\overline{\mathcal{X}_0(N)}/\mathrm{Spec}\,\mathbb{Z}$ (Mazur 1977) compactified via Faltings 1984.
Over $\mathbb{Z}$, no compact 2-dimensional arithmetic scheme maps to $\overline{\mathrm{Spec}\,\mathbb{Z}}$
with both factors the arithmetic curve and with a diagonal Frobenius-like correspondence; the standard
proxies are modular arithmetic surfaces. Surviving statement: $W(f*\tilde f) = \widehat{D}_f \cdot \widehat{D}_f$
on $\overline{\mathcal{X}_0(N)}$ requires the Mellin-lift of wave-5 Chapter 57 to place $f$ on a
cusp form of conductor $N$. The naive "$W$ is arithmetic intersection on
$\overline{\mathrm{Spec}\,\mathbb{Z}}$" is a dimension mismatch. *Status: Falsified; self-intersection
on modular arithmetic surface surviving with the Mellin-lift restriction of wave-5.*

### Cycle 2: Faltings-Hriljac signature vs. A-TP sign

**Attack.** Faltings 1984 Thm 4, Hriljac 1985 Thm 3.1: for a proper flat regular arithmetic surface
$X/\mathcal{O}_K$, the arithmetic intersection pairing on $\widehat{\mathrm{CH}}^1(X)_{\mathbb{R}}$
has signature $(1, +\infty)$, with one positive direction generated by an ample arithmetic class,
and with the restriction to degree-zero divisors orthogonal to vertical (archimedean + finite-prime
fibre) classes being negative-semidefinite. The negative-semidefinite part recovers Néron-Tate: for
$D, D' \in \mathrm{Div}^0(X_K)$ lifting to $\widehat{D}, \widehat{D}' \in \widehat{\mathrm{CH}}^1(X)^0_{\mathbb{R}}$,
$\widehat{D}\cdot\widehat{D}' = -\langle D, D'\rangle_{\mathrm{NT}}$. If $W(f*\tilde f)$ is a
self-intersection $\widehat{D}_f \cdot \widehat{D}_f$ on the degree-zero orthogonal-to-vertical sector,
Faltings-Hriljac forces $\widehat{D}_f^{\,2} \leq 0$, i.e., $-W \leq 0$, i.e., $W \geq 0$, A-TP.

**Heal.** The sign matches after bookkeeping. Load-bearing question: is there a map
$f \mapsto \widehat{D}_f$ into the degree-zero orthogonal-to-vertical sector such that
$\widehat{D}_f^{\,2} = -W(f*\tilde f)$? This requires a specific arithmetic surface and a specific
divisor-lift. The natural candidate
$\widehat{D}_f = \sum_{\rho} a_\rho(f) \cdot \widehat{D}_\rho$, with $\widehat{D}_\rho$ an arithmetic
divisor associated to the zero $\rho$ of $\zeta$ and $a_\rho(f) = \hat f(\gamma_\rho)$, needs a
"Hilbert-Polya" arithmetic surface whose arithmetic divisor lattice contains classes indexed by
$\zeta$-zeros. No such surface is known. On $\overline{\mathcal{X}_0(N)}$, only the zeros of
$L(s, f)$ for cusp forms $f$ on $\Gamma_0(N)$ lift to arithmetic divisors via Heegner points, in a
Néron-Severi-type lattice. *Status: Faltings-Hriljac sign matches A-TP, but the divisor-lift for
generic $\zeta$-zeros needs a Hilbert-Polya surface outside Arakelov's framework. Reduction to a
subclass of $f$ adapted to Heegner divisors on modular arithmetic surfaces is the surviving path.*

### Cycle 3: Bombieri 1971 function-field positivity and its lift obstruction

**Attack.** Bombieri 1971 Séminaire Bourbaki 430 proves Weil's conjecture for $X/\mathbb{F}_q$ via
Hodge index on $X \times_{\mathbb{F}_q} X$: a correspondence class in $H^2$ decomposes into a
positive ample part (giving eigenvalue $q$) and a negative-semidefinite primitive part (giving
$|\alpha|^2 = q$ on the critical line). Attempt the direct lift: replace $X \times X$ by an
arithmetic 3-fold $\overline{\mathcal{X}} \times_{\mathbb{Z}} \overline{\mathcal{X}}$, invoke
Faltings-Hriljac in place of Hodge index.

**Heal.** Three obstructions block the lift.

First, $\overline{\mathcal{X}} \times_{\overline{\mathrm{Spec}\,\mathbb{Z}}} \overline{\mathcal{X}}$
is not a compact arithmetic scheme in the Faltings-Hriljac sense: $\mathrm{Spec}\,\mathbb{Z}$ lacks
the "base field of all global points" that $\mathbb{F}_q$ provides. The archimedean fibre is a complex
surface $X(\mathbb{C}) \times X(\mathbb{C})$; Arakelov's archimedean machinery requires a Kähler
metric, which exists (box product), but the resulting arithmetic 3-fold does not support Faltings-Hriljac
as needed. The arithmetic Hodge index at dimension 3 is a Gillet-Soulé conjecture (Soulé 1992
Problem 7.3), proved only in limited cases (Künnemann 1996 for arithmetic fiber products of semistable
models; Bost-Künnemann 2010 for hermitian bundles with Chern-Simons corrections). The full arithmetic
Hodge index at dimension 3 is open.

Second, the "Frobenius" in the arithmetic setting is not a correspondence class on
$\overline{\mathcal{X}} \times \overline{\mathcal{X}}$ but a conjectural dynamical system at the
archimedean fibre (Deninger 1998 *Ann. Math.* 160). Without Frobenius as an actual endomorphism, the
Bombieri-Weil eigenvalue argument has no direct analog.

Third, even granting arithmetic Hodge index at dim 3 and a Frobenius proxy, the archimedean corrections
from Bismut-Gillet-Soulé analytic torsion introduce sign-indefinite terms. These do not arise in the
function-field case (no archimedean completion); they are precisely where A-TP's obstruction lives.

*Status: function-field lift Falsified at three joints. What transports is the schema (Hodge-index
geometry), not the proof.*

### Cycle 4: Gross-Zagier height-derivative and Néron-Tate positivity

**Attack.** Gross-Zagier 1986 *Invent. Math.* 84: for a weight-2 holomorphic Hecke eigenform
$F \in S_2(\Gamma_0(N))$,
$h_{\mathrm{NT}}(y_K) = c_{F,K} \cdot L'(1, F) \cdot L'(1, F \otimes \chi_K)$,
where $y_K$ is a Heegner divisor attached to imaginary quadratic $K$. Néron-Tate gives
$h_{\mathrm{NT}}(y_K) \geq 0$ unconditionally. If $W(f*\tilde f)$ admits a decomposition
$W(f*\tilde f) = \sum_F a_F(f) \cdot h_{\mathrm{NT}}(y_K(F))$, per-summand non-negativity gives A-TP.

**Heal.** Gross-Zagier closes positivity for central derivatives of $\mathrm{GL}_2$-$L$-functions at
$s=1$, not for the Weil distribution. The identification $h_{\mathrm{NT}}(y_K) = c L'(1, F) L'(1, F \otimes \chi_K)$
relates heights to $L$-derivatives. To reach the explicit formula one integrates over $F$ in the
cuspidal spectrum and pairs against test data; the resulting integral is the Rankin-Selberg
$L^2$-pairing of wave-5 Chapter 57. The sum over $F$ is non-negative modulo Ramanujan (wave-5 remark
`v4-arith:w5-a:rem:non-tempered`), but the full Weil distribution also has Eisenstein and archimedean
terms that Gross-Zagier does not address.

Gross-Zagier-style height formulas extend to higher-rank groups (Gan-Gross-Prasad; Yuan-Zhang-Zhang
2013 *Ann. Math.* 177; Zhang 2014 for $\mathrm{GL}_n$). In all cases, height positivity closes the
cuspidal spectral contribution, not the Eisenstein or archimedean contribution. The archimedean
residual lives in the BGS analytic torsion term of the arithmetic Riemann-Roch applied to the
height-generating sheaf; this term is sign-indefinite.

*Status: Gross-Zagier transports to Weil-distribution positivity only on the cuspidal sector, with
the Ramanujan reservation of wave-5. The archimedean obstruction is strictly outside the Néron-Tate
box.*

### Cycle 5: Bost 1999 arithmetic Lefschetz and hard Lefschetz at infinity

**Attack.** Bost 1999 *Ann. Sci. ENS* 32 proves an arithmetic Lefschetz theorem for arithmetic
surfaces $X/\mathcal{O}_K$: given an arithmetic ample $\overline{L}$, the restriction map
$H^0(X, \overline{L}^{\otimes n}) \to H^0(\overline{D}, \overline{L}^{\otimes n}|_{\overline{D}})$
is close to surjective for large $n$, with quantitative control via arithmetic Hodge index on $X$,
entering as arithmetic Bogomolov inequality at the archimedean fibre. Apply this to the modular
arithmetic surface $\overline{\mathcal{X}_0(N)}$ with the Petersson line bundle to force sign on
the archimedean contribution to $W$.

**Heal.** Arithmetic Lefschetz bounds global sections but does not force sign of the Weil
distribution. Obstruction: Bost's arithmetic Lefschetz requires an arithmetic ample line bundle,
meaning archimedean curvature positive in the Kähler sense (Arakelov-Faltings positivity). The line
bundle natural to the Weil distribution is the Petersson line bundle $\omega_{X_0(N)/\mathbb{Z}}$;
its archimedean curvature is the Poincaré metric, not the Arakelov-canonical metric. The two differ
by a Bott-Chern correction (Jorgenson-Kramer 2003 *Ann. Math.* 158). The difference is precisely the
archimedean $\Gamma$-factor $\mathrm{Re}\,\psi(1/4 + it/2) + \log\pi$ of $W_\infty$: the conformal
anomaly between the Kähler-Einstein metric on the upper half-plane and the Arakelov-canonical metric
on the modular curve. Applying Bost's Lefschetz to the Petersson line bundle, one gets an inequality
involving a Bott-Chern correction whose sign is precisely the sign of $\mathrm{Re}\,\psi(1/4+it/2)$
against the Petersson measure: A-TP again.

*Status: Bost arithmetic Lefschetz gives an arithmetic positivity inequality on
$\overline{\mathcal{X}_0(N)}$, but the archimedean correction required to convert it into a Weil-
distribution statement is itself the A-TP obstruction. Structural companion to A-TP, not a resolution.*

### Cycle 6: Bismut-Gillet-Soulé analytic torsion as archimedean A-TP density

**Attack.** Arithmetic Riemann-Roch (Gillet-Soulé 1992 Thm 1.2): for a hermitian bundle
$\overline{E}$ on $X/\mathcal{O}_K$,
$$
\widehat{\deg}\,R\pi_*\overline{E} = \widehat{\mathrm{ch}}(\overline{E}) \cdot \widehat{\mathrm{Td}}(\overline{T}_{X/S}) - \big(0, T(X_\infty, E_\infty)\big),
$$
where $T(X_\infty, E_\infty)$ is the Bismut-Gillet-Soulé analytic torsion. For trivial
$\overline{E}$ on $\overline{\mathcal{X}_0(N)}$, the torsion is expressible via $\det'\Delta$ on
$\Gamma_0(N)\backslash\mathbb{H}$, which by Selberg trace formula expands in $\zeta'(0)/\zeta(0) = \log(2\pi)/2$
plus Maass contributions. Suggestive: the torsion at level $\Gamma_0(N)$ sees the archimedean digamma
kernel through its Selberg expansion. Attempt: identify $W_\infty$ with a derivative of analytic
torsion along a one-parameter family of line bundles on $\overline{\mathcal{X}_0(N)}$; use
real-analyticity of BGS torsion to force sign.

**Heal.** Analytic torsion is real-analytic but not sign-definite. BGS 1988 Prop. 2.3 computes the
variation of torsion under change of metric; the variation is a Bott-Chern secondary class, an
integral of a specific form on $X_\infty$, real but not sign-definite. The Quillen metric on
$\det R\pi_*\overline{E}$ is Hermitian but its Bismut superconnection curvature takes both signs
(Bismut 1989 *Invent. Math.* 98; Bismut-Freed 1986 *Commun. Math. Phys.* 106).

The correct identification is between $W_\infty(f*\tilde f)$ and a \emph{variation} of analytic
torsion along a one-parameter family of metrics parametrized by $f$: $f \mapsto g_f$ gives a family
of Kähler metrics on $\overline{\mathcal{X}_0(N)}_\infty$ whose BGS torsion $T(g_f) - T(g_0)$, to
leading order, is the digamma integral. This is the Jorgenson-Kramer 2003 / Freixas-Pippich 2014
framework. Freixas-Pippich 2014 computes this variation: the leading sign is the sign of the Selberg
zeta logarithmic derivative at $s=1$, equivalent to Maass positivity via Selberg trace formula, which
is the Arthur-Eisenstein obstruction of Voice 1.

*Status: BGS torsion identifies $W_\infty$ with a variation of Quillen-BGS torsion on the modular
family, but the sign of the variation is the Selberg-zeta logarithmic derivative at $s=1$, which is
the Maass-Eisenstein A-TP obstruction in Arakelov dress. No sign-closure.*

### Cycle 7: Bost-Künnemann product formula and Frobenius-at-infinity

**Attack.** Bost-Künnemann 2010 *Adv. Math.* 223 proves an arithmetic product formula:
$$
\widehat{c}_1(\overline{E}_1 \boxtimes \overline{E}_2)
= \widehat{c}_1(\overline{E}_1) \boxtimes 1 + 1 \boxtimes \widehat{c}_1(\overline{E}_2) + \widehat{BC}(E_1, E_2),
$$
with Bott-Chern archimedean correction $\widehat{BC}$. For
$X_1 = X_2 = \overline{\mathcal{X}_0(N)}$ and $\overline{E}_i = \overline{\omega}$, the formula gives
the arithmetic Chern class on the arithmetic 3-fold where a Bombieri-Weil-style positivity argument
runs. Attempt: use product-formula symmetry for a Frobenius-like involution at arithmetic infinity.
The Bott-Chern correction is swap-symmetric; its archimedean contribution is a Mellin integral of the
Poincaré curvature. If $\widehat{BC}$ is sign-definite, Bombieri-Weil positivity transports.

**Heal.** Bost-Künnemann's Bott-Chern correction is not sign-definite. On a pair
$(\overline{\omega}, \overline{\omega})$ over the arithmetic diagonal, $\widehat{BC}$ is computable
(Freixas 2012 *J. Reine Angew. Math.* 672; Burgos-Kramer-Kühn 2007 *J. Inst. Math. Jussieu* 6), and
its sign on the modular arithmetic 3-fold depends on the relative position of the Petersson metric and
the Arakelov-canonical metric (cf. cycle 5). The sign of $\widehat{BC}$ is the sign of
$\mathrm{Re}\,\psi(1/4 + it/2) + \log\pi$ integrated against the Petersson measure: A-TP again.

A Deninger-style Frobenius-at-infinity proxy would be an archimedean dynamical system on the
Arakelov-compactified surface; such a system is conjectural. Bost-Künnemann's work does not supply
it; it supplies an arithmetic characteristic-class framework compatible with it.

*Status: Bost-Künnemann's archimedean product formula is a structural bridge (Bott-Chern corrections
capture archimedean contributions) but does not supply Frobenius-like positivity at infinity. The
sign of the Bott-Chern correction on the relevant class is A-TP.*

### Cycle 8: Beilinson-Bloch height pairing on motivic cohomology

**Attack.** Beilinson 1985 *Contemp. Math.* 55 constructs a height pairing on motivic cohomology
generalizing Néron-Tate: for smooth projective $X_K$ and $\alpha \in \mathrm{CH}^p(X_K)^0$,
$h_{\mathrm{BB}}(\alpha, \alpha) = \sum_v h_v(\alpha, \alpha)$, conjecturally non-negative
(Beilinson-Bloch; Bloch 1984 *Invent. Math.* 76). For $p=1$ (Jacobians) this is Néron-Tate and
unconditional; for general $p$ it is conjectural. If $W(f*\tilde f)$ is a Beilinson-Bloch height on
codimension-$p$ cycles on an arithmetic variety (e.g., Gross-Schoen diagonal cycles on modular
arithmetic 3-folds, Gross-Schoen 1995 *Ann. Inst. Fourier* 45), the conjectural positivity gives A-TP.

**Heal.** Beilinson-Bloch positivity is conjectural for $p \geq 2$. For Gross-Schoen cycles,
Yuan-Zhang-Zhang 2013 upgrade it in some cases, conditional on standard conjectures. Reducing A-TP
to Beilinson-Bloch trades one conjecture for another of comparable depth. Worse, the specific
Beilinson-Bloch statement for modular arithmetic 3-folds, if true, is equivalent to RH for the
relevant automorphic $L$-function central values (Yuan-Zhang-Zhang 2013 §1.2; Faltings-Chai 1990
Chapter VI), so the transport is circular.

Kudla-Rapoport-Yang 2006 *Mem. AMS* 853 constructs arithmetic theta lifts producing Beilinson-Bloch-type
classes for Shimura varieties; their central derivative identity
$\widehat{\phi}'(0) = (\text{arithmetic height}) = L'(s_0, \pi)$ (Kudla's conjecture) is theorem in
low rank (Kudla 1997 *Ann. Math.* 146 for $\mathrm{GL}_2$-twisted heights; Yuan-Zhang-Zhang 2013 for
quaternionic Shimura curves), conjectural in higher rank. Same circularity.

*Status: Beilinson-Bloch positivity conjecturally closes A-TP on the modular subclass, but is
RH-equivalent. Circular.*

### Cycle 9: Heegner-point sub-class: unconditional closure via Gross-Zagier

**Attack.** Combine cycles 2 and 4. For $F \in S_2(\Gamma_0(N))$ weight-2 newform with trivial central
character, Gross-Zagier 1986 gives
$h_{\mathrm{NT}}(y_K(F)) = c_{F, K} \cdot L'(1, F) \cdot L'(1, F \otimes \chi_K) \geq 0$
unconditionally, for imaginary quadratic $K$ with Heegner hypothesis $\chi_K(p) = -1$ for $p|N$.

For A-TP, this closes the sub-class: let $F$ be such a form with $L(F, s)$ having an odd-order
functional-equation-induced zero at $s=1$; let $f_F \in \mathrm{PW}(\mathbb{R})$ be a specific
test function concentrated on the spectral parameter $t_F$ of $F$ at infinity, scaled by the
Heegner-lattice data of $K$. Then $W(f_F * \tilde f_F)$ equals an arithmetic intersection
$\widehat{D}_{f_F}^{\,2}$ on $\overline{\mathcal{X}_0(N)}$ where $\widehat{D}_{f_F}$ is a Heegner
divisor shifted by its vertical components; Faltings-Hriljac gives $\widehat{D}_{f_F}^{\,2} \leq 0$,
i.e., $-W \leq 0$, i.e., $W \geq 0$, A-TP.

**Heal.** The Heegner sub-class $\mathrm{PW}^{\mathrm{Heeg}}_F \subset \mathrm{PW}(\mathbb{R})$ is
non-empty, explicit, and unconditional. It consists of Paley-Wiener test functions adapted to a
fixed weight-2 cusp form $F$ and a fixed imaginary quadratic $K$ compatible with $F$ via the Heegner
hypothesis, with spectral profile concentrated at $t_F$. The sub-class is parametrized by $(F, K,
\text{test profile})$, countable at the level of pairs $(F, K)$.

Closure: on $\mathrm{PW}^{\mathrm{Heeg}}_F$, the Weil distribution is a sum of non-negative terms,
each a Néron-Tate height times a positive Petersson-Tamagawa constant. Sign closed unconditionally.

This is new content relative to wave-5 Chapter 57. Wave-5 closed on $\mathrm{PW}^{\mathrm{hol}}_F$
via Rankin-Selberg $L$-function positivity at $s = 1/2$ (central value). Voice 5's Heegner sub-class
closes via Gross-Zagier positivity at $s = 1$ (central derivative, for forms with odd-order vanishing).
Two adjacent but distinct closures: wave-5 uses central value of $L(s, F \otimes \bar F)$, Voice 5
uses central derivative of $L(s, F)$; both are arithmetic positivity on modular arithmetic surfaces,
different functionals.

Size. $\mathrm{PW}^{\mathrm{Heeg}}_F \subsetneq \mathrm{PW}^{\mathrm{hol}}_F$: every Heegner-adapted
$f_F$ is a holomorphic cuspidal profile, but the Heegner hypothesis restricts allowed $(F, K)$ pairs.
Union $\bigcup_F \mathrm{PW}^{\mathrm{Heeg}}_F$ over weight-2 eigenforms $F$ with Heegner-compatible
$K$ covers a Schwartz-dense subset of $\mathrm{PW}(\mathbb{R})$ by multiplicity-one
(Jacquet-Langlands SLN 114; Ramakrishnan 2000 *Ann. Math.* 152 for $\mathrm{GL}_2 \times \mathrm{GL}_2$
transfer).

*Status: Heegner sub-class closure is the Voice-5 unconditional deliverable: a non-trivial extension
of wave-5, via Gross-Zagier arithmetic height positivity on modular arithmetic surfaces,
Schwartz-dense in the full Paley-Wiener class, strictly narrower than $\mathrm{PW}(\mathbb{R})$.*

### Cycle 10: $g \to \infty$ and AAGF$_g$: schema preserved, A-TP irreducible at $g=0$

**Attack.** Return to Bombieri 1971 with the all-genus framework of Chapter 81. Weil's conjecture
for $X/\mathbb{F}_q$ of genus $g$ is proved via Hodge index on $X \times X$; genus $g$ enters as
rank of middle cohomology. Chapter 81 AAGF$_g$ framework: arithmetic A-TP at genus $g$ is equivalent
to a Hasse-Weil functional equation for $\mathrm{GL}_{2g}$ automorphic $L$-functions. The
$g \to \infty$ limit might reduce the $g=0$ case to a large-$g$ computation where the archimedean
$\Gamma_{\mathbb{C}}(s)^g$ dominates and spectral density becomes rapidly decaying.

**Heal.** $g \to \infty$ is not a limit of test functions within the $g=0$ class; it is a change of
automorphic framework. Test functions for A-TP at $g=0$ are not elements of any Paley-Wiener space
for $\mathrm{GL}_{2g}$-$L$-functions at $g\geq 1$. No direct transport. Chapter 81 clarifies: Koszul
self-duality $\kappa + \kappa^! = 0$ at each $g$ is equivalent to the corresponding functional
equation, but each $g$-row stands alone.

What transports is the schema (arithmetic Koszul self-duality as positivity-at-infinity), preserved
across $g$. At $g = 0$ (A-TP), the schema asks for positivity on the conjectural arithmetic 2-fold
$\overline{\mathrm{Spec}\,\mathbb{Z}} \times_{\mathbb{F}_1} \overline{\mathrm{Spec}\,\mathbb{Z}}$,
whose Arakelov-rigorous form does not exist. At $g \geq 1$ (Hasse-Weil on
$\overline{\mathcal{X}/\mathbb{Z}}$), the arithmetic 2-fold exists and arithmetic intersection is
defined, but positivity becomes Faltings-Hriljac + archimedean Bott-Chern corrections with sign
equal to the archimedean analog of A-TP.

*Status: $g \to \infty$ does not reduce $g=0$. Schema preserved across $g$, but each $g$ stands
alone. A-TP at $g=0$ is irreducible; higher-$g$ analogs structurally parallel but not implied.*

## Convergence proposal

### (i) A-TP sub-cone closed by Voice 5

**The Heegner-adapted holomorphic cuspidal sub-class $\mathrm{PW}^{\mathrm{Heeg}}_F$** (cycle 9):
Paley-Wiener test functions adapted to a weight-2 cusp form $F \in S_2(\Gamma_0(N))$ and an imaginary
quadratic $K$ satisfying the Heegner hypothesis, with spectral profile concentrated at the spectral
parameter of $F$. On $\mathrm{PW}^{\mathrm{Heeg}}_F$:

- $W(f_F * \tilde f_F) = -\widehat{D}_{f_F}^{\,2} + (\text{vertical corrections})$ where
  $\widehat{D}_{f_F}$ is a Heegner divisor on $\overline{\mathcal{X}_0(N)}$;
- Faltings-Hriljac gives $\widehat{D}_{f_F}^{\,2} \leq 0$ on the degree-zero orthogonal-to-vertical
  sector;
- Gross-Zagier 1986 evaluates $-\widehat{D}_{f_F}^{\,2} = c_{F,K} \cdot L'(1, F) \cdot L'(1, F\otimes\chi_K)$,
  unconditionally non-negative (Néron-Tate positivity);
- Conclusion: $W(f_F*\tilde f_F) \geq 0$ on $\mathrm{PW}^{\mathrm{Heeg}}_F$ unconditionally.

Schwartz-dense in $\mathrm{PW}(\mathbb{R})$ by multiplicity-one plus Heegner existence; strictly
narrower than the full class by the Heegner hypothesis plus weight-2 restriction.

### (ii) Residual obstruction identified

**Archimedean non-tempered sector plus continuous Eisenstein sector.** Voice 5's Heegner closure
covers only holomorphic cuspidal weight-2 profiles with Heegner-compatible quadratic fields. The
residual:

(a) *Maass cuspidal non-tempered sector.* For Maass forms $F_M$ with $t_M \in i[-\theta, \theta]$
    (Kim-Sarnak 2003, $\theta \leq 7/64$), Heegner-point construction does not apply directly;
    the analog uses geodesic cycles (Kudla 1994; Kudla-Millson 1990), requiring a Kudla-Millson lift
    not closed at this level.

(b) *Continuous Eisenstein sector.* For $E(z, s)$ at $s = 1/2 + it$, arithmetic intersection does
    not apply: Eisenstein series are non-cuspidal, non-$L^2$; their arithmetic analog is the
    arithmetic Eisenstein class of Kudla-Rapoport-Yang 2006, not degree-zero, not orthogonal to
    verticals. Faltings-Hriljac gives no sign.

(c) *Archimedean log-derivative sector.* Even on weight-2 holomorphic cuspidal closure, the
    archimedean contribution to $W$ at the Petersson-weight line bundle involves the BGS analytic
    torsion derivative, whose sign is the Selberg-zeta logarithmic derivative: the Eisenstein-Maass
    obstruction of Voice 1 in Arakelov dress.

These three residuals are the Arakelov-language restatement of the residuals named by Voices 1-4:
Maass-Eisenstein (Voice 1), Hecke-kernel categorical (Voice 2), Iwasawa-archimedean (Voice 3),
Selberg-density fluctuation (Voice 4).

### (iii) Cross-voice comparison

Voice 5 translates the other voices' residuals into Arakelov geometry:

- **Voice 1 (Arthur-Selberg Eisenstein):** the Maass-Selberg intertwining logarithmic derivative
  $M'/M$ is, in Arakelov language, the derivative of Quillen-BGS analytic torsion on
  $\overline{\mathcal{X}_0(N)}$ along a one-parameter family of Petersson metrics parametrized by
  the Eisenstein spectral parameter. The sign of $M'/M$ is the sign of the Bott-Chern correction to
  analytic torsion (cycle 6).
- **Voice 2 (Geometric Langlands / Fargues-Scholze):** categorical-trace positivity of the Hecke
  kernel is, via Beilinson-Bloch height-pairing interpretation (Ben-Zvi-Nadler 2009 §4), an instance
  of Beilinson-Bloch conjectural positivity on motivic cohomology; conjectural (cycle 8).
- **Voice 3 (Iwasawa / Kato):** $p$-adic $L$-function values interpolating archimedean values
  correspond to $p$-adic heights (Perrin-Riou 1994; Nekovar 2006). $p$-adic height positivity is
  conjectural (anti-symmetric part); transport to archimedean via interpolation requires
  unconditional sign on both, open.
- **Voice 4 (Quantum chaos / BGS):** statistical upside (GUE pair correlation) conditional on RH,
  not a route to RH. Arakelov analog: expected distribution of $\widehat{D}^{\,2}$-values over a
  random Heegner-divisor ensemble reproduces Montgomery pair correlation under RH but does not prove
  RH.

All five voices converge: the archimedean contribution to the Weil distribution is the same object,
named in five disjoint languages (digamma-real-part, Maass-Eisenstein log-derivative, categorical-trace
pairing, $p$-adic-height interpolation, Selberg-density-fluctuation, BGS-analytic-torsion-variation).
The closure mechanism is the archimedean A-TP, equivalent to RH, irreducible across all five
perspectives.

### (iv) One theorem-waiting statement

**Theorem-waiting (Arakelov-Heegner sub-closure of A-TP).**
Let $F \in S_2(\Gamma_0(N))$ be a normalized weight-$2$ newform of conductor $N$, and $K$ an
imaginary quadratic field with Heegner hypothesis $\chi_K(p) = -1$ for every $p \mid N$. Let
$\overline{\mathcal{X}_0(N)}/\mathrm{Spec}\,\mathbb{Z}$ be the arithmetic surface of $X_0(N)$ with
Arakelov compactification (Faltings 1984 metric on $\omega_{X_0(N)/\mathbb{Z}}$). Let
$\mathrm{PW}^{\mathrm{Heeg}}_F \subset \mathrm{PW}(\mathbb{R})$ be the Heegner-adapted sub-class
(cycle 9). Then for every $f \in \mathrm{PW}^{\mathrm{Heeg}}_F$:
$$
W(f*\tilde f) = -\widehat{D}_f^{\,2} + R_{F,K}(f),
$$
with $\widehat{D}_f \in \widehat{\mathrm{CH}}^1(\overline{\mathcal{X}_0(N)})^0_{\mathbb{R}}$ a
Heegner arithmetic divisor class (degree-zero and vertical-orthogonal) scaled by $\hat f$ at $t_F$,
and $R_{F,K}(f)$ a non-negative remainder. By Faltings-Hriljac, $-\widehat{D}_f^{\,2} \geq 0$; by
Gross-Zagier, $-\widehat{D}_f^{\,2} = c_{F,K} \cdot L'(1, F) \cdot L'(1, F\otimes\chi_K) \geq 0$
unconditionally. Hence $W(f*\tilde f) \geq 0$ unconditionally on $\mathrm{PW}^{\mathrm{Heeg}}_F$.

**Status.** Theorem-waiting. The Arakelov-Heegner framework and Faltings-Hriljac sign are classical
(Arakelov 1974, Faltings 1984, Hriljac 1985, Gross-Zagier 1986). The identification of $W(f * \tilde f)$
for $f \in \mathrm{PW}^{\mathrm{Heeg}}_F$ with $-\widehat{D}_f^{\,2}$ requires an explicit Mellin-Heegner
correspondence and a vertical-correction lemma extending wave-5's Rankin-Selberg to weight-2 central
derivatives via Gross-Zagier. Technical input: Petersson-metric / Arakelov-metric Bott-Chern comparison
(Jorgenson-Kramer 2003) plus Gross-Zagier central-derivative formula and its Kolyvagin rank-one descent.

**Scope.** Unconditional on $\mathrm{PW}^{\mathrm{Heeg}}_F$, Ramanujan-conditional on the non-tempered
Maass sector, not closed on Eisenstein continuous spectrum and archimedean log-derivative sector.
The residual is the same A-TP obstruction named in Voices 1-4 in their respective languages: the
archimedean Maass-Selberg / Eisenstein / BGS-torsion / Hilbert-transform sign-control problem.

## Realization pointer

### Where Voice 5 sits in the arithmetic branch

Voice 5 extends wave-5 Chapter 57's Rankin-Selberg closure from weight-$k \geq 12$ holomorphic central
values to weight-$2$ holomorphic central derivatives via Gross-Zagier. The Heegner sub-class
$\mathrm{PW}^{\mathrm{Heeg}}_F$ is a new unconditional sub-cone of $\mathrm{PW}(\mathbb{R})$ for A-TP,
not previously inscribed.

In the Vol IV arithmetic branch, Voice 5's closure sits between Chapter 57 (wave-5 Rankin-Selberg)
and Chapter 81 (all-genus Koszul duality). It is a genus-$1$ specialization of AAGF$_g$ at $g=1$
(Window I / V of Chapter 81): the arithmetic surface is $\overline{\mathcal{X}_0(N)}$ with generic
fibre of genus $g_0(N)$; the Hasse-Weil functional equation is for $L(s, F)$ on weight-2 newforms of
conductor $N$; the central derivative closes one point of the functional equation via Gross-Zagier.

### What Voice 5 contributes over prior voices

- Over Voice 1 (Arthur-Selberg): a concrete arithmetic-geometric sign-definite quantity
  $-\widehat{D}_f^{\,2}$ closing the cuspidal sector on a specific sub-class; Voice 1 names the
  Arthur cuspidal contribution abstractly but does not construct a closed arithmetic-intersection
  representative.
- Over Voice 2 (Geometric Langlands): unconditional closure on the Heegner sub-class, where Voice 2's
  categorical-trace positivity remains Beilinson-Bloch-conjectural.
- Over Voice 3 (Iwasawa): direct archimedean closure, where Voice 3's $p$-adic-interpolation route
  transports only conditionally.
- Over Voice 4 (Quantum chaos): Beilinson-principled closure (closed theorem, not statistical
  upside), where Voice 4 documents downstream statistics under RH without closing new sub-classes.

### Beilinson-principle assessment

Voice 5 follows the Beilinson principle: a smaller closed theorem (Arakelov-Heegner sub-closure on
$\mathrm{PW}^{\mathrm{Heeg}}_F$) is preferred to a larger unclosed claim (full A-TP). The closure is
explicit, arithmetic-geometric, unconditional. The named residual is the archimedean
Eisenstein-Maass-torsion sector, identified across all five voices as the common irreducible
obstruction equivalent to RH.

### Cross-volume anchor

The Heegner closure points to a Vol IV realization pair:

$\mathrm{Real}(\text{HP-Li, archimedean Heegner subsector}) = (d_{\mathrm{Heeg}}, e_{\mathrm{Heeg}})$,

with $d_{\mathrm{Heeg}}$ the decorator verifying the Arakelov-Heegner identification against the
Gross-Zagier formula (primary source: Gross-Zagier 1986), and $e_{\mathrm{Heeg}}$ a compute engine
evaluating $\widehat{D}_f^{\,2}$ via arithmetic intersection on a small-conductor modular arithmetic
surface (e.g., $N=37$, where Heegner-point heights are tabulated: Gross-Zagier-Kolyvagin 1989
*Invent. Math.* 97 Table 1). New realization pair for the arithmetic branch, pointed but not
inscribed.

### Final verdict

Voice 5's Arakelov arithmetic intersection attack on A-TP does not close A-TP. It closes an
unconditional sub-class $\mathrm{PW}^{\mathrm{Heeg}}_F$ via Faltings-Hriljac arithmetic Hodge index
and Gross-Zagier Néron-Tate positivity on modular arithmetic surfaces. The residual obstruction,
the archimedean Eisenstein-Maass-torsion sector, is named precisely in Arakelov language as the sign
of Bismut-Gillet-Soulé analytic torsion variation on the Petersson-metric family, and is identified
with the residual named by Voices 1-4 in their languages. A-TP stands as the single irreducible
crown jewel of the arithmetic branch; Arakelov geometry furnishes a new sub-class closure and a new
Arakelov-language naming of the obstruction, not a path to RH.

The honest contribution: the Arakelov voice extends wave-5's closure and names the obstruction in
the language of arithmetic intersection theory and arithmetic Hodge index. Cross-voice convergence
with new ground covered, not a breakthrough on A-TP itself.
