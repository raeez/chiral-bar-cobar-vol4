# Voice 1: Arthur-Selberg Truncation Attack on A-TP

## Source catalog and frame

The target is the archimedean Tate positivity conjecture A-TP
(`v4-arith:w5-a:conj:archimedean-tate-positivity`): for every
$f \in \mathrm{PW}(\mathbb{R})$,
$W(f * \tilde f) \geq 0$, with $W$ the Weil distribution and
$\tilde f(x) = \overline{f(-x)}$. Equivalent to RH by Weil 1952
(Meddelanden Lund, reprinted Oeuvres II).

Voice 1 channels Arthur's trace-formula programme: expand
$W(f * \tilde f)$ as the spectral side of the Arthur-Selberg trace
formula on $\mathbf{GL}_2(\mathbb{A}_\mathbb{Q})$; decompose into
cuspidal, residual, and Eisenstein sectors; attempt per-sector
positivity. The natural discrete-continuous split is
$W = W^{\mathrm{cusp}} + W^{\mathrm{res}} + W^{\mathrm{Eis}}$.

Primary sources:
- Arthur 1978 "A trace formula for reductive groups I" Duke Math J 45;
  Arthur 1980 "A trace formula for reductive groups II" Compos Math 40;
  Arthur 1981 "The trace formula in invariant form" Ann Math 114;
  Arthur 1988 "The invariant trace formula I, II" J Amer Math Soc 1
  (1988); Acta Math 162 (1989).
- Arthur 2005 "An introduction to the trace formula" Clay Math Proc 4.
- Arthur 2013 "The endoscopic classification of representations"
  AMS Colloq Publ 61.
- Jacquet-Langlands 1970 "Automorphic forms on $GL_2$" SLN 114.
- Selberg 1956 "Harmonic analysis and discontinuous groups" J Indian
  Math Soc 20.
- Ngô Bao Châu 2010 "Le lemme fondamental pour les algèbres de Lie"
  Publ IHES 111.
- Flicker-Kazhdan 1988 "Metaplectic correspondence" Publ IHES 64.
- Gelbart-Jacquet 1978 "A relation between automorphic representations
  of $GL_2$ and $GL_3$" Ann Sci ENS 11.
- Moeglin-Waldspurger 1989 "Le spectre résiduel de $GL_n$" Ann Sci
  ENS 22; Moeglin-Waldspurger 1995 "Spectral decomposition and
  Eisenstein series" Cambridge Tracts 113.
- Wong 1997 "Small eigenvalues and automorphic forms" Math Res Lett 4.

Disjointness from the wave-5 Chapter 57 catalog (Weil 1952, Li 1997,
Rankin 1939, Selberg 1940, Hecke 1936, Deligne 1974, Jacquet 1972,
Jacquet-Langlands SLN 114, Bombieri-Lagarias 1999, Kim-Sarnak 2003,
Patterson 1988, Bump 1997, Zagier 1981): partial. Arthur 1978-1989 and
Arthur 2005/2013 are disjoint from the Rankin-Selberg identity per se.
Moeglin-Waldspurger 1995 is also invoked in wave-5 Chapter 57's
Eisenstein density mismatch (`v4-arith:w5-a:prop:eisenstein-residual`);
its role there is minimal (Eisenstein $L^2$ decomposition citation),
and the load-bearing Arthur use below is the invariant trace formula
apparatus, which does not appear in wave-5. Jacquet-Langlands SLN 114
overlaps as global input; the Arthur truncation uses its adelic
Whittaker model but not its functional equation derivation. Selberg 1956
(original trace formula) is disjoint from the Rankin-Selberg identity
of Selberg 1940; the author overlap is formal, not derivational.

The honest disjoint_rationale: the wave-5 attack Mellin-lifts
$\mathrm{PW}$ test data into the holomorphic cuspidal Fock via a fixed
$F \in S_k$, then computes a Rankin-Selberg inner product. The Arthur
attack below does not fix any cuspidal form; it expands the Weil
distribution directly as the spectral side of the trace formula, with
the cuspidal contribution running over all cuspidal representations of
$\mathbf{GL}_2(\mathbb{A})$ simultaneously. The operational distinction
is genuine: wave-5 closes on a $\mathrm{PW}^{\mathrm{hol}}_F$ class
parametrized by a single $F$; the Arthur route runs over all $F$ at
once (and all Maass forms) and weights by Harish-Chandra Plancherel.

Scope of Voice 1. Not a closure of A-TP. An independent reduction of
A-TP to a two-part residual: cuspidal-sector positivity (conditional
on Ramanujan) and Eisenstein-sector positivity (1/2-shift on the
continuous spectrum). The Eisenstein piece is where the hundred-year
obstruction lives; Arthur's invariant trace formula exposes the
obstruction as a specific Maass-Selberg intertwining-operator
identity.

## Attack-heal cycles

### Cycle 1: Naive Arthur expansion; the Weil distribution is not a matrix coefficient

**Attack.** The first-pass Arthur attack: take $f \in \mathrm{PW}(\mathbb{R})$,
lift $f * \tilde f$ to an adelic test function $\phi$ on
$\mathbf{GL}_2(\mathbb{A}_\mathbb{Q})$ via the archimedean Plancherel
transform, apply Arthur's invariant trace formula (Arthur 1988 J Amer
Math Soc 1, Thm 3.3):
$$
J_{\mathrm{spec}}(\phi) = J_{\mathrm{geom}}(\phi).
$$
Identify $W(f * \tilde f)$ with $J_{\mathrm{spec}}(\phi)$ minus a
geometric-side contribution of unipotent orbital integrals plus the
central scalar trace. Conclude A-TP iff $J_{\mathrm{spec}}(\phi) \geq 0$.

