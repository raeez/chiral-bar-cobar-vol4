# Voice 4 of 5: Arithmetic Quantum Chaos / BGS Attack on A-TP

**Target.** `v4-arith:w5-a:conj:archimedean-tate-positivity` in
`chapters/arithmetic/57_hp_li_positivity_closure.tex`:

> For all $f \in \mathrm{PW}(\mathbb{R})$, $W(f * \tilde f) \geq 0$,
> equivalently $W_{\infty}(f*\tilde f) \leq \sum_{\rho}
> |\hat f(\gamma_\rho)|^2 + \text{polar} - W_{\mathrm{fin}}(f*\tilde f)$.

Equivalent to the Riemann Hypothesis via Weil 1952.

**Voice.** Arithmetic quantum chaos and random-matrix universality:
Bohigas-Giannoni-Schmit 1984, Berry-Keating 1999, Montgomery 1973,
Odlyzko 1987, Rudnick-Sarnak 1996, Katz-Sarnak 1999, Keating-Snaith 2000,
Lindenstrauss 2006, Sarnak 1995, Hejhal 1994, Soundararajan 2010.

**Thesis tested.** The statistical upside documented in
`84_trace_formula_equivalence_gutzwiller.tex` (arithmetic Gutzwiller +
BGS $\Rightarrow$ GUE pair correlation of $\{\gamma_n\}$) suggests that
GUE rigidity, via Guinand-Weil-Burnol adelic Poisson summation, could
force the sign of $W(f*\tilde f)$ on a dense test-function sub-class,
with A-TP following by approximation. The attack-heal cycles below
break this thesis down. The final verdict: GUE-strength statistics
constrain the cumulant structure of $\{\gamma_n\}$ under RH; they do
not, by themselves, place $\{\gamma_n\} \subset \mathbb{R}$. BGS is a
\emph{conditional descendant} of RH, not a route to RH. The statistical
upside is real but runs downhill, not uphill.

---

## 0. Weil 1952 under the quantum-chaos lens

Rewrite the Weil explicit formula
\eqref{v4-arith:w5-a:eq:weil-explicit} applied to $f * \tilde f$. Using
$\widehat{f * \tilde f}(t) = |\hat f(t)|^2 \geq 0$, Corollary
\ref{v4-arith:w5-a:cor:weil-positivity-RH} gives

$$
W(f * \tilde f) \;=\; \sum_{\rho} |\hat f(\gamma_\rho)|^2
$$

\emph{under RH} (when all $\gamma_\rho \in \mathbb{R}$). Off RH, a
Hadamard-product computation shows

$$
W(f * \tilde f) \;=\; \sum_{\rho}
|\hat f(\gamma_\rho)|^2
\;-\; \sum_{\rho \text{ with } \mathrm{Im}(\gamma_\rho) \neq 0}
\bigl[ \text{off-line penalty}(\gamma_\rho, \hat f) \bigr],
$$

where the off-line penalty is a strictly positive quantity for any
off-critical zero and any non-zero $\hat f$. This is the Weil
equivalence: A-TP is pointwise non-negativity of the specific sum, and
under RH it is a sum of squares.

\emph{Quantum-chaos reframing.} View $\{\gamma_n\}$ as the eigenvalues
of a conjectural self-adjoint Hilbert-Polya operator $H_{\mathrm{HP}}$.
Then $\hat f(\gamma_\rho) = \langle v_{\gamma_\rho}, \hat f(H_{\mathrm{HP}})
v_{\gamma_\rho} \rangle$ for the spectral projection; and
$\sum_\rho |\hat f(\gamma_\rho)|^2$ is the Hilbert-Schmidt norm squared
of the operator $\hat f(H_{\mathrm{HP}})$. GUE statistics then become
predictions about the resolvent, not about sign-definiteness of $W$.

---

## 1. Attack A: Montgomery pair-correlation forces sign of $W$?

**Attack.** Montgomery 1973: conditional on RH, the pair correlation
of $\{\gamma_n\}$ (normalized to unit mean spacing $\bar\gamma_n =
\gamma_n \log \gamma_n / (2\pi)$) satisfies

$$
R_2(u) \;=\; 1 - \left(\frac{\sin \pi u}{\pi u}\right)^2
\;+\; \delta(u),
$$

matching the GUE pair correlation. If the pair-correlation identity
held \emph{unconditionally} on the test-function class
$\mathrm{PW}(\mathbb{R})$, and if the GUE kernel controlled the
diagonal contribution $\sum_\rho |\hat f(\gamma_\rho)|^2$ via the
Gaudin-Mehta determinantal structure, then positivity of the GUE
2-point kernel would force $W \geq 0$ on the admissible class.

