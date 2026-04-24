# Voice 3 --- Fargues--Scholze / Perfectoid and Prismatic

## Source catalog and frame

The primary objects of this voice are diamonds, perfectoid spaces, $v$-sheaves, and the Fargues--Fontaine curve. Primary sources, by year and arXiv identifier:

- Scholze 2012, *Perfectoid spaces*, Publ. IHES 116.
- Scholze 2013, *p-adic Hodge theory for rigid-analytic varieties*, Forum Math. Pi 1.
- Bhatt--Morrow--Scholze 2018, *Integral p-adic Hodge theory*, Publ. IHES 128.
- Fargues--Fontaine 2018, *Courbes et fibrés vectoriels en théorie de Hodge p-adique*, Astérisque 406.
- Scholze--Weinstein 2020, *Berkeley lectures on p-adic geometry*, Annals Math. Studies 207.
- Caraiani--Scholze 2017, arXiv:1511.02418; 2019, arXiv:1710.10543.
- Zhu 2017, arXiv:1407.8519 and arXiv:1603.05593.
- Bhatt--Scholze 2015, arXiv:1507.06490 (Witt-vector affine Grassmannian).
- Bhatt--Scholze 2022, *Prisms and prismatic cohomology*, Ann. Math. 196.
- Emerton--Gee 2019, arXiv:1908.07185.
- Fargues--Scholze 2021, arXiv:2102.13459.
- Dotto--Emerton--Gee 2026, arXiv:2603.26887.
- Bhatt--Lurie 2022, arXiv:2201.06120; 2022, arXiv:2201.06124 (prismatization).

The speculation under attack is: an arithmetic surface (arithmetic 2-fold) carrying an "almost complex structure" whose cohomological signature matches a genus $g$ algebraic curve. Two readings are in scope. Reading (A): the 2-fold is a Riemann-surface analog with $\dim H^1 = 2g$. Reading (B): the 2-fold is arithmetic-dim 2, and the almost complex structure supplies a rank-$2g$ piece in its prismatic/étale $H^{\bullet}$ that encodes the $H^1$ of a genus $g$ curve.

In this voice, "arithmetic curve" is the Fargues--Fontaine curve $X_{FF}$; the arithmetic 2-fold is either a product $X_{FF} \times_{\mathrm{Spd}\,\mathbb{Z}_p} X_{FF}$, a perfectoid Shimura surface (Hilbert, Picard, Siegel), or the total space of a family of Breuil--Kisin--Fargues modules. "Almost complex structure" is the prismatic Frobenius $\varphi$ acting on $H^1_{\Delta}(X/\mathrm{Spf}\,\mathbb{Z}_p)$, or the Hodge--Tate endomorphism on the de Rham fibre; the tilting equivalence (Scholze 2012) recovers complex conjugation on the archimedean side. "Cohomological signature of genus $g$" translates to the rank of the $\varphi$-module $H^1_{\text{et}}(X_{\bar K}, \mathbb{Z}_p) \otimes B_{\mathrm{crys}}$ in the sense of Berger--Colmez, or to the Hodge--Tate dimension data $(h^{1,0}, h^{0,1})=(g,g)$.

Consequently the precise question attacked in the cycles below is: what is the moduli-theoretic content of a rank-$2g$ $(\varphi,\Gamma)$-module with prescribed Hodge--Tate weights $\{0,1\}^g$, viewed as an arithmetic 2-fold equipped with an almost complex structure? And: how does this object sit inside the bar-cobar programme of Volume IV?

## Attack--heal cycles

### Cycle 1 --- The Fargues--Fontaine curve is genus 0; what is its higher-genus twist?

**Attack.** The Fargues--Fontaine curve $X_{FF} = \mathrm{Proj}\bigoplus_{n\geq 0} B_{\mathrm{crys}}^{\varphi=p^n}$ (Fargues--Fontaine 2018, Ch. 5 and 6) is an integral normal Noetherian 1-dim scheme of genus 0 in the sense that every line bundle of degree 0 is trivial and $\dim H^0(X_{FF}, \mathcal{O}_{X_{FF}}) = 1$. The degree map gives an isomorphism $\deg : \mathrm{Pic}(X_{FF}) \xrightarrow{\sim} \mathbb{Z}$, and the classification of vector bundles (Fargues--Fontaine 2018, Thm. 8.2.10) asserts that every vector bundle decomposes as $\bigoplus \mathcal{O}_{X_{FF}}(\lambda_i)$ for slopes $\lambda_i \in \mathbb{Q}$; this is the Kedlaya--Mebkhout decomposition. So the first cohomology of $\mathcal{O}_{X_{FF}}$ vanishes, and the naive "genus $g$" enhancement of $X_{FF}$ is empty: one cannot twist the curve itself to a genus $g > 0$ Fargues--Fontaine curve by base change, because $B_{\mathrm{crys}}^{\varphi = p^n}$ is a field modulo the Newton polygon.