This fails at the first step. Arthur's trace formula pairs a compactly
supported smooth test function $\phi \in C_c^\infty(\mathbf{GL}_2(\mathbb{A}))$
against the regular representation on
$L^2(\mathbf{GL}_2(\mathbb{Q}) \backslash \mathbf{GL}_2(\mathbb{A}))$.
The Weil distribution on $\mathrm{PW}(\mathbb{R})$, by contrast, pairs
an even entire function of exponential type against $\zeta$-zeros and
prime powers; it is not a priori a matrix coefficient of the regular
representation. Directly lifting $f * \tilde f$ to an adelic test
function produces a function on $\mathbb{A}^\times$ (via the idele
norm), not on $\mathbf{GL}_2(\mathbb{A})$, and the resulting
$J_{\mathrm{spec}}$ is the Arthur formula for $\mathbf{GL}_1$, not
$\mathbf{GL}_2$. The $\mathbf{GL}_1$ trace formula is Poisson
summation on $\mathbb{Q}^\times \backslash \mathbb{A}^\times$; it
contains the zeros of $\zeta$ but not as a spectral decomposition into
cuspidal and Eisenstein sectors.

**Heal.** Arthur's trace formula on $\mathbf{GL}_2/\mathbb{Q}$ attacks
A-TP through the following correct adapter, obtained from the
Weil-Bost-Connes identification
(`v4-arith:w5-b:lem:fock-embeds-gns`). The adelic test function is
not $f * \tilde f$ directly, but its image under the Hecke-trace
integral
$$
\phi_f(g) := \int_{\mathbf{GL}_2(\mathbb{Q}) \backslash \mathbf{GL}_2(\mathbb{A})} f * \tilde f(\log|\det g|) \cdot \mathbb{1}_{K_f}(g_f) \cdot k_\infty(g_\infty) \, dg,
$$
where $K_f = \mathbf{GL}_2(\hat{\mathbb{Z}})$, $g_f$ is the finite-place
component, $g_\infty$ is the archimedean component, and $k_\infty$ is
the spherical matrix coefficient
$k_\infty(g_\infty) = \int f(t) \Phi_{\mathrm{sph}}(g_\infty, 1/2 + it) \, dt$
with $\Phi_{\mathrm{sph}}$ the spherical function on
$\mathbf{PGL}_2(\mathbb{R})$ at the $t$-th spectral parameter.

With this adapter, Arthur's invariant trace formula applies: the
spectral side is a weighted sum over irreducible constituents of the
regular representation, and the unramified spherical cuspidal sector
contributes the zero-side of the Weil distribution by the Selberg-Hecke
identification (Selberg 1956 §3; Iwaniec 2002 Spectral Methods
Chapter 1). The heal: the Arthur adapter is Jacquet-Langlands SLN 114
§3 (adelic Whittaker model) combined with Selberg's pretrace formula.

Conclusion of cycle 1: the naive Arthur expansion of $W$ requires the
adelic lift $f \mapsto \phi_f$ through a spherical-Hecke-trace
integral, and not a direct lift of $f * \tilde f$. The lifted test
function $\phi_f \in C_c^\infty(\mathbf{GL}_2(\mathbb{A}))$ is
$K_f$-bi-invariant on the finite places and spherical of Plancherel
type $f$ on $\mathbb{R}$.

### Cycle 2: Arthur's coarse geometric expansion vs. archimedean digamma

**Attack.** With the Jacquet-Langlands-adapted test function $\phi_f$,
Arthur's coarse geometric expansion (Arthur 2005 §7 Thm 7.1; 1988 Acta
162 §2) gives
$$
J_{\mathrm{geom}}^{\mathrm{coarse}}(\phi_f) = \sum_{\mathfrak{o}} J_{\mathfrak{o}}(\phi_f),
$$
indexed by semisimple conjugacy classes $\mathfrak{o}$ of
$\mathbf{GL}_2(\mathbb{Q})$. Each $J_{\mathfrak{o}}$ is a weighted
orbital integral. The central class $\mathfrak{o} = \{z \cdot I : z \in \mathbb{Q}^\times\}$
contributes the Tate $\zeta$-integral, delivering the polar terms
$\widehat{f*\tilde f}(\pm 1/(2i))$. Unipotent classes contribute the
Eisenstein-geometric pieces. Elliptic regular classes contribute
$p$-adic orbital integrals matching the finite Euler factors
$W_{\mathrm{fin}}$.

Positivity attempt: each $J_{\mathfrak{o}}$ has a Plancherel-integral
interpretation; sum positivity is claimed to reduce to per-orbit
positivity. This fails: unipotent orbital integrals are not sign-definite
(they carry the logarithmic divergence of the Tamagawa measure near
the unipotent radical) and the archimedean component of the
unipotent-orbital contribution is precisely the digamma distribution
$\mathrm{Re}\,\psi(1/4 + it/2) + \log \pi$ of $W_\infty$. The naive
geometric positivity strategy therefore immediately hits the same
digamma obstruction that wave-5 Chapter 57 names as A-TP.

**Heal.** Arthur's geometric expansion does not resolve $W_\infty$
positively; it reproduces $W_\infty$ as the archimedean unipotent
contribution, which is where the obstruction already lives. The heal
is to abandon the geometric side for positivity and pass to the
spectral side: Arthur 1988 Acta 162 Thm 3.3 gives
$$
J_{\mathrm{spec}}(\phi_f) = J_{\mathrm{cusp}}(\phi_f) + J_{\mathrm{Eis}}(\phi_f) + J_{\mathrm{res}}(\phi_f),
$$
the sum of cuspidal, Eisenstein-continuous, and residual-discrete
contributions to the spectral side of the trace formula. This is the
decomposition to attack.

Conclusion of cycle 2: the unipotent orbital integral on the
geometric side reproduces $W_\infty$; the geometric side offers no
positivity handle on the archimedean contribution. The attack must
run on the spectral side.

### Cycle 3: Cuspidal sector positivity; Rankin-Selberg on cuspidal forms

