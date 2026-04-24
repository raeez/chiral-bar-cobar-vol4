# Voice 3: Iwasawa theory / Kato-Fukaya / p-adic L-functions

## Source catalog and frame

The voice is Iwasawa's p-adic line through analytic number theory,
built from 1969 to 2010. A $p$-adic $L$-function is a measure on the
Iwasawa algebra $\Lambda=\mathbb{Z}_{p}[[\Gamma]]$, with
$\Gamma=\mathrm{Gal}(\mathbb{Q}_{p}^{\mathrm{cyc}}/\mathbb{Q})\cong\mathbb{Z}_{p}$,
whose specialisations at continuous characters recover, up to
interpolation factors, the values of a complex-analytic $L$-function
at integer or Dirichlet-twisted points. The Iwasawa main conjecture
(Mazur-Wiles 1984 for cyclotomic $\mathbb{Z}_{p}$-extensions of
$\mathbb{Q}$; Wiles 1990 for totally real fields; Kato 2004 for
elliptic modular forms) equates such a measure to the characteristic
ideal of a Selmer / Iwasawa module. When positivity holds, it is
positivity of a height pairing on the Bloch-Kato Selmer group, pulled
back by the Bloch-Kato exponential from a syntomic cohomology class
constructed through Kato's Euler system. The question: can Iwasawa
positivity transport to archimedean Tate positivity A-TP?

Primary catalog: Iwasawa 1969/1972 *On p-adic L-functions* (Ann. Math.
89); Kubota-Leopoldt 1964 *Eine p-adische Theorie der Zetawerte* (J.
Reine Angew. Math. 214-215); Mazur-Wiles 1984 *Class fields of abelian
extensions of $\mathbb{Q}$* (Invent. Math. 76); Ferrero-Washington 1979
(Ann. Math. 109); Kolyvagin 1988/1990; Kato 2004 *p-adic Hodge theory
and values of zeta functions of modular forms* (Astérisque 295);
Perrin-Riou 1994/1995 (Invent. Math. 115; Astérisque 229); Coates-Wiles
1977 (Invent. Math. 39); Greenberg 1989 (Adv. Stud. Pure Math. 17);
Fukaya-Kato 2006 (Proc. St. Petersburg Math. Soc. XII); Colmez 2010
(Astérisque 330); Bloch-Kato 1990 (Grothendieck Festschrift). Secondary:
Colmez-Fontaine 2000 (Invent. Math. 140); Coates-Sujatha 2006; Washington
1997; Iwaniec-Kowalski 2004 for complex-analytic cross-checks; Burnol
2000/2002 for the co-Poisson side.

Disjointness rationale. The Kubota-Leopoldt measure (1964) and
Iwasawa's construction (1969/1972) predate Weil's 1952 explicit
formula reformulation by two decades on the derivation side.
Mazur-Wiles (1984) uses arithmetic geometry of modular curves and the
Eisenstein ideal (Mazur 1977), disjoint from Rankin-Selberg (1939,
1940) and from Hurwitz-zeta used in wave-6 digamma analysis. Kato's
Euler system (2004) is built from motivic $K_{2}$ elements through
Beilinson's Eisenstein symbol (1984); disjoint from the Bost-Connes
$C^{*}$-algebraic construction of Chapter 45 and from Burnol's Hankel
/ Sonine-space construction. The only potential source-collision is
Kato's use of complex-analytic $L(s,f)$ as the target of
interpolation; the direction is $L_{p}\to L_{\mathbb{C}}$, not the
other way, and no Weil-positive inequality is a derivational input.

## Attack-heal cycles

### Cycle 1: The Mazur-Wiles route: does positivity of $L_{p}$-values transport?

**Attack.** The classical Mazur-Wiles theorem (Invent. Math. 76, 1984)
states that for $\chi\colon(\mathbb{Z}/p^{n}\mathbb{Z})^{\times}\to\overline{\mathbb{Q}}_{p}^{\times}$
an even non-trivial Dirichlet character of conductor $p^{n}$ (or more
generally a character of $\Gamma=\mathrm{Gal}(\mathbb{Q}(\mu_{p^{\infty}})/\mathbb{Q})$),
the Kubota-Leopoldt $p$-adic $L$-function $L_{p}(\chi,s)$ satisfies
$(L_{p}(\chi,s))=\mathrm{char}_{\Lambda}(X_{\chi})$ as principal ideals
in $\Lambda$, where $X_{\chi}$ is the $\chi$-isotypic component of the
Iwasawa module $\varprojlim_{n}A(\mathbb{Q}(\mu_{p^{n}}))\otimes\mathbb{Z}_{p}$
of $p$-primary class groups. A naive transport: if
$L_{p}(\chi,s)\geq 0$ at $s=0$ for all even $\chi$, and the
interpolation factor $\mathrm{Euler}_{p}(0,\chi)=1-\chi(p)$ is
positive, then by the interpolation identity
$L_{p}(\chi,0)=(1-\chi(p))L(0,\chi^{-1})$ one gets $L(0,\chi^{-1})\geq 0$,
which is an archimedean positivity statement. A stronger naive
transport: specialize at sufficiently many characters, apply Stone-Weierstrass
on the character space, recover archimedean positivity on a dense subset
of test functions, conclude A-TP by continuity.

**Attempt 1.** Both transports fail. First, $L_{p}(\chi,0)$ is not
sign-definite: concrete computations (Ernvall-Metsankyla 1991 in
*Compos. Math.* for small $p$; Washington 1997 Table 3 for
Kubota-Leopoldt values) exhibit $L_{p}(\chi,0)$ taking both signs as
$\chi$ varies over even characters. Second, the interpolation factor
$1-\chi(p)$ vanishes for trivial $\chi\cdot\omega^{-1}$ where $\omega$
is the Teichmuller character, which is the cyclotomic $p$-stabilization
locus; positivity there is the wrong question (it is forced by the
vanishing of the Euler factor). Third, A-TP asserts positivity of a
distribution $W_{\infty}$ on Paley-Wiener test functions, not
positivity of individual $L$-values; the transport target is
mis-typed.