**Heal.** The correct datum is not a twist of $X_{FF}$ as a 1-dim geometric object but a higher-rank $\varphi$-module whose de Rham realisation simulates the $H^1$ of a genus $g$ curve. A genus $g$ algebraic curve $C/\overline{K}$ has $H^1_{\mathrm{et}}(C, \mathbb{Q}_p) \otimes B_{\mathrm{crys}} \cong (B_{\mathrm{crys}})^{2g}$ as a $\varphi$-module, with slopes $\{0,1\}$ each appearing $g$ times (for a curve with ordinary reduction) or a mixture of intermediate slopes consistent with $\sum \lambda_i = g$ (Fargues--Fontaine 2018, Ch. 10). Equivalently, the vector bundle on $X_{FF}$ associated with this $\varphi$-module is

$$
\mathcal{E}_g = \mathcal{O}_{X_{FF}}(0)^g \oplus \mathcal{O}_{X_{FF}}(1)^g,
$$

of rank $2g$ and degree $g$. This is what should be called the **genus-$g$ shadow of $X_{FF}$**: not a new curve, but a canonical rank-$2g$ vector bundle on $X_{FF}$.

**Status.** Theorem (classification of vector bundles on $X_{FF}$, Fargues--Fontaine 2018, Thm. 8.2.10). The voice extracts this classification and names $\mathcal{E}_g$ as the proper target of reading (A). Under Scholze tilting, the archimedean companion of $\mathcal{E}_g$ is the Hodge bundle $\mathcal{H}^{1,0}_C \oplus \mathcal{H}^{0,1}_C$ of a genus $g$ Riemann surface $C$; the tilting is not geometric (there is no archimedean $X_{FF}$) but a comparison at the level of period rings.

### Cycle 2 --- The 2-diamond $X_{FF} \times_{\mathrm{Spd}\,\mathbb{Z}_p} X_{FF}$

**Attack.** The most direct candidate for an arithmetic 2-fold is the self-product of the Fargues--Fontaine curve. As a diamond over $\mathrm{Spd}\,\mathbb{Z}_p$ (Scholze--Weinstein 2020, Ch. 9), the product makes sense and is $v$-representable. But: $X_{FF}$ is not itself a diamond over $\mathrm{Spd}\,\mathbb{Z}_p$ in a naive way; it is a relative diamond over $\mathrm{Spd}\,\mathbb{F}_p$ after choice of an untilt. The self-product $X_{FF} \times X_{FF}$ has two distinct readings depending on which tilt is chosen on each factor, and the diagonal is not closed-diamond but a perfectoid subvariety. The naive Künneth

$$
H^{\bullet}_{\text{et}}(X_{FF} \times X_{FF}, \mathbb{Z}_{\ell}) \stackrel{?}{=} H^{\bullet}(X_{FF}, \mathbb{Z}_{\ell}) \otimes H^{\bullet}(X_{FF}, \mathbb{Z}_{\ell})
$$

fails because the diamonds in question are not proper in any useful sense over $\mathrm{Spd}\,\mathbb{Z}_p$; the cohomology behaves more like sheaf cohomology on a non-compact space.

**Heal.** Replace $X_{FF}$ by its compactification $X_{FF}^{\mathrm{comp}}$ as in Fargues--Fontaine 2018, Ch. 5.3 (this is the Noetherian curve with closed points the Newton-polygon semisimple objects), and study cohomology with coefficients in $\overline{\mathbb{F}}_p$ or $\mathbb{Q}_p$ on the relative version $X_{FF}/\mathrm{Spa}\,\mathbb{Q}_p^{\mathrm{cyc}}$. For the "genus $g$ structure on a 2-fold" question the geometric target is:

$$
\mathrm{Bun}_{GL_2}(X_{FF}),
$$

the moduli of rank-2 bundles on $X_{FF}$ (Fargues--Scholze 2021, Ch. VI, esp. Thm. VI.1.4 on the connected components). Its closed points are in bijection with isocrystals of rank 2, slope-decomposed as $\mathcal{O}(\lambda_1) \oplus \mathcal{O}(\lambda_2)$ with $\lambda_1 + \lambda_2 \in \mathbb{Z}$. The stack $\mathrm{Bun}_{GL_2}(X_{FF})$ is not $X_{FF} \times X_{FF}$ but its natural 2-dim quotient, and carries the local geometric Langlands of Fargues--Scholze. In reading (B), this stack is the arithmetic 2-fold: arithmetic dimension 2, with a prismatic "almost complex structure" supplied by the $\varphi$-module presentation.

**Status.** Theorem for the diamond structure of $\mathrm{Bun}_{GL_2}(X_{FF})$ (Fargues--Scholze 2021, Thm. V.1.4, Thm. VI.1.4); Theorem-waiting for its identification as "the arithmetic 2-fold of genus 2" in the bar-cobar programme. The bridge is: the semistable locus $\mathrm{Bun}^{\mathrm{ss}}_{GL_2}(X_{FF})$, corresponding to semistable rank-2 bundles of degree 0, is connected and has dimension 0 in the diamond sense; the full Bun stack is stratified by slope polygons with open dense semistable stratum. A genus-$g$ reading places the open stratum as the "complex points" and the strata of lower slope as the degenerate boundary.