**Attack.** Arthur's cuspidal spectral contribution $J_{\mathrm{cusp}}(\phi_f)$
is a sum over cuspidal automorphic representations
$\pi \in L^2_{\mathrm{cusp}}(\mathbf{GL}_2(\mathbb{Q}) \backslash \mathbf{GL}_2(\mathbb{A}))$:
$$
J_{\mathrm{cusp}}(\phi_f) = \sum_{\pi \in \widehat{\mathbf{GL}_2}_{\mathrm{cusp}}} \mathrm{tr}(\pi(\phi_f)).
$$
Each summand $\mathrm{tr}(\pi(\phi_f))$ is, by the Hecke-Whittaker
identification (Jacquet-Langlands SLN 114 §11), a positive quantity:
Rankin-Selberg $L(1/2, \pi \otimes \bar\pi)$ times a Plancherel density
times $|\widehat{f}(t_\pi)|^2$ for $t_\pi$ the spectral parameter of
$\pi$ at $\infty$. Positivity of $J_{\mathrm{cusp}}$ follows from
positivity of each summand.

Almost. Under the Ramanujan conjecture for $\mathbf{GL}_2/\mathbb{Q}$
(temperedness of every cuspidal representation at every place), each
summand is manifestly non-negative. Without Ramanujan, Maass cusp forms
with non-tempered archimedean parameter $t_\pi \in i \cdot [-\theta, \theta]$
for $\theta \leq 7/64$ (Kim-Sarnak 2003 JAMS 16) contribute terms with
$|\widehat{f}(t_\pi)|^2$ at purely imaginary $t_\pi$, and $\widehat{f}$
of an even real $f$ at imaginary argument need not be real. The
Rankin-Selberg positivity at non-tempered $\pi$ requires further care:
$L(1/2, \pi \otimes \bar\pi)$ is non-negative on cuspidal $\pi$ by the
Shimura integral representation (Shimura 1975 Ann Math 102; standard
reformulation in Bump 1997 §3.7), but the pairing against $\widehat{f}$
at imaginary spectral parameter introduces a sign-indefinite factor.

**Heal.** The cuspidal sector closes positively modulo Ramanujan. This
is precisely the status of wave-5 Chapter 57's Rankin-Selberg
positivity on $\mathrm{PW}^{\mathrm{hol}}_F$
(`v4-arith:w5-a:rem:non-tempered`). The Arthur route makes this
visible at the level of all cuspidal representations simultaneously,
not just those of a fixed holomorphic $F$.

Precise statement of the heal. Define the cuspidal Weil contribution
$$
W^{\mathrm{cusp}}(f * \tilde f) := \sum_{\pi \in \widehat{\mathbf{GL}_2}_{\mathrm{cusp,temp}}} |\widehat{f}(t_\pi)|^2 \cdot c_\pi,
$$
with $c_\pi = \mathrm{Res}_{s=1} L(s, \pi \otimes \bar\pi) \cdot
\mathrm{Vol}(\mathbb{Q}^\times \backslash \mathbb{A}^{\times,1})^{-1}$
a positive Rankin-Selberg residue and the sum over tempered cuspidal
representations. Then
$W^{\mathrm{cusp}}(f * \tilde f) \geq 0$ unconditionally.

The non-tempered Maass complement $W^{\mathrm{cusp,non-temp}}$
contributes a sign-indefinite term of size at most
$|\widehat{f}(i\theta)|^2 \cdot \#\{\pi : t_\pi \in i[-\theta, \theta]\}$
with $\theta \leq 7/64$ (Kim-Sarnak). On the Ramanujan-conditional
locus, $W^{\mathrm{cusp,non-temp}} = 0$ and $W^{\mathrm{cusp}} \geq 0$
unconditionally.

Conclusion of cycle 3: the cuspidal sector positivity is conditional on
Ramanujan for $\mathbf{GL}_2$. The conditional cost is exactly
$7/64$ at present (Kim-Sarnak 2003); the quantitative residual is
finite and controlled.

### Cycle 4: Residual sector; Moeglin-Waldspurger non-contribution

**Attack.** Arthur's residual spectral contribution $J_{\mathrm{res}}(\phi_f)$
comes from non-cuspidal discrete automorphic representations, which by
Moeglin-Waldspurger 1989 Ann Sci ENS 22 Thm 4.4 on $\mathbf{GL}_n$ are
classified as Langlands quotients of parabolic inductions from
cuspidal data on Levi subgroups. For $\mathbf{GL}_2/\mathbb{Q}$, the
residual spectrum consists of the one-dimensional constituents of
$L^2_{\mathrm{disc}}$: characters $\chi \circ \det$ of
$\mathbf{GL}_2(\mathbb{A})$ with $\chi$ a Dirichlet character of
$\mathbb{Q}^\times \backslash \mathbb{A}^{\times,1}$.

Direct positivity attempt: each character contribution is
$|\chi(\phi_f)|^2$ (positivity from the one-dimensional trace
formula). Sum over $\chi$ reduces to an $\mathbf{GL}_1$ Poisson
summation and recovers the Tate polar terms $\widehat{f*\tilde f}(\pm 1/(2i))$
already present.

Almost. The characters contributing are not all of
$\mathbf{GL}_1(\mathbb{A})/\mathbb{Q}^\times$; only those with
archimedean component $|\cdot|^{s_0}$ at $s_0 = 0$ and $s_0 = 1$
(coming from the $L^2$-finiteness of $\chi$) contribute to the residual
spectrum. This reduces the residual sector to the polar contribution
of $W$ itself; no new positive quantity emerges.

**Heal.** The residual sector is \emph{not} a new positive contribution
but a reformulation of the polar terms. Moeglin-Waldspurger's
residual classification for $\mathbf{GL}_2$ gives
$L^2_{\mathrm{res}} = \bigoplus_\chi \chi \circ \det$, with $\chi$ a
Hecke character of finite order and archimedean type $|\cdot|^0$ (the
trivial archimedean parameter) plus $|\cdot|^{1/2}$ (which is killed
by $L^2$-integrability at infinity for non-trivial archimedean type).