**Heal.** The correct transport is not pointwise. The Iwasawa main
conjecture equates an ideal $(L_{p})$ in $\Lambda$ with an ideal
$\mathrm{char}(X)$. An ideal is not a sign. What is sign-definite is
the *height pairing* on the Iwasawa module's dual, not the
characteristic ideal. The Mazur-Wiles route closes cycle 1 as
*Falsified in the naive form*, with the corrected statement: the
transport is at the level of ideals / characteristic modules, not at
the level of values, and the positivity that transports is the
height-pairing positivity of the Bloch-Kato Selmer group (Cycle 4
below), not the value positivity of the $L_{p}$-function itself.
*Status: naive value-positivity Falsified; ideal-level Mazur-Wiles
restated as a preparatory fact for later cycles.*

### Cycle 2: Kato's Euler system and the Beilinson-Deninger-Scholl positivity

**Attack.** Kato 2004 (Astérisque 295) constructs an Euler system on
$\mathbb{Z}_{p}(1)$ attached to modular forms: zeta elements
$\mathbf{z}_{\mathrm{Kato}}\in\varprojlim_{N}H^{2}(\mathbb{Z}[1/Np],\mathbb{Z}_{p}(2))$
which live in the motivic cohomology of modular curves. The Kato Euler
system has a *norm relation* of Euler-product shape:
$\mathrm{cor}(\mathbf{z}_{N\ell})=(1-\mathrm{Frob}_{\ell})\mathbf{z}_{N}$
at primes $\ell\nmid N$. Under the Bloch-Kato exponential
$\exp_{\mathrm{BK}}\colon H^{1}(\mathbb{Q}_{p},V)\to D_{\mathrm{dR}}(V)/D_{\mathrm{dR}}^{+}$,
Kato's zeta element maps to the modular-form side-values
$L(f,j)/\Omega^{\pm}$ at critical integers $j\in\{1,\ldots,k-1\}$.
Beilinson, Deninger, and Scholl (Beilinson 1984; Deninger-Scholl 1991
in *Beilinson's Conjectures on Special Values of L-Functions*, Perspectives
in Math. 4) identified the height pairing on Beilinson elements as a
Hodge-theoretic positive form. Claim: Kato's height-pairing positivity
at $p$ transports to archimedean Tate positivity.

**Attempt 1.** The Kato Euler system lives in $K_{2}$ of modular
curves (or equivalently in motivic cohomology $H^{2}_{\mathcal{M}}(Y_{1}(N),\mathbb{Q}(2))$).
Its image under the Beilinson regulator
$r_{\mathcal{D}}\colon H^{2}_{\mathcal{M}}(Y_{1}(N),\mathbb{Q}(2))\to H^{2}_{\mathcal{D}}(Y_{1}(N)_{\mathbb{R}},\mathbb{R}(2))$
into Deligne cohomology lands in a real Hodge structure carrying the
archimedean $L$-value $L^{\prime}(f,0)$, up to a period. The Beilinson
regulator is *not* manifestly sign-positive; the Hodge-theoretic
positivity that is available is the Hodge-Riemann bilinear relation
on $H^{1,0}\otimes H^{0,1}$, which controls the sign of
$\|\omega_{f}\|^{2}_{\mathrm{Pet}}$, not the sign of
$L^{\prime}(f,0)$. A naive "Kato-to-archimedean" transport conflates
these two distinct sign structures.

**Heal.** Separate Beilinson's two positivities. The first is the
Petersson norm positivity $\|\omega_{f}\|^{2}_{\mathrm{Pet}}\geq 0$,
which is already what Chapter 57 uses via the Mellin lift
$\Upsilon_{F}$. The second, Beilinson-Deninger-Scholl, concerns the
*height pairing* on the Bloch-Kato Selmer group of the motive
$M(f)(1)$ and is the honest arithmetic positivity statement: for
elements $x,y\in H^{1}_{f}(\mathbb{Q},M(f)(1))$, the
Bloch-Kato-Beilinson height pairing
$\langle x,y\rangle_{\mathrm{BKB}}\in\mathbb{R}$ is conjectured to be
positive-definite (Beilinson 1984 conjecture; proved for abelian
surfaces at $p$ good by Nekovar 1995 *Compos. Math.* 98). This height
positivity is at the *motivic* level and does not pass through the
Paley-Wiener test function $f$ of the Weil distribution. The
connection to A-TP is indirect: A-TP is a statement about a specific
archimedean distribution $W_{\infty}$ applied to $|\widehat{f}|^{2}$;
the Kato-Beilinson height positivity is a statement about a specific
real quadratic form on a finite-dimensional Selmer group. They are
both called "positivity" but they are different objects.
*Status: naive Kato-to-A-TP transport Falsified; Beilinson-Deninger-Scholl
positivity is a genuine p-adic positivity but does not close A-TP.*

### Cycle 3: Ferrero-Washington $\mu=0$ has no archimedean analog

**Attack.** Ferrero-Washington 1979 (Ann. Math. 109) proves
$\mu_{p}(K)=0$ for every abelian number field $K$: the Iwasawa
$\mu$-invariant of the $p$-primary class group tower
$X_{K}=\varprojlim_{n}\mathrm{Cl}(K(\mu_{p^{n}}))_{p}$ vanishes for
abelian $K$. This is a statement of the form "no $p$-torsion part in
an Iwasawa module", proved by a Weil-equidistribution argument applied
to normal numbers in base $p$. A naive archimedean analog: does there
exist a real-analog of Ferrero-Washington, asserting that the
archimedean Weil distribution has no "$\mu$-part" (i.e., no
contribution from trivial zeros or gamma-factor anomalies), which
would close part of A-TP?

**Attempt 1.** The Ferrero-Washington argument uses specifically that
$p$-adic integers are fractally structured in base $p$ (Weil
equidistribution in a profinite compact group). The archimedean
integers are a discrete cyclic group $\mathbb{Z}$; they carry no
$\mu$-invariant in any sense. The argument does not extend to the
archimedean place as stated.

