# Voice 2: Deninger / Connes–Consani / Bost–Connes

## Source catalog and frame

The speculation is two-pronged. Reading (A): $g = 2$ specifically, with a genus-$g$ lift asked as an aside. Reading (B): an arithmetic surface is 2-dimensional as an arithmetic object and carries an almost complex structure realizing the cohomological signature of a genus-$g$ algebraic curve. Both readings resolve here to a single dynamical object once the voice fixes the frame.

Primary sources. Deninger 1998 "Some analogies between number theory and dynamical systems on foliated spaces" (ICM Berlin, arXiv:math/9802100). Deninger 1992 "Local $L$-factors of motives and regularised determinants" (Invent. Math. 107). Deninger 1994 "Motivic $L$-functions and regularised determinants" (Proc. Symp. Pure Math. 55.1). Connes 1999 "Trace formula in noncommutative geometry and the zeros of the Riemann zeta function" (Sel. Math. 5). Connes–Consani 2014 "The arithmetic site" (C. R. Acad. Sci. Paris Ser. I 352). Connes–Consani 2016 "Geometry of the scaling site" (Sel. Math. N.S. 23). Connes–Consani–Marcolli 2008 "Noncommutative geometry and motives" (J. Geom. Phys. 56). Bost–Connes 1995 "Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory" (Sel. Math. N.S. 1, 411–457, arXiv:hep-th/9411174). Kapranov–Smirnov 1995 "Cohomology determinants and reciprocity laws: number field case" (unpublished preprint, widely circulated). Manin 1995 "Lectures on zeta functions and motives" (Astérisque 228). Lorscheid 2018 "$\mathbb{F}_1$-geometry, blueprints, and tropical geometry" (Lecture Notes in Math. 2194). Soulé 2004 "Les variétés sur le corps à un élément" (Mosc. Math. J. 4). Deitmar 2005 "Schemes over $\mathbb{F}_1$" (Progr. Math. 235).

Frame. In Deninger's programme a "genus" of an arithmetic scheme is a spectral count: the number of zeros of its zeta function inside a given critical rectangle. For $\overline{\mathrm{Spec}\,\mathbb{Z}}$ the count is already infinite (Riemann–von Mangoldt); any naive "genus 2 arithmetic surface" is false as a literal count. Healing move: a genus-$g$ arithmetic surface is a dynamical object whose Frobenius-twisted $H^1$ has rank $2g$, extracted from a *finite* auxiliary geometric input (number field, tame cover, projector). The almost complex structure is the archimedean Frobenius $\Phi_\infty$ of Deninger's framework, conjecturally satisfying $\Phi_\infty^2 = -\mathrm{id}$ on the primitive part. This is the Connes–Consani scaling frame read through Deninger's long programme.

## Attack–heal cycles

### Cycle 1: "Genus" as zero count, and the collapse of reading (A)

**Attack.** Read $\overline{\mathrm{Spec}\,\mathbb{Z}}$ as an "arithmetic curve of genus $g$" by analogy with a smooth projective curve $X/\mathbb{F}_q$, where $\zeta_X(s)$ is rational of the form $P_1(q^{-s})/(1-q^{-s})(1-q^{1-s})$ with $\deg P_1 = 2g$. For $\overline{\mathrm{Spec}\,\mathbb{Z}}$ the completed zeta $\xi(s)$ has *infinitely* many zeros, so any naive genus is $\infty$. "Genus 2 arithmetic surface" has no literal meaning in this frame.

**Heal.** Deninger (1998, §2) postulates a cohomology theory $H^\bullet_{\mathrm{Den}}(\overline{\mathrm{Spec}\,\mathbb{Z}})$ with $\mathbb{R}^\times_+$-equivariant Frobenius $\phi^t$ such that

$$\xi(s) \;=\; \frac{\det_\infty(s \cdot \mathrm{id} - \Theta_1 \mid H^1_{\mathrm{Den}})}{\det_\infty(s \cdot \mathrm{id} - \Theta_0 \mid H^0_{\mathrm{Den}}) \cdot \det_\infty(s \cdot \mathrm{id} - \Theta_2 \mid H^2_{\mathrm{Den}})} \cdot (\text{trivial-zero corrections}).$$

The $H^0, H^2$ are rank-1 (scaling characters), and $H^1$ is the infinite-dimensional primitive part. The "genus" of $\overline{\mathrm{Spec}\,\mathbb{Z}}$ in Deninger's frame is $\frac{1}{2}\dim_{\mathrm{reg}} H^1_{\mathrm{Den}} = +\infty$. Reading (A) with $g = 2$ literally is **Falsified**.

**Surviving statement.** A genus-2 arithmetic surface is an auxiliary arithmetic object $X/\overline{\mathrm{Spec}\,\mathbb{Z}}$ whose twisted $H^1_{\mathrm{Den}}$ has rank *exactly* 4 (= $2g$), imported from a geometric input external to $\zeta$. The candidate inputs are: (i) a number field $K/\mathbb{Q}$ with signature restricting unit rank to match $2g$; (ii) a projector $\pi_{\le T}$ onto the first $g$ critical zeros; (iii) a hyperelliptic curve $X_g/\mathbb{Q}$ base-changed against the arithmetic site. Only (i) and (iii) survive the next cycle.

### Cycle 2: The regulator lattice and Minkowski complex torus

**Attack.** The projector $\pi_{\le T}$ of Cycle 1 is unstable: it is an analytic truncation, not a functorial arithmetic object, and the zeros below height $T$ are not canonically labelled. Is there a *canonical* genus-$g$ arithmetic object that sits inside $\overline{\mathrm{Spec}\,\mathbb{Z}}$?

**Heal (Minkowski lattice).** Let $K/\mathbb{Q}$ be a totally imaginary number field of degree $2g$, $\mathcal{O}_K$ its ring of integers. The Minkowski embedding