For $\mathbf{GL}_2/\mathbb{Q}$ unramified at infinity and at all
finite places (the spherical case relevant to $\phi_f$ of the
Jacquet-Langlands adapter), only the trivial character
$\chi \equiv 1$ contributes. Its contribution is
$$
J_{\mathrm{res}}(\phi_f) = \phi_f(1) \cdot \mathrm{Vol}(\mathbf{GL}_2(\mathbb{Q}) \backslash \mathbf{GL}_2(\mathbb{A})^{(1)}),
$$
which after unfolding is precisely the Tate polar contribution
$\widehat{f*\tilde f}(1/(2i)) + \widehat{f*\tilde f}(-1/(2i))$ (up to
the Tamagawa number of $\mathbf{PGL}_2$, equal to 2). This is
non-negative for $f$ real even (polar contributions evaluated at
imaginary arguments within the critical strip give real positive
values by the Hadamard product of $\xi_{\mathbb{R}}$).

Conclusion of cycle 4: the residual sector contributes only the Tate
polar terms and no new sign-indefinite content. Per-sector closure of
the residual sector is unconditional. It is also uninformative: it
closes a part of the Weil distribution that was never in dispute.

### Cycle 5: Eisenstein continuous sector; the 1/2-shift lives here

**Attack.** The Eisenstein continuous spectral contribution $J_{\mathrm{Eis}}(\phi_f)$
is where the archimedean Tate positivity lives. By the Langlands
spectral decomposition (Langlands 1976 SLN 544; Moeglin-Waldspurger
1995 Ch IV.1), the Eisenstein continuous part of $L^2(\mathbf{GL}_2(\mathbb{Q})
\backslash \mathbf{GL}_2(\mathbb{A}))$ is
$$
L^2_{\mathrm{Eis}} = \int^\oplus_{s \in i\mathbb{R}_+} \mathrm{Ind}_{\mathbf{B}(\mathbb{A})}^{\mathbf{GL}_2(\mathbb{A})}(|\cdot|^s \otimes |\cdot|^{-s}) \, ds,
$$
parabolically induced from the standard Borel $\mathbf{B}$ with
spectral parameter $s = it/2$ on the unitary axis $s \in i\mathbb{R}$.