**Heal.** There is a genuine archimedean analog, but it is not
Ferrero-Washington's theorem: it is the *Gamma-Euler completion*
vanishing of the trivial-zero contribution. For
$\xi_{\mathbb{R}}(s)=\frac{1}{2}s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$,
trivial zeros at $s=-2,-4,\ldots$ are cancelled by poles of
$\Gamma(s/2)$, and the Weil kernel
$\Phi_{\infty}^{W}(t)=\frac{1}{2\pi}[\mathrm{Re}\,\psi(1/4+it/2)+\log\pi]$
carries no trivial-zero contribution. This is a definitional
cancellation (the reason for working with $\xi$ not $\zeta$), not a
theorem. The sign-indefiniteness of $W_{\infty}$ concentrated on the
finite-width Rankin-Selberg complement is already inscribed in
Chapters 57, 71-80 independent of Iwasawa theory. *Status: naive
Ferrero-Washington archimedean analog Falsified; no new A-TP
content.*

### Cycle 4: The p-adic Beilinson conjectures and the Bloch-Kato exponential

**Attack.** Perrin-Riou 1995 (Astérisque 229) states a p-adic
Beilinson conjecture: special values of p-adic $L$-functions are
equal, up to explicit factors, to syntomic regulators of motivic
elements. Specifically, for $M$ a motive and $p$ a prime of good
ordinary reduction, one has the Perrin-Riou exponential map
$\Omega_{\mathrm{PR}}\colon H^{1}_{\mathrm{Iw}}(\mathbb{Z}_{p}^{\mathrm{cyc}},V)\to D_{\mathrm{dR}}^{+}(V)\otimes\Lambda_{\infty}$
where $\Lambda_{\infty}$ is the Colmez-Perrin-Riou integrated Iwasawa
algebra. The Perrin-Riou conjecture equates
$\Omega_{\mathrm{PR}}(\mathbf{z}_{\mathrm{Kato}})\in D_{\mathrm{dR}}^{+}(V)\otimes\Lambda_{\infty}$
with the $p$-adic $L$-function of the motive. Claim: if syntomic
regulator positivity and Hodge-theoretic positivity both hold, then
via the Bloch-Kato exponential
$\exp_{\mathrm{BK}}\colon D_{\mathrm{dR}}^{+}(V)\to H^{1}(\mathbb{Q}_{p},V)$
one can push a positive class from the syntomic side to the Galois
side and thereby close part of A-TP.

**Attempt 1.** The Bloch-Kato exponential is not an isometry on any
canonical positive-definite form. It is an $R$-linear isomorphism
between finite-dimensional $\mathbb{Q}_{p}$-vector spaces; the
positivity available on $D_{\mathrm{dR}}^{+}(V)$ (from Hodge-Riemann)
is not preserved under $\exp_{\mathrm{BK}}$ in any canonical way.
Further, the image of $\exp_{\mathrm{BK}}$ is inside
$H^{1}_{f}(\mathbb{Q}_{p},V)$, a finite-dimensional $p$-adic space,
while A-TP lives on an infinite-dimensional real test-function space
$\mathrm{PW}(\mathbb{R})$. Dimension count alone defeats the transport.

**Attempt 2.** Perhaps the transport works at the level of one
character-specialization at a time: fix an even Dirichlet character
$\chi$ of conductor $p^{n}$; specialise Kato's zeta element to the
$\chi$-component; apply $\exp_{\mathrm{BK}}$; pair with a specific
modular form; extract the value $L(f\otimes\chi,k/2)$; conclude
something about the archimedean $L$-function sign. This gives a
single scalar sign per character specialisation. But A-TP requires a
sign inequality simultaneously for *all* Paley-Wiener test functions,
a condition not reducible to finitely many (or even countably many)
character specialisations.

**Heal.** The Perrin-Riou / Bloch-Kato machinery gives a p-adic
positivity on a different object from A-TP: it gives the positivity
of the $p$-adic $L$-function at specific critical integer arguments,
interpreted as pairings of syntomic regulator classes. This is the
Greenberg-Iwasawa positivity conjecture (Greenberg 1994 "Iwasawa
theory and $p$-adic deformations of motives", Proc. Symp. Pure Math.
55 part 2) and has been verified in many cases (Skinner-Urban 2014
*Invent. Math.* 195 for symmetric-square of modular forms; Ciperiani-Wiles
2008 for CM elliptic curves). But it is a p-adic $L$-value positivity,
not an archimedean distribution positivity. The connection to A-TP is
through a long chain:
$(L_{p}\text{-positivity})\to(\text{Selmer height-pairing positivity})\to(\text{Beilinson conjectures})\to(\text{archimedean }L\text{-value positivity})$,
but each arrow is conditional (the first is a specific case of the
Iwasawa main conjecture; the second depends on Bloch-Kato; the third
is the full Beilinson programme; the fourth gives pointwise $L$-value
positivity, not the distributional A-TP).
*Status: Bloch-Kato transport Falsified in the naive form; the
p-adic-archimedean chain is too long and each link is at least as
hard as A-TP itself.*

### Cycle 5: The $p\to\infty$ limit and the Bost-Connes KMS connection

**Attack.** Iwasawa theory operates at a fixed prime $p$. Taking the
limit $p\to\infty$ should, heuristically, recover archimedean content:
the "limit prime" $p=\infty$ is precisely the archimedean place in
the Tate adelic picture. Formalising this: Bost-Connes 1995 (Selecta
Math. 1) constructs a $C^{*}$-algebra whose KMS states at inverse
temperature $\beta=s$ are parametrised by the zeta values $\zeta(s)$;
Connes-Marcolli 2008 *Noncommutative Geometry, Quantum Fields and
Motives* Ch. 3 embeds the Bost-Connes system in a larger adele-class
space whose arithmetic is simultaneously $p$-adic at each prime and
archimedean at $\infty$. Within this framework, the transition from
finite $p$ to $p=\infty$ is KMS phase transition. Claim: in the
$p\to\infty$ limit of Iwasawa theory (formalised via Connes-Marcolli),
the characteristic ideal of the Iwasawa module becomes a distribution
on the archimedean idele class, and its positivity is A-TP.

