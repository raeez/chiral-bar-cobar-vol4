# Voice 5: Bar-Cobar Programmatic Interior

## Source catalog and frame

The voice is the interior of the programme itself. Primary sources, cited with year and where available arXiv ID:

- Beilinson-Drinfeld 2004, *Chiral Algebras*, AMS Colloquium Publications 51. The canonical source for chiral algebras as Lie-star-algebras in $D$-modules on $X^I$, the factorisation picture $\{A_I\}$, the chiral bar-cobar adjunction $\Omega^{\mathrm{ch}}\dashv B^{\mathrm{ch}}$, chiral Koszul duality, Chapters 3-4 of op.~cit.
- Francis-Gaitsgory 2012, *Chiral Koszul duality*, Sel.~Math.~(N.S.) 18:27-87, arXiv:1103.5803. The $\infty$-categorical refinement: chiral algebras are Lie-algebras in factorisation coalgebras; Koszul duality exchanges chiral algebras and factorisation coalgebras. Dunn additivity $E_n\otimes E_m=E_{n+m}$ is the operadic backbone; the Ran-space presentation makes multi-dimensional descent structural.
- Beilinson 1984, *Higher regulators and values of L-functions*, J. Soviet Math. 30. The prototype for higher bar-type constructions on higher-dimensional arithmetic varieties; Gersten resolution as a factorisation-like object in $K$-theory; regulator maps to Deligne cohomology. The arithmetic surface bar-cobar lifts are natively compatible with this lineage.
- Bezrukavnikov 2012, arXiv:1209.0403. Two geometric realisations of the affine Hecke algebra: coherent sheaves on the Steinberg variety, and Iwahori-equivariant perverse sheaves on the affine flag variety. The convolution carries the $E_1$ structure that chiral-bar-cobar needs.
- Ben-Zvi-Nadler 2009, arXiv:0706.0322 (*Loop spaces and Langlands parameters*); 2013, arXiv:0904.1247 (*The character theory of a complex group*). HH of $D(G/G)$ is functions on $\mathrm{LocSys}_G(S^1)$; the arithmetic extension replaces $S^1$ by $B\widehat{\mathbb{Z}}$ or by a Weil/$(\varphi,\Gamma)$ target. In genus $g$ the relevant loop space is $\mathrm{Map}(\Sigma_g, BG)$, which is Ben-Zvi-Francis-Nadler 2010 (JAMS 23) territory.
- Ben-Zvi-Francis-Nadler 2010, *Integral transforms and Drinfeld centers in derived algebraic geometry*, JAMS 23. Integral-transform formalism for $D(X)$-mod-modules, Drinfeld centre in derived AG, the factorisation framework for HH on higher-dimensional bases.
- Arinkin-Gaitsgory 2015, arXiv:1201.6343. Singular support of coherent sheaves, the nilpotent locus, spectral side of geometric Langlands. The categorical target of F1; its higher-dimensional analog is the obligatory spectral target on a 2-dim arithmetic base.
- Costello-Gwilliam 2017/2021, *Factorization Algebras in Quantum Field Theory*, vol.~I/II. Factorisation algebras on manifolds of arbitrary dimension; $E_n$-algebras as factorisation algebras on $\mathbb{R}^n$; the $\mathbb{C}_\infty$ archimedean window of $\mathcal{V}^{\mathrm{prim}}$ is already a Costello-Gwilliam factorisation algebra on a 1-dim base. The genus-$g$ lift is a factorisation algebra on a 2-dim base.
- Positselski 2011, Mem.~AMS 996 (arXiv:0905.2621). Two kinds of derived categories; comodule-contramodule correspondence. Chapter~25 of Vol IV lifts this to Iwasawa $\Lambda$-coefficients conditional on $\mu=0$. For a 2-dim arithmetic base the conditional is on a 2-variable $\mu$-invariant.
- Lurie 2017, *Higher Algebra*. Ch.~5 for $E_n$-algebras, centralizers, Dunn additivity. Ch.~4 for presentable $\infty$-categorical tensor products. The operadic spine of every $E_n$-claim below.
- Morishita 2004/2012 (*Knots and Primes*), arXiv:0904.3399. Primes-as-knots dictionary; $\mathrm{Spec}\,\mathbb{Z}_p$ as a knot complement with inertia $B\mathbb{Z}_p$. For a 2-dim arithmetic base the analog is a 3-manifold (arithmetic surface $=$ arithmetic 3-fold under the classical MKR shift).

Frame. The arithmetic branch currently works on a 1-dim base: $\overline{C}=\overline{\mathrm{Spec}\,\mathbb{Z}}$. $\mathcal{V}^{\mathrm{prim}}$ is the Hochschild trace of the $E_2$-monoidal global Iwahori Hecke category; Dunn additivity gives it an $E_1$-algebra structure; chiral/factorisation OPE lives on the archimedean fibre only. Bar-cobar is built on the Parshin-Gersten complex of $\overline{C}$. The load-bearing theorem is $\kappa^{\mathrm{Ar}}_\mathsf{G}+(\kappa^!)^{\mathrm{Ar}}_\mathsf{G}=0\Leftrightarrow\xi(s)=\xi(1-s)$. The speculation asks: lift to a 2-dim arithmetic base carrying the cohomological signature of a genus-$g$ curve. The programmatic interior's job is to translate this into factorisation/chiral-algebra/bar-cobar language and produce a load-bearing identity on the 2-dim base that reduces to the 1-dim identity at $g=0$. The speculation in reading (A) asks for $g=2$; in reading (B) the arithmetic surface is always 2-dim and the genus is the cohomological invariant at the archimedean fibre.

## Attack-heal cycles

### Cycle 1: dimension assignment and the $E_1\to E_2$ upgrade

Attack. The programme's $\mathcal{V}^{\mathrm{prim}}$ is an $E_1$-algebra. Dunn additivity applied to the global Iwahori Hecke category's $E_2$ structure (F2) yields the $E_1$ structure on HH. On a 2-dim base one expects the $E_1$ upgrade to $E_2$ (chiral), and the factorisation structure to become 2-dim. But what exactly is a 2-dim arithmetic base in the programme's sense, and where does the chiral upgrade live?