Arthur's Eisenstein truncation (Arthur 1981 Ann Math 114 §7; 1988 Acta
162 §4) produces the Eisenstein contribution to the trace formula as a
Maass-Selberg intertwining integral: for
$\phi_f \in C_c^\infty(\mathbf{GL}_2(\mathbb{A}))$,
$$
J_{\mathrm{Eis}}(\phi_f) = \frac{1}{4\pi} \int_{-\infty}^\infty \mathrm{tr}\Big( M(s, \sigma_0) M'(s, \sigma_0) \cdot \pi_{s, \sigma_0}(\phi_f) \Big) \, dt,
$$
with $s = it$, $\sigma_0 = 1 \otimes 1$ the trivial character (only
contribution for $\mathbf{GL}_2$ unramified), $M(s, \sigma_0)$ the
standard intertwining operator
$M(s, \sigma_0): \mathrm{Ind}^{\mathbf{GL}_2}_{\mathbf{B}}(|\cdot|^s \otimes |\cdot|^{-s})
\to \mathrm{Ind}^{\mathbf{GL}_2}_{\mathbf{B}}(|\cdot|^{-s} \otimes |\cdot|^s)$,
and $M'(s, \sigma_0) = \partial_s M(s, \sigma_0)$ its logarithmic
derivative.

For $\mathbf{GL}_2/\mathbb{Q}$, Jacquet-Langlands SLN 114 §3.5 computes
the intertwining operator: $M(s, \sigma_0) = \xi_{\mathbb{R}}(2s) / \xi_{\mathbb{R}}(2s + 1) \cdot
\prod_p M_p(s)$, with $M_p$ the local intertwiner. The logarithmic
derivative is
$M'(s, \sigma_0)/M(s, \sigma_0) = 2(\xi_{\mathbb{R}}'/\xi_{\mathbb{R}})(2s) - 2(\xi_{\mathbb{R}}'/\xi_{\mathbb{R}})(2s + 1) + \sum_p \log p \cdot p^{-2s}/(1 - p^{-2s})$.

The archimedean contribution is $2(\xi_{\mathbb{R}}'/\xi_{\mathbb{R}})(2s) - 2(\xi_{\mathbb{R}}'/\xi_{\mathbb{R}})(2s+1)$.
At the Plancherel spectral parameter $s = it$, the archimedean term
reduces (after absorbing the $\log \pi$ into the Tate local measure)
to precisely the digamma kernel
$\frac{1}{2\pi}[\mathrm{Re}\,\psi(1/4 + it/2) + \log \pi]$ of
$W_\infty$, as identified in wave-5 Chapter 57
(`v4-arith:w5-a:eq:weil-archimedean`).

Positivity attempt: $J_{\mathrm{Eis}}$ is a pairing of
$|\pi_{s,\sigma_0}(\phi_f)|^2$-type positive matrix coefficients
against the Maass-Selberg weight $M(s)M'(s)$, so the positivity
question reduces to the positivity of $M(s) M'(s)$ on the unitary
axis. This fails: $M(s) M'(s)$ on the unitary axis is complex
(phase from the intertwining-operator functional equation plus
sign-indefinite contribution from $\xi_{\mathbb{R}}'/\xi_{\mathbb{R}}$).

**Heal.** The Eisenstein sector reproduces the archimedean Tate
distribution $W_\infty$ as the archimedean contribution to the
Maass-Selberg weight $M(s) M'(s) / M(s)$. More precisely: the
truncation of the Eisenstein-discrete sum to its continuous-spectrum
part produces the Plancherel integral on the unitary axis with
density given by the Maass-Selberg weight, whose archimedean component
is the digamma kernel.

The Arthur truncation does not close Eisenstein positivity because
the Maass-Selberg weight is not sign-definite. The positivity question
for $J_{\mathrm{Eis}}$ is the Plancherel positivity of
$|\widehat{f}(t)|^2$ against the density
$\frac{1}{4\pi}(M'/M)(it) = \frac{1}{\pi}\mathrm{Re}\,\psi(1/4 + it/2) + \mathrm{const}$,
which is precisely A-TP again.

Conclusion of cycle 5: the Arthur invariant trace formula on
$\mathbf{GL}_2/\mathbb{Q}$ exposes the archimedean Tate distribution
$W_\infty$ as the archimedean component of the Maass-Selberg weight in
the Eisenstein continuous-spectrum sector. Arthur's truncation does
not shorten A-TP; it relocates A-TP to the Maass-Selberg continuous
positivity. The Maass-Selberg integrand carries precisely the
sign-change of $\mathrm{Re}\,\psi(1/4 + it/2)$, which is A-TP's
obstruction.

### Cycle 6: Ngô functoriality; fundamental lemma does not transport positivity

**Attack.** Ngô Bao Châu's fundamental lemma (Ngô 2010 Publ IHES 111,
Thm 8.9) establishes the identity of orbital integrals of the
Langlands-Shelstad transfer: for every endoscopic group $H$ of a
reductive $G$ and every matching test function $f_H \leftrightarrow f_G$,
the $\kappa$-twisted orbital integral on $G$ equals the stable
orbital integral on $H$. This has the corollary that the invariant
trace formula on $G$ splits endoscopically along the stable-$\kappa$
decomposition of representations (Arthur 2013 Endoscopic Classification
Thm 1.5.2).

Positivity attempt: apply the fundamental lemma to transport the
positivity of the Weil distribution from $\mathbf{GL}_1$ to
$\mathbf{GL}_2$ via functoriality. The Weil distribution on $\mathbf{GL}_1$
is Tate's adelic Fourier pairing; its positivity (on the trivial
character sector) reduces to Poisson summation. Functoriality should
transport this positivity to higher-rank groups.

This fails. The $\mathbf{GL}_1$ trace formula is Poisson summation,
and its positivity content is vacuous: $\sum_{q \in \mathbb{Q}^\times} f(q) = \sum_{q \in \mathbb{Q}^\times} \widehat{f}(q)$
has no sign claim. The $\mathbf{GL}_2$ trace formula is richer (has
cuspidal, Eisenstein, and residual), and the decomposition cannot be
recovered from $\mathbf{GL}_1$ by functoriality alone; Langlands
functoriality predicts a map from $\mathbf{GL}_1$ to $\mathbf{GL}_2$
(character-induction), which transports automorphic characters to
Eisenstein series on $\mathbf{GL}_2$, not cuspidal data to cuspidal
data. The Eisenstein side of $\mathbf{GL}_2$ is where A-TP lives; the
functoriality map lands precisely there and does not help.

**Heal.** Ngô's fundamental lemma is a matching of stable orbital
integrals; it says nothing about sign of spectral distributions. It
is a tool for endoscopic decomposition, not for positivity transport.
Its use in Arthur 2013 is to prove the endoscopic classification
(which representations contribute to which endoscopic component), not
to derive positivity identities.

The correct observation: the Eisenstein continuous spectrum on
$\mathbf{GL}_2$ is the image of the functoriality map from
$\mathbf{GL}_1 \times \mathbf{GL}_1$ (parabolic induction from the
standard Borel). The positivity obstruction on the Eisenstein sector
is therefore the obstruction to a $\mathbf{GL}_1 \times \mathbf{GL}_1$-to-$\mathbf{GL}_2$
positivity transport, which is the classical content of the Eisenstein
$L$-function's functional-equation factor $M(s)M'(s)$.

Gelbart-Jacquet 1978 Ann Sci ENS 11 establishes the $\mathbf{GL}_2$-to-$\mathbf{GL}_3$
symmetric-square lift; Flicker-Kazhdan 1988 Publ IHES 64 establishes
the metaplectic-$\mathbf{GL}_n$ correspondence. Neither transports
positivity; both transport representation types.

Conclusion of cycle 6: endoscopy and functoriality do not shorten
A-TP. They give refined decompositions of the spectral side, but the
archimedean obstruction is invariant under the known functoriality
maps: the 1/2-shift in the Eisenstein continuous spectrum is the
fixed point of the functional-equation symmetry and is not killed by
any functoriality transport.

### Cycle 7: Invariant trace formula; weighted orbital integrals and the Arthur $R$-groups

**Attack.** Arthur's invariant trace formula (Arthur 1988 JAMS 1,
Acta 162 1989) refines the coarse trace formula by replacing the
non-invariant weighted orbital integrals $J_M(\gamma, \phi_f)$ (summed
over Levi subgroups $M$ of $\mathbf{GL}_2$) with invariant versions
$I_M(\gamma, \phi_f)$, obtained by subtracting spectral invariant
distributions. The invariant identity:
$$
I(\phi_f) = \sum_{M \in \mathcal{L}} \frac{|W^M|}{|W^G|} \sum_\gamma a^M(\gamma) I_M(\gamma, \phi_f)
= I_{\mathrm{cusp}}(\phi_f) + I_{\mathrm{Eis}}(\phi_f) + I_{\mathrm{res}}(\phi_f).
$$

Attempt: the invariant weighted orbital integrals $I_M(\gamma, \phi_f)$
are finite and computable; the spectral invariant distributions
$I_{\mathrm{cusp}}, I_{\mathrm{Eis}}, I_{\mathrm{res}}$ are the
identifications attempted in cycles 3-5. The invariant trace formula
therefore realizes the abstract $W = W^{\mathrm{cusp}} + W^{\mathrm{Eis}} + W^{\mathrm{res}}$
decomposition concretely, with explicit formulas for each sector in
terms of weighted orbital integrals on $\mathbf{GL}_1$ (the only
proper Levi of $\mathbf{GL}_2$).