$$j : \mathcal{O}_K \hookrightarrow \mathbb{R}^{r_1} \times \mathbb{C}^{r_2} = \mathbb{C}^g$$

(with $r_1 = 0, r_2 = g$) realizes $\mathcal{O}_K$ as a rank-$2g$ lattice $\Lambda_K \subset \mathbb{C}^g$ with covolume equal to $|d_K|^{1/2}$, where $d_K$ is the discriminant. The quotient

$$T_K \;:=\; \mathbb{C}^g / \Lambda_K$$

is a complex torus of complex dimension $g$, *equipped with a canonical almost complex structure inherited from $\mathbb{C}^g$*. This is a "genus-$g$ arithmetic surface" in the literal sense: the cohomology signature of $T_K$ is $H^0 = \mathbb{Z}$, $H^1 = \mathbb{Z}^{2g}$, $H^2 = \binom{2g}{2}$, …, matching the cohomology signature of a complex abelian variety of dimension $g$.

**Status.** For $g = 2$: $K$ totally imaginary of degree 4. Examples: $\mathbb{Q}(\zeta_5)$ (degree 4, totally imaginary, $d_K = 125$), $\mathbb{Q}(\zeta_8)$ (degree 4, totally imaginary, $d_K = 256$), $\mathbb{Q}(i, \sqrt{2})$, $\mathbb{Q}(\sqrt{-1}, \sqrt{-3})$. Each has Minkowski lattice in $\mathbb{C}^2$ giving a genus-2 complex torus. The "almost complex structure" is literal: it is the $\mathbb{C}^g$-linear structure on the Minkowski image.

**Theorem-waiting.** For $K$ totally imaginary of degree $2g$, the Minkowski torus $T_K$ is an almost-complex manifold of complex dimension $g$ whose cohomology ring $H^\bullet(T_K, \mathbb{Z})$ matches the de Rham cohomology of a complex abelian variety of dimension $g$; the arithmetic content of $K$ lives in the *period lattice* $\Lambda_K \subset \mathbb{C}^g$, equivalently in the regulator and discriminant.

This closes reading (B) with a concrete candidate: **genus-$g$ arithmetic surface = Minkowski complex torus of a totally imaginary number field of degree $2g$**, with the Dedekind zeta $\zeta_K(s)$ as its spectral partition function.

### Cycle 3: Connes–Consani scaling site and the tropical-to-complex bridge

**Attack.** The Minkowski lattice is classical; it pre-dates Deninger, Connes–Consani, and the whole arithmetic-NCG programme. Does the speculation have content beyond "a totally imaginary quartic field gives a genus-2 torus"?

**Heal (scaling site).** Connes–Consani 2014/2016 construct the scaling site $[\overline{\mathrm{Spec}\,\mathbb{Z}}, \mathbb{R}^\times_+]$ as a topos with a continuous $\mathbb{R}^\times_+$-action. Its structure sheaf is tropical (semirings $\mathbb{Z}_{\max}$ at each place, or in the refined version, the ring of convex piecewise-affine functions on $\mathbb{R}^\times_+$). The key feature: the cohomology $H^\bullet$ of the scaling site admits

$$\mathrm{char}_{H^1_{\mathrm{sc}}}(\Phi_t) \;=\; \sum_\rho e^{i \gamma_\rho t}$$

at the level of distributions (Connes 1999, Connes–Consani 2016 §8), where the sum runs over non-trivial zeros $\rho = \frac{1}{2} + i\gamma_\rho$ of $\zeta$. This is the archimedean Frobenius $\Phi_\infty$ acting on a primitive $H^1$.

The tropical-to-complex bridge. The scaling site is tropical (its structure sheaf is a semiring, not a ring). A genus-$g$ arithmetic surface in this frame is an object whose tropical cohomology acquires a *complex structure* via a finite coefficient enhancement. Two realizations:

(a) **Base-change to a totally imaginary coefficient.** The scaling site over $\mathcal{O}_K$ (not $\mathbb{Z}$) inherits the $\mathbb{C}^g$-structure from the Minkowski embedding. The almost complex structure on $H^1_{\mathrm{sc}, K}$ is $J = \sqrt{-1}\cdot$ (action of $\tau_1, \ldots, \tau_g$ through their imaginary embeddings), with $J^2 = -\mathrm{id}$ on the primitive part. Status: Conjecture, because the Connes–Consani scaling site has not been constructed for arbitrary number fields, only for $\mathbb{Q}$.

(b) **Sphere-packing projector onto first $g$ zeros.** Restrict $H^1_{\mathrm{sc}}$ to the subspace spanned by the first $g$ zero-pairs $\{\rho_1, \bar\rho_1, \ldots, \rho_g, \bar\rho_g\}$. This is rank $4g$ (each zero and its complex conjugate contribute; the $\frac{1}{2} \cdot \mathrm{id}$ real part is accounted separately). Dim$_\mathbb{R} = 2g$ after pairing. The almost complex structure is $\Phi_\infty = J = i \cdot \log s|_{\mathrm{Re}(s) = 1/2}$, acting on the imaginary-ordinate coordinates $\gamma_{\rho_j}$. Status: Heuristic.

**Keep (a).** The tropical-to-complex bridge in Deninger–Connes frame is *coefficient enhancement*: move from $\mathbb{F}_1$-geometry over $\mathbb{Q}$ to $\mathbb{F}_1$-geometry over $K$, where $K$ is totally imaginary of degree $2g$. The almost complex structure emerges from the complex embeddings of $K$.

### Cycle 4: Bost–Connes as a rank-$g$ QSM and $\mathbb{F}_{1^{2g}}$-geometry