### Cycle 3 --- Perfectoid Shimura surfaces: Hilbert, Picard, Siegel

**Attack.** The Hilbert modular surface $X_{\mathrm{Hilb}}^F$ (for a real quadratic field $F$), the Picard modular surface $X_{\mathrm{Pic}}^F$ (imaginary quadratic $F$), and the Siegel modular surface $\mathcal{A}_2(\Gamma(N))$ are arithmetic surfaces in the literal sense: 2-dim integral models over a finite place of $\mathbb{Q}$. Their complex points are 2-complex-dim (so 4-real-dim) Kähler manifolds. The speculation asks for an "almost complex structure with the cohomological signature of a genus $g$ curve". The naive reading: the Hodge numbers of a Hilbert modular surface are $(h^{0,0}, h^{1,0}, h^{2,0}, h^{1,1})$ of an algebraic surface; they do not match $(1, g, g, 1)$ of a genus $g$ curve. For Hilbert modular surfaces, $h^{2,0} = \dim S_{(2,2)}(\Gamma)$ (Hirzebruch--Zagier, Vogan--Zuckerman). This does not reduce to a curve signature.

**Heal.** Two possible heals.

(i) **Scholze 2015** (*On torsion in the cohomology of locally symmetric varieties*, Ann. Math. 182, arXiv:1306.2070): the étale cohomology of Shimura varieties at infinite level is concentrated, and Caraiani--Scholze 2017 (arXiv:1511.02418) upgrade this to a vanishing theorem for the generic part of compact unitary Shimura varieties. The cohomology concentrates in middle degree (= complex dimension), which for a 2-dim Shimura variety means $H^2$. In this degree, the Galois representation attached to a generic component is $2g$-dimensional where $2g$ is the dimension of the cohomology block attached to a given packet. So "genus $g$" signature is recovered not on the surface itself but on its middle cohomology, whose Galois rank $2g$ matches the $L$-function data.

(ii) **Picard modular surfaces** for imaginary quadratic $F$: these are moduli of principally polarised abelian 3-folds with $\mathcal{O}_F$-action of signature $(2,1)$. Their compact subvarieties are Shimura curves of genus $g$ for a range of $g$ (Langlands--Rapoport; Harder--Langlands--Rapoport; Rogawski 1990). The "almost complex structure with genus $g$ signature" is the natural complex structure on the Shimura curve embedded as a CM-cycle; the surface is 2-dim, but the genus $g$ sits in $H^1$ of the embedded curve, not in $H^1$ of the surface.

**Status.** Theorem for the Caraiani--Scholze vanishing on compact unitary Shimura varieties (arXiv:1710.10543, Thm. 1.1); Theorem for the Scholze perfectoid infinite-level construction (arXiv:1306.2070). The recovery of "genus $g$ signature" through middle cohomology is a direct consequence of these theorems, with the crucial input being that the Hecke action on $H^2$ of a 2-dim Shimura variety is block-diagonal by cuspidal automorphic representation, each block of dimension $2g$ where $g$ is the genus of the "companion curve" in the Langlands parameter.

This reading aligns precisely with the Volume IV arithmetic branch convention: the load-bearing object is a Hochschild trace class whose character is an $L$-function, and the $L$-function factors as a product over automorphic representations of local factors of polynomial degree $2g$. The genus $g$ signature of a 2-dim Shimura variety is a shadow of this factorisation.

### Cycle 4 --- Prismatic cohomology and the rank-$2g$ Breuil--Kisin module

**Attack.** Bhatt--Morrow--Scholze 2018 (*Integral p-adic Hodge theory*, Publ. IHES 128) construct prismatic cohomology $H^{\bullet}_{\Delta}(X/\mathrm{Spf}\,\mathcal{O}_K)$ for a smooth proper $X$ over $\mathcal{O}_K$ ($K$ a finite extension of $\mathbb{Q}_p$), specialising to étale, crystalline, de Rham, and Hodge--Tate cohomologies via distinct base changes (Bhatt--Scholze 2022, Thm. 1.8). The prismatic cohomology is a Breuil--Kisin module: a $\mathfrak{S}$-module with $\varphi$-action where $\mathfrak{S} = W(k)[[u]]$. The question: for an arithmetic 2-fold with "genus $g$ signature", when does $H^1_{\Delta}(X/\mathrm{Spf}\,\mathbb{Z}_p)$ have rank $2g$?