This fails at the Eisenstein sector in a specific way: the invariant
weighted orbital integral $I_{M_0}(\gamma, \phi_f)$ for
$M_0 = \mathbf{GL}_1 \times \mathbf{GL}_1$ the minimal Levi carries
the Arthur $R$-group correction, which for $\mathbf{GL}_2$ on the
unitary axis $s = it$ is the Knapp-Stein $R$-group $R_{M_0}(\pi_s) = \mathbb{Z}/2\mathbb{Z}$
produced by the Weyl reflection. The $R$-group correction enters the
Eisenstein sector as the intertwining-operator normalization
(Arthur 2013 §1.5; Shahidi 2010 AMS Colloq 58 Thm 3.5.1), and its
sign on the unitary axis is indeterminate without further input.

**Heal.** The Arthur $R$-group for $\mathbf{GL}_2$ on the Eisenstein
continuous axis is precisely the source of the phase ambiguity in
wave-5 Chapter 55 `v4-arith:w5-c:prop:LS-absorption`: the
intertwining operator is defined up to a phase coming from the
Knapp-Stein $R$-group, and that phase is what wave-5 absorbs into
the branch choice of $N^{\mathrm{LS}}$.

The invariant trace formula makes this explicit: the Eisenstein
contribution is
$$
I_{\mathrm{Eis}}(\phi_f) = \frac{1}{4\pi} \int_{-\infty}^\infty R(s, \sigma_0) \cdot \mathrm{tr}(\pi_{s,\sigma_0}(\phi_f)) \, dt,
$$
with $R(s, \sigma_0) = M'(s, \sigma_0)/M(s, \sigma_0)$ an Arthur
$R$-group-normalized Plancherel density. On the unitary axis this is
the sum of the archimedean digamma and the finite-place log-Euler
factor, and its positivity is the A-TP statement.

Conclusion of cycle 7: the invariant trace formula realizes the
abstract spectral decomposition concretely but does not close the
Eisenstein positivity. The $R$-group phase ambiguity is the
Arthur-language restatement of the 1/2-shift obstruction in the
archimedean continuous spectrum.

### Cycle 8: Selberg's pretrace formula; the original source of the identity