**Attempt 1.** The $p\to\infty$ limit of $\Lambda_{p}=\mathbb{Z}_{p}[[\Gamma_{p}]]$
is formally $\varprojlim_{p}\Lambda_{p}$, an object not living in any
single adelic framework. One can compute
$\lim_{p\to\infty}L_{p}(\chi,s_{0})$ for specific $\chi$ and $s_{0}$;
for example, $L_{p}(\chi,0)$ depends on $p$ through the Euler factor
$1-\chi(p)$, and as $p$ varies over primes, this stays in a compact
set but does not tend to a specific archimedean limit. The $p\to\infty$
operation does not converge to an archimedean $L$-value in any
straightforward sense. Connes-Marcolli 2008 \S3 formalises this
non-convergence as the KMS$_{\beta}\to$ KMS$_{1}$ phase transition
at $\beta=1$, where the low-temperature pure states (indexed by primes)
collapse to the high-temperature $\zeta$-phase.

**Attempt 2.** The Bost-Connes framework has an archimedean avatar:
the "archimedean Bost-Connes system" of Consani-Marcolli 2005
(arXiv:math/0508070) whose KMS state at $\beta=1$ is the archimedean
analog of the zeta partition function. If one believes this system
carries an A-TP-positive Gibbs measure at $\beta=1/2$ (the critical
temperature corresponding to the critical line), then the Gibbs measure
positivity would imply A-TP. But the critical-line KMS state has not
been explicitly constructed: Bost-Connes operates at $\beta>1$ and
$\beta\leq 1$ separately, with a phase transition at $\beta=1$; the
$\beta=1/2$ "critical line" regime is in the low-temperature phase
where individual primes dominate and no finite Gibbs measure exists.
The would-be "$\beta=1/2$ archimedean Bost-Connes positivity" is
therefore not a theorem but a conjecture equivalent to A-TP.

**Heal.** Chapter 46's KMS$_{1}$/GNS identification is the genuine
Bost-Connes-Iwasawa bridge but does not reach A-TP: it establishes
GNS positivity on the cyclic vector and matches Chapter 57
finite-prime Petersson positivity, both finite-place statements. The
archimedean Weil kernel $\Phi_{\infty}^{W}$ lives outside the
KMS$_{1}$ framework; the archimedean place is handled separately via
Gaussian Fourier self-duality (Chapter 25 Attack 5). The $p\to\infty$
limit in the Bost-Connes / Connes-Marcolli framework is the
transition from the finite-prime KMS regime to the $\beta=1$
critical regime, and A-TP sits at $\beta=1/2$, where no KMS state
exists classically. *Status: naive $p\to\infty$ Iwasawa-to-A-TP
transport Falsified; Consani-Marcolli archimedean Bost-Connes at
$\beta=1/2$ is conjecturally A-TP-carrying but its construction is
open and RH-equivalent.*

### Cycle 6: Kato's reciprocity and the $\exp^{*}$ / $\log$ pairing

**Attack.** Kato's reciprocity (Kato 1993 Trento; Kato 2004
Astérisque 295 \S2) relates the Coleman logarithm
$\log_{p}\colon\hat{\mathcal{O}}_{K,v}^{\times}\to K_{v}$ to a Tate
invariant pairing, with dual
$\exp^{*}\colon H^{1}(K_{v},V)\to D_{\mathrm{dR}}^{+}(V)^{\vee}$.
Claim: if $\exp^{*}$ is sign-definite on a specific divisor class
(canonical or Eisenstein), its archimedean analog (Deligne period
pairing) inherits the sign and closes part of A-TP.

**Attempt 1.** $\exp^{*}$ is $\mathbb{Q}_{p}$-linear and not
sign-definite in any canonical sense (signs depend on basis, and
natural bases are lattices). The archimedean analog is the Beilinson
regulator into Deligne cohomology, also not canonically sign-definite
(Cycle 2).

**Heal.** Kato's reciprocity is local-global compatibility, not
positivity. The sign data it provides is the local root number
$\epsilon_{v}(V)$, a unit, not a distributional positivity.
*Status: Kato reciprocity does not touch A-TP; Falsified as a route.*

### Cycle 7: Cross-compare with Chapter 79 (Guinand-Weil)

**Attack.** Chapter 79's co-Poisson framework closes A-TP on a
sub-class $\mathrm{PW}^{\mathrm{CP}}$ defined by Hilbert-transform
positivity against the Burnol dual kernel $\widetilde{g}$. The
co-Poisson formalism uses the Jacobi theta function
$\theta(x)=\sum_{n\in\mathbb{Z}}e^{-\pi n^{2}x}$ and its modular
transform $x^{1/2}\theta(x)=\theta(1/x)$. Iwasawa theory uses the
$p$-adic congruence $\zeta_{p}(s)\equiv\zeta(s)\pmod{p}$ (Kummer,
Kubota-Leopoldt). Where do these two axes meet?

**Attempt 1.** They meet at the Stickelberger element. For a
cyclotomic field $\mathbb{Q}(\mu_{p^{n}})$, the Stickelberger element
$\theta_{\mathrm{Stick},n}\in\mathbb{Q}[\mathrm{Gal}(\mathbb{Q}(\mu_{p^{n}})/\mathbb{Q})]$
is defined as $\theta_{\mathrm{Stick},n}=\sum_{a\in(\mathbb{Z}/p^{n}\mathbb{Z})^{\times}}\langle a/p^{n}\rangle\sigma_{a}^{-1}$
(with $\langle\cdot\rangle$ the fractional part and $\sigma_{a}$ the
Galois automorphism $\zeta\mapsto\zeta^{a}$). The Stickelberger theorem
(Stickelberger 1890; modern exposition in Washington 1997 \S6) states
$\theta_{\mathrm{Stick},n}$ annihilates the $p$-primary ideal class
group of $\mathbb{Q}(\mu_{p^{n}})$; it interpolates to an Iwasawa
element which pairs with even characters to give $L_{p}(\chi,0)$. The
name "Stickelberger" derives from a zeta-function-like formula, which
in Iwasawa-theoretic language is the $p$-adic analog of the
Jacobi-theta-function formula: $\theta_{\mathrm{Stick},n}$ is the
$p$-adic truncation of a formal theta sum. However, the $p$-adic
Stickelberger element is *not* the $p$-adic reduction of the
archimedean Jacobi theta function in any direct sense; their only
common ancestor is the Dedekind eta function / Eisenstein series on
the upper half-plane, at which both sides specialise. The meeting
point of the two axes is therefore at the Eisenstein-series level,
not at the theta-function level.