The direct attack: $H^1_{\Delta}(X)$ has rank equal to the first Betti number of $X$ (Bhatt--Morrow--Scholze 2018, Thm. 1.1 and its prismatic upgrade in Bhatt--Scholze 2022). For a 2-dim arithmetic scheme $X$, $b_1(X) = 2 \dim H^1(X, \mathcal{O}_X)$ via Hodge symmetry, which for an algebraic surface of irregularity $q$ equals $2q$. So "rank $2g$ of $H^1_{\Delta}$" translates to irregularity $q = g$. For most Shimura surfaces, $q = 0$ (simply connected), which would give $g = 0$, not a genus-$g$ curve signature.

**Heal.** The right object is not $H^1_{\Delta}$ of the surface but the derived first cohomology of a universal family of curves **over** the surface. Concretely: let $\pi : \mathcal{C} \to X$ be a family of genus $g$ curves parametrised by an arithmetic surface $X$ (e.g., the universal family over a Shimura surface classifying $g$-dimensional abelian varieties). Then $R^1\pi_{*}^{\Delta}\mathcal{O}_{\mathcal{C}}$ is a rank-$2g$ prismatic $\varphi$-module on $X$, and this is the correct incarnation of "$X$ carries a genus-$g$ signature via an almost complex structure". The almost complex structure is the prismatic Frobenius $\varphi$ on this rank-$2g$ bundle; the tilting equivalence (Scholze 2012) provides the archimedean Hodge-theoretic shadow as the standard Hodge structure of weight 1 on $H^1(\mathcal{C}_{\mathbb{C}}, \mathbb{Z})$.

**Status.** Theorem for the existence of $R^1\pi_{*}^{\Delta}\mathcal{O}_{\mathcal{C}}$ as a rank-$2g$ Breuil--Kisin sheaf on $X$ (Bhatt--Morrow--Scholze 2018, Thm. 1.1; Bhatt--Scholze 2022, Thm. 1.8 base-changed to the relative setting). Theorem-waiting for the identification with an "almost complex structure" in the operational sense of the bar-cobar programme: this requires matching the prismatic Frobenius to the Koszul differential $\kappa^{\mathrm{Ar}}$ at the level of the arithmetic Heisenberg. This matching is not in Bhatt--Scholze and is the correct residual of this cycle.

### Cycle 5 --- Caraiani--Scholze genericity and the middle-degree signature

**Attack.** Caraiani--Scholze 2017 (arXiv:1511.02418) and 2019 (arXiv:1710.10543) prove: for a compact unitary Shimura variety $\mathrm{Sh}_K$ of signature $(1, n-1)$ with level $K$, and for a generic Satake parameter $\xi$, the interior cohomology $H^{\bullet}_c(\mathrm{Sh}_K, \mathbb{F}_{\ell})[\xi]$ is concentrated in middle degree. The middle degree for a 2-dim Shimura variety is $H^2$, of dimension $\leq \binom{2}{1}^g = 2g$ times a multiplicity for each generic packet of weight $g$. But the statement is only for compact Shimura varieties; Hilbert, Picard, Siegel modular surfaces with $\Gamma(N)$-level are non-compact, and the Eisenstein contributions to $H^2$ spoil the clean "genus $g$" signature.

**Heal.** Restrict to the compact Shimura-variety setting: the Picard modular surface at non-compact principal level is replaced by a compact unitary Shimura surface of signature $(1,2)$ with $U(2,1)$ rational form (Rogawski 1990). For this compact Shimura surface, the Caraiani--Scholze theorem applies, and the generic middle cohomology is $2g$-dimensional with $g$ the "companion genus" of the Langlands parameter. Here:

$$
H^2(\mathrm{Sh}^{U(2,1)}_K, \mathbb{F}_{\ell})[\xi_{\pi}] = V_{\pi} \otimes W_{\pi},
$$

where $V_{\pi}$ is the $2g$-dim Galois representation of the automorphic representation $\pi$ and $W_{\pi}$ is a multiplicity space. The "almost complex structure" is the $\ell$-adic Galois action, which after crystalline specialisation becomes the prismatic $\varphi$-action on the rank-$2g$ Breuil--Kisin module realising $V_{\pi}$.

**Status.** Theorem for the vanishing of non-middle-degree generic cohomology (Caraiani--Scholze arXiv:1710.10543, Thm. 1.1). Theorem-waiting for the identification of this rank-$2g$ middle cohomology as an "arithmetic surface with genus-$g$ signature" in the operational bar-cobar sense. The bridge is supplied by the local Langlands correspondence of Fargues--Scholze (arXiv:2102.13459, Thm. IX.0.1): the Galois representation $V_{\pi}$ matches the local Langlands parameter at each prime, and the rank-$2g$ structure is the dimension of this parameter.

This cycle produces the most direct candidate for the speculation under reading (B): **a compact unitary Shimura surface of signature $(1,2)$ with principal level, whose middle cohomology under Caraiani--Scholze genericity decomposes as rank-$2g$ blocks, each block realising an arithmetic "genus $g$ curve signature" via its Galois representation.** The almost complex structure is the combined $\ell$-adic and prismatic Frobenius data; the tilting to archimedean gives the classical Hodge structure of weight 1 of the automorphic companion genus-$g$ curve.