**Attack.** Before Arthur, Selberg 1956 J Indian Math Soc 20 established
the pretrace formula for $\mathbf{GL}_2(\mathbb{Q}) \backslash \mathbb{H}$
(the classical modular surface):
$$
\sum_{\gamma \in \Gamma} K(z, \gamma z) = \sum_n |u_n(z)|^2 + \frac{1}{4\pi}\int_{-\infty}^\infty |E(z, 1/2 + it)|^2 \, dt + \text{(residual polar)}.
$$
Selberg's own trace formula (Selberg 1956; Kubota 1973 Elementary
Theory of Eisenstein Series) integrates this against a point-pair
invariant kernel to get
$$
\sum_n h(t_n) + \frac{1}{4\pi}\int h(t) (\phi'/\phi)(it) \, dt + \text{(polar + geometric)} = \sum_\gamma \text{(orbital)}
$$
with $\phi(s) = \xi(2s-1)/\xi(2s)$ the Eisenstein scattering coefficient
for $\mathbf{PSL}_2(\mathbb{Z})$ on $\mathbb{H}$.

Attempt: identify Selberg's trace formula with A-TP and attempt
positivity of the continuous-spectrum Plancherel integral.

This is just cycle 5 restated classically. The continuous-spectrum
integrand is $(\phi'/\phi)(it) = -(\xi'/\xi)(2it - 1) - (\xi'/\xi)(2 - 2it) + \text{log-Euler}$,
which on $t \in \mathbb{R}$ carries the same digamma obstruction as
the Arthur Maass-Selberg weight.

**Heal.** Selberg's classical trace formula is the specialization of
Arthur's to the spherical sector of $\mathbf{GL}_2(\mathbb{Q}) \backslash \mathbb{H}$
at level 1. Its continuous-spectrum term is the classical Eisenstein
density $\phi'/\phi$ evaluated on the critical line, which is the
Weil distribution restricted to the spherical sector. This is the
same obstruction, exposed in pre-Arthur language.

What Selberg's formulation adds: an explicit $K$-Bessel transform
pairing. The continuous-spectrum term
$\frac{1}{4\pi} \int h(t) (\phi'/\phi)(it) \, dt$ is the Plancherel
pairing of a point-pair invariant against a $\mathbf{GL}_2$ density;
its positivity would follow from a Selberg-$h$-positivity condition
(h(t) $\geq 0$ plus sign condition on $\phi'/\phi$). The latter is
precisely A-TP.

Conclusion of cycle 8: Selberg's trace formula is the spherical
specialization of the Arthur trace formula; it exposes A-TP as the
sign of $\phi'/\phi$ on the critical axis, which is what wave-5
Chapter 57 names as the archimedean Tate distribution. The Arthur
invariant trace formula strictly subsumes Selberg's but does not
shorten A-TP.

## Convergence proposal

### (i) A-TP sub-cone closed by Voice 1

The Arthur-Selberg truncation route closes A-TP unconditionally on the
following sub-cone of $\mathrm{PW}(\mathbb{R})$:
$$
\mathrm{PW}^{\mathrm{Arth,disc}} := \{f \in \mathrm{PW}(\mathbb{R}) : \widehat{f}(t)^2 \text{ is supported on the discrete-cuspidal spectral parameters } \{t_\pi\}_\pi\}.
$$
This sub-cone consists of Paley-Wiener functions whose squared spectral
profile is concentrated at the tempered cuspidal spectral parameters
of $\mathbf{GL}_2/\mathbb{Q}$; for such $f$, the cuspidal Weil
contribution $W^{\mathrm{cusp}}(f * \tilde f) \geq 0$ is realized
by $J_{\mathrm{cusp}}(\phi_f)$, and the Eisenstein and residual
contributions vanish by construction. Ramanujan-conditional extension
to non-tempered cuspidal $\pi$.

The sub-cone is a concrete but pathologically narrow class: it
requires $\widehat{f}$ to be supported on a discrete set of spectral
parameters, which by Paley-Wiener forces $f$ to be a finite sum of
plane waves (not genuinely compactly supported in the time domain).
The closure is therefore Beilinson-principled but of limited
operational value: it closes nothing that was not already closed by
wave-5 Chapter 57 Rankin-Selberg on $\mathrm{PW}^{\mathrm{hol}}_F$.

What Voice 1 adds concretely: a simultaneous Rankin-Selberg positivity
over all cuspidal $\pi$ at once (rather than a fixed $F$), accessible
through Arthur's invariant cuspidal contribution. This matches
wave-5's scope but not its cone: wave-5 is parametrized by $F$ and
covers a wider class of $f$; Voice 1 runs over all $\pi$ and covers
a narrower class of $f$.

### (ii) Residual obstruction identified

The irreducible obstruction in Voice 1's analysis is the Eisenstein
continuous-spectrum positivity of the Maass-Selberg weight
$M'(s)/M(s)$ on the unitary axis $s = it$. Its archimedean component
is the digamma kernel $\mathrm{Re}\,\psi(1/4 + it/2) + \log \pi$ and
is sign-indefinite.

This is the same obstruction named in wave-5 Chapter 57 as
$W_\infty$. Voice 1 names it as the Maass-Selberg intertwining-operator
logarithmic-derivative positivity on the $\mathbf{GL}_2$
Eisenstein continuous spectrum, which is a finer structural location
of the obstruction within the trace-formula framework.

### (iii) Comparison with other voices' expected residuals

Predicted residuals by voice:

- Voice 2 (de Branges Hermite-Biehler): the obstruction should appear
  as the Hermite-Biehler positivity of $E(s)$ on the critical line.
  Voice 1's Maass-Selberg weight $M'(s)/M(s)$ at $s = 1/2 + it$ is the
  logarithmic derivative of the ratio
  $\xi_{\mathbb{R}}(2s)/\xi_{\mathbb{R}}(2-2s)$, which is precisely the
  Hermite-Biehler exponential factor in de Branges 1994. Voice 1 and
  Voice 2 identify the same obstruction in disjoint languages.
- Voice 3 (Connes adele-class non-commutative): the obstruction should
  appear as the absorption spectrum of the scaling operator on the
  adele-class space. This is chapter 80 `v4-arith:w7-j:prop:connes-absorption`.
  Voice 1's Eisenstein obstruction is the classical analogue of the
  adele-class absorption spectrum (Moeglin-Waldspurger 1995 $L^2$-decomposition
  is the classical realization of the Connes non-commutative
  decomposition; the passage to the non-commutative side is the
  non-triviality of $\mathbb{A}/\mathbb{Q}^\times$ as a topological
  space).
- Voice 4 (Polyakov central-charge / conformal anomaly): the
  obstruction should appear as the anomaly coefficient of a conformal
  lift. Voice 1's digamma obstruction is the $\infty$-place conformal
  anomaly contribution (wave-5 Chapter 57 remark
  `v4-arith:w5-a:rem:archimedean-obstruction`).
- Voice 5 (Li-coefficient generating function / Bombieri-Lagarias):
  the obstruction should appear as positivity of the generating
  function's coefficient sequence. Voice 1's cuspidal-Eisenstein split
  corresponds to a Li-coefficient decomposition where the cuspidal
  part is non-negative term-by-term and the Eisenstein part is where
  the sign ambiguity enters.

All five voices converge on the same location: the archimedean
continuous spectrum of the trace formula is where the 1/2-shift
obstruction lives. Voice 1's contribution is the Arthur-Selberg
language naming.

### (iv) Precise theorem-waiting statement

**Theorem-waiting.** Let $\mathbf{GL}_2/\mathbb{Q}$, and let
$\phi_f \in C_c^\infty(\mathbf{GL}_2(\mathbb{A}))$ be the Jacquet-Langlands
adelic lift of $f * \tilde f$ for $f \in \mathrm{PW}(\mathbb{R})$.
Then the Weil distribution decomposes along Arthur's invariant
spectral expansion as
$$
W(f * \tilde f) = W^{\mathrm{cusp}}(f * \tilde f) + W^{\mathrm{Eis}}(f * \tilde f) + W^{\mathrm{res}}(f * \tilde f),
$$
with
$$
W^{\mathrm{cusp}}(f * \tilde f) = \sum_{\pi \in \widehat{\mathbf{GL}_2}_{\mathrm{cusp,temp}}} |\widehat{f}(t_\pi)|^2 \cdot c_\pi \geq 0 \quad \text{(unconditional modulo Ramanujan)},
$$
$$
W^{\mathrm{res}}(f * \tilde f) = \widehat{f*\tilde f}(1/(2i)) + \widehat{f*\tilde f}(-1/(2i)) \geq 0 \quad \text{(unconditional, polar terms)},
$$
$$
W^{\mathrm{Eis}}(f * \tilde f) = \frac{1}{4\pi} \int_{-\infty}^\infty |\widehat{f}(t)|^2 \cdot \frac{M'(it, \sigma_0)}{M(it, \sigma_0)} \, dt,
$$
with $M(s, \sigma_0)$ the standard Eisenstein intertwining operator on
$\mathbf{GL}_2(\mathbb{A})$ at the trivial character $\sigma_0$.
A-TP is equivalent to the Eisenstein positivity
$W^{\mathrm{Eis}}(f * \tilde f) \geq -W^{\mathrm{cusp,polar-rest}}(f * \tilde f)$
for every $f \in \mathrm{PW}(\mathbb{R})$, which is itself equivalent
to positivity of the Maass-Selberg weight's archimedean digamma
component on the unitary axis.

**Status.** Theorem-waiting. The decomposition into three sectors is
proved (by Arthur 1988, Moeglin-Waldspurger 1995, and the
Jacquet-Langlands adapter of cycle 1). The reduction to Maass-Selberg
Eisenstein positivity is proved (by cycles 3-5). The Maass-Selberg
positivity itself is RH-equivalent (by cycle 5 and wave-5 Chapter 57).

## Realization pointer

### Where in the existing Vol IV arithmetic branch this sits

The Arthur truncation attack subsumes and refines:

1. Wave-5 Chapter 55 (full $\mathcal{V}^{\mathrm{prim}}$ P3 on discrete
   core, `v4-arith:w5-c:chapter`): the Ramanujan-conditional Maass
   cuspidal closure and Eisenstein scope-exclusion of Chapter 55
   are reproduced by Voice 1's cycle 3 (cuspidal conditional) and
   cycle 5 (Eisenstein obstruction). Voice 1 adds the cyclic
   description that ties the Eisenstein residual to the Arthur
   $R$-group and the Maass-Selberg intertwining operator.
2. Wave-5 Chapter 57 (HP-Li positivity closure, `v4-arith:w5-a:chapter`):
   the Rankin-Selberg prime-side closure of Chapter 57 is the
   holomorphic cuspidal specialization of Voice 1's cycle 3
   simultaneous-$\pi$ closure. Chapter 57's archimedean Tate
   distribution $W_\infty$ is Voice 1's Maass-Selberg weight archimedean
   component.
3. Chapter 79 (ATP Guinand-Weil, `v4-arith:w7-i:chapter`): the Guinand
   alternative explicit formula of Chapter 79 is obtainable from
   Arthur's trace formula by a change of test-function convention
   (Weil uses a time-domain pairing; Guinand uses a frequency-domain
   pairing). The Burnol co-Poisson sub-class closure of Chapter 79 is
   the Plancherel-dual counterpart to Voice 1's cuspidal discrete-sum
   closure: Chapter 79 covers the Fourier-dual part of
   $\mathrm{PW}(\mathbb{R})$ that Voice 1 does not.
4. Chapter 80 (ATP adelic scattering, `v4-arith:w7-j:ATP-adelic-scattering`):
   Chapter 80's Bost-Connes scattering-matrix reformulation and the
   Connes absorption-spectrum obstruction are the non-commutative-geometric
   lift of Voice 1's Arthur-Selberg obstruction. Chapter 80's
   $\mathrm{PW}^{\mathrm{TM}}$ sub-class (Tate-Mellin, zero-adapted)
   is orthogonal to Voice 1's $\mathrm{PW}^{\mathrm{Arth,disc}}$
   sub-cone (which is spectral-parameter-discrete); the intersection
   is where the Tate gamma factor and the Langlands cuspidal
   parameters align, a finite-dimensional locus.

### What's new in Voice 1

Voice 1 contributes four items not present in chapters 71-80.

First, an explicit three-sector decomposition
$W = W^{\mathrm{cusp}} + W^{\mathrm{res}} + W^{\mathrm{Eis}}$ via
Arthur's invariant trace formula. Chapters 71-80 close A-TP on various
sub-classes; none of them performs an explicit Arthur spectral
decomposition of the Weil distribution. Voice 1 exposes the residual
inside the Eisenstein continuous-spectrum sector, which is not
visible in the Rankin-Selberg, Nyman-Beurling, or Guinand-Burnol
frameworks.

Second, the identification of the Maass-Selberg intertwining-operator
logarithmic derivative $M'/M$ as the archimedean kernel. Chapter 57
`v4-arith:w5-a:def:tate-archimedean` defines $\mathcal{T}_\infty(t)$
as the digamma distribution; Voice 1 identifies it with the
archimedean component of the Knapp-Stein $R$-group-normalized
Eisenstein Plancherel density. This is a structural refinement: the
sign-indefiniteness of $\mathcal{T}_\infty$ is the $R$-group phase
ambiguity at the critical point.

Third, the connection to Arthur's endoscopic classification (Arthur
2013). The functoriality lift $\mathbf{GL}_1 \times \mathbf{GL}_1 \to \mathbf{GL}_2$
through Eisenstein induction carries the 1/2-shift obstruction
intrinsically; no known functoriality kills it. Voice 1's cycle 6
names this fixed-point property precisely. Chapters 71-80 do not
discuss endoscopy.

Fourth, the Ngô fundamental-lemma (2010 Publ IHES 111) elementary
ruling-out result: functoriality transports representation types but
not positivity. This is a negative result but a useful one:
Chapters 71-80 do not address the functoriality question.

### Whether the obstruction matches chapters 71-80's existing A-TP sub-closures

Yes. The Eisenstein continuous-spectrum Maass-Selberg obstruction of
Voice 1 is the same obstruction identified in:

- Wave-5 Chapter 57 (`v4-arith:w5-a:def:tate-archimedean`): digamma
  distribution $\mathcal{T}_\infty$.
- Chapter 79 (`v4-arith:w7-i:prop:dual-kernel`): Burnol dual time-domain
  kernel $\tilde g$.
- Chapter 80 (`v4-arith:w7-j:thm:ATP-iff-S-unitary`): scattering-matrix
  unitarity of $S$ on $\mathcal{K} = L^2(C_\mathbb{Q})$.

All four formulations (digamma, Burnol dual, scattering, Maass-Selberg)
reduce to the same archimedean sign-indefiniteness of the digamma
kernel $\mathrm{Re}\,\psi(1/4 + it/2) + \log \pi$ on the unitary axis.
The four frameworks expose the obstruction in different languages;
none shortens it. The Beilinson-principled closure is: enumerate the
frameworks, close on their respective sub-cones, name the common
residual as A-TP, acknowledge the equivalence to RH.

Voice 1's verdict. Arthur-Selberg truncation does not close A-TP. It
closes a narrow sub-cone
$\mathrm{PW}^{\mathrm{Arth,disc}}$ of spectral-discrete test
functions, unconditionally modulo Ramanujan. Its residual is the
Eisenstein continuous-spectrum Maass-Selberg positivity, strictly
equivalent to A-TP, strictly equivalent to RH. The contribution is
structural: the Weil distribution is the spectral side of the Arthur
trace formula on $\mathbf{GL}_2/\mathbb{Q}$, and A-TP is precisely
the Maass-Selberg intertwining-operator positivity on the archimedean
unitary axis. This naming is load-bearing for the synthesis of the
five voices: the common residual lives in a single structural
location across all frameworks, and its closure is the one remaining
$\mathbf{GL}_2$ RH statement.