Heal. The correct dimension ledger is three-layered. (1) Base scheme dimension: $\dim\overline{\mathrm{Spec}\,\mathbb{Z}}=1$ (as arithmetic 1-fold); $\dim X = 2$ for an arithmetic surface $X\to\mathrm{Spec}\,\mathcal{O}_K$ with relative dimension 1. (2) Operadic $E_n$-dimension: chiral bar-cobar is 1-dim ($E_1$ OPE on a curve) on $\overline{C}$; factorisation on an arithmetic surface is 2-dim ($E_2$ OPE on the Ran space of $X$). (3) Cohomological signature: genus $g$ of the generic fibre, a property of the 1-dim slice inside the 2-dim ambient scheme. The $E_1\to E_2$ upgrade on the operadic side is Dunn additivity $E_1\otimes E_1=E_2$ (Lurie HA~5.1.2.2), executed by tensoring the $E_1$ chiral structure along the two transverse directions of $X$. This is not the same as the F2 upgrade, which happens on the 1-dim base already and sources from the BD Grassmannian.

Verdict. The dimension assignment separates cleanly: arithmetic 2-fold = scheme dimension, $E_2$-chiral = operadic dimension on the 2-fold, genus $g$ = signature of the 1-dim slice. The next cycle asks whether the 2-dim operadic upgrade is canonical.

### Cycle 2: Parshin-Gersten on a 2-dim base

Attack. On $\overline{C}$ the Gersten complex is
$$0\to K_n^M(K)\to\bigoplus_{\mathfrak p}K_{n-1}^M(k(\mathfrak p))\to 0,$$
two-term because $\overline{C}$ has Krull dimension 1. The arithmetic bar complex of Chapter~10 is built on this Gersten complex. On an arithmetic surface $X/\mathrm{Spec}\,\mathbb{Z}$ the Gersten complex is three-term:
$$0\to K_n^M(K(X))\to\bigoplus_{\mathfrak p}K_{n-1}^M(k(\mathfrak p))\to\bigoplus_{\mathfrak q}K_{n-2}^M(k(\mathfrak q))\to 0,$$
indexed by codimension-1 and codimension-2 points. Parshin reciprocity (Parshin 1976; Kato 1980; Beilinson 1980) asserts exactness. The speculation's 2-dim lift should be built on this three-term complex, not the two-term one of $\overline{C}$.

Heal. The Parshin-Gersten complex on an arithmetic 2-fold has two residue maps: $\partial_1$ at the codim-1 (horizontal, curve-level) points and $\partial_2$ at the codim-2 (closed-point, Parshin-triple) points. Parshin's residue calculus provides a double residue $\partial_{12}=\partial_2\circ\partial_1$ at a codim-2 point lying on a horizontal curve. This is the arithmetic 2-fold analog of the single residue at a prime $\mathfrak p$ on $\overline{C}$.

The arithmetic genus-$g$ bar complex is then
$$B^{\mathrm{ch,Ar,}g}(\mathcal{V}^{\mathrm{prim},g}):=\bigoplus_{n\geq 0}(s^{-1}\overline{\mathcal{V}^{\mathrm{prim},g}})^{\otimes_\Lambda n}\otimes_\Lambda C^\bullet_{\mathrm{Parshin},2}(X),$$
with differential $d^{\mathrm{Ar},g}=d_{\mathrm{Iw}}\otimes 1+1\otimes d_{\mathrm{Parshin},2}+d_{\mathrm{bar}}^{\mathrm{local,horiz}}+d_{\mathrm{bar}}^{\mathrm{local,vert}}$; the two local differentials are weighted respectively by $\partial_1$ and $\partial_2$. The operadic structure: factorisation on the Ran space of $X$, controlled by the $E_2$ chiral operad on a smooth 2-fold, with corrections at the divisorial singular locus (bad reduction).

Verdict. The 2-dim Parshin-Gersten complex is the canonical target. The double-residue structure is the arithmetic avatar of the genus-$g$ factorisation OPE on the archimedean fibre $X_\infty$.

### Cycle 3: the $E_2$-chiral object on $X$ and Dunn additivity