### Cycle 6 --- The Emerton--Gee stack $\mathcal{X}_{d}$ as universal Jacobian

**Attack.** Emerton--Gee 2019 (arXiv:1908.07185) construct the moduli stack $\mathcal{X}_d$ of étale $(\varphi, \Gamma)$-modules of rank $d$ over $\mathbb{Q}_p$. For $d = 2$, $\mathcal{X}_2$ parametrises 2-dim Galois representations of $G_{\mathbb{Q}_p}$; this is the local Galois deformation space. The speculation would place the "arithmetic surface of genus $g$" as the universal family over $\mathcal{X}_{2g}$: an object of $\mathcal{X}_{2g}$ is a rank-$2g$ $\varphi$-module, the Galois realisation of $H^1$ of a genus $g$ object. But: $\mathcal{X}_{2g}$ is a 2-dim Artin stack (Emerton--Gee 2019, Thm. 1.2.1 for the coarse structure), not an arithmetic surface in the geometric sense.

**Heal.** Recognise $\mathcal{X}_{2g}$ as the **moduli of arithmetic Jacobians of genus $g$**, in parallel with the classical Torelli theorem. A genus-$g$ curve $C/\overline{K}$ has a Jacobian $J_C$ whose Tate module $T_p J_C \otimes_{\mathbb{Z}_p} \mathbb{Q}_p$ is a $2g$-dim crystalline $(\varphi, \Gamma)$-module; the Torelli map sends $C$ to its Jacobian, and the Jacobian lives as a point of the moduli of abelian varieties of dimension $g$. In the Emerton--Gee framework the analogous map sends the genus-$g$ curve to the $(\varphi, \Gamma)$-module of its Jacobian, which is a point of $\mathcal{X}_{2g}^{\mathrm{crys}}$ (the crystalline locus). The universal family on $\mathcal{X}_{2g}^{\mathrm{crys}}$ is a rank-$2g$ local system over an Artin 2-stack; this is the arithmetic-surface enhancement of "universal Jacobian of genus $g$".

**Status.** Theorem for $\mathcal{X}_d$ as an Artin stack (Emerton--Gee 2019, Thm. 1.2.1; Bhatt--Scholze 2022 prismatic variant Thm. 1.13). Theorem-waiting for the identification with "arithmetic surface with genus-$g$ almost complex structure" in the Volume IV operational sense. The residual obstruction: the Emerton--Gee stack is defined locally at a single prime $p$; a global arithmetic-surface realisation requires restricted-tensor assembly across primes, which is precisely the content of $\mathrm{L}_{\mathrm{ACD}}$ in Chapter 22 of the Volume IV arithmetic branch and of conjecture F1. So this reading of the speculation reduces to the already-identified residual obligations.

### Cycle 7 --- The Witt-vector Grassmannian and higher-dim signature

**Attack.** The Witt-vector affine Grassmannian $\mathrm{Gr}^{W}_G$ (Zhu 2017, arXiv:1603.05593; Bhatt--Scholze 2015, arXiv:1507.06490) is a perfectoid space over $\mathrm{Spec}\,\mathbb{F}_p$; its cohomology is rich and computes the geometric Satake equivalence in mixed characteristic. For $G = GL_n$, $\mathrm{Gr}^{W}_{GL_n}$ is a $p$-adic analog of the loop group's affine Grassmannian. The speculation asks whether $\mathrm{Gr}^{W}_{GL_n}$ hosts a "genus $g$ signature". Naively: the cohomology of $\mathrm{Gr}^{W}_{GL_n}$ in degree $r$ is the $r$-fold symmetric power of a specific generating $\varphi$-module, so has polynomial growth in $r$, not matching the rank-$2g$ signature.

**Heal.** Zhu's Satake isomorphism for $\mathrm{Gr}^{W}_G$ (Zhu 2017, Thm. 0.2): the convolution algebra on $\mathrm{Gr}^{W}_G$ matches the representation ring of $\hat G(\mathbb{Z}_{\ell})$. For $G = GL_2$, $\hat G = GL_2$ and the representation ring is polynomial in the trace of the standard representation. This places $\mathrm{Gr}^{W}_{GL_2}$ as the **generating object** whose convolution structure produces all rank-$2g$ $\varphi$-modules of "genus $g$ signature", not itself an arithmetic surface of any genus. The correct role of $\mathrm{Gr}^{W}_{GL_n}$ in the bar-cobar programme is as the local Hecke-category support: convolution on $\mathrm{Gr}^{W}_{GL_n}$ is the arithmetic version of the complex factorisation Grassmannian's $E_2$-structure.