**Attempt 2.** The co-Poisson transform of Burnol uses the
$y\mapsto 1/y$ involution on $(0,\infty)$; Iwasawa theory uses the
$\gamma\mapsto\gamma^{-1}$ involution on $\Gamma\cong\mathbb{Z}_{p}$.
These are not directly comparable; the first is real-analytic, the
second is $p$-adic-analytic. They arise from different sides of the
Riemann functional equation: the co-Poisson formalism exhibits
$\xi(s)=\xi(1-s)$ as a self-duality of $\mathcal{C}\varphi$ under
$y\mapsto 1/y$; the Iwasawa formalism exhibits functional equations
as $\Gamma$-equivariance properties of characteristic ideals under
Iwasawa involution $\iota\colon\gamma\mapsto\gamma^{-1}$. Both sides
know about the functional equation; they encode it differently.

**Heal.** The honest meeting point is the *Kato zeta element*
$\mathbf{z}_{\mathrm{Kato}}\in H^{2}_{\mathrm{Iw}}(\mathbb{Z}[1/p],\mathbb{Z}_{p}(2))$
and its archimedean Beilinson regulator
$r_{\mathcal{D}}(\mathbf{z}_{\mathrm{Kato}})\in H^{2}_{\mathcal{D}}(\mathbb{R},\mathbb{R}(2))$.
Kato's explicit formula for the regulator (Kato 2004 \S10 and
Bannai-Kings 2010 in *Compos. Math.* 146) expresses
$r_{\mathcal{D}}(\mathbf{z}_{\mathrm{Kato}})$ in terms of Eisenstein
series values, which in turn connect to Jacobi theta via the
Kronecker limit formula. Through this chain, the Iwasawa side and the
co-Poisson side share a common motivic ancestor (the Eisenstein /
theta / Beilinson-Eisenstein class). They do not, however, share a
common positivity statement: the Iwasawa side's height-pairing
positivity (Bloch-Kato-Beilinson) and the co-Poisson side's
Hilbert-transform positivity (Burnol) are different positivities on
different spaces, converging on A-TP as a joint target that neither
closes alone. *Status: genuine meeting point identified at the
Beilinson-Eisenstein class; both axes converge on A-TP but neither
closes it unconditionally.*

### Cycle 8: Cross-compare with Chapter 25 (arithmetic Positselski) and Chapter 45 (primitive zeta-character)

**Attack.** Chapter 25 inscribes the arithmetic Positselski
equivalence for the Iwasawa algebra $\Lambda$, using
Ferrero-Washington $\mu=0$ as the key hypothesis and Nakayama lifting
through a Weierstrass tower. Chapter 45 inscribes the primitive
zeta-character theorem, equating the character of the primary subspace
of the arithmetic Heisenberg Fock with $\xi(s)=\Gamma_{\mathbb{R}}(s)\zeta(s)$.
These chapters already carry substantial Iwasawa content. What is
missing from an A-TP perspective?

**Attempt 1.** Chapter 25 proves a categorical equivalence; Chapter
45 proves a character identity. Neither is a positivity statement.
The Iwasawa content in these chapters is the *denominator* of the
Riemann functional equation: $\mu=0$ ensures that the bar-cobar
Koszul pairing respects $\Lambda$-coefficient structure; Chapter 45
establishes that the character of the pair is symmetric under
$s\mapsto 1-s$. This gives $\xi(s)=\xi(1-s)$ at the level of
characters, not positivity.

**Heal.** What is missing from an A-TP perspective: a direct Iwasawa
input to the positivity of $W_{\infty}(f\ast\widetilde{f})$ on test
functions $f\in\mathrm{PW}(\mathbb{R})$. Chapters 25 and 45 give the
*functional equation framework* (symmetry under $s\mapsto 1-s$) but
not the *positivity framework* (sign of a distributional pairing).
The closest Iwasawa-side analog of a positivity is the
Bloch-Kato-Beilinson height pairing (Cycle 2), which lives on Selmer
groups of motives and is a pointwise positivity on a finite-dimensional
space, not a distributional positivity on $\mathrm{PW}(\mathbb{R})$.
The Iwasawa framework as developed in Chapters 25, 45, 54 supplies the
*arithmetic scaffolding* for the functional-equation side of RH (the
$s\mapsto 1-s$ symmetry) but not for the positivity side (A-TP).
*Status: Iwasawa content already in Vol IV is functional-equation
content, not positivity content; A-TP requires a different
contribution.*

### Cycle 9: The Colmez-Fontaine $(\varphi,\Gamma)$-module perspective

**Attack.** Colmez-Fontaine 2000 (Invent. Math. 140) classify
$p$-adic representations of $\mathrm{Gal}(\overline{\mathbb{Q}}_{p}/\mathbb{Q}_{p})$
by admissible $(\varphi,\Gamma)$-modules: finite-rank
$\mathcal{E}$-modules ($\mathcal{E}$ the Amice ring of Laurent series
over $\mathcal{O}_{K}$) with compatible $\varphi$-semilinear and
$\Gamma$-linear actions. Colmez 2010 (Astérisque 330) uses this to
construct the $p$-adic local Langlands correspondence for
$GL_{2}(\mathbb{Q}_{p})$. Claim: positivity of the $p$-adic
$L$-function at a $(\varphi,\Gamma)$-module level is controlled by
the weakly admissible filtration, and this positivity lifts to A-TP.

**Attempt 1.** The weakly admissible filtration on a
$(\varphi,\Gamma)$-module is a Hodge-like filtration
$\cdots\supset F^{i}\supset F^{i+1}\supset\cdots$ with the
Mazur-Fontaine slope inequalities $\mathrm{tN}(F^{i})\geq\mathrm{tH}(F^{i})$
(Newton polygon above Hodge polygon). These inequalities are
positivity statements but not in the sense A-TP needs: they are
discrete constraints on slopes, not inequalities on values of
distributions.