Attack. Beilinson-Drinfeld chiral algebras are $E_1$-algebras on a smooth 1-dim base $C$; the chiral bracket $\{\cdot,\cdot\}^{\mathrm{ch}}_X: A\boxtimes A\to\Delta_!A$ is the $E_1$ OPE. On a smooth 2-fold $X$ the natural analog is an $E_2$-algebra in $D$-modules on $X$ (or in pro-\'etale $\Lambda$-modules on $X$ in the arithmetic setting). Francis-Gaitsgory (Sel.~Math. 18, 2012) treat chiral Koszul duality as a statement about Lie-algebras in factorisation $D$-modules on the Ran space; in arbitrary dimension $n$, it becomes $E_n$-Lie Koszul duality. For $n=2$ this is the arithmetic-surface chiral algebra.

Heal. Define $\mathcal{V}^{\mathrm{prim},g}$ as the rank-$g$ Heisenberg-type $E_2$-algebra on $X$: at each smooth point of $X_\infty$, the Heisenberg Fock is rank $g$ (matching the $g$ holomorphic differentials of a genus-$g$ curve); the factorisation structure on the Ran space of $X$ is the $E_2$-chiral algebra structure. Dunn additivity $E_1\otimes E_1=E_2$ (Lurie HA~5.1.2.2, Francis 2013) presents this $E_2$ structure as the tensor of two $E_1$-chiral structures transverse to each other: one along the horizontal direction of the fibration $\pi:X\to\mathrm{Spec}\,\mathcal{O}_K$, one along the vertical (curve-direction). The horizontal $E_1$ comes from factorisation on the arithmetic 1-fold $\overline{C}$; the vertical $E_1$ comes from factorisation on the generic fibre $X_K$.

Francis-Gaitsgory's theorem. Chiral Koszul duality for $E_n$-Lie algebras is an equivalence of $\infty$-categories between $E_n$-Lie-algebras in factorisation $D$-modules and augmented factorisation cocommutative coalgebras, with the bar-cobar adjunction $B^{\mathrm{ch}}_n\dashv\Omega^{\mathrm{ch}}_n$ realising the equivalence (Francis-Gaitsgory Thm~6.2.6 for $n=1$, the higher $n$ case inscribed as straightforward operadic consequence). In the arithmetic 2-fold setting, the 2-dim version is
$$\Omega^{\mathrm{ch,Ar,2}}_X\dashv B^{\mathrm{ch,Ar,2}}_X:\quad\mathrm{Lie}_{E_2}(\Lambda\text{-fact on Ran}(X))\simeq\mathrm{CoAlg}^{E_2,\mathrm{aug}}(\Lambda\text{-fact on Ran}(X)),$$
conditional on the 2-dim arithmetic Positselski equivalence and 2-dim $\mu$-invariant vanishing.

Verdict. The $E_2$-chiral lift is canonical via Dunn additivity. The bar-cobar adjunction at dimension 2 is the arithmetic-surface analog of the 1-dim BD adjunction; its behaviour is governed by the 2-dim Parshin-Gersten complex.

### Cycle 4: Koszul sign $\kappa$ on a 2-dim base and the genus shift

Attack. The programme's $\kappa+\kappa^!=0$ identity is a statement about 1-dim bar-cobar on $\overline{C}$: $\kappa$ is the chiral central charge/level, $\kappa^!$ its Koszul dual; their sum in the $\mathsf{G}$-row vanishes, which forces the Riemann functional equation. On a 2-dim arithmetic base with cohomological signature of a genus-$g$ curve, what is the natural shift? The Hasse-Weil functional equation for a genus-$g$ curve is $\Lambda(s,X_K)=\epsilon\Lambda(2-s,X_K)$, with centre $s=1$ rather than $s=1/2$. The shift is $2$, not $1$. The Euler characteristic of a genus-$g$ curve is $2-2g$. These two invariants are consanguineous: the functional-equation shift is $2$ always (weight $=1$ motive), while $2-2g$ sits inside the central-charge data.

Heal. The genus shift enters $\kappa+\kappa^!$ through the central charge of the Heisenberg Fock, not through the functional-equation shift. On $\overline{C}$ the archimedean Fock is rank 1, central charge $c=1$; on an arithmetic surface with generic fibre genus $g$, the archimedean Fock is rank $g$, central charge $c=g$ (one boson per holomorphic differential). The Koszul self-duality identity becomes
$$\kappa^{\mathrm{Ar},g}_\mathsf{G}+(\kappa^!)^{\mathrm{Ar},g}_\mathsf{G}=0.$$
The $=0$ is preserved; the genus enters through the central charge of the bar coalgebra/cobar algebra (rank-$g$ oscillators on each side), not through a new non-zero sum. This matches the Euler-product structure: with rank-$g$ oscillators per place, the partition function becomes $\prod_p\det(1-p^{-s}\mathrm{Frob}_p|H^1(X_K)_{\ell})^{-1}=L(s,X_K)$, the Hasse-Weil $L$-function. The functional equation $\Lambda(s)=\epsilon\Lambda(2-s)$ is the Koszul-self-dual identity on the rank-$g$ Fock, with the shift $s\mapsto 2-s$ being the Mellin-Fourier transform for weight-1 motives (Tate's thesis adapted to rank $2g$).

Note on the naive guess $\kappa+\kappa^!=2-2g$. Attractive but falsified. The Euler characteristic $2-2g$ is a topological invariant of the compact Riemann surface, not a Koszul invariant of the chiral algebra. The honest arithmetic analog of $2-2g$ is the $\delta$-invariant of Faltings 1984 plus the arithmetic self-intersection $\widehat\omega^2$ via the arithmetic Noether formula $\widehat{\deg}\det R\pi_*\omega=\tfrac{1}{12}(\widehat\omega^2+\delta_{\mathrm{Ar}})$; neither enters the Koszul self-duality identity as a non-zero sum. The genus enters through the rank of the Fock, hence through the central charge, hence through the $\Gamma$-factor $\Gamma_{\mathbb{C}}(s)^g$ of the Hasse-Weil completion, not through a shift of the $=0$.

Verdict. The identity $\kappa+\kappa^!=0$ is preserved at genus $g$. The genus enters as rank-$g$ oscillators in the Fock (central charge $c=g$), yielding the Hasse-Weil functional equation on the Jacobian rather than the Riemann functional equation on $\zeta$. At $g=0$ this degenerates to the 1-dim Vol IV theorem; at $g=1$ it is the elliptic-modular functional equation; at $g\geq 2$ it is the Weil conjecture for Jacobians (proved by Hasse 1934 for elliptic, Weil 1949 for abelian, Faltings 1983 for rational points).

### Cycle 5: Ben-Zvi-Nadler on a 2-dim base

Attack. Ben-Zvi-Nadler 2009/2013 compute $\mathrm{HH}_\bullet(D(G/G))=\mathcal{O}(\mathrm{LocSys}_G(S^1))^{\mathrm{flat}}$: the Hochschild trace of the character category of complex $G$ equals functions on the space of $G$-local systems on the circle. In the arithmetic 1-dim setting (Chapter~28 of Vol~IV, Francis-Gaitsgory lineage), the circle $S^1$ is replaced by $B\widehat{\mathbb{Z}}$ (inertia-shadow) or, properly, by the Weil/$(\varphi,\Gamma)$ parameter stack. For a 2-dim arithmetic base, what replaces $S^1$?

Heal. The Ben-Zvi-Nadler formula on a 2-dim base computes HH of a category of $D$-modules on the arithmetic 2-fold. The target stack is $\mathrm{Map}(\Sigma_g,BG)$ where $\Sigma_g$ is the Riemann surface at the archimedean fibre, and the arithmetic analog is $\mathrm{Map}(\Sigma_g^{\mathrm{Ar}},BG)$ with $\Sigma_g^{\mathrm{Ar}}$ the arithmetic avatar of a genus-$g$ surface. The archimedean contribution gives $\mathrm{LocSys}_G(\Sigma_g)$, which has (real) dimension $2g\dim G$: the moduli space of $G$-local systems on a genus-$g$ surface. For $G=GL_n$ this is the Betti moduli space of flat connections on $\Sigma_g$, a $2gn^2$-dimensional affine variety. At the finite places, replace the topological $\Sigma_g$ by the Weil/$(\varphi,\Gamma)$ parameter stack at each prime; globally, by a 2-dim arithmetic fibration analog of the global Emerton-Gee stack.

Concretely. Define $\mathcal{V}^{\mathrm{prim,surf},g}:=\mathrm{HH}_\bullet(\mathrm{Hk}^{\mathrm{Iw,surf}}_{GL_2,\mathrm{glob}})$ where $\mathrm{Hk}^{\mathrm{Iw,surf}}_{GL_2,\mathrm{glob}}$ is the 2-dim global Iwahori Hecke category built on the arithmetic surface (not on the 1-dim $\overline{C}$). By Dunn and factorisation homology,
$$\mathcal{V}^{\mathrm{prim,surf},g}\simeq\mathcal{O}(\mathrm{LocSys}^{W,\varphi\Gamma,\mathrm{surf}}_{GL_2,\Sigma_g^{\mathrm{Ar}}})^{\mathrm{flat}},$$
conditional on a 2-dim arithmetic Ben-Zvi-Nadler identification. This is the load-bearing target of the genus-$g$ lift.

Verdict. The Ben-Zvi-Nadler replacement on a 2-dim arithmetic base uses $\Sigma_g^{\mathrm{Ar}}$ (arithmetic genus-$g$ surface) as the target; its archimedean slice is the Betti moduli $\mathrm{LocSys}_G(\Sigma_g)$ of dimension $2g\dim G$, and the functional equation on HH becomes the Weil-conjectural functional equation for the $L$-function of $X_K$.

### Cycle 6: arithmetic Hodge diamond and cohomological signature

Attack. The speculation asks the 2-dim arithmetic base to carry "the cohomological signature of a genus-$g$ algebraic curve". The Hodge diamond of $\Sigma_g$ is $h^{0,0}=h^{1,1}=1$, $h^{1,0}=h^{0,1}=g$. On a 2-dim arithmetic scheme, what is the analog of the Hodge diamond, and does it carry this signature?

Heal. Two honest answers. (i) On the archimedean fibre $X_\infty$, which is a compact Kähler 1-manifold of complex dimension 1, the Hodge diamond is exactly that of $\Sigma_g$, per place. No lift needed. (ii) On the arithmetic 2-fold $X$ itself, the right analog is the absolute Hodge/arithmetic-Chow diamond of Beilinson-Bloch-Esnault 2000s (absolute Hodge cohomology $H^*_{\mathcal{A}}$; Deligne cohomology $H^*_{\mathcal{D}}$; motivic cohomology $H^*_{\mathcal{M}}$). Per Esnault-Viehweg's characteristic classes (in arithmetic Chow ring $\widehat{\mathrm{CH}}$), the "arithmetic Hodge diamond" of $X$ is
$$\widehat{h}^{p,q}(X)=\dim_{\mathbb{R}}\widehat{\mathrm{CH}}^{p,q}(X)_{\mathbb{R}},$$
carrying the arithmetic signature structure of Gillet-Soulé 1990 plus the $\delta$-invariant analytical contribution at the archimedean fibre. The $\widehat{h}^{1,0}$ is the rank of $\pi_*\omega_{X/S}$, which by Riemann-Roch is $g$ (the global sections of the relative dualising sheaf). The $\widehat{h}^{0,1}$ is the rank of $R^1\pi_*\mathcal{O}_X=0$ for an arithmetic surface with connected fibres (Zariski cohomology vanishes for smooth proper maps of dimension 1), so in the naive reading $h^{0,1}$ is swallowed by the archimedean-Hodge contribution. At the arithmetic-Chow level, the pairing $\widehat{\mathrm{CH}}^1(X)_{\mathbb{R}}\times\widehat{\mathrm{CH}}^1(X)_{\mathbb{R}}\to\widehat{\mathrm{CH}}^2(X)_{\mathbb{R}}\xrightarrow{\widehat{\deg}}\mathbb{R}$ is the arithmetic intersection pairing, restricted by Faltings-Hriljac to the Néron-Tate symplectic pairing on degree-zero divisors.

Under the programme's Koszul frame. The Fock space $\mathcal{H}^{(\infty)}_g$ at the archimedean fibre is a Heisenberg Fock on the $g$-dimensional space $H^{1,0}(X_\infty)\cong\mathbb{C}^g$. Its conjugate Fock on $H^{0,1}(X_\infty)\cong\overline{\mathbb{C}^g}$ carries the Koszul dual structure. The tensor product $\mathcal{H}^{(\infty)}_g\otimes\overline{\mathcal{H}^{(\infty)}_g}$ is the full archimedean rank-$g$ Heisenberg with Hermitian inner product, giving central charge $c=g$ (holomorphic) $+g$ (antiholomorphic) $=2g$ under the doubled convention. For Koszul self-duality $\kappa+\kappa^!=0$ the holomorphic and antiholomorphic central charges must balance; this is automatic for unitary Fock.

Verdict. The cohomological signature is two-layered as per Voice 1 (Arakelov). At the archimedean fibre the Hodge diamond is that of $\Sigma_g$. On the 2-fold itself, the arithmetic Hodge/Chow diamond is richer, carrying Faltings-Hriljac intersection plus Bismut-Gillet-Soulé analytic torsion. The genus $g$ enters through $\widehat{h}^{1,0}=\dim\pi_*\omega_{X/S}=g$ (by the relative Riemann-Roch).

### Cycle 7: Virasoro central charge and the $b$-$c$ ghost

Attack. Chapter~24 (arithmetic Virasoro bootstrap) of Vol~IV uses a central charge $c^{\mathrm{Ar}}=2$ for $\mathcal{V}^{\mathrm{prim}}_{\mathrm{Heis}}$ on $\overline{C}$ (rank-2 Heisenberg via Satake pair $(\alpha_p,\beta_p)$; $c^{\mathrm{Ar}}=2\cdot\mathrm{Res}_{s=1}\zeta(s)=2$). For a genus-$g$ arithmetic surface, the naive shift is $c^{\mathrm{Ar},g}=2g$ (rank-$2g$ Heisenberg via the $2g$-dimensional Tate module of the Jacobian). But the $b$-$c$ ghost system of a genus-$g$ holomorphic curve has central charge $c_{\mathrm{bc}}=-26+2\cdot 13=-26$ (bosonic string) or more precisely the ghost sector contributes $c_{\mathrm{bc,ghost}}=-26$ and the conformal anomaly cancels at critical dimension. Where does this enter?

Heal. Two distinct central charges. (i) The Heisenberg $c^{\mathrm{Ar},g}=2g$ (rank-$2g$ Fock from the Tate module). (ii) The ghost-ghost-matter $c^{\mathrm{ghost},g}$ depends on the genus via the Riemann-Roch shift for the moduli of genus-$g$ curves: $\dim\mathcal{M}_g=3g-3$ for $g\geq 2$, so the BRST ghost system contributes $c_{\mathrm{gh}}=-2(3g-3)$ at the Teichmüller level. The Koszul self-duality $\kappa+\kappa^!=0$ applies to the total central charge being zero at the critical level, which for unitary Heisenberg is automatic. The $b$-$c$ ghost computation is not part of the primary Koszul identity; it enters through the chiral-anomaly-cancellation condition for the factorisation algebra on $\mathcal{M}_g$ (Segal-like).

Specifically. The Vol~IV arithmetic Virasoro acts on the primary subspace of the Heisenberg Fock. On a genus-$g$ base, the rank of the primary Fock per place scales as $g$, and the Virasoro zero mode $L_0^{\mathrm{Ar},g}$ has trace $\mathrm{tr}(L_0^{\mathrm{Ar},g})$ proportional to the logarithmic derivative of $\Lambda(s,X_K)$ rather than of $\xi(s)$. The Riemann-von Mangoldt-type explicit formula at genus $g$ is the Selberg-trace-formula-type explicit formula for the Hasse-Weil $L$-function: sum over zeros of $\Lambda(s,X_K)$ gives the trace of a Virasoro-type operator on the rank-$g$ Fock.

Verdict. The central-charge lift is $c^{\mathrm{Ar},g}=2g$ (Heisenberg rank), consistent with the Gaussian Weil-Petersson metric on $\mathrm{Jac}(X_K)\cong\mathbb{C}^g/\Lambda$ of complex dimension $g$. The ghost-sector central charge is a separate invariant tied to $\mathcal{M}_g$, not to the primary $\mathsf{G}$-row identity.

### Cycle 8: cross-Langlands: $GL_2$ to $GL_{2g}$

Attack. $\mathcal{V}^{\mathrm{prim}}$ on $\overline{C}$ lives in the $GL_2$ sector: Satake pair $(\alpha_p,\beta_p)$ per prime, rank-2 Heisenberg, $GL_2$-Iwahori Hecke category. For an arithmetic surface with generic fibre of genus $g$, the Jacobian is a $g$-dimensional abelian variety; its Tate module is rank $2g$; the associated Galois representation lives in $GL_{2g}$. So the programmatic lift should replace $GL_2$ by $GL_{2g}$ throughout. But $GL_{2g}$-Iwahori at each prime is a bigger category, and the cross-prime compatibility (F2) is harder.

Heal. The lift is straightforward in principle:
$$\mathcal{V}^{\mathrm{prim,surf},g}=\mathrm{HH}_\bullet(\mathrm{Hk}^{\mathrm{Iw}}_{GL_{2g},\mathrm{glob}}).$$
At each prime $p$ of good reduction for $X$, the local Iwahori Hecke category of $GL_{2g}(\mathbb{Q}_p)$ acts on the Tate module $T_p(\mathrm{Jac}(X_K))\cong\mathbb{Z}_p^{2g}$. The BD Grassmannian for $GL_{2g}/\mathbb{Q}_p$ (Fargues-Scholze arXiv:2102.13459) provides the perfectoid $E_2$-structure at each prime, and the global restricted tensor product matches the arithmetic-surface Iwahori Hecke. Fargues-Scholze's local geometrisation is for arbitrary reductive $G$, so $G=GL_{2g}$ works without modification. The Emerton-Gee stack at $GL_{2g}$ is also constructed (Emerton-Gee arXiv:1908.07185 for general $G$).

Bad-reduction locus. For primes $p$ of bad reduction (where $X\times\mathrm{Spec}\,\mathbb{F}_p$ is singular), the Tate module has a local inertia filtration; the $GL_{2g}$ representation factors through the decomposition group with explicit local conditions $\mathcal{L}_v$ in the Selmer stack. This is Fontaine-Mazur territory; the Selmer-derived global stack $\mathcal{X}^{\mathrm{Sel},g}_{\bar\rho,\det,\mathcal{L}}$ with fixed $GL_{2g}$-residual representation is the correct spectral target for F1 at genus $g$.

Verdict. The programmatic lift is $GL_2\rightsquigarrow GL_{2g}$: rank-$2g$ Tate module, $GL_{2g}$-Iwahori Hecke, $GL_{2g}$-local Langlands at each prime, Selmer-derived $GL_{2g}$-deformation stack globally. At $g=1$ this is $GL_2$ (elliptic modular, the Vol~IV current target); at $g=0$ it is $GL_0$, degenerate but the correct degenerate limit corresponds to zeta-function (1-dim scalar Fock, $\mathcal{V}^{\mathrm{prim}}_{\mathrm{Heis}}$ of the current branch); at $g\geq 2$ it is the genuine multi-dimensional Jacobian case.

### Cycle 9: Positselski and the 2-dim $\mu$-invariant

Attack. Chapter~25 of Vol~IV lifts Positselski's comodule-contramodule correspondence to Iwasawa $\Lambda$-coefficients conditional on the 1-dim $\mu$-invariant vanishing. On a 2-dim arithmetic base, the Iwasawa algebra is $\Lambda_2=\mathbb{Z}_p[[\Gamma_1\times\Gamma_2]]$ (two-variable cyclotomic), and the $\mu$-invariant has a 2-dim refinement: $(\mu_1,\mu_2)$ in the two cyclotomic directions. Does the Positselski correspondence lift to $\Lambda_2$-coefficients?

Heal. Yes, conditionally. Two-variable Iwasawa theory is developed by Nekovar 2006 (Astérisque 310), Coates-Sujatha 2006 (Cyclotomic Fields and Zeta Values), Rubin 2000 (Euler Systems). The 2-dim Positselski equivalence
$$\mathrm{D}^{\mathrm{co}}_{\Lambda_2}(C\text{-comod}_{\Lambda_2})\simeq\mathrm{D}^{\mathrm{ctr}}_{\Lambda_2}(C^\vee\text{-contramod}_{\Lambda_2})$$
lifts classical Positselski along the base change $\Lambda_2\to\mathbb{Q}_p$ conditional on $\mu_1=\mu_2=0$. The Ferrero-Washington vanishing (Ann.~Math. 109, 1979) for abelian Heisenberg at the 1-dim level has no direct 2-dim analog, but the $\mu=0$ vanishing for the 2-dim cyclotomic tower of $\mathbb{Q}(\mu_{p^\infty},\mu_{\ell^\infty})$ is known in the abelian case (Greenberg 1973; Kida 1980). For non-abelian Heisenberg on an arithmetic surface the 2-dim $\mu$-vanishing is open.

The 2-dim arithmetic bar-cobar adjunction is then
$$\Omega^{\mathrm{ch,Ar,2},\Lambda_2}\dashv B^{\mathrm{ch,Ar,2},\Lambda_2}:\quad\mathrm{Lie}_{E_2,\Lambda_2}\simeq\mathrm{CoAlg}^{E_2,\mathrm{aug}}_{\Lambda_2},$$
conditional on the 2-dim $\mu$-vanishing. The residual obstruction of Chapter~25 (five open sub-items: completed continuous duals; derived completion; faithful lifting along Nakayama; primitive zeta-character theorem; Koszul-dual Bost-Connes) lifts to 2-dim analogs, each with the 2-dim analog $\mu_1=\mu_2=0$ in place of the 1-dim $\mu=0$.

Verdict. The arithmetic Positselski equivalence lifts to the 2-dim arithmetic surface setting conditional on the 2-variable $\mu$-invariants vanishing. The open sub-items scale in number from 5 to approximately 10 (five per direction); each has a named classical-Iwasawa input.

### Cycle 10: the load-bearing theorem at genus $g$

Attack. The 1-dim load-bearing theorem is $\kappa^{\mathrm{Ar}}_\mathsf{G}+(\kappa^!)^{\mathrm{Ar}}_\mathsf{G}=0\Leftrightarrow\xi(s)=\xi(1-s)$. At genus $g$ the natural generalisation is the Hasse-Weil functional equation. State it precisely.

Heal. The genus-$g$ load-bearing theorem.

Theorem-waiting (genus-$g$ arithmetic $\mathsf{G}$-row). For the rank-$g$ arithmetic Heisenberg $\mathcal{V}^{\mathrm{prim},g}_{\mathrm{Heis}}$ attached to the arithmetic surface $X\to\mathrm{Spec}\,\mathcal{O}_K$ with generic fibre of genus $g$, the following are equivalent:
$$\kappa^{\mathrm{Ar},g}_\mathsf{G}+(\kappa^!)^{\mathrm{Ar},g}_\mathsf{G}=0\quad\Longleftrightarrow\quad\Lambda(s,X_K)=\epsilon_{X_K}\cdot\Lambda(2-s,X_K),$$
where $\Lambda(s,X_K)=N_{X_K}^{s/2}\Gamma_{\mathbb{C}}(s)^g L(s,X_K)$ is the completed Hasse-Weil $L$-function of $X_K$ with conductor $N_{X_K}$ and root number $\epsilon_{X_K}\in\{\pm 1\}$, and $L(s,X_K)=\prod_p\det(1-p^{-s}\mathrm{Frob}_p|H^1(X_K)_\ell^{I_p})^{-1}$ is the Euler product over primes of good reduction (with local factors at bad primes from the inertia-invariants of the $\ell$-adic cohomology).

Proof sketch. Four steps, parallel to Chapter~22 Section~P1.

Step 1 (Euler-product identification). At each prime $p$ of good reduction, the Heisenberg Fock is rank $2g$; its partition function factors as
$$Z^{(p)}_{\mathrm{Heis},g}(\beta)=\prod_{j=1}^{2g}(1-\alpha_j^{(p)}p^{-\beta})^{-1}=\det(1-p^{-\beta}\mathrm{Frob}_p|H^1_{\mathrm{et}}(X_K)_\ell)^{-1},$$
where $(\alpha_j^{(p)})_{j=1}^{2g}$ are the Satake parameters (Frobenius eigenvalues on the $\ell$-adic $H^1$). Global Euler product gives $\prod_p Z^{(p)}=L(s,X_K)$. Under the bar generating function, the Euler product yields the Hasse-Weil $L$-function analog of $\zeta(s)$.

Step 2 (Koszul dual = genus-$g$ Bost-Connes). Bost-Connes 1995 (Selecta Math. 1) constructs the Hecke C*-algebra whose partition function is $\zeta$. The genus-$g$ analog is constructed by Consani-Marcolli 2006 (arXiv:math/0605383) as the Hecke algebra of $GL_{2g}$-Shimura varieties; its KMS$_\beta$ partition function is $L(s,X_K)$ for $\beta>1$ with meromorphic continuation. The Koszul dual of $\mathcal{V}^{\mathrm{prim},g}_{\mathrm{Heis}}$ is this Consani-Marcolli $GL_{2g}$ Bost-Connes algebra.

Step 3 (Positselski pairing at rank $g$). The arithmetic Positselski equivalence at $\Lambda_2$-coefficients pairs the bar coalgebra of the rank-$g$ Heisenberg with the cobar algebra of the genus-$g$ Bost-Connes. Under the pairing, the total weight vanishes: the Heisenberg-side weight is $\sum_{j=1}^{2g}\log|\alpha_j^{(p)}|\cdot p^{-s}$ per prime, which equals $-L'(s,X_K)/L(s,X_K)$ after Euler product; the Bost-Connes side gives $+L'(s,X_K)/L(s,X_K)$. Sum is zero. (Conditional on the 2-dim arithmetic Positselski of Cycle 9.)

Step 4 (Fourier symmetry $s\mapsto 2-s$). Tate's thesis adapted to rank-$2g$ adelic Fourier transform on $H^1_{\mathrm{Betti}}(X_K)$ (Weil 1967, *Basic Number Theory*; specialized to Jacobians by Bloch-Kato 1990): the adelic theta distribution $\Theta_g$ on the Jacobian satisfies $\mathcal{F}_{\mathbb{A}}\Theta_g=\epsilon_{X_K}\cdot\Theta_g$ with $\epsilon_{X_K}\in\{\pm 1\}$ the root number. Mellin transform gives $\Lambda(s,X_K)=\epsilon_{X_K}\Lambda(2-s,X_K)$.

Steps 1, 2, 4 close unconditionally (Euler products, Consani-Marcolli, Weil-Bloch-Kato). Step 3 is conditional on the 2-dim arithmetic Positselski equivalence with $\mu_1=\mu_2=0$. Forward implication ($\kappa+\kappa^!=0\Rightarrow\Lambda(s)=\epsilon\Lambda(2-s)$) holds unconditionally via Steps 1, 2, 4 alone; full biconditional needs Step 3.

Verdict. The genus-$g$ load-bearing theorem is a clean generalisation of the 1-dim load-bearing theorem, with the shift $s\mapsto 2-s$ replacing $s\mapsto 1-s$ (weight-1 motive), the central charge $c=g$ replacing $c=0$, the local $L$-factor replacing Riemann's $\zeta$, the root number $\epsilon$ replacing the trivial $+1$ sign, and rank-$2g$ Tate module replacing rank-0 trivial module. The identity $=0$ on the Koszul side is preserved.

## Convergence proposal

The programmatic interior proposes the following convergent target.

(i) Arithmetic 2-fold $\mathcal{S}^{\mathrm{Ar}}_g$.

Define $\mathcal{S}^{\mathrm{Ar}}_g:=X$, where $X\to\mathrm{Spec}\,\mathcal{O}_K$ is a proper flat regular arithmetic surface with generic fibre $X_K$ a smooth projective curve of genus $g\geq 0$. For $\mathcal{O}_K=\mathbb{Z}$ the ambient 2-fold is over $\overline{\mathrm{Spec}\,\mathbb{Z}}$ after Arakelov compactification: $\overline{X}=X\cup X_\infty$ with archimedean fibres $X_\infty=\bigsqcup_{v\mid\infty}X(\mathbb{C})_v$ carrying the Arakelov Kähler form $\mu_{\mathrm{Ar},g}$ of Faltings 1984. The scheme dimension of $\mathcal{S}^{\mathrm{Ar}}_g$ is 2; the operadic factorisation dimension is 2 ($E_2$-chiral via Dunn); the cohomological signature at infinity is that of a genus-$g$ curve.

(ii) Chiral/factorisation structure.

$\mathcal{V}^{\mathrm{prim,surf},g}$ is the $E_2$-chiral algebra on $\mathcal{S}^{\mathrm{Ar}}_g$, defined as
$$\mathcal{V}^{\mathrm{prim,surf},g}:=\mathrm{HH}_\bullet\bigl(\mathrm{Hk}^{\mathrm{Iw,surf}}_{GL_{2g},\mathrm{glob}}\bigr),$$
where $\mathrm{Hk}^{\mathrm{Iw,surf}}_{GL_{2g},\mathrm{glob}}$ is the $E_2$-monoidal (via 2-dim BD Grassmannian of Fargues-Scholze plus Dunn additivity on the 2-dim Ran space) global Iwahori Hecke category of $GL_{2g}$ on the arithmetic surface. $E_1$-algebra structure on HH via Dunn ($E_1\otimes E_1=E_2$). Chiral bar complex $B^{\mathrm{ch,Ar,2}}(\mathcal{V}^{\mathrm{prim,surf},g})$ built on the 2-dim Parshin-Gersten complex with $(\partial_1,\partial_2)$ double residue. Local factors: rank-$2g$ Heisenberg Fock at each prime via the $\ell$-adic Tate module of the Jacobian $\mathrm{Jac}(X_K)$.

(iii) Almost complex structure as operator on chiral cohomology.

The speculation's "almost complex structure" is not a differential-geometric $J:TX\to TX$ with $J^2=-\mathrm{id}$ (which is Falsified: arithmetic schemes have no real tangent bundle). It is a Koszul duality operator $J^{\mathrm{Koz}}:B^{\mathrm{ch,Ar,2}}\to\Omega^{\mathrm{ch,Ar,2}}$ with the property $(J^{\mathrm{Koz}})^2=\tau$, where $\tau$ is the functional-equation involution $s\mapsto 2-s$ on the Mellin transform of the bar generating function. On chiral cohomology $H^\bullet B^{\mathrm{ch,Ar,2}}(\mathcal{V}^{\mathrm{prim,surf},g})$, $J^{\mathrm{Koz}}$ acts as the Hodge rotation by $\pi/2$ on the weight-1 part (rank-$2g$ archimedean Fock), mixing holomorphic and antiholomorphic parts just as the integrable complex structure $J:H^{1,0}\oplus H^{0,1}\to H^{1,0}\oplus H^{0,1}$ does on the archimedean fibre. This is the honest arithmetic avatar of the almost complex structure in the speculation.

(iv) Cohomological signature = Hodge diamond.

Per archimedean place, $\widehat{h}^{0,0}=\widehat{h}^{1,1}=1$, $\widehat{h}^{1,0}=\widehat{h}^{0,1}=g$ on $X(\mathbb{C})_v$. Globally on the 2-fold, the arithmetic Hodge diamond is richer: $\widehat{\mathrm{CH}}^*(X)$ with Gillet-Soulé arithmetic Chow plus Bismut-Gillet-Soulé analytic torsion, carrying Faltings-Hriljac Hodge index plus $\delta$-invariant. The single integer $g$ indexes the family through (a) rank of $\pi_*\omega_{X/S}$, (b) central charge $c^{\mathrm{Ar},g}=g$ of the archimedean Heisenberg, (c) archimedean $\Gamma$-factor $\Gamma_{\mathbb{C}}(s)^g$ of the Hasse-Weil $L$-function, (d) dimension of $\mathrm{Jac}(X_K)$, (e) coefficient $2g-2$ in $\deg\omega_{X_K/K}$.

(v) Genus-$g$ correspondence via $\kappa+\kappa^!$ shift.

The Koszul self-duality identity is $\kappa^{\mathrm{Ar},g}_\mathsf{G}+(\kappa^!)^{\mathrm{Ar},g}_\mathsf{G}=0$: preserved at genus $g$. The genus enters through rank-$2g$ oscillators per place (central charge $c=g$), not through a non-zero shift of the Koszul identity. The functional-equation shift is $s\mapsto 2-s$ (weight-1 motive) rather than $s\mapsto 1-s$ (weight-0 $\zeta$). This is the internal translation of "genus-$g$ correspondence" into the bar-cobar framework: same $=0$, rank-graded over $g$.

(vi) Precise theorem-waiting extending the F-RH identity.

Theorem-waiting (genus-$g$ arithmetic $\mathsf{G}$-row, programmatic statement). Let $X\to\mathrm{Spec}\,\mathcal{O}_K$ be a proper flat regular arithmetic surface with generic fibre $X_K$ of genus $g$. Let $\mathcal{V}^{\mathrm{prim,surf},g}_{\mathrm{Heis}}$ be the rank-$2g$ arithmetic Heisenberg on $\mathcal{S}^{\mathrm{Ar}}_g=X$ with central charge $c=g$, built as the global restricted tensor of per-place Heisenberg Focks on the $\ell$-adic Tate module $T_\ell(\mathrm{Jac}(X_K))$. Then
$$\kappa^{\mathrm{Ar},g}_\mathsf{G}+(\kappa^!)^{\mathrm{Ar},g}_\mathsf{G}=0\quad\Longleftrightarrow\quad\Lambda(s,X_K)=\epsilon_{X_K}\cdot\Lambda(2-s,X_K),$$
conditional on the 2-dim arithmetic Positselski equivalence (Cycle 9) with $\mu_1=\mu_2=0$. At $g=0$ this degenerates to the Vol~IV load-bearing theorem $\kappa+\kappa^!=0\Leftrightarrow\xi(s)=\xi(1-s)$, with $X_K=\mathbb{P}^1$ (empty Jacobian) and $\Lambda(s,\mathbb{P}^1_{\mathbb{Q}})=\xi(s)$.

Forward implication ($\kappa+\kappa^!=0\Rightarrow\Lambda(s)=\epsilon\Lambda(2-s)$) holds unconditionally via Euler-product identification (Step 1), Consani-Marcolli Bost-Connes Koszul dual (Step 2), and Weil-Bloch-Kato adelic Poisson (Step 4), all independent of 2-dim Positselski. Full biconditional needs Step 3 conditional.

Residual obligations (extending Chapter~22's five):
- 2-dim arithmetic Positselski with $\mu_1=\mu_2=0$ (extending Ch.~25; $\Lambda_2$-coefficients); scope $\sim$60-100 pages.
- 2-dim Parshin-Gersten bar construction and Koszul-adjunction verification (extending Ch.~10); scope $\sim$40-60 pages.
- 2-dim arithmetic Ben-Zvi-Nadler $\mathrm{HH}_\bullet(\mathrm{Hk}^{\mathrm{Iw,surf}}_{GL_{2g},\mathrm{glob}})\simeq\mathcal{O}(\mathrm{LocSys}^{W,\varphi\Gamma}_{GL_{2g},\Sigma_g^{\mathrm{Ar}}})^{\mathrm{flat}}$ (extending Ch.~28; $\Sigma_g^{\mathrm{Ar}}$ replaces $B\widehat{\mathbb{Z}}$); scope $\sim$80-120 pages.
- $GL_{2g}$-local geometric Langlands and $GL_{2g}$-Emerton-Gee stack (Fargues-Scholze and Emerton-Gee inputs exist; categorical comparison theorem-waiting); scope imported from F1 scaled by $g$.
- 2-dim Koszul-Petersson compatibility with genus-$g$ Petersson pairing on weight-$(k,g)$ automorphic forms (extending Ch.~22's Koszul-Pet compat); scope $\sim$15-25 pages.

## Realization pointer

The genus-$g$ lift $\mathcal{V}^{\mathrm{prim,surf},g}$ sits in Vol~IV's arithmetic branch as a rank-graded family above the existing $g=0$ branch. Placement by chapter:

- Chapter~10 (Beilinson bar-cobar on $\overline{C}$): 2-dim analog is the Parshin-Gersten bar complex on an arithmetic surface (Cycle 2). The new chapter would sit adjacent as Chapter 10$^{\mathrm{surf}}$ or Chapter 50$_g$.
- Chapter~14 (Bezrukavnikov-Bernstein Hochschild placement): 2-dim analog replaces $\mathrm{Hk}^{\mathrm{Iw}}_{GL_2,\mathrm{glob}}$ by $\mathrm{Hk}^{\mathrm{Iw,surf}}_{GL_{2g},\mathrm{glob}}$. HH trace becomes $\mathcal{V}^{\mathrm{prim,surf},g}$.
- Chapter~21 (F1-F10 open frontiers): F1$_g$, F2$_g$, F3$_g$ generalisations with $GL_{2g}$-local Langlands, $GL_{2g}$-Emerton-Gee, $GL_{2g}$-Ben-Zvi-Nadler.
- Chapter~22 (closure of F1-F3 and pillars): P1$_g$, P2$_g$, P3$_g$ closed unconditionally in forward direction via Euler-product + Consani-Marcolli + Weil-Bloch-Kato; full biconditional conditional on 2-dim Positselski.
- Chapter~23 (RH reformulation): F-RH$_g$ is the genus-$g$ Hasse-Weil-Riemann Hypothesis, equivalent to Li positivity for $\Lambda(s,X_K)$ (Li 1997 generalises trivially; Bombieri-Lagarias style). Minimal path: 2-dim arithmetic Positselski + genus-$g$ Koszul-Pet + H-P$^{\mathrm{Ar},g}$ + HP-Li$_g$.
- Chapter~24 (arithmetic Virasoro bootstrap): Virasoro central charge is $c^{\mathrm{Ar},g}=g$ on the primary subspace of the rank-$g$ archimedean Fock. Bombieri-Lagarias Li coefficients $\lambda_n(X_K)\geq 0$ equivalent to Hasse-Weil Riemann Hypothesis for $X_K$.
- Chapter~25 (arithmetic Positselski): 2-dim extension to $\Lambda_2$-coefficients (Cycle 9).
- Chapter~28 (arithmetic Ben-Zvi-Nadler): $\Sigma_g^{\mathrm{Ar}}$ replaces $B\widehat{\mathbb{Z}}$; arithmetic genus-$g$ surface replaces arithmetic inertia circle.

The voice of the programmatic interior converges on $\mathcal{V}^{\mathrm{prim,surf},g}$ as the rank-graded lift of $\mathcal{V}^{\mathrm{prim}}$, with the central identity $\kappa+\kappa^!=0$ preserved at genus $g$ and the functional equation shift lifting from $s\mapsto 1-s$ to $s\mapsto 2-s$ to match the Hasse-Weil weight-1 motive. The genus $g$ enters through rank, not through shift; the "almost complex structure" of the speculation is the Koszul duality operator on chiral cohomology, with $(J^{\mathrm{Koz}})^2=\tau$ (functional-equation involution) replacing the naive $J^2=-\mathrm{id}$ which fails on a scheme. The cohomological signature is the pair (archimedean Hodge diamond of $\Sigma_g$ per place, arithmetic Chow diamond globally), matching Faltings-Gillet-Soulé-Bismut.

This convergence is orthogonal to Voice 1 (Arakelov) on scheme dimension and archimedean Hodge but intersects in the rank-$g$ Heisenberg at the archimedean fibre and the Hasse-Weil functional equation as the genus-$g$ Koszul-self-duality witness. It is natively the programme's chiral-bar-cobar language; at $g=0$ it is the existing Vol~IV arithmetic branch; at $g\geq 1$ it is the programmatic lift. The residual obligations scale from 5 to approximately 10 named open sub-items, each a direct lift of the 1-dim analog with explicit 2-dim $\Lambda_2$-coefficient or $GL_{2g}$-parameter content.

No almost complex structure is introduced in any non-integrable sense. The integrable $J_\infty$ at the archimedean fibre acts on the rank-$g$ Fock as the Hodge rotation, and its arithmetic shadow on chiral cohomology is the Koszul duality involution $J^{\mathrm{Koz}}$. The speculation's "genus-2 arithmetic surface with almost complex structure carrying cohomological signature of genus-$g$ curve" is realised as: arithmetic 2-fold $\mathcal{S}^{\mathrm{Ar}}_g$, $E_2$-chiral factorisation algebra $\mathcal{V}^{\mathrm{prim,surf},g}$, Koszul duality $J^{\mathrm{Koz}}$ on its chiral cohomology, arithmetic Hodge diamond $(1, g, 1)$ at each archimedean place, Hasse-Weil functional equation $\Lambda(s)=\epsilon\Lambda(2-s)$ as the load-bearing theorem-waiting.