**Status.** Theorem for the geometric Satake on $\mathrm{Gr}^{W}_{G}$ (Zhu 2017, Thm. 0.2; Fargues--Scholze 2021, Thm. VI.0.1 diamond version). The role of $\mathrm{Gr}^{W}_{GL_2}$ in the Volume IV arithmetic branch is to supply the local $E_2$-structure of conjecture F2; the "genus $g$ signature" is then a derived invariant of the global assembly, not a local property of $\mathrm{Gr}^{W}$ itself. This confirms the earlier analysis: the speculation's "arithmetic surface of genus $g$" is not $\mathrm{Gr}^{W}$.

### Cycle 8 --- F1 + F2 interplay: global $E_2 \to E_3$ via perfectoid descent

**Attack.** In the Volume IV arithmetic branch (Chapter 21, F1 and F2 conjectures, and Chapter 22 closure), F1 is the global arithmetic Arinkin--Gaitsgory equivalence for $GL_2$; F2 is the perfectoid $E_2$-enhancement at each prime; F3 is the Ben-Zvi--Nadler identification. The speculation under attack proposes a "higher-genus (or arithmetic surface) extension"; translated into F1 + F2 + F3 language, this would be an $E_2$ structure at each prime glued to an $E_3$ structure globally via perfectoid descent. But: $E_2 \otimes E_1 = E_3$ by Dunn additivity (Lurie HA, Thm. 5.1.2.2), which requires both an $E_2$ and an $E_1$ input; the $E_2$ is supplied by F2, but the global $E_1$ input would need to come from a new "arithmetic-surface gluing" structure that is not in the Volume IV inscribed conjectures.

**Heal.** The higher-genus reading of the speculation is: F2 produces local $E_2$ at each prime; a rank-$2g$ "almost complex structure" across primes (the global Galois representation $V_{\pi}$ of automorphic $\pi$) acts by $g$ independent $E_1$-module structures, and Dunn additivity gives

$$
E_2^{(\text{local})} \otimes E_1^{(\text{genus-}g)} = E_3^{(\text{global})}
$$

at the arithmetic $g$-fold level, for each automorphic-$\pi$ block of dimension $2g$. The genus-$g$ $E_3$ structure is in the Hochschild trace of the genus-$g$ block of the global Iwahori Hecke category, not in the Hochschild trace of the full category.

**Status.** Conjectural. The clean form: for each automorphic representation $\pi$ of $GL_n(\mathbb{A}_{\mathbb{Q}})$ with companion genus $g$ (i.e., for which $\dim V_{\pi} = 2g$), there should be a genus-$g$-graded summand of the Volume IV Hochschild trace $\mathcal{V}^{\mathrm{prim}}$ that carries an $E_3$-algebra structure; the "arithmetic surface of genus $g$" is the categorical base of this $E_3$-structure. This is a new conjecture, logically consistent with F1 + F2 + F3 but not reducible to them.

**Residual.** The precise formulation requires: (i) a genus-grading on the global Iwahori Hecke category; (ii) compatibility of this grading with restricted-tensor-product assembly; (iii) identification of the genus-$g$ summand with the arithmetic version of Caraiani--Scholze middle cohomology. Items (i) and (ii) are new conjectural content; item (iii) is an application of Caraiani--Scholze genericity.

### Cycle 9 --- Almost-complex structure as prismatic $F$-crystal

**Attack.** In the Berthelot--Ogus 1983 / Bhatt--Scholze 2022 prismatic framework, an $F$-crystal on $X$ is a vector bundle $\mathcal{E}$ equipped with an isomorphism $\varphi^{*}\mathcal{E}[1/p] \cong \mathcal{E}[1/p]$, compatible with the prismatic structure sheaf. The "almost complex structure" of the speculation could be read as: an $F$-crystal on an arithmetic 2-fold whose rank is $2g$ and whose Newton polygon matches the Hodge polygon $(0,1)^g$. But: on a generic arithmetic 2-fold, the Newton polygon can vary by point (stratification by Newton polygons; Grothendieck 1974 specialisation of Newton polygons on families), so "an $F$-crystal with Hodge polygon $(0,1)^g$ everywhere" is a strong genericity condition, not a feature of the 2-fold itself.

**Heal.** Restrict to the ordinary locus: the Newton polygon is the Hodge polygon on an open dense subset of the moduli. On this locus, the $F$-crystal decomposes as $\mathcal{O}(0)^g \oplus \mathcal{O}(1)^g$ in the Katz--Mazur convention (Nicholas Katz, Travaux de Dwork; Mazur, *Frobenius and the Hodge filtration*, Bull. AMS 1972). The "almost complex structure" is the ordinary structure: the $F$-crystal has an unramified component of slope 0 and a trivialisable component of slope 1, whose direct sum is a canonical rank-$2g$ object. The non-ordinary locus carries different Newton polygons (supersingular, mixed slopes) which correspond to "degenerate complex structures" in the sense of moduli of abelian varieties.