**Heal.** The Colmez-Fontaine framework is orthogonal to A-TP. It
classifies local representations at $p$; A-TP is a global archimedean
positivity statement. The two frameworks can interact through Kato's
Euler system (which uses local $p$-adic Hodge theory to control
Selmer groups globally), but the interaction is the one catalogued
in Cycle 2 and 4 and does not give new A-TP content. *Status:
Colmez-Fontaine $(\varphi,\Gamma)$-modules do not touch A-TP;
Falsified as an A-TP route.*

### Cycle 10: Fukaya-Kato non-commutative main conjectures and the non-abelian Iwasawa axis

**Attack.** Fukaya-Kato 2006 (Proc. St. Petersburg Math. Soc. XII)
formulate non-commutative Iwasawa main conjectures for motives with
coefficients in non-commutative Iwasawa algebras
$\Lambda_{G}=\mathbb{Z}_{p}[[G]]$ where $G$ is a compact $p$-adic Lie
group. The non-abelian case captures $GL_{2}$-level phenomena that
the abelian $\Lambda=\mathbb{Z}_{p}[[\Gamma]]$ cannot. Coates-Fukaya-
Kato-Sujatha-Venjakob 2005 (Publ. IHES 101) give the "GL_{2}-main
conjecture" for elliptic curves with good ordinary reduction at $p$.
Claim: the non-commutative $K_{1}$-theoretic formulation of the
main conjecture (Fukaya-Kato 2006 \S4) carries a positivity
(equivalently, a sign of a $K_{1}$-determinant) which transports to
A-TP.

**Attempt 1.** The non-commutative main conjecture asserts a
$K_{1}(\Lambda_{G,S})$ element $\zeta_{M,S}$ whose image in
$K_{1}(\mathrm{Frac}\,\Lambda_{G,S})$ matches the characteristic class
of the Selmer module. $K_{1}$ elements carry signs via
$R^{\times}/[R^{\times},R^{\times}]$, but the sign of a
Stickelberger-like element is not scalar positivity; it is a refined
constraint, not a sign inequality.

**Attempt 2.** Try the Coates-Fukaya-Kato-Sujatha-Venjakob
$GL_{2}$-main conjecture for a specific modular form $f$:
$(L_{p}(f))=\mathrm{char}_{\Lambda_{GL_{2}}}(\mathrm{Sel}(f))$. When
$\mathrm{Sel}(f)=0$, $L_{p}(f)$ is a unit. Apply at infinitely many
$f$ and use density to recover archimedean information about $\zeta$.
Skinner-Urban 2014 (Invent. Math. 195) proved the main conjecture
for $GL_{2}/\mathbb{Q}$ in many cases. But the proof is about
characteristic-ideal equality, not pointwise $L_{p}$-positivity, and
the density argument does not give archimedean positivity of $\zeta$
on the critical line.

**Heal.** The non-commutative Iwasawa framework refines the abelian
theory at the $GL_{2}$-level but operates on the same
functional-equation axis; it does not add a positivity axis. *Status:
Fukaya-Kato non-commutative main conjectures do not close A-TP;
orthogonal to the A-TP axis.*

### Cycle 11: Kolyvagin, Coates-Wiles, and pointwise versus distributional positivity

**Attack.** Two classical Euler-system theorems furnish pointwise
archimedean positivity that deserves examination as A-TP routes.
Kolyvagin 1988/1990 builds Euler systems from Heegner points on CM
elliptic curves, proving finiteness of $\mathrm{III}(E/\mathbb{Q})[p^{\infty}]$
when Gross-Zagier supplies a non-trivial Heegner point; the Heegner
height is non-negative and equals $L^{\prime}(E,1)$ up to an explicit
period (Gross-Zagier 1986 *Invent. Math.* 84). Coates-Wiles 1977
(*Invent. Math.* 39) uses a $p$-adic logarithmic-derivative
homomorphism $\phi(P)=\log_{p}(L_{p}(E,1))$ to prove the first
instance of BSD: if $E/\mathbb{Q}$ is CM and $L(E,1)\neq 0$, then
$E(\mathbb{Q})$ is finite. Claim: the non-negative Heegner height
and the non-vanishing $p$-adic regulator, taken together, furnish an
archimedean positivity that closes part of A-TP.

**Attempt 1.** Both theorems deliver positivity of a single
archimedean scalar ($L^{\prime}(E,1)$ in the Heegner case; $L(E,1)$
in the Coates-Wiles case), not positivity of a distribution on
$\mathrm{PW}(\mathbb{R})$. A single scalar positivity at a single
$L$-value is not the distributional data A-TP requires: A-TP
asserts a sign inequality simultaneously for all Paley-Wiener test
functions, and no countable collection of pointwise $L$-value
positivities recovers this.

**Heal.** Kolyvagin and Coates-Wiles are classical progenitors of
the Kato Euler system machinery; they furnish pointwise archimedean
positivity at specific $L$-values through specific Euler-system
constructions, but do not furnish distributional positivity. The
content they add beyond Cycle 2 is the explicit connection between
the motivic Euler system and the archimedean $L$-value via the
Gross-Zagier formula (for Kolyvagin) and the Coleman logarithm (for
Coates-Wiles); both connections pass through pointwise evaluation,
not distributional pairing. *Status: same as Cycle 2 at the
distributional level; Falsified as A-TP routes.*

### Cycle 12: A specific concrete attempt at a transport