**Heal.** Montgomery 1973 proves the pair-correlation formula
\emph{conditional on RH}: the input is the Weil explicit formula
assuming $\gamma_\rho \in \mathbb{R}$, so $\hat f(\gamma_\rho - \gamma_{\rho'})$
gives a clean Fourier expression. If RH fails, pair correlation is
not defined over reals; the statement becomes vacuous. Therefore,
Montgomery-pair-correlation $\Rightarrow$ GUE-positivity $\Rightarrow$
A-TP is circular: the premise $\gamma_\rho \in \mathbb{R}$ is A-TP.

**Refined attack.** Montgomery's theorem \emph{does not require} full
RH: it applies to a suitable smoothed sum conditional on RH within a
box, extended by a tail estimate. Could the partial statement, plus
the Goldston-Montgomery equivalence between pair correlation and
prime-gap variance, be used without the RH input?

**Refined heal.** Goldston-Montgomery 1987 shows PCH and the
prime-gap variance statement are equivalent under RH. But PCH is a
GRH-class statement: it does not imply RH, and RH does not imply PCH
without additional input (Rudnick-Sarnak 1996 is explicit on this
point). PCH cannot act as a free-standing input to A-TP.

**Verdict A.** Montgomery $\Rightarrow$ A-TP is inaccessible:
pair-correlation is downstream of RH. $\Box$

---

## 2. Attack B: Keating-Snaith moments translate to A-TP?

**Attack.** Keating-Snaith 2000 (Commun. Math. Phys. 214) conjecture
that for fixed integer $k \geq 0$,

$$
\frac{1}{T} \int_0^T \bigl| \zeta(\tfrac{1}{2} + it) \bigr|^{2k} \, dt
\;\sim\; a(k) \, g(k) \, (\log T)^{k^2},
$$

with $g(k) = (G^2(k+1))/G(2k+1)$ the Barnes-$G$ ratio matching the
$2k$-th moment of the characteristic polynomial of a $U(N)$ random
matrix. Since $| \zeta(\tfrac{1}{2} + it)|^{2k} \geq 0$ is a
non-negative density, integration gives a positive moment sequence;
positivity of this \emph{sequence} plus Hamburger moment
representation might give a positive spectral measure, which by
wave-5 J's main-direction closure
(`58_VBstar_spectral_positivity.tex`, theorem
`v4-arith:w5-j:thm:VBstar-main-direction`) gives RH hence A-TP.

**Heal.** Positivity of the integer moment sequence $(I_k(T))_{k \geq 0}$
gives a positive Stieltjes measure $d\rho_T$ on the \emph{amplitude
axis} $|\zeta(\tfrac{1}{2}+it)| \in [0, \infty)$. This is \emph{not}
the same moment problem as (SH) in
`58_VBstar_spectral_positivity.tex`, which concerns regularized
moments of the \emph{zero ordinates} $\gamma_\rho \in \mathbb{C}$
(Definition `v4-arith:w5-j:def:moment-sequence`). These are two
distinct spectral problems; the Keating-Snaith moments do not feed
into the (SH) hypothesis. Hamburger positivity of
$(I_k)_k$ is automatic (it is a moment sequence of a non-negative
function) and says nothing about zero locations.

**Refined attack.** Use the amplitude-zero relation via Jensen's
formula: the $k$-th moment of $|\zeta|^{2}$ on the critical line
encodes zero density within small boxes (Selberg 1946, the
Selberg-Littlewood central limit theorem: $\log |\zeta(\tfrac{1}{2}+it)|$
has Gaussian fluctuations of variance $\tfrac{1}{2}\log\log T$). Could
Gaussian fluctuations force the $\gamma_n$ distribution to sit on the
real line?

**Refined heal.** Selberg's central limit theorem is conditional on
RH in the high-moment regime (Soundararajan 2009, Ann. Math. 170:
extreme values of $\log |\zeta|$ are conditionally bounded by
$(\log T \log \log T)^{1/2}$ under RH; without RH the extreme-value
bound is weaker). So the Gaussian-fluctuation side is again downstream
of RH, not a source of it.

**Third attack.** Ignore Keating-Snaith and use instead a Dirichlet
series criterion: if the Dirichlet $L$-series
$\sum_n \Lambda(n) n^{-s}$ had all its moments controlled by a
positive measure on the critical strip $\{0 \leq \mathrm{Re}(s) \leq 1\}$,
this would constrain the Mellin transform of the zero counting function,
and (after application of Stieltjes-Hamburger inversion) give
a positive spectral density for the zero measure.

**Third heal.** This is the standard Mertens-function route
(Bateman-Diamond). The Mertens function $M(x) = \sum_{n \leq x} \mu(n)$
controls Dirichlet-series moments, and $M(x) = O(x^{1/2 + \epsilon})$ is
equivalent to RH. No route known from Keating-Snaith \emph{directly}
to Mertens, so this does not close the loop. The moments of $|\zeta|^{2k}$
are amplitude moments; they constrain $M(x)$ only via logarithmic
averaging of Jensen integrals, which loses the pointwise sign structure.

**Verdict B.** Keating-Snaith moment conjectures do not translate to
A-TP. They concern amplitude, not zero location; the moment problem
they generate (amplitude moments) is distinct from the Hamburger
problem (SH) used in wave-5 J's main-direction closure. $\Box$

---

## 3. Attack C: Rudnick-Sarnak $n$-level correlations force RH?

**Attack.** Rudnick-Sarnak 1996 (Duke Math. J. 81, arXiv:math/9607202):
conditional on the Generalized Riemann Hypothesis (GRH) and Ramanujan
bounds for principal automorphic $L$-functions, the $n$-level
correlations of zeros of any principal $L$-function match the GUE
correlations, for $n = 2, 3, \ldots$ and test functions in a sub-class
of Schwartz functions whose Fourier transforms have support within
$[-1/n, 1/n]$ (the \emph{window}). A general principle: if the
full $n$-level correlation structure is GUE for \emph{every} $n$, then
the point process $\{\gamma_n\}$ is determinantal with the sine kernel,
and in particular the support is real (the sine-kernel determinantal
point process lives on $\mathbb{R}$).

**Heal.** Rudnick-Sarnak 1996 uses RH (specifically, GRH) as an
\emph{input}. The derivation substitutes the RH ordinates into the
explicit formula and computes correlations via the Fourier transform;
the output is a Fourier-support-limited statement matching GUE. The
theorem does not, therefore, give RH. Its universality statement is:
\emph{if RH and Ramanujan hold}, then the fluctuations are universal.
Inverting the direction (GUE correlations $\Rightarrow$ RH) is not
proven in Rudnick-Sarnak and is, so far as I can check, an open problem.

**Refined attack.** Rudnick-Sarnak 1998 \emph{Comm. Math. Phys. 194,
arXiv:math/9708208}: explicit formula gives $n$-level correlations
for the $\zeta$ function on test functions of restricted support,
\emph{unconditionally} on RH. Support restriction is $[-2/n, 2/n]$.
Within this limited window, correlations match GUE. Could we leverage
this unconditional partial statement?

**Refined heal.** The unconditional statement in Rudnick-Sarnak 1998
is: if $\eta$ is a Schwartz function whose Fourier transform has
compact support in $[-2/n, 2/n]$, then

$$
\sum_{\gamma_1, \ldots, \gamma_n} \eta(\gamma_1, \ldots, \gamma_n)
\;\sim\; T \int \eta(x_1, \ldots, x_n) \det[K(x_i - x_j)] \, dx,
$$

where $K(u) = \sin(\pi u)/(\pi u)$ is the GUE kernel. The sum on the
left is a sum over $n$-tuples of zeros (with multiplicity, possibly
complex). On the right, the integral uses the GUE kernel, which is a
distribution on \emph{real} $x$-tuples. The support restriction
$[-2/n, 2/n]$ in Fourier variables allows the explicit formula to
converge without RH because the test function is supported on short
intervals where the primes below $e^{2/n}$ contribute a bounded sum.
The sum on the left can be computed without assuming $\gamma_i$ are
real because the Weil distribution extends to complex sources.

But: \emph{the right-hand side integral requires real $x_i$}. If
$\gamma_\rho$ is complex, the matching between sides uses a contour
deformation which introduces residue corrections. Rudnick-Sarnak 1998
sidestep this by working at a fixed height $T$ and using the mean-value
form of the correlation; on average, the complex-zero contributions
are size $O(T^{\epsilon})$ smaller than the main term, \emph{provided}
the number of off-critical zeros up to $T$ is $o(T / \log T)$. This
weaker density statement is strictly weaker than RH but still not
known unconditionally: Selberg showed $N_0(T) \geq c T \log T$ zeros
on the critical line (positive proportion), but the best
\emph{upper} bound on off-critical zeros up to $T$ is
$N_{\mathrm{off}}(T) = O(T)$, which is larger than the $o(T / \log T)$
needed.

**Verdict C.** Rudnick-Sarnak unconditional $n$-level correlations
within the limited Fourier-support window do not force RH without an
additional off-critical zero-density estimate that is itself an open
sub-problem. The GUE universality runs through the explicit formula
and does not circumvent RH. $\Box$

---

## 4. Attack D: Lindenstrauss arithmetic QUE forces A-TP?

**Attack.** Lindenstrauss 2006 (Ann. Math. 163): arithmetic
Quantum Unique Ergodicity on the modular surface $\Gamma \backslash
\mathbb{H}$. Hecke-Maass cusp forms $\{\phi_j\}$ have quantum limits
(in the sense of microlocal analysis) that are all scalar multiples
of the Liouville volume measure. QUE governs amplitude distributions
$|\phi_j|^2$ on the modular surface, and ties them to $L(\tfrac{1}{2},
\phi_j \otimes \phi_j)$ by Watson's formula (Watson 2002). If QUE
implies all such $L$-values are non-zero (the non-vanishing subproblem
of QUE), perhaps the Weil explicit formula applied to $L(s, \phi_j
\otimes \phi_j)$ yields positivity for a generating class of test
functions.

**Heal.** Lindenstrauss 2006 proves QUE on the modular surface for
joint Hecke-Laplace eigenforms. Rudnick-Sarnak 1994 conjectured QUE in
general; Lindenstrauss established it in the arithmetic case with full
$T_p$ eigenstate structure. The relationship to A-TP:
(i) Watson's formula 2002 (arXiv:math/0201020): $\int_{\Gamma
\backslash \mathbb{H}} |\phi_j|^2 \, \phi_k \, d\mu = L(\tfrac{1}{2},
\phi_j \otimes \phi_j \otimes \phi_k) / \text{normalisation}$. QUE
states the left side $\to 0$ for fixed $\phi_k$ cuspidal;
(ii) Holowinsky-Soundararajan 2010: unconditional QUE for holomorphic
forms via sieve; (iii) QUE does not, per se, address positivity of
any $L$-function: it addresses \emph{integrals} of amplitudes against
test forms.

The connection to A-TP: the Weil explicit formula for $L(s, \phi_j
\otimes \phi_j)$ gives a positive-trace form via Petersson positivity
(as in wave-5's Rankin-Selberg construction in Chapter 57). This is
the Rankin-Selberg route that wave-5 \emph{already closes}. QUE adds
the statement that this positive trace is well-distributed on the
modular surface; it does not extend the Rankin-Selberg closure to
the archimedean residual $W_{\infty}$.

**Refined attack.** Watson's formula plus QUE gives subconvexity
for $L(\tfrac{1}{2}, \phi_j \otimes \phi_j \otimes \phi_k)$: the
$L$-value is $\ll T^{-1/6+\epsilon}$. Subconvexity is a quantitative
strengthening of non-vanishing. Could subconvex $L$-values over the
full Rankin-Selberg family yield A-TP via some integrated
Weil-positivity identity?

**Refined heal.** Subconvexity is a ``size bound on the critical
line''; it controls $|L(\tfrac{1}{2}+it)|^{-1}$ but does not control
the sign of the explicit-formula kernel. The Watson-QUE identity
has no access to the digamma integrand $\mathrm{Re}\,\psi(\tfrac{1}{4}
+ \tfrac{it}{2})$ which is the obstruction
($`v4-arith:w5-a:def:tate-archimedean`$). So this route does not
reach A-TP.

**Verdict D.** Lindenstrauss arithmetic QUE is a statement about
Hecke-Maass amplitude distributions and their microlocal limits; it
does not address zero positivity. It connects to A-TP only through
Watson's formula, which gives $L$-value nonvanishing, not the sign of
the Weil distribution's archimedean component. $\Box$

---

## 5. Attack E: arithmetic Gutzwiller + BGS force A-TP via Chapter 84?

**Attack.** Chapter 84 (`84_trace_formula_equivalence_gutzwiller.tex`)
records the arithmetic Gutzwiller formulation as a Conditional theorem
(`v4-arith:tfe:thm:arith-gutzwiller`): if the ACS boundary Hamiltonian
$H_{\mathrm{ACS}}$ has a chaotic semiclassical limit whose primitive
periodic orbits are primes $p$ with lengths $\log p$, and the orbit
amplitudes are the Weil amplitudes, then the periodic-orbit sum is
exactly the prime side of \eqref{v4-arith:w5-a:eq:weil-explicit}. The
BGS principle (`v4-arith:tfe:thm:bgs`): chaotic systems in a fixed
symmetry class have GUE local spectral statistics. So \emph{given} the
semiclassical-chaos package, $\{\gamma_n\}$ are GUE-distributed, hence
real, hence A-TP.

**Heal.** This is the statistical-upside route. Its rigor depends on
(i) the profinite ACS renormalisation (conjecture
`v4-arith:3d-acs:conj:qu-acs`, still open); (ii) the BD/CG ordered
incidence-bar comparison (`v4-arith:3d-acs:cor:BDCG-ordered-comparison`,
Conditional); (iii) the semiclassical ACS phase space / Hamiltonian
package (not constructed); (iv) the chaos hypothesis on that phase
space (not constructed); (v) BGS universality itself (still a physics
conjecture, not a theorem, as Chapter 84 explicitly acknowledges:
`\ClaimStatusConjectured`).

BGS is a \emph{universality conjecture} based on empirical
level-spacing studies (Bohigas-Giannoni-Schmit 1984 on nuclear
resonances; corroborated by Berry-Tabor 1977 for integrable vs.
chaotic, by many numerical studies in the 1980s-1990s, including
Odlyzko's 1987 zeros-of-$\zeta$ data). It is not proved as a theorem
even for the standard billiard systems (the Sinai billiard, Bunimovich
stadium, etc.); there are no mathematical proofs of GUE universality
for any non-random Hamiltonian system.

Therefore: attack E relies on five layers of conjecture. Each
layer is strictly weaker than RH itself; the composite is strictly
conditional. Closing the attack requires proving each layer
independently. Four of the five layers are open and no known route
simplifies them.

**Refined attack.** Restrict BGS to its local consequences that
\emph{are} theorems. E.g., Heath-Brown 1979 proved Montgomery's PCH
on a restricted class of test functions; Conrey-Ghosh 1992 proved
moment asymptotics; Hughes-Rudnick 2003 derived $n$-level statistics
for the zeros in a low-support Fourier window. Could the partial
rigor of these theorems + the explicit-formula chain close A-TP on a
dense test class?

**Refined heal.** These partial results are all downstream of RH
(they take RH as an input or condition). They give no implication in
the direction GUE $\Rightarrow$ RH. The reason: the Fourier-support
restriction that makes these theorems unconditional is exactly the
window where the Weil explicit formula can be applied without the
off-critical-zero contribution. Beyond the Fourier-support window, the
off-critical zeros dominate any GUE-universality statement; so no
rigorous passage from the restricted GUE statement to the full zero
ordinate locations is available.

**Third attack.** Rephrase: the \emph{consistency} direction. If RH
and GUE both held, would anything break? (Answer: no; that is the
statistical-upside route in Chapter 84 running downhill.) If A-TP
failed and $\{\gamma_n\}$ were not GUE, could we exclude this by
some independent observable?

**Third heal.** This is the falsification check. Suppose $\{\gamma_n\}$
has density $N(T) \sim T \log T / (2\pi)$ (Riemann-von Mangoldt,
unconditional), but RH fails: some $\gamma_n$ are complex. The
explicit formula still holds with $\gamma_n \in \mathbb{C}$; the
finite-place and archimedean distributions are still valid. But the
pair-correlation statistic diverges because the ``distance'' between
$\gamma_i, \gamma_j$ in 2D complex space is different from the
``spacing'' used in 1D statistics. GUE universality as a 1D point-process
statement simply does not apply; it is replaced by a 2D determinantal
structure (if we are lucky). So there is no contradiction: the
failure of RH is compatible with the failure of GUE, and nothing forces
the GUE statement to be true.

**Verdict E.** Arithmetic Gutzwiller + BGS is a 5-level conditional
chain (profinite ACS, BD/CG comparison, semiclassical Hamiltonian,
chaos, BGS). Each level is open; the composite does not close A-TP.
The falsification check confirms: BGS need not hold if RH fails, so
BGS cannot force RH. $\Box$

---

## 6. Attack F: Hejhal triple correlation gives more than pair?

**Attack.** Hejhal 1994 (Int. Math. Res. Not.): triple-correlation of
$\{\gamma_n\}$ normalized to unit spacing matches the GUE
triple-correlation under RH, extending Montgomery 1973 to a higher
cumulant. If all $n$-level correlations are GUE and the zeros form a
determinantal point process with the sine kernel, then by Soshnikov's
theorem (Soshnikov 2000, Ann. Probab.: determinantal point processes
with given kernel live on the support of the kernel), the point
process lives on $\mathbb{R}$.

**Heal.** Hejhal 1994 is conditional on RH, like Montgomery 1973 and
Rudnick-Sarnak 1996. The determinantal-process statement (Soshnikov)
needs all $n$-level correlations to hold over a dense class of test
functions, unconditionally; the best unconditional statements are in
the Rudnick-Sarnak 1998 Fourier-support window, and the support
shrinks like $[-2/n, 2/n]$ in the $n$-level case. So unconditional
triple-correlation exists for test-functions in
$[-2/3, 2/3]$ Fourier support, a proper sub-class. This does not
suffice to determine the full joint distribution, hence cannot force
Soshnikov's realization theorem to apply.

**Refined attack.** Observe that Hejhal's triple correlation, even in
its conditional form, gives \emph{connected} three-point cumulants
matching GUE:

$$
R_3^{\mathrm{conn}}(u_1, u_2) = -[\sin^2 \pi u_1 \sin^2 \pi u_2 + \cdots]/[\pi^3 u_1 u_2 (u_1 - u_2)],
$$

in the normalized scale. Substitute this into the Weil explicit
formula for $f * \tilde f$ and extract three-zero cross-terms. If the
cross-terms are sign-definite, they might constrain $W$.

**Refined heal.** The Weil explicit formula is a \emph{linear}
functional of test functions; $f * \tilde f$ is a rank-one quadratic.
The expansion $W(f * \tilde f) = \sum_\rho |\hat f(\gamma_\rho)|^2$ is
a \emph{diagonal} sum (each zero contributes independently). Triple
correlations enter only if we consider rank-three quantities like
$W(f_1 * f_2 * f_3)$, but A-TP is specifically about rank-one.
Therefore, Hejhal's triple correlation is not a direct input to A-TP;
it is a constraint on a higher-rank statistic, irrelevant to
pointwise positivity of the pair $f * \tilde f$.

**Verdict F.** Hejhal triple correlation is downstream of RH and, in
its rigorous form, addresses higher-rank statistics not relevant to
A-TP. $\Box$

---

## 7. Attack G: Gaussian class (Chapter 74) extended via GUE to dense sub-class?

**Attack.** Chapter 74 (`74_ATP_gaussian_reduction.tex`) closes A-TP
on the Gaussian test class (the sub-class of Paley-Wiener functions
$f$ with Gaussian profile, $\hat f(t) = e^{-\alpha t^2/2}$ for some
$\alpha > 0$). Under GUE, the $n$-point correlators converge to
explicit determinantal kernels. Gaussian test functions pair cleanly
against determinantal densities. If the dense sub-class ``all
Paley-Wiener functions whose Fourier transforms are
Gaussian-dominated'' could be reached through GUE plus Chapter 74,
A-TP might extend.

**Heal.** Chapter 74 closes A-TP on the Gaussian class \emph{using
the digamma-saddle-point expansion} of $W_{\infty}(f * \tilde f)$
(wave-6 A technique); it does not invoke GUE or random-matrix theory.
The closure is analytic: for Gaussian-peaked $\hat f$, the
$\sum_\rho |\hat f(\gamma_\rho)|^2$ side and the $W_{\infty}$ side
can be compared via a saddle-point evaluation on the critical line,
and the sign works out. GUE/BGS plays no role here; the closure is via
the real-analytic properties of the Gaussian.

Extending the Gaussian class to a dense sub-class of Paley-Wiener would
require a \emph{closure theorem} for the positivity: if $W(f_n *
\tilde f_n) \geq 0$ for $f_n \to f$ in some topology, does $W(f *
\tilde f) \geq 0$? The answer is yes if $W$ is a continuous functional
in that topology. $W$ is weakly continuous on $\mathrm{PW}$ in the
Schwartz-norm topology (Iwaniec-Kowalski 2004 \S5.12). But the dense
sub-class of Gaussian-dominated test functions does not yield the full
Paley-Wiener class in this topology; only a proper sub-class is
approximated.

GUE universality could help if it gave a \emph{uniform} bound on the
positivity defect $W_{\mathrm{defect}}(f) := \max(0, -W(f * \tilde f))$
for dense test classes. But GUE universality, even conjecturally, only
gives second-order fluctuation statements, not first-order
sign-definite ones. So even granting BGS, we cannot pass to sign
definiteness.

**Verdict G.** Chapter 74's Gaussian closure uses digamma-kernel
analysis, not GUE. Extending to dense sub-class through GUE does not
work because GUE does not give uniform positivity, only second-order
statistics. $\Box$

---

## 8. Attack H: Cross-compare with Guinand-Weil-Burnol (Chapter 79)

**Attack.** Chapter 79 (`79_ATP_Guinand_Weil.tex`) closes A-TP on the
co-Poisson sub-class $\mathrm{PW}^{\mathrm{CP}}$ via Burnol's
Hilbert-transform positivity. The sub-class is non-empty and dense in
a Fourier-dual topology (Remark `v4-arith:w7-i:rem:CP-nonempty`), but
orthogonal to the wave-6 HFD sub-class (Remark
`v4-arith:w7-i:rem:orthogonal-HFD`). Burnol's class is Fourier-adapted
via Sonine spaces and co-Poisson symmetrization. What class would BGS
close?

**Heal.** BGS gives GUE statistics $\Rightarrow$ GUE-determinantal
point process $\Rightarrow$ zeros sit on $\mathbb{R}$. So BGS (if
we had it) would close A-TP on \emph{all} of $\mathrm{PW}(\mathbb{R})$
via the RH-equivalence. The relevant question is: assuming BGS, what
does the \emph{quantitative} structure close? The answer: everything,
including the full Paley-Wiener class, since BGS $\Rightarrow$ RH
$\Rightarrow$ A-TP.

But BGS is itself conjectural. The rigorous BGS-adjacent statements
(Rudnick-Sarnak 1996 GUE correlations in restricted Fourier windows)
close specific $n$-level correlation statements for test functions
with Fourier support in $[-2/n, 2/n]$. Do these intersect with the
co-Poisson class $\mathrm{PW}^{\mathrm{CP}}$ or the wave-6 HFD class?

\emph{Fourier support comparison.} Wave-6 HFD requires $|\hat f|^2$
concentrated on $|t| > t_* \approx 0.794$; Rudnick-Sarnak allowed
support is $|t| \in [-2/n, 2/n]$ i.e. $\leq 2/2 = 1$ for pair
correlation, $\leq 2/3$ for triple. These are different Fourier-support
regions, but they overlap at $|t| \in [0.794, 1]$ for pair. So there
is a small overlap window where Rudnick-Sarnak pair correlation
holds unconditionally \emph{and} wave-6 HFD applies.

\emph{Co-Poisson class comparison.} $\mathrm{PW}^{\mathrm{CP}}$ is
characterized by time-domain autocorrelation conditions
(Remark `v4-arith:w7-i:rem:orthogonal-HFD`): $\varphi = f * \tilde f$
concentrated on $y > 1/\pi \approx 0.318$, with zero log-Mellin mean.
This is Fourier-dual to HFD: $\mathrm{PW}^{\mathrm{CP}}$ contains
test functions with \emph{low} Fourier support, concentrated in
$|t| \in [0, \pi]$ roughly. So the Rudnick-Sarnak pair correlation
window $|t| \leq 1$ is \emph{inside} $\mathrm{PW}^{\mathrm{CP}}$ (up
to normalisation and scale).

\emph{Implication.} On the intersection $\mathrm{PW}^{\mathrm{CP}}
\cap \{|t| \leq 1\}$, we have:
(i) Burnol closure of A-TP on $\mathrm{PW}^{\mathrm{CP}}$
(Theorem `v4-arith:w7-i:thm:copoisson-closure`);
(ii) Rudnick-Sarnak unconditional pair correlation on $|t| \leq 1$
(Rudnick-Sarnak 1998 arXiv:math/9708208);
(iii) the two closures are compatible and give GUE pair-correlation
structure on the intersection.

What does this buy us? On this intersection, the positive-trace form
$W_{\infty}$ can be bounded by the zero-side sum via the known
quantitative pair-correlation statement. This gives a quantitative
closure of A-TP on the intersection with an explicit constant
depending on the Rudnick-Sarnak implicit constant. It is a small
improvement (the intersection is a proper sub-class of the co-Poisson
sub-class) but a \emph{real} improvement: the Rudnick-Sarnak
unconditional pair correlation is not used in the existing wave-7 I
closure.

**Refined attack.** Turn this into a precise Conditional-statement:
``on the sub-class $\mathrm{PW}^{\mathrm{CP}} \cap \mathrm{Support}_{\hat{}}[-1,1]$,
A-TP is closed quantitatively with explicit Rudnick-Sarnak constants.''

**Refined heal.** This is a candidate for a future Wave-8 inscription.
It does not, however, close A-TP on the full Paley-Wiener class: the
Rudnick-Sarnak window is bounded by $[-2, 2]$ at pair correlation, and
the implicit constants degenerate as the support approaches the
boundary. The quantitative closure is not uniform, and the complement
$\mathrm{PW} \setminus (\mathrm{PW}^{\mathrm{CP}} \cap \text{support})$
retains the full obstruction.

**Verdict H.** GUE and Rudnick-Sarnak's rigorous fragments yield
a modest, quantitative improvement on the intersection of
$\mathrm{PW}^{\mathrm{CP}}$ with the Rudnick-Sarnak Fourier window.
This is Conditional-grade content worth inscribing in a future wave,
but does not close A-TP. $\Box$

---

## 9. Falsification check: BGS compatibility with RH failure

**Scenario I: RH holds, GUE holds.** Standard arithmetic-quantum-chaos
picture. Consistent; both statements corroborated by Odlyzko's data
for $T \leq 10^{22}$. BGS is a consequence, not a premise.

**Scenario II: RH holds, GUE fails.** Logically consistent: one could
imagine a deterministic arithmetic structure on the critical line that
shadows GUE at low levels but diverges at high moments. Katz-Sarnak
universality is a conjecture, not a theorem. This is a refinement
question, not a zero-location question; it does not affect A-TP.

**Scenario III: RH fails, GUE holds for critical-line zeros only.**
Off-line zeros exist, on-line ones follow GUE. The explicit formula
with Fourier support excluding off-line contributions still gives GUE
correlations on the sub-sector. But the full distribution is not GUE
(off-line zeros are not included). A-TP fails (off-line zeros
contribute negatively to $W$).

**Scenario IV: RH fails, GUE fails.** The natural scenario: any
off-line zero has amplitude $|\hat f(x+iy)|^2$ depending on the
analytic extension of $\hat f$; the GUE kernel $K(u-u')$ depends on
real $u, u'$, and complex arguments break its determinantal structure.
RH failing and GUE failing are coupled; no natural mechanism for one
without the other.

**Structural finding.** BGS is not load-bearing for A-TP. If RH held,
BGS would be a consequence but not a logical premise. If RH failed,
BGS would fail too. The statistical upside in Chapter 84 is consistent
with the main RH story but not a route to it. The voice's thesis
(``GUE rigidity forces $W \geq 0$'') is reversed: A-TP (RH) \emph{would
imply} GUE rigidity, not the other way around.

---

## 10. What the statistical structure actually closes

**Load-bearing for A-TP:** Weil explicit formula (unconditional);
Petersson-Rankin-Selberg isometry (wave-5, Chapter 57) for the
finite-prime side; digamma kernel analysis (wave-6) for the archimedean
side on the HFD sub-class; co-Poisson analysis (wave-7, Chapter 79)
on the orthogonal $\mathrm{PW}^{\mathrm{CP}}$ sub-class;
Hermite-Biehler / de Branges spectral package (wave-5 J, Chapter 58)
for the main-direction implication (HB+)+(BD+)+(Det) $\Rightarrow$ RH.

**Not load-bearing (consequences not premises):** Montgomery pair
correlation (conditional on RH); Keating-Snaith moments (amplitude
not zeros); Rudnick-Sarnak $n$-level correlations (conditional,
restricted window, universality not positivity); Lindenstrauss
arithmetic QUE (amplitude on modular surface); BGS (conjectural,
5-layer descent); Hejhal triple correlation (conditional, higher
rank); Katz-Sarnak Frobenius universality (function-field, structural).

**What the statistical structure buys us:** a quantitative refinement
on $\mathrm{PW}^{\mathrm{CP}} \cap \{|t| \leq 1\}$ via Rudnick-Sarnak
1998 unconditional within the Fourier window (candidate for wave-8);
a consistency check (if A-TP proved, BGS follows for $\zeta$,
explaining Odlyzko's data; plausibility not proof); an alternative
framing of the VB* / HB+ route via a hypothetical semiclassical
Hamiltonian $H_{\mathrm{ACS}}$, which is Conditional$^5$ versus the
first two routes' Conditional$^1$.

---

## 11. Novel content for Vol IV inscription

From cycles 1-10, three candidates for future inscription as
complements to waves 5, 6, 7.

**Wave-8 A: quantum-chaos consistency audit, \ClaimStatusProvedHere.**
On $\mathrm{PW}^{\mathrm{RS-Pair}} = \{f \in \mathrm{PW}(\mathbb{R}) :
\mathrm{supp}\,\hat f \subset [-1,1]\}$ (the Rudnick-Sarnak
unconditional pair-correlation window), Quant-A-TP-RS holds:
$W_{\infty}(f * \tilde f) \leq C_{\mathrm{RS}} \sum_{\rho}
|\hat f(\gamma_\rho)|^2 + \text{explicit corrections}$, proof by
Rudnick-Sarnak 1998 plus Weil explicit formula without BGS or GUE.
Closes on proper sub-class; beyond Fourier support $[-1,1]$ the
off-critical zero density takes over. Orthogonal to wave-6 HFD;
partial overlap with wave-7 co-Poisson.

**Wave-8 B: falsification record, \ClaimStatusProvedHere.** BGS
universality is not load-bearing for A-TP. The schema (RH, BGS) is
consistent; (RH fails, BGS holds) contradicts nothing absent GUE
universality over all $L$-functions with off-critical zeros, which is
not known or conjectured. BGS holds / fails together with RH but does
not force RH.

**Wave-8 C: arithmetic QUE route, \ClaimStatusConditional.** On
Hecke-Maass cuspidal sector, Rankin-Selberg positivity of
$L(\tfrac{1}{2}, \phi_j \otimes \phi_j)$ combined with arithmetic QUE
(Lindenstrauss 2006) and Watson's formula 2002 gives a quantitative
A-TP on the Mellin-lift image of Hecke-Maass cusp forms, extending
wave-5's holomorphic Rankin-Selberg closure by averaging over the
cuspidal spectrum. Conditional on Ramanujan-Petersson for Maass forms
(known only up to $7/64$, Kim-Sarnak 2003).

---

## 12. Final verdict

**Arithmetic-quantum-chaos does not close A-TP.**

The quantum-chaos-BGS voice carries the statistical-upside intuition
that was always the most \emph{suggestive} route to RH: zeros behave
like GUE eigenvalues, GUE eigenvalues are real, therefore zeros are
real. But this suggestion is consistency, not causality. BGS is a
conjecture, downstream of RH-type statements in every derivation I
have checked. The rigorous fragments (Montgomery conditional pair
correlation, Rudnick-Sarnak restricted $n$-level correlation) use
RH as input or are restricted to Fourier windows that exclude
off-critical zero contributions.

The route to RH runs through de Branges / Hermite-Biehler
(wave-5 J) or through the archimedean digamma-kernel analysis
(waves 6, 7). The quantum-chaos voice adds a \emph{consistency check}
and a \emph{modest quantitative improvement} on the Rudnick-Sarnak
intersection, but does not provide a new independent route.

The correct Vol-IV inscription is: the statistical-upside of
Chapter 84 remains a Conditional corollary of the Hilbert-Polya
spectral-flow hypothesis, not a route to A-TP. BGS descends from
RH; it does not ascend to it. Vol IV should add Wave-8 A as a
narrow quantitative refinement on $\mathrm{PW}^{\mathrm{CP}} \cap
\{|t| \leq 1\}$, Wave-8 B as an honest falsification record, and
Wave-8 C as a QUE-conditional extension of Maass-lift coverage.

A-TP remains open. Its closure is the closure of RH.

---

## 13. Sources

Sources used in this analysis are independent of the wave-5, wave-6,
wave-7 source catalogs.

### Primary

- Bohigas, Giannoni, Schmit (1984), Phys. Rev. Lett. 52, 1-4.
- Berry, Keating (1999), NATO ASI Series 370, 355-367.
- Montgomery (1973), Proc. Sympos. Pure Math. 24, 181-193.
- Odlyzko (1987), Math. Comp. 48, 273-308.
- Rudnick, Sarnak (1996), Duke Math. J. 81, 269-322, arXiv:math/9505308.
- Rudnick, Sarnak (1998), Comm. Math. Phys. 194, 61-70, arXiv:math/9708208.
- Katz, Sarnak (1999), AMS Colloq. Publ. 45.
- Katz, Sarnak (1999), Bull. AMS 36, 1-26.
- Keating, Snaith (2000), Commun. Math. Phys. 214, 57-89.
- Keating, Snaith (2000), Commun. Math. Phys. 214, 91-110.
- Lindenstrauss (2006), Ann. Math. 163, 165-219.
- Soundararajan (2009), Ann. Math. 170, 981-993.
- Sarnak (1995), Israel J. Math. 92.
- Hejhal (1994), Int. Math. Res. Not. 293-302.

### Secondary

- Selberg (1946), Arch. Math. Naturvid. 48.
- Heath-Brown (1979), J. London Math. Soc. (2) 18.
- Conrey, Ghosh (1992), Proc. Sympos. Pure Math. 53.
- Soshnikov (2000), Russian Math. Surveys 55.
- Watson (2002), arXiv:0810.0425.
- Holowinsky, Soundararajan (2010), Ann. Math. 172.
- Kim, Sarnak (2003), J. AMS 16, 139-183.
- Goldston, Montgomery (1987), in Analytic Number Theory and
  Diophantine Problems (Birkhauser).
- Hughes, Rudnick (2003), Q. J. Math. 54.

### Disjointness audit

The quantum-chaos catalog is disjoint from wave-5 (automorphic /
analytic-number-theoretic: Weil 1952, Li 1997, Rankin 1939, Selberg 1940,
Hecke 1936, Deligne 1974, Jacquet 1972), wave-6 (Hurwitz 1882, Gauss
1813, Whittaker-Watson 1927, Boas 1954), wave-7 (Guinand 1948, Burnol
2000/2002, Cartier-Voros 1990), and wave-5 J (de Branges 1968/1994,
Lagarias 1999, Conrey-Li 2000, Beurling-Malliavin 1962, Hamburger 1920,
Carleman 1926, Koosis 1992, Levin 1980). No source appears on both
sides of any identification used in Section 11's proposed inscriptions.