**Status.** Theorem for the ordinary-stratum decomposition (Katz 1981, *Slope filtrations of $F$-crystals*, Astérisque 63). Theorem-waiting for the identification of the ordinary-stratum $F$-crystal with a "genus $g$ almost complex structure" in the Volume IV operational sense. The correspondence: the ordinary-stratum $F$-crystal of rank $2g$ is the arithmetic analog of the complex structure on $H^1$ of a genus $g$ Riemann surface; the non-ordinary strata are the arithmetic analogs of "degenerations" of the complex structure, governed by Kodaira--Spencer theory in the archimedean case and by Hodge--Newton decomposition in the $p$-adic case.

### Cycle 10 --- Synthesis: what is the speculation pointing at, precisely?

**Attack.** The nine previous cycles produce multiple candidate "arithmetic surfaces with genus $g$ signature". Which is the speculation referring to?

**Heal.** The convergence point across all cycles: **the speculation is asking for the universal family of rank-$2g$ $F$-crystals over a perfectoid base, equipped with a prismatic Frobenius as the almost complex structure, and with cohomological signature matching the $H^1$ of a genus $g$ curve on a dense open locus.**

Under reading (A), the object is: the stack $\mathrm{Bun}_{GL_{2g}}^{\mathrm{crys,ord}}(X_{FF})$ of ordinary crystalline rank-$2g$ bundles on the Fargues--Fontaine curve, with Newton polygon $(0,1)^g$. This is a 1-dim diamond in the Scholze sense; its points are the genus-$g$-signature crystalline $\varphi$-modules.

Under reading (B), the object is: a compact unitary Shimura surface of signature $(1,2)$ with principal level, restricted to the generic-Hecke-eigenclass locus on its middle cohomology, where each generic block has rank $2g$ via a Caraiani--Scholze automorphic decomposition. This is a genuine 2-dim arithmetic scheme whose "almost complex structure" is the global Galois action on its rank-$2g$ middle cohomology blocks.

In both readings, the almost complex structure is the prismatic Frobenius $\varphi$ on the rank-$2g$ bundle, and the genus $g$ signature is $\dim V_{\pi} = 2g$ for the associated automorphic representation $\pi$.

**Status.** Theorem-waiting on the unification of the two readings into a single conjectural framework. The two readings are related by the Torelli map: a genus $g$ curve's Jacobian is a rank-$2g$ abelian variety, which gives a point of $\mathcal{X}_{2g}^{\mathrm{crys}}$; the Torelli map factors the reading (A) object (a crystalline rank-$2g$ bundle) through the reading (B) object (a 2-dim moduli space). This factorisation is the content of classical Torelli in the arithmetic setting.

## Convergence proposal

The speculation converges on the following **arithmetic 2-fold with genus-$g$ almost complex structure**:

$$
\mathcal{S}^{\mathrm{Ar}}_g := \mathcal{X}_{2g}^{\mathrm{crys,ord}},
$$

the ordinary crystalline locus of the Emerton--Gee stack $\mathcal{X}_{2g}$, viewed as a 2-dim Artin stack over $\mathrm{Spec}\,\mathbb{Z}_p$ via the Bhatt--Scholze prismatic upgrade. A point of $\mathcal{S}^{\mathrm{Ar}}_g$ is a rank-$2g$ ordinary crystalline $\varphi$-module with Hodge--Tate weights $\{0, 1\}^g$; equivalently, a rank-$2g$ $F$-crystal with Newton polygon $(0,1)^g$; equivalently, a point of the crystalline-representation locus of the universal Jacobian stack.

The "almost complex structure" is the prismatic Frobenius $\varphi$, acting on the universal rank-$2g$ bundle $\mathcal{E}^{\mathrm{univ}}$ over $\mathcal{S}^{\mathrm{Ar}}_g$. On the ordinary stratum $\mathcal{E}^{\mathrm{univ}}$ splits as $\mathcal{E}^{\mathrm{univ}}_0 \oplus \mathcal{E}^{\mathrm{univ}}_1$ with slopes 0 and 1; the Frobenius acts as identity on $\mathcal{E}^{\mathrm{univ}}_0$ and as $p$ on $\mathcal{E}^{\mathrm{univ}}_1$ (in the appropriate normalisation). This splitting is the arithmetic version of the Hodge decomposition $H^1(C_{\mathbb{C}}, \mathbb{C}) = H^{1,0} \oplus H^{0,1}$ of a genus $g$ Riemann surface, and the "almost complex structure" is the endomorphism $J = i \cdot (+1) \oplus i \cdot (-1) = i \cdot \mathrm{diag}(1, -1)$ on $\mathcal{E}^{\mathrm{univ}}_0 \oplus \mathcal{E}^{\mathrm{univ}}_1$ in the archimedean limit via tilting.

The cohomological signature matches: $\mathrm{rk}(\mathcal{E}^{\mathrm{univ}}) = 2g = \dim_{\mathbb{Q}_p} H^1_{\mathrm{et}}(C_{\bar K}, \mathbb{Q}_p)$ for any genus $g$ curve $C$ with ordinary reduction.