**Attack.** Fix an even Dirichlet character $\chi\colon(\mathbb{Z}/N\mathbb{Z})^{\times}\to\mathbb{C}^{\times}$
of conductor $N$. The Mazur-Wiles theorem gives
$(L_{p}(\chi,s))=\mathrm{char}_{\Lambda}(X_{\chi})$ for each prime
$p\nmid N$. The corresponding Dirichlet $L$-function $L(\chi,s)$ has
a functional equation $\Lambda(\chi,s)=w(\chi)\Lambda(\chi^{-1},1-s)$
with $w(\chi)$ the root number. The Dirichlet $L$-function satisfies
a Weil explicit formula (summed over non-trivial zeros of $L(\chi,s)$):
$W^{\chi}(f)=\sum_{\rho}\widehat{f}(\gamma_{\rho})$. The $\chi$-twisted
A-TP is: $W^{\chi}_{\infty}(f\ast\widetilde{f})\leq W^{\chi}_{\mathrm{spec}}(f\ast\widetilde{f})$
for Paley-Wiener $f$. Specific attempt: use the Mazur-Wiles identity
to equate $(L_{p}(\chi,s))$ with $\mathrm{char}(X_{\chi})$ for many
primes $p$, and by the infinite-product formula $\zeta^{-1}=\prod_{p}(1-p^{-s})$,
transport the Iwasawa identity to the archimedean side.

**Attempt 1.** The infinite product $\prod_{p}(1-p^{-s})$ converges
for $\mathrm{Re}(s)>1$ but does not extend to a product over Iwasawa
main-conjecture ideals. Each Mazur-Wiles identity is at a fixed prime
$p$; the product over primes of the characteristic ideals is not a
well-defined object in any single framework. The naive transport
fails at the level of convergence.

**Heal.** The correct framework for the product over primes is
Bost-Connes / Connes-Marcolli (Cycle 5), which already captures the
multi-prime structure at the level of KMS states. Within this
framework, the $p\to\infty$ limit is not a naive product but a phase
transition. The Mazur-Wiles identity at each $p$ contributes one
pure-phase KMS state, and the archimedean A-TP is at the critical
temperature $\beta=1/2$ where no KMS state exists. *Status: the
specific concrete transport Falsified at the level of convergence;
the Bost-Connes framework absorbs it into the same phase-transition
picture of Cycle 5.*

### Cycle 13: What Iwasawa theory contributes, and what it does not

**Attack.** After twelve cycles the naive transports are all Falsified.
What does Iwasawa theory contribute to A-TP, if anything?

**Attempt 1.** Iwasawa theory contributes *nothing direct* to A-TP:
no Iwasawa theorem closes even a sub-class of the Paley-Wiener cone
on which A-TP holds. The only indirect contributions are (a)
Ferrero-Washington $\mu=0$, used in Chapter 25 to close the
$\Lambda$-coefficient Positselski equivalence on the functional-equation
axis; (b) the Kato Euler system, used (in Vol IV Chapter 45) implicitly
through the Eisenstein-series ancestor in the primitive zeta-character
computation; (c) the Bloch-Kato-Beilinson height pairing, used as a
motivating positivity statement at the motivic level but not at the
distribution level needed for A-TP.

**Heal.** The honest summary: Iwasawa theory is orthogonal to A-TP.
The Iwasawa axis encodes the functional-equation structure of
$\zeta$ through $p$-adic interpolation; A-TP is a positivity
statement about the archimedean distribution $W_{\infty}$. These are
two different structural features of $\zeta$, and Iwasawa theory
does not supply the positivity content. The Iwasawa axis *does*
supply the $\mu=0$ input to Chapter 25, the primitive zeta-character
closure of Chapter 45, and the categorical scaffolding of
$\Lambda$-coefficient Positselski equivalence. These are essential
*structural* contributions but not *positivity* contributions.

*Status: naive "Iwasawa closes A-TP" Falsified in all twelve specific
variants; Iwasawa axis contributes functional-equation scaffolding
but not positivity.*

### Cycle 14: The one residual Iwasawa-adjacent route worth flagging

**Attack.** Is there any single Iwasawa-adjacent theorem that, if
proved, would close A-TP? Not a transport of an existing Iwasawa
theorem, but a new Iwasawa theorem with explicit A-TP content?

**Attempt 1.** Consider the conjecture: *for the cyclotomic character
$\chi_{\mathrm{cyc}}\colon\Gamma\to\mathbb{Z}_{p}^{\times}$, the
$\Lambda$-valued $p$-adic $L$-function $L_{p}(\chi_{\mathrm{cyc}},\Lambda)$
satisfies a Deninger-style archimedean regulator positivity at the
$p\to\infty$ limit*. This is not a theorem; it is a reformulation of
A-TP in Iwasawa language, with the $p\to\infty$ limit absorbing the
archimedean place as in Connes-Marcolli 2008. The reformulation is
equivalent to A-TP (hence to RH) and does not simplify the problem.

**Heal.** The one Iwasawa-adjacent route that is *not* a tautological
reformulation is the following: consider the *archimedean Iwasawa
algebra* $\Lambda_{\infty}$ defined as the Connes-Marcolli adelic
enhancement of $\Lambda$ at the archimedean place, with generator the
logarithmic derivative $d/ds$ at $s=1/2$. The archimedean analog of
the Iwasawa main conjecture would equate $\Lambda_{\infty}$-valued
distributions with characteristic ideals of archimedean Iwasawa
modules. Such an archimedean main conjecture is Deninger's "zeta
function as a determinant of an archimedean Frobenius" programme
(Deninger 1998 *J. Reine Angew. Math.* 497; extended 2002
*Ann. Math.* 160). A Deninger-style archimedean Iwasawa main conjecture,
if formulated precisely, would be equivalent to RH and its positivity
instance would be A-TP. This is not an Iwasawa-theoretic route to A-TP
but a statement that A-TP is the expected content of the archimedean
Iwasawa main conjecture in Deninger's programme. *Status: honest
reformulation of A-TP in archimedean Iwasawa language via Deninger;
does not close A-TP; identifies the correct conjectural framework.*

## Convergence proposal

The shared object onto which this voice converges with the others
attacking A-TP is the *Iwasawa-archimedean orthogonal decomposition
of A-TP*: archimedean Tate positivity admits a functional-equation
axis and a positivity axis. The functional-equation axis is closed
by Iwasawa theory (Mazur-Wiles supplies $s\leftrightarrow 1-s$ at
every prime; Ferrero-Washington supplies $\mu=0$ enabling the
Positselski equivalence; Chapters 25 and 45 encode this axis in
bar-cobar form). The positivity axis is *not* closed by Iwasawa
theory: it is the residual after the functional-equation axis is
discharged, and requires Weil-axis (Chapters 57, 80: Rankin-Selberg
isometry, HFD bounded-spectral-interval) or Guinand-axis (Chapter
79: co-Poisson, Hilbert-transform) archimedean machinery.