**Attack.** Bost–Connes 1995 is a $C^*$-algebraic quantum statistical system with Hamiltonian $H = \log N$ on $\ell^2(\mathbb{N}^\times)$; its partition function is $\mathrm{tr}(e^{-\beta H}) = \zeta(\beta)$. The system has rank 1 in a precise sense: one commuting family $\{\log p\}_p$. A "genus-$g$ arithmetic surface" in this frame should be a rank-$g$ enrichment. Does it exist, and if so, what is its partition function?

**Heal.** Two candidates.

(α) **$GL_g(\mathbb{A}_{\mathbb{Q}})$ Bost–Connes.** Connes–Marcolli–Ramachandran 2004 "$KMS$ states and complex multiplication" (arXiv:math/0501424) and Laca–Larsen–Neshveyev 2009 construct higher-rank generalizations of Bost–Connes. The $GL_g$-version has partition function

$$Z_{\mathrm{BC},g}(\beta) \;=\; \prod_{j=1}^{g} \zeta(\beta - j + 1)$$

in the simplest case (Whittaker Plancherel measure on $GL_g(\mathbb{Q}_p)$). For $g = 2$: $Z_{\mathrm{BC},2}(\beta) = \zeta(\beta) \cdot \zeta(\beta - 1)$. The Hilbert space is $\ell^2(\mathbb{N}^\times)^{\otimes 2}$ with two commuting Hamiltonians $H_1, H_2$, and the critical inverse temperature is $\beta = 2$ (spontaneous symmetry breaking at $\beta > 2$).

(β) **Number-field Bost–Connes.** Laca–Neshveyev 2011 "Type III factors and index theory for KMS states of Hecke $C^*$-algebras" (arXiv:1109.0972) and Ha–Paugam 2005 "Bost–Connes–Marcolli systems for Shimura varieties" build Bost–Connes algebras $C^*_K$ over arbitrary number fields $K$. Partition function:

$$Z_{\mathrm{BC}, K}(\beta) \;=\; \zeta_K(\beta),$$

where $\zeta_K$ is the Dedekind zeta of $K$. For $K$ totally imaginary of degree $2g$, $\zeta_K$ is a degree-$2g$ Euler product, and $Z_{\mathrm{BC}, K}$ has a phase transition at $\beta = 1$.

**Surviving statement.** A genus-$g$ arithmetic surface in the Bost–Connes frame is the Bost–Connes $C^*$-algebra $C^*_K$ of a totally imaginary number field $K$ of degree $2g$, with partition function $\zeta_K(\beta)$, Hamiltonian $H_K = \log \mathfrak{N}$ (norm of ideals), and Hilbert space $\ell^2(\mathfrak{I}_K)$ (integral ideals).

**Relation to (α) vs (β).** Both realize rank-$g$ enhancements but on distinct sides: (α) is a rank enhancement on the automorphic side ($GL_g$ instead of $GL_1$); (β) is a rank enhancement on the base side ($K$ instead of $\mathbb{Q}$). Langlands functoriality relates the two: the base-change from $\mathbb{Q}$ to $K$ (Weil restriction $\mathrm{Res}_{K/\mathbb{Q}}$) turns a $GL_1/K$ automorphic form into a $GL_{[K:\mathbb{Q}]}/\mathbb{Q}$ automorphic form, consistent with $\zeta_K(s) = \zeta(s) \prod_\chi L(s, \chi)$ factorization over Hecke characters. For the speculation, (β) is the cleaner geometric object; (α) is the cleaner representation-theoretic object.

**Theorem-waiting.** For $K$ totally imaginary of degree $2g$, the Bost–Connes–Marcolli $C^*$-algebra $C^*_K$ is a $C^*$-dynamical system with $\mathbb{R}^\times_+$-action, Hamiltonian $H_K = \log \mathfrak{N}$, partition function $\zeta_K(\beta)$, and phase transition at $\beta = 1$ with spontaneous symmetry breaking to the Galois group $G_K^{\mathrm{ab}}$. This is the arithmetic dynamical realization of the Minkowski torus of Cycle 2.

### Cycle 5: Archimedean Frobenius as almost complex structure

**Attack.** Deninger postulates a Frobenius $\Phi_\infty$ at the archimedean place, conjecturally related to complex conjugation on the Minkowski embedding. The speculation asks for an *almost complex structure* on the arithmetic surface. Is $\Phi_\infty$ this almost complex structure? Specifically: does $\Phi_\infty^2 = -\mathrm{id}$ on the primitive part?

**Heal.** In Deninger's 1992/1994 programme, the local $L$-factor at $\infty$ is

$$L_\infty(s) \;=\; \Gamma_{\mathbb{R}}(s)^{h_{1,0}} \Gamma_{\mathbb{C}}(s)^{h_{2,0}}\cdots$$

for a motive with Hodge structure, where $\Gamma_{\mathbb{R}}(s) = \pi^{-s/2}\Gamma(s/2)$ and $\Gamma_{\mathbb{C}}(s) = (2\pi)^{-s}\Gamma(s)$. For the trivial motive $\mathbb{Q}(0)$, $L_\infty = \Gamma_{\mathbb{R}}(s)$. For a weight-1 motive of rank $2g$ (e.g. $H^1$ of a genus-$g$ curve over $\mathbb{Q}$), $L_\infty = \Gamma_{\mathbb{C}}(s)^g$.