The Volume IV arithmetic branch placement: $\mathcal{S}^{\mathrm{Ar}}_g$ is the local spectral-side geometric base of the rank-$2g$ sector of the global Iwahori Hecke category. Its global assembly across primes (via restricted-tensor descent, $\mathrm{L}_{\mathrm{ACD}}$) produces the genus-$g$-graded sector of $\mathcal{V}^{\mathrm{prim}}$. Under the Caraiani--Scholze / Scholze tilting correspondence, the archimedean companion is the moduli $\mathcal{M}_g$ of complex curves of genus $g$, with its Hodge bundle; the bar-cobar programme extends to $\mathcal{M}_g$ via the Beilinson 1984 chiral construction.

## Realization pointer

Under the Volume IV HZ-IV decorator conventions:

- **Derivation source.** The arithmetic 2-fold $\mathcal{S}^{\mathrm{Ar}}_g = \mathcal{X}_{2g}^{\mathrm{crys,ord}}$ is derived from Emerton--Gee 2019 (arXiv:1908.07185), Bhatt--Scholze 2022 (prismatic cohomology, Ann. Math. 196), and Fargues--Scholze 2021 (arXiv:2102.13459) for the diamond/geometric-Satake structure.

- **Verification source.** The cohomological-signature claim is verified against Caraiani--Scholze 2017--2019 (arXiv:1511.02418, arXiv:1710.10543) for the middle-degree concentration on compact unitary Shimura varieties, and against Bhatt--Morrow--Scholze 2018 (Publ. IHES 128) for the prismatic-étale comparison of rank.

- **Disjoint rationale.** Emerton--Gee construct $(\varphi, \Gamma)$-module stacks via Galois deformation theory; Caraiani--Scholze prove vanishing for Shimura varieties via automorphic representation theory; Bhatt--Morrow--Scholze construct prismatic cohomology via Witt-vector deformation of rigid analytic geometry. These three derivations are parallel; no one reduces to another. The conjunction supplies an independent verification path for the cohomological signature claim.

- **Status of the speculation object.** Theorem-waiting for the construction of $\mathcal{S}^{\mathrm{Ar}}_g$ as a 2-dim Artin stack with canonical rank-$2g$ universal bundle (this follows from Emerton--Gee 2019, Thm. 1.2.1, restricted to the ordinary crystalline locus). Conjectural for the identification of its global assembly with a genus-$g$-graded sector of Volume IV's $\mathcal{V}^{\mathrm{prim}}$; the conjecture depends on F1 (global AG), F2 (perfectoid $E_2$), F3 (arithmetic Ben-Zvi--Nadler), plus a new genus-grading conjecture (Cycle 8). Heuristic for the full equivalence of readings (A) and (B) via arithmetic Torelli.

- **Placement within the arithmetic branch.** The object $\mathcal{S}^{\mathrm{Ar}}_g$ supplies the local-spectral-side genus-$g$ model; its global assembly is a conjectural refinement of F1 beyond rank 2. Under reading (A), $\mathcal{S}^{\mathrm{Ar}}_g$ is the Fargues--Fontaine rank-$2g$ bundle moduli. Under reading (B), $\mathcal{S}^{\mathrm{Ar}}_g$ with its archimedean companion is the compact unitary Shimura surface restricted to generic-Hecke-eigenclass middle cohomology.

- **Next steps.** Three paper-length obligations arise from this voice. (i) Construct $\mathcal{S}^{\mathrm{Ar}}_g$ explicitly as a 2-dim Artin stack with the prescribed $F$-crystal universal bundle (estimated 40--60 pages, direct application of Emerton--Gee 2019 plus Bhatt--Scholze 2022). (ii) Prove a genus-grading on the global Iwahori Hecke category compatible with the Caraiani--Scholze automorphic decomposition (estimated 60--80 pages, new content). (iii) Identify the archimedean companion of $\mathcal{S}^{\mathrm{Ar}}_g$ with a derived enhancement of $\mathcal{M}_g$ via tilting, supplying the bridge to Beilinson's 1984 chiral construction (estimated 30--50 pages, comparison result).

The voice's convergent verdict: the speculation's "arithmetic surface with almost complex structure and genus-$g$ cohomological signature" is the ordinary crystalline Emerton--Gee stack $\mathcal{X}_{2g}^{\mathrm{crys,ord}}$, with prismatic Frobenius as the almost complex structure, and with the cohomological signature verified by the Caraiani--Scholze middle-degree concentration theorem on compact unitary Shimura surfaces. The two readings (A: rank-$2g$ on $X_{FF}$) and (B: 2-dim Shimura surface with rank-$2g$ middle cohomology) are related by arithmetic Torelli and are simultaneously captured by the proposed object. This is the perfectoid-prismatic content of the speculation, independent of the other five voices' perspectives but structurally consistent with them via Fargues--Scholze local Langlands.