**Formal statement.** *(Iwasawa-A-TP orthogonality.)* The Iwasawa
contribution to A-TP closure is:

1. For every even Dirichlet $\chi$ of conductor $N$ and every prime
   $p\nmid N$, Mazur-Wiles gives $\xi(\chi,s)=w(\chi)\xi(\chi^{-1},1-s)$
   at the characteristic-ideal level, the $s\leftrightarrow 1-s$
   symmetry required by A-TP's sign structure.
2. Ferrero-Washington $\mu(X_{K})=0$ for abelian $K$ is the
   torsion-finite hypothesis for the arithmetic Positselski
   equivalence of Chapter 25, hence for the Koszul formulation of
   $\xi(s)=\xi(1-s)$ of Chapter 45.
3. The residual A-TP positivity is orthogonal to Iwasawa theory:
   Bloch-Kato-Beilinson height pairings, Kato Euler system, $p$-adic
   regulators all furnish pointwise motivic positivity, not
   distributional positivity on $\mathrm{PW}(\mathbb{R})$. A-TP's
   positivity requires archimedean analytic machinery that Iwasawa
   theory does not supply.

**Joint statement with other voices.** The three-axis decomposition:

- Axis 1 (Weil-Petersson, Voice 1): prime-side positivity via
  Rankin-Selberg isometry, closes finite-prime Weil contribution
  on $\mathrm{PW}^{\mathrm{hol}}_{F}$ unconditionally; archimedean
  Tate positivity residual on the Weil kernel $\Phi_{\infty}^{W}$.
- Axis 2 (Guinand-Burnol, Voice 2): co-Poisson Hilbert-transform
  positivity on $\mathrm{PW}^{\mathrm{CP}}$ unconditionally;
  Fourier-dual to Axis 1, covering complementary test-function
  geometry.
- Axis 3 (Iwasawa, Voice 3 = this voice): functional-equation
  scaffolding; closes the $s\leftrightarrow 1-s$ symmetry at every
  prime via Mazur-Wiles main conjecture; enables the Koszul-duality
  formulation of $\xi(s)=\xi(1-s)$ through Ferrero-Washington $\mu=0$
  plus Chapter 25 arithmetic Positselski equivalence plus Chapter
  45 primitive zeta-character theorem. Does not close positivity.

A-TP's residual obstruction, after all three axes are discharged, is
the Fourier-self-dual bounded-spectral / bounded-time-domain locus
of Chapter 79 Remark 79.25 (the canonical Burnol-de Branges
obstruction to RH), which no axis individually closes.

**Theorem-waiting (joint with Voices 1, 2).** *(Three-axis A-TP
reduction.)* A-TP on the full Paley-Wiener class is strictly
equivalent to the Fourier-self-dual bounded-spectral-interval-plus-bounded-time-interval
positivity of the arithmetic Heisenberg pairing against the Burnol
kernel at the $p\to\infty$ critical-temperature limit of the
Connes-Marcolli Bost-Connes system. The reduction uses:

- (Weil axis) Chapter 57 Theorem 57.19 (Mellin-RS isometry).
- (Guinand axis) Chapter 79 Theorem 79.18 (co-Poisson sub-class
  closure).
- (Iwasawa axis) Chapter 25 Theorem 25.10 (arithmetic Positselski)
  + Chapter 45 Theorem 45.2 (primitive zeta-character) + Chapter
  54 Theorem 54.1 (four Positselski sub-items closed).

Status: Theorem-waiting (equivalent to RH; not a new result on
A-TP's positivity content but a precise decomposition of A-TP into
functional-equation content closed by Iwasawa and positivity content
orthogonal to Iwasawa).

## Summary

Iwasawa theory / Kato-Fukaya / $p$-adic $L$-functions contributes no
direct route to A-TP. Twelve naive transports (Mazur-Wiles value-
positivity; Kato Euler system / Bloch-Kato-Beilinson height pairing;
Ferrero-Washington archimedean analog; Perrin-Riou / Bloch-Kato
exponential; $p\to\infty$ Connes-Marcolli limit; Kato reciprocity;
Kolyvagin and Coates-Wiles pointwise positivity; Colmez-Fontaine
$(\varphi,\Gamma)$-modules; Fukaya-Kato non-commutative main
conjectures; Skinner-Urban; density of Dirichlet-$L$-twisted A-TP;
infinite-product transport) are all Falsified; the cross-compare
cycles identify Beilinson-Eisenstein class as common ancestor and
functional-equation scaffolding as Iwasawa's genuine contribution,
without closing A-TP.

The contribution: Iwasawa theory supplies the *functional-equation
axis* of A-TP (Mazur-Wiles main conjecture + Ferrero-Washington
$\mu=0$ + arithmetic Positselski equivalence + primitive
zeta-character theorem), the $s\leftrightarrow 1-s$ symmetry required
by A-TP's sign structure. It does *not* supply the *positivity axis*,
which remains orthogonal and must be closed by Voice-1 Weil-axis
(Rankin-Selberg / Petersson) or Voice-2 Guinand-axis (co-Poisson /
Hilbert-transform) or by new archimedean analytic methods. The
three-axis decomposition isolates the residual A-TP obstruction as
the Fourier-self-dual bounded-spectral-plus-bounded-time-domain
locus: the canonical Burnol-de Branges obstruction to RH.

Beilinson-principle closure: Iwasawa's contribution is named
precisely (functional-equation scaffolding via Chapters 25, 45, 54),
orthogonality to A-TP is named precisely (positivity is not an
Iwasawa content), and the joint three-axis decomposition is stated
as a Theorem-waiting equivalent to RH. No Iwasawa route to A-TP is
claimed; the one Iwasawa-adjacent framework worth flagging is
Deninger's archimedean-regulator programme (1998, 2002), which
formulates A-TP as the expected content of a hypothetical archimedean
Iwasawa main conjecture, itself RH-equivalent.