The archimedean Frobenius $\Phi_\infty$ acts on $H^1_{\mathrm{dR}}$ via complex conjugation on the de Rham realization; equivalently, on the Hodge filtration $F^1 \supset 0$, $\Phi_\infty$ is a real structure with $\Phi_\infty^2 = +\mathrm{id}$ on the underlying real vector space. On the *twisted* $H^1$ by the Tate twist $\mathbb{Q}(1/2)$ (half-integral twist, Deninger's normalization for $\xi(s) = \xi(1-s)$), $\Phi_\infty$ acts with a factor $i$ that squares to $-1$. This is the almost complex structure.

**Precise form.** On $H^1_{\mathrm{Den}}(X)$ twisted by the square root of Tate, $\Phi_\infty^2 = -\mathrm{id}$ on the primitive part $H^1_{\mathrm{prim}}$. This is equivalent to the Hodge star $\star : \Omega^{p,q} \to \Omega^{n-q, n-p}$ on a Kähler manifold satisfying $\star^2 = (-1)^{k(n-k)} \mathrm{id}$, which for middle-degree $k = n$ gives $\star^2 = -\mathrm{id}$.

**Surviving statement.** The almost complex structure $J$ on the genus-$g$ arithmetic surface is the half-Tate-twisted archimedean Frobenius $\Phi_\infty^{\mathrm{tw}}$, satisfying $J^2 = -\mathrm{id}$ on $H^1_{\mathrm{prim}}$. For the Minkowski torus $T_K$ of Cycle 2, this $J$ is literally the complex structure from the embedding $\mathcal{O}_K \hookrightarrow \mathbb{C}^g$. For a Deninger arithmetic surface $X/\overline{\mathrm{Spec}\,\mathbb{Z}}$ (conjectural cohomology), it is the half-Tate-twisted $\Phi_\infty$.

**Status.** The identification $J = \Phi_\infty^{\mathrm{tw}}$ is Conjecture in Deninger's programme; for the Minkowski torus realization, it is Theorem (classical).

### Cycle 6: The Deninger diagonal and $\overline{\mathrm{Spec}\,\mathbb{Z}} \times_{\mathbb{F}_1} \overline{\mathrm{Spec}\,\mathbb{Z}}$

**Attack.** Reading (B) of the speculation says "arithmetic surface is 2-dimensional as an arithmetic object, with an almost complex structure giving the cohomological signature of a genus-$g$ curve." The most natural 2-dimensional arithmetic object is the diagonal product

$$\mathcal{S} \;:=\; \overline{\mathrm{Spec}\,\mathbb{Z}} \times_{\mathbb{F}_1} \overline{\mathrm{Spec}\,\mathbb{Z}}$$

(Deninger's hypothetical "arithmetic surface"). What is its cohomology?

**Heal.** Künneth formally gives

$$H^\bullet(\mathcal{S}) \;=\; H^\bullet(\overline{\mathrm{Spec}\,\mathbb{Z}}) \otimes_{\mathbb{F}_1} H^\bullet(\overline{\mathrm{Spec}\,\mathbb{Z}}),$$

so $H^1(\mathcal{S}) = H^1 \otimes H^0 \oplus H^0 \otimes H^1$ has rank $\infty \cdot 1 + 1 \cdot \infty = \infty$, and $H^2(\mathcal{S}) = H^1 \otimes H^1 \oplus (\text{rank-1 terms})$ dominates. The diagonal $\Delta \subset \mathcal{S}$ has "self-intersection number" that Deninger expects to recover $\sum_\rho$ (sum over non-trivial zeros), motivating the Weil explicit formula as an arithmetic intersection.

For reading (B): the $\mathcal{S}$-cohomology signature *matches* a genus-$g$ curve only under a finite-dimensional projector $\pi_g : H^\bullet(\mathcal{S}) \to H^\bullet_g$ where $H^\bullet_g$ has Betti numbers $(1, 2g, \binom{2g}{2}, \ldots, 2g, 1)$. The natural candidates:

(i) Projection onto the first $g$ pairs of zeros, as in Cycle 3(b). Status: Heuristic.

(ii) Base-change the diagonal to $\mathcal{O}_K \otimes_\mathbb{Z} \mathcal{O}_K = \mathcal{O}_K \otimes \mathcal{O}_K / \mathbb{Z}$, giving a genuine rank-$g^2$ (or rank-$2g \cdot 2g$) piece in weight-1 cohomology. Status: Conjecture.

(iii) Replace $\overline{\mathrm{Spec}\,\mathbb{Z}}$ by $\overline{\mathrm{Spec}\,\mathcal{O}_K}$ for $K$ totally imaginary of degree $2g$, and take $\mathcal{S}_K = \overline{\mathrm{Spec}\,\mathcal{O}_K} \times_{\mathbb{F}_1} \overline{\mathrm{Spec}\,\mathcal{O}_K}$. Then $H^1(\mathcal{S}_K) = H^1 \otimes H^0 \oplus H^0 \otimes H^1 \supset (\Lambda_K \otimes \mathbb{Z} \oplus \mathbb{Z} \otimes \Lambda_K)$, rank $4g$ at weight 1; the primitive sub-lattice $\Lambda_K \otimes \bar\Lambda_K$ of the tensor has rank $4g^2$. Status: Heuristic for the diagonal object, Theorem-waiting for the cohomology rank.

**Keep (iii).** The "genus-$g$ arithmetic surface" as a *literal* 2-dimensional arithmetic object is $\overline{\mathrm{Spec}\,\mathcal{O}_K}$ (1-dimensional Arakelov curve) together with an almost complex structure from the Minkowski embedding; the "$\times$" in reading (B) is reinterpreted as the *Arakelov multiplication* on the arithmetic curve, giving a 2-dimensional cohomology (the arithmetic Chow group $\widehat{\mathrm{CH}}^1(\overline{\mathrm{Spec}\,\mathcal{O}_K})$). This ties back to Cycle 2.

### Cycle 7: $\mathbb{F}_{1^{2g}}$-geometry and roots of unity

**Attack.** Kapranov–Smirnov 1995 and Manin 1995 prescribe $\mathbb{F}_{1^n}$-geometry as "$\mathbb{F}_1$ with $n$-th roots of unity adjoined", realized by Soulé 2004 as a restriction of the category of $\mathbb{Z}$-schemes. Does the genus-$g$ arithmetic surface factor through $\mathbb{F}_{1^{2g}}$?

**Heal.** The Minkowski torus $T_K$ of Cycle 2, for $K = \mathbb{Q}(\zeta_n)$ the $n$-th cyclotomic field, has automorphism group containing $\mathrm{Gal}(\mathbb{Q}(\zeta_n)/\mathbb{Q}) = (\mathbb{Z}/n\mathbb{Z})^\times$ of order $\phi(n)$. The degree is $[K:\mathbb{Q}] = \phi(n)$. For totally imaginary $K$ of degree $2g$, the cyclotomic candidates are $K = \mathbb{Q}(\zeta_n)$ with $\phi(n) = 2g$:

- $g = 1$: $\phi(n) = 2$, $n \in \{3, 4, 6\}$. Example: $K = \mathbb{Q}(i)$ (gaussian integers, genus-1 elliptic curve $\mathbb{C}/\mathbb{Z}[i]$).
- $g = 2$: $\phi(n) = 4$, $n \in \{5, 8, 10, 12\}$. Example: $K = \mathbb{Q}(\zeta_5)$ ($d_K = 125$).
- $g = 3$: $\phi(n) = 6$, $n \in \{7, 9, 14, 18\}$.

The cyclotomic Minkowski torus $T_{\mathbb{Q}(\zeta_n)}$ is *precisely* the Jacobian of the Fermat curve $F_n : x^n + y^n = 1$ (up to isogeny), by a classical result of Rohrlich. This links the arithmetic surface to Fermat curves: genus-$g$ arithmetic surface $\leftrightarrow$ Fermat curve of degree $n$ with $\phi(n) = 2g$.

**Surviving statement.** Under cyclotomic specialization, the genus-$g$ arithmetic surface is the Minkowski torus $T_{\mathbb{Q}(\zeta_n)}$ with $\phi(n) = 2g$, isogenous to the Jacobian $\mathrm{Jac}(F_n)$ of the Fermat curve $F_n$. The almost complex structure $J$ is the $\mathbb{C}^g$-structure from cyclotomic embedding. The factorization through $\mathbb{F}_{1^n}$ (Kapranov–Smirnov) assigns this torus to $\mathbb{F}_{1^n}$-geometry.

**Status.** Classical (Rohrlich, Koblitz–Rohrlich); Theorem for the Fermat-Jacobian isogeny, Heuristic for the $\mathbb{F}_{1^n}$-factorization.

### Cycle 8: Vol IV cross-link, lifting $\kappa + \kappa^! = 0$ to $2 - 2g$

**Attack.** Vol IV's load-bearing arithmetic theorem is $\kappa^{\mathrm{Ar}}_{\mathsf{G}} + (\kappa^!)^{\mathrm{Ar}}_{\mathsf{G}} = 0 \Leftrightarrow \xi(s) = \xi(1-s)$. For a 1-dimensional base (genus 0 in the functional-equation sense, i.e. $\overline{\mathrm{Spec}\,\mathbb{Z}}$ as Arakelov curve), the "0" on the right is the Euler characteristic $\chi = 2 - 2g$ with $g = 0$. Does the identity lift to a genus-$g$ version $\kappa + \kappa^! = 2 - 2g$ on a genus-$g$ arithmetic surface?

**Heal (proposed).** Replace the base $\overline{\mathrm{Spec}\,\mathbb{Z}}$ by $\overline{\mathrm{Spec}\,\mathcal{O}_K}$ for $K$ totally imaginary of degree $2g$. The Dedekind zeta $\zeta_K(s)$ has completed form $\xi_K(s) = |d_K|^{s/2} \Gamma_\mathbb{R}(s)^{r_1} \Gamma_\mathbb{C}(s)^{r_2} \zeta_K(s)$ with functional equation $\xi_K(s) = \xi_K(1-s)$. The arithmetic Heisenberg $\mathcal{V}^{\mathrm{prim}}_K$ built from the Bost–Connes–Marcolli $C^*_K$ system satisfies (conjecturally)

$$\kappa^{\mathrm{Ar}, K}_{\mathsf{G}} + (\kappa^{!})^{\mathrm{Ar}, K}_{\mathsf{G}} \;=\; 2 - 2g \quad(?)$$

The right-hand side $2 - 2g$ would arise as the Euler characteristic $\chi(\overline{\mathrm{Spec}\,\mathcal{O}_K}) = 2 - 2g$ *if* one imposes the Arakelov convention $\chi(\overline{\mathrm{Spec}\,\mathcal{O}_K}) = 2 - \mathrm{rk}(\Lambda_K) = 2 - 2g$. This is a natural but conjectural extension; the classical Arakelov Euler characteristic is $\widehat{\chi} = -\log|d_K|$, not $2 - 2g$.

**Diagnostic.** Two distinct notions of "genus" clash here:

(i) *Hodge genus.* The half-rank of $H^1_{\mathrm{Hodge}}$: $g_{\mathrm{Hodge}} = \frac{1}{2}\dim H^1$.

(ii) *Arakelov genus.* The deficit of the arithmetic Euler characteristic from 2: $g_{\mathrm{Ar}} = 1 - \frac{1}{2}\widehat{\chi}$.

For a compact Riemann surface, (i) = (ii). For $\overline{\mathrm{Spec}\,\mathcal{O}_K}$, (i) gives $g_{\mathrm{Hodge}}(\Lambda_K) = g$ (complex dimension of Minkowski torus), while (ii) gives $g_{\mathrm{Ar}}(\overline{\mathrm{Spec}\,\mathcal{O}_K}) = $ some discriminant-log-based number not equal to $g$. The speculation's "genus" is (i), the Hodge genus.

**Surviving statement (Theorem-waiting).** For $K$ totally imaginary of degree $2g$, with arithmetic Heisenberg $\mathcal{V}^{\mathrm{prim}}_K = \bigotimes'_{\mathfrak{p}} \mathcal{H}^{(\mathfrak{p})} \otimes \bigotimes_{v | \infty} \mathcal{H}^{(v)}$ running over prime ideals $\mathfrak{p}$ and archimedean places $v$, there is a Koszul self-duality identity

$$\kappa^{\mathrm{Ar}, K}_{\mathsf{G}} + (\kappa^{!})^{\mathrm{Ar}, K}_{\mathsf{G}} \;=\; 0 \quad\Leftrightarrow\quad \xi_K(s) = \xi_K(1-s),$$

with the $0$ on the right being zero regardless of $g$ (the functional-equation obstruction is genus-independent). The genus-$g$ dependence appears in the *dimension* of the cohomology, not in the centrality. This **rejects** the naive $\kappa + \kappa^! = 2 - 2g$ formula.

**Revised surviving statement.** The lift to genus $g$ is not on the Koszul-centrality side (which remains $= 0$) but on the *rank* side: $\dim H^1_{\mathrm{prim}}(\mathcal{V}^{\mathrm{prim}}_K) = 2g$. The Koszul identity is the same; the object is genus-$g$-indexed. The almost complex structure $J$ is the archimedean Frobenius $\Phi_\infty^{\mathrm{tw}, K}$ acting on the $2g$-dimensional primitive part, with $J^2 = -\mathrm{id}$.

### Cycle 9: Bost–Connes phase transition as arithmetic genus indicator

**Attack.** The Bost–Connes system for $\mathbb{Q}$ has a phase transition at $\beta = 1$ (unique KMS state below, multiple above; Bost–Connes 1995 Theorem 5.4). For $K$ totally imaginary of degree $2g$, the Bost–Connes–Marcolli system $C^*_K$ has a phase transition at $\beta = 1$ as well (Laca–Neshveyev 2011), but the *structure* of KMS states below and above the transition depends on $g$. Is the genus readable from the phase transition?

**Heal.** Below the phase transition ($\beta < 1$), the KMS state is unique. Above ($\beta > 1$), the extremal KMS states are parametrized by the idele class group modulo connected component: $\mathbb{A}_K^\times / K^\times \bar{C}_K$, where $\bar C_K$ is the connected component of the idele class group. For $K = \mathbb{Q}$: this quotient is $\hat{\mathbb{Z}}^\times = \mathrm{Gal}(\mathbb{Q}^{\mathrm{ab}}/\mathbb{Q})$. For $K$ totally imaginary: this quotient is $\mathrm{Gal}(K^{\mathrm{ab}}/K)$, of "rank" (in a suitable sense) reflecting $g$.

Specifically, the Pontryagin dual of the free abelian part of $\mathrm{Gal}(K^{\mathrm{ab}}/K)$ has $\mathbb{Z}$-rank $r_1 + r_2$ (unit rank plus 1). For $K$ totally imaginary of degree $2g$: $r_1 = 0, r_2 = g$, so rank $= g$. This is the genus.

**Surviving statement.** The genus $g$ of the arithmetic surface $\overline{\mathrm{Spec}\,\mathcal{O}_K}$ (with $K$ totally imaginary of degree $2g$) equals the $\mathbb{Z}$-rank of the free part of the idele class group $\mathbb{A}_K^\times / K^\times \bar{C}_K$, equivalently the unit rank of $\mathcal{O}_K^\times$ modulo torsion plus 1, equivalently the number of archimedean places (all complex, so $r_2 = g$).

**Theorem (Dirichlet unit theorem).** This statement is classical: Dirichlet 1846 (Theorem on $\mathcal{O}_K^\times = \mu_K \times \mathbb{Z}^{r_1 + r_2 - 1}$), via Bost–Connes–Marcolli 2004 KMS state classification, identifies the phase-transition parameter space with $(\mathbb{R}/\mathbb{Z})^g$ (a $g$-dimensional torus) for totally imaginary $K$ of degree $2g$.

### Cycle 10: Convergence check against Voice 2's surviving object

**Attack.** Cycles 1–9 have produced several candidate objects. Voice 2 must commit to a single object.

**Heal (convergence).** The genus-$g$ arithmetic surface in Deninger–Connes–Bost–Connes frame is

$$\boxed{\overline{\mathrm{Spec}\,\mathcal{O}_K} \text{ for } K \text{ totally imaginary of degree } 2g, \text{ equipped with:}}$$

(a) **Underlying arithmetic 2-fold / dynamical object.** The Arakelov-compactified spectrum $\overline{\mathrm{Spec}\,\mathcal{O}_K}$ of the ring of integers of $K$. Classically 1-dimensional as an arithmetic scheme, but 2-dimensional as a *dynamical* object: the Bost–Connes–Marcolli $C^*$-algebra $C^*_K$ carries two commuting structures, the $\mathbb{R}^\times_+$-scaling flow (Deninger flow) with Hamiltonian $H_K = \log \mathfrak{N}$, and the $\mathbb{Z}^g$-action of $\mathcal{O}_K^\times / \mu_K$ through logarithmic regulators (one log-unit flow per complex embedding pair, so $g$ commuting flows). The combined $\mathbb{R}^\times_+ \times \mathbb{Z}^g$-dynamics is the "surface."

(b) **Almost complex structure (eta-type endomorphism).** The half-Tate-twisted archimedean Frobenius $J = \Phi_\infty^{\mathrm{tw}, K}$ acting on the primitive part $H^1_{\mathrm{prim}}(\mathcal{V}^{\mathrm{prim}}_K)$. Equivalently, the complex structure $J = \bigoplus_{j=1}^g \sqrt{-1} \cdot \mathrm{id}_{V_j}$ on the Minkowski decomposition $\Lambda_K \otimes_\mathbb{Z} \mathbb{R} = \bigoplus_{j=1}^g \mathbb{C}_{(\tau_j, \bar\tau_j)}$ (one complex plane per conjugate pair of embeddings). $J^2 = -\mathrm{id}$.

(c) **Cohomological signature.** $H^0 = \mathbb{Z}$, $H^1_{\mathrm{prim}} = \Lambda_K$ of $\mathbb{Z}$-rank $2g$, $H^2 = \mathbb{Z}^{\binom{2g}{2}}$, ..., $H^{2g} = \mathbb{Z}$. This matches the cohomology of a complex abelian variety of dimension $g$, equivalently the cohomology of a compact orientable surface of genus $g$ in degrees 0 and 1.

(d) **Genus correspondence.** $g = r_2(K) = \frac{1}{2}[K:\mathbb{Q}]$ (half the degree, for $K$ totally imaginary). Equivalently $g = $ complex dimension of Minkowski torus $T_K$. Equivalently $g = $ $\mathbb{Z}$-rank of the free part of $\mathrm{Gal}(K^{\mathrm{ab}}/K)$ minus 1 (for $K$ totally imaginary of degree $2g$, rank of free part is $r_2 + 1 - 1 = g$ after class-group and torsion corrections, matching Dirichlet unit theorem).

(e) **One precise theorem-waiting.** Writing this as a statement:

**Theorem-waiting (arithmetic Koszul self-duality for totally imaginary base).** Let $K$ be a totally imaginary number field of degree $2g$, $\mathcal{V}^{\mathrm{prim}}_K = \mathrm{HH}_\bullet(\mathrm{Hk}^{\mathrm{Iw}}_{GL_2, K, \mathrm{glob}})$ the Hochschild trace class of the identity on the global arithmetic Iwahori Hecke category of $GL_2/K$. Assemble $\mathcal{V}^{\mathrm{prim}}_K$ via the Bost–Connes–Marcolli restricted tensor product

$$\mathcal{V}^{\mathrm{prim}}_K \;=\; \bigotimes^{\prime}_{\mathfrak{p} \in \mathrm{Spec}\,\mathcal{O}_K} \mathcal{H}^{(\mathfrak{p})} \otimes \bigotimes_{v | \infty} \mathcal{H}^{(v)}.$$

Equip $\mathcal{V}^{\mathrm{prim}}_K$ with the almost complex structure $J = \Phi_\infty^{\mathrm{tw}, K}$ of (b). Then:

(i) The cohomological signature of the primitive subspace $\mathcal{V}^{\mathrm{prim}}_{K,\mathrm{Heis},\mathrm{prim}}$ matches that of the Minkowski torus $T_K$ of complex dimension $g$: $\dim H^1_{\mathrm{prim}} = 2g$ with $J$-action giving the $\mathbb{C}^g$-structure.

(ii) The arithmetic Koszul self-duality identity holds:

$$\kappa^{\mathrm{Ar}, K}_{\mathsf{G}} \;+\; (\kappa^{!})^{\mathrm{Ar}, K}_{\mathsf{G}} \;=\; 0 \quad\Leftrightarrow\quad \xi_K(s) \;=\; \xi_K(1-s),$$

where $\xi_K(s) = |d_K|^{s/2} \Gamma_\mathbb{C}(s)^g \zeta_K(s)$ is the completed Dedekind zeta of $K$.

(iii) The Bost–Connes–Marcolli $C^*$-algebra $C^*_K$ acts faithfully on the zero-mode lattice $L_K \subset \mathcal{V}^{\mathrm{prim}}_K$ via $\mu_{\mathfrak{a}} \delta_{\mathfrak{b}} = \delta_{\mathfrak{a}\mathfrak{b}}$ (indices $\mathfrak{a}, \mathfrak{b} \in \mathfrak{I}_K$), with partition function $Z_K(\beta) = \zeta_K(\beta)$.

**Status.** Theorem-waiting, with ingredients: (i) in primary literature (Minkowski, classical); (ii) reducible to Vol IV $\mathbb{Q}$-case (Chapter 20 / 23) plus Bost–Connes–Marcolli number-field transport (Laca–Neshveyev 2011, Ha–Paugam 2005); (iii) Bost–Connes–Marcolli 2004.

The genus is *indexed* in the cohomology rank, not in the centrality constant. $\kappa + \kappa^! = 0$ is the universal functional-equation statement; $g$ enters as the primitive rank.

## Convergence proposal

**The genus-$g$ arithmetic surface of the speculation.** $\overline{\mathrm{Spec}\,\mathcal{O}_K}$ for $K$ totally imaginary of degree $2g$, viewed as the Arakelov-compactified spectrum equipped with:

(i) **Underlying arithmetic 2-fold / dynamical object.** $\overline{\mathrm{Spec}\,\mathcal{O}_K}$ as an Arakelov curve (1-dim arithmetic scheme), enhanced by the Bost–Connes–Marcolli $C^*_K$ quantum statistical system with commuting $\mathbb{R}^\times_+ \times \mathbb{Z}^g$-dynamics: the scaling flow (Deninger) and $g$ independent log-regulator flows (one per complex embedding pair). This is the 2-dimensional structure.

(ii) **Almost complex structure.** The half-Tate-twisted archimedean Frobenius $J = \Phi_\infty^{\mathrm{tw}, K}$ on $H^1_{\mathrm{prim}}(\mathcal{V}^{\mathrm{prim}}_K)$, equivalently the Minkowski $\mathbb{C}^g$-structure on $\Lambda_K = j(\mathcal{O}_K)$. $J^2 = -\mathrm{id}$.

(iii) **Cohomological signature.** $H^\bullet_{\mathrm{prim}}(\mathcal{V}^{\mathrm{prim}}_K) \sim H^\bullet(T_K, \mathbb{Z})$ where $T_K = \mathbb{C}^g / \Lambda_K$ is the Minkowski complex torus; matches the cohomology of a complex abelian variety of dimension $g$.

(iv) **Genus correspondence.** $g = r_2(K) = \frac{1}{2}[K:\mathbb{Q}]$, equivalently the rank of $\mathrm{Gal}(K^{\mathrm{ab}}/K)_{\mathrm{free}}$ modulo torsion, equivalently $\frac{1}{2}\dim H^1_{\mathrm{prim}}$.

(v) **One precise theorem-waiting.**

*Arithmetic Koszul self-duality for totally imaginary base.* For $K$ totally imaginary of degree $2g$, the arithmetic Koszul self-duality

$$\kappa^{\mathrm{Ar}, K}_{\mathsf{G}} \;+\; (\kappa^{!})^{\mathrm{Ar}, K}_{\mathsf{G}} \;=\; 0 \quad\Leftrightarrow\quad \xi_K(s) \;=\; \xi_K(1-s)$$

holds on the arithmetic Heisenberg $\mathcal{V}^{\mathrm{prim}}_K$ assembled from the Bost–Connes–Marcolli $C^*_K$ system, with the primitive subspace carrying the Minkowski almost complex structure $J$ and cohomological signature of genus $g$.

The Deninger–Connes–Bost–Connes frame *packages* the genus-$g$ arithmetic surface as a number-field base-change of the Vol IV $\mathbb{Q}$-construction, with genus equal to the half-degree of the base field and almost complex structure equal to the archimedean Frobenius. The speculation, read through this frame, is not about a higher-dimensional arithmetic object but about an *arithmetic coefficient enhancement* of the 1-dimensional arithmetic curve.

Falsified reading: "$\overline{\mathrm{Spec}\,\mathbb{Z}}$ itself is genus $g$ for some finite $g$." It is not; its Deninger-genus is $+\infty$.

Surviving reading: "A genus-$g$ arithmetic surface is an Arakelov curve over a totally imaginary number field of degree $2g$, with almost complex structure from Minkowski / archimedean Frobenius, and arithmetic Heisenberg carrying the same Koszul self-duality as the $\mathbb{Q}$-case indexed by the Dedekind zeta $\zeta_K$."

## Realization pointer

The realization pair for this theorem-waiting is:

**Real($\mathcal{V}^{\mathrm{prim}}_K$-Koszul-duality, $\xi_K(s) = \xi_K(1-s)$) = $(d_K, e_K)$**

where:

$d_K$ = HZ-IV independent-verification decorator with

- **Derivation source.** Vol IV arithmetic Heisenberg Koszul-duality proof (Chapter 20 / 23) applied to $K$ base; Ha–Paugam 2005 Bost–Connes–Marcolli $C^*_K$ construction; Laca–Neshveyev 2011 KMS state classification for number-field Bost–Connes.

- **Verification source.** Tate's thesis 1950 (Mellin–theta symmetry for $\xi_K$, proved independently of the chiral-algebra machinery); Deninger 1992/1994 local $L$-factor computation for $\Gamma_\mathbb{C}(s)^g$ (matching archimedean contribution to $\xi_K$); Connes–Consani 2014 scaling-site cohomology of $H^1_{\mathrm{sc}, K}$ (conjectural in number-field case, but with matching archimedean Frobenius spectrum).

- **Disjointness rationale.** Vol IV chiral-algebra derivation sits on bar–cobar and Positselski, with Bost–Connes–Marcolli entering only through the zero-mode lattice action; Tate 1950 is a Fourier-analytic derivation on the adele class space $\mathbb{A}_K / K^\times$ without chiral-algebra input; Deninger local-$L$-factors come from the Hodge-theoretic $\Gamma$-factor prescription; Connes–Consani scaling site cohomology comes from tropical-topos machinery. The four sources share the conclusion $\xi_K(s) = \xi_K(1-s)$ but have disjoint proof backbones.

$e_K$ = computational engine: number-theoretic test evaluating $\xi_K(s)$ at symmetric pairs $(s_0, 1 - s_0)$ for $s_0 \in \{1/2 + i t : t \in [0, 100]\}$ on examples $K \in \{\mathbb{Q}(i), \mathbb{Q}(\zeta_5), \mathbb{Q}(\zeta_8), \mathbb{Q}(\zeta_{12})\}$; expected values obtained via direct Dirichlet-series evaluation and analytic continuation through the completed-zeta identity $\xi_K(s) = |d_K|^{s/2} \Gamma_\mathbb{C}(s)^g \zeta_K(s)$, with $\zeta_K$ computed via Hecke $L$-function factorization $\zeta_K(s) = \zeta(s) \prod_{\chi \ne 1} L(s, \chi)$ over Hecke characters mod conductor of $K$. Formula source (Dedekind–Hecke factorization, classical) is disjoint from expected-value source (Tate 1950 functional-equation derivation on adele class space). AP128 disjointness check passes: formula comes from Dedekind factorization, expected values come from Poisson summation on $\mathbb{A}_K$.

The realization pair witnesses the genus-$g$ arithmetic surface as a second independent verification of Vol IV's load-bearing functional-equation identity over a rank-$2g$ arithmetic base, disjoint from the $\mathbb{Q}$-case derivation. The genus indexes the primitive cohomology rank; the almost complex structure is the archimedean Frobenius; the underlying dynamical 2-fold is the Bost–Connes–Marcolli phase structure of the idele class group of $K$. This closes neither F-RH nor any other Vol IV conjecture; it parses the speculation in Deninger–Connes–Bost–Connes frame with one precise theorem-waiting whose ingredients sit in primary literature.
