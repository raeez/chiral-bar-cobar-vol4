# Volume IV mathematical reference

Read the relevant section for realization, source-disjoint verification, or arithmetic work.
The root AGENTS.md and CLAUDE.md carry the execution contract.
This reference preserves programme definitions, source catalogues, and initial mathematical targets.
Its coverage and theorem-status summaries are historical, non-authoritative context, not proof of current completion.
For current status, inspect the cited manuscript proof, local registry, and `notes/hziv_coverage.md`.
For arithmetic residuals, start with `chapters/arithmetic/98_arithmetic_branch_residual_boundary.tex` and follow its dependencies.
Do not promote an assertion because an instruction reference calls it proved.

## Identity

Vol IV is the verification capstone. Vols I-III inscribed the programme:
Vol I the algebra (bar complex, Koszul duality, five theorems A-D+H,
shadow tower, standard landscape), Vol II the physics (3D HT QFT, BRST,
celestial, 3D quantum gravity), Vol III the geometry (CY categories,
chiral Yangians, BPS algebras, six routes to H_Muk). Each of these
volumes carries claim-status tags, and a majority of main theorems are
inscribed as `\ClaimStatusProvedHere`. What Vols I-III do NOT do is
furnish, for every such inscription, an independent verification path
that could catch its own malpractice.

Vol IV addresses this deficit. A theorem `T` inscribed in a chapter `X`
of Vols I-III is *realized* when Vol IV exhibits the pair

    Real(X, T) = (d, e)

where `d` is an HZ-IV independent-verification decorator with disjoint
derivation and verification sources, and `e` is a computational engine
whose expected values are obtained along a path disjoint from the one
used to derive the theorem's formula. The first component guards
against tautological verification; the second against
engine-test-synchronized malpractice (AP10, AP128). Vol IV exhibits
`Real(X, T)` for every ProvedHere `T`, and in so doing converts the
programme from a claim corpus into a verified corpus.

Vol IV is neither a narration nor an aspirational document. It is a
mathematical object in its own right: the realization functor `Real`
from inscribed theorems to verification pairs, together with the
theorem that `Real` is defined on the full non-degenerate locus of the
programme.

## Mission

1. 100 percent HZ-IV decorator coverage across Vols I-III ProvedHere
   claims. Vol IV closes coverage gaps with an independent decorator.
   Record unsupported scope honestly while retaining its proof obligation. The
   live coverage roster lives in `notes/hziv_coverage.md`.
2. Engine-claim alignment. Every ProvedHere claim backed by a compute
   engine in Vols I-III carries a cross-reference from Vol IV that
   verifies the engine's expected values come from a source disjoint
   from the engine's own formula.
3. Cross-volume AP5 closure is a programme target. Track each affected dependency in the current coverage and source records.
   The initial notes/cross_volume_aps.md path is absent. Resolve each dependency or state its remaining condition explicitly.

Vol IV does not create new mathematics by default. When the
verification path forces a strengthening (a sharper theorem, a wider
domain, a missing corollary), the strengthening is inscribed; but the
default action is verification.

## Structure

Vol IV has three parts.

### Part A. Inscriptions (index)

Part A is a cross-referenced index of every ProvedHere claim in Vols
I-III, organized by theorem class:

- A.1 Five theorems (A, B, C, D, H) across all three volumes.
- A.2 Master conjectures MC1-MC5.
- A.3 Shadow tower, G/L/C/M depth classification, SC-formality.
- A.4 Chiral quantum groups (sl_2 Yangian, affine KM, gl_N, elliptic,
  toroidal formal disk).
- A.5 CY landscape (Phi functor, kappa_BKM universality, CY-A_3, CY-D
  stratification, six routes to H_Muk).
- A.6 Reconstitution chapters: Koszul Reflection Theorem,
  kappa-conductor K, d_bar = KZ^*(nabla_Arnold), quadrichotomy, MC5,
  S_5 Wick, Phi functor Vol III, infinite fingerprint classification.

Each entry in Part A records: claim label, source chapter (Vol:file),
status tag, the derivation path used in the original proof, and the
realization pointer into Part B.

Part A is index, not content. Theorems stay in their home chapters of
Vols I-III. Vol IV refers; it does not re-prove.

### Part B. Decorators (HZ-IV full-coverage campaign)

Part B is the operational heart of Vol IV. For each ProvedHere claim
indexed in Part A, Part B contains one of three entries.

1. `\RealizedHere{claim}` -- a verification decorator in
   `compute/tests/test_realization_*.py` with disjoint derivation and
   verification sources, plus a short remark in the chapter explaining
   why the two sources are genuinely independent (not renamed). This
   is the default action for every ProvedHere claim whose proof admits
   an independent verification path.
2. `\ScopeRestricted{claim, domain}` -- a restriction of the theorem's
   scope to the locus where an honest independent path exists, with
   the complementary locus either reduced to a proposition (partial
   result) or downgraded to a conjecture. Used when the original
   statement was too broad.
3. `\DowngradedHere{claim}` -- an explicit status downgrade from
   ProvedHere to Conjectured (or in rare cases, retracted entirely)
   when no genuine disjoint path exists and no restriction captures
   the intended scope. An evidence-supported status correction preserves truth.
   It does not complete the original proof obligation.

Decorator sources are drawn from the three canonical disjoint catalogs:

- **Primary disjoint sources** (Vol IV canon):
  (a) Pridham-Toen-Vezzosi derived deformation theory (DAG VIII, VIII.2
  in particular);
  (b) Lurie HA 5.3 (higher Deligne and (infinity,2)-centralizers);
  (c) Vols I-III independent test infrastructure (cross-imported with
  an import-time disjointness check).
- **Secondary disjoint sources**: Costello-Gwilliam factorization
  homology, Gelfand-Kazhdan formal geometry, Ben-Zvi-Francis-Nadler
  integral transforms, Francis-Gaitsgory factorization gluing,
  Mok 2025 logarithmic FM compactifications, Hua-Keller N=1 Calabi-Yau
  categorification, Costello-Witten-Yamazaki 6d hCS, Schiffmann-Vasserot
  CoHA. Cited per-claim with explicit disjoint_rationale.

The local `compute/lib/realization_registry.py` loads predecessor registries through explicit file paths.
It keeps the local registry separate from the predecessor registries.
For imported claims, it compares verification sources with visible predecessor derivations or the supplied upstream derivation list.
Inspect this implementation and its tests when changing registration behavior.

### Part C. Infrastructure

Part C aligns compute engines across the four volumes. For each
compute engine in Vols I-III that backs a ProvedHere claim, Part C
records:

1. The engine's formula source (where the formula was obtained).
2. The engine's expected-value source (where the test hardcoded
   constants come from).
3. The disjointness audit (engine formula vs expected values must come
   from disjoint sources; AP128 enforcement at the Vol IV level).
4. Vol IV's own cross-engine: an independent computation, usually at
   different numerical precision or via a different algebraic path,
   yielding the same hardcoded expected values modulo rtol = 1e-10.

Part C does not duplicate compute engines. It adds a verification layer
on top of them.

## Cross-Volume Bridges

Vol IV's dependency graph on its three predecessors is explicit.

- Vol I -> Vol IV: every Vol I ProvedHere claim is a node in Part A.
  Five theorems, master conjectures, shadow tower, SC-formality, depth
  gap, D^2=0, Theta_A, ChirHoch^1 KM, topologization tower, E_3
  identification, chiral QG equivalence on ordered Koszul locus, gl_N
  chiral QG, Verlinde recovery, ker(av) formula, genus-2 construction,
  Miura coefficient universality, Z_g closed forms, conformal anomaly,
  critical level jump.
- Vol II -> Vol IV: HT landscape theorems, 3D HT QFT inscriptions, BV
  slab = bimodule, celestial moonshine bridge, 3D quantum gravity
  climax (Part VI). Vol II's MC5 Wick implementation (S_5 = -48/(c^2
  (5c+22))) is independently verified in Vol IV via a Wick contraction
  engine disjoint from Vol II's lambda-bracket derivation.
- Vol III -> Vol IV: Phi functor, kappa_BKM universality, CY-A_3
  inf-categorical proof, K3 abelian Yangian, ZTE T, class M E_3 bar
  dim 6^g, mock modular K3, six routes to H_Muk. AP-CY60 six-routes
  status is retired in Vol IV either by proof of convergence or by
  explicit conditional status per route.

The bridge from Vol II HZ-IV ("four irreducible opens -- all closed or
reduced") and Vol III AP-CY60 ("six routes status") is the initial
content of Part B.

## Vol IV Protocol

### Claim editing and labels

Read the source proof, formula, and relevant registry before changing a realization.
Record the full source label, chapter, and independent verification rationale.
For registry changes, run `python3 -m pytest compute/tests/test_realization_programme.py -x` after the coherent edit.
Update the affected Part A pointer, Part B entry, compute audit, and coverage roster together.
Use `v4-` for native labels and `v4-arith:` for arithmetic labels.
Keep imported labels unchanged and identify their home volume.
Search the relevant source trees for collisions before creating a label.

### Claim-status discipline

Vol IV inscribes almost no new ProvedHere claims. Its own claims are
of three kinds:

1. `Real(X, T) = (d, e)` realization claims (ProvedHere by
   construction, backed by a decorator and an engine).
2. Realization-existence theorems (ProvedHere, by enumeration over
   Part A).
3. Realization-completeness theorems (ProvedHere on the non-degenerate
   locus, Conjectured on the complement).

New mathematics in Vol IV is rare. When it happens, the new claim
obeys the same HZ-IV discipline: two disjoint sources, explicit
rationale, decorator in place at inscription time.

### HZ-IV (Vol IV coverage target)

Target: 100 percent coverage of ProvedHere claims in Vols I-III by Vol
IV decorators. The live coverage roster lives in `notes/hziv_coverage.md`.

Three seed Vol IV decorators sit in Part B:

1. `thm:realization-programme-definition` (defines Real).
2. `thm:realization-existence-for-platonic-theorems` (Real exists for
   the seven Platonic theorems of the programme).
3. `thm:realization-completeness-programme` (Real extends to the
   non-degenerate locus).

Each campaign targets a batch of Vol I-III claims, inscribes Vol IV
decorators, and updates the coverage roster.

## Three Platonic Anchors for Vol IV

Beyond the mission, Vol IV carries three anchor objects that give it
mathematical content beyond bookkeeping.

1. The realization functor `Real: Inscribed -> VerifiedPairs`. Objects:
   inscribed ProvedHere theorems in Vols I-III. Morphisms: theorem
   specializations (restrictions, corollaries). Vol IV proves `Real`
   is functorial on the non-degenerate locus: a specialization of an
   inscribed theorem induces a specialization of its verification pair.
2. The disjointness 2-functor `Disj: Sources -> Sources -> {0, 1}`.
   Objects: canonical source catalogs (Pridham-Toen-Vezzosi, Lurie HA
   5.3, Costello-Gwilliam, Francis-Gaitsgory, Mok25, etc.). Morphisms:
   citation chains. `Disj(S, T) = 1` iff `S` and `T` are disjoint in
   the Vol IV sense. Vol IV computes `Disj` on the catalog pairs used
   across Parts B and C.
3. The non-degenerate locus. Vol IV defines the non-degenerate locus
   of the programme as the complement of: (a) the critical-level locus
   (k = -h^v for affine KM), (b) the Psi = 0 locus for chiral
   Yangians, (c) the logarithmic CKL lane (Creutzig-Kanade-Linshaw)
   for admissible representations, (d) the super-Yangian chain-level
   chiral coproduct sector (FM230 absorbed, computation pending). Vol
   IV proves Real is defined on the non-degenerate locus and describes
   its behavior on the degenerate locus.

## Open Ends (end-of-programme)

The initial programme recorded the following open sectors and scope restrictions.
They remain mathematical obligations wherever a requested target includes them.
Use current source proofs to determine their present status.

1. Degenerate admissible logarithmic lane (Creutzig-Kanade-Linshaw):
   Realization restricts to non-admissible parameters. The admissible
   logarithmic sector is tracked as a scope restriction (Part B `ScopeRestricted`),
   not as a Vol IV gap.
2. Super-Yangian chain-level chiral coproduct: FM230 absorbs the
   concrete computation; Vol IV records the realization as a
   `ProofPending` open problem, not as a ProvedHere claim.
3. Vol III CY-C conditional bridges (5 of 6 routes to H_Muk await
   proof of convergence): each of the five outstanding routes carries
   a Vol IV `Conditional` entry tied to the hypothesis that the route
   converges.

These entries preserve the initial mathematical boundaries. They do not establish current closure.


## The Arithmetic Realization Branch (2026-04-24)

Vol IV carries a third Part alongside the original `Frame` and
`Realization Programme`: the `Arithmetic Realization Branch`,
inscribed 2026-04-24. This branch extends the realization mission
from Vols I-III claim verification to arithmetic verification:
verifying the programme's five theorems (A, B, C, D, H) on the
Arakelov-compactified arithmetic curve
$\overline{\mathrm{Spec}\,\mathbb{Z}}$ in addition to the curve
$C/\mathbb{C}$.

### Identity of the Arithmetic Branch

The object of study is $\mathcal{V}^{\mathrm{prim}}$, the Hochschild
trace class of the identity on the global arithmetic Iwahori Hecke
category of $GL_2$. It admits six equivalent presentations
converging from fifteen independent adversarial-protocol
trajectories: Langlands-automorphic, TQFT-Chern-Simons
(Kim arXiv:1510.05818), categorical-Hochschild-trace
(Bezrukavnikov arXiv:1209.0403, Ben-Zvi-Nadler arXiv:0904.1247),
integrability-Bethe-algebra, statistical-mechanics-Bost-Connes,
and factorization-homotopical (Costello-Gwilliam).

### Initial theorem target (2026-04-24)

$\kappa^{\mathrm{Ar}}_{\mathsf{G}} + (\kappa^{!})^{\mathrm{Ar}}_{\mathsf{G}} = 0 \Leftrightarrow \xi(s) = \xi(1-s)$:
arithmetic Heisenberg Koszul duality implies the Riemann functional
equation. Status: Theorem-waiting (Chapter 10 / 20).

### Files

- `chapters/arithmetic/00_manifesto.tex` -- Identity and scope.
- `chapters/arithmetic/01_construction.tex` -- Speculative starting point.
- `chapters/arithmetic/02_*.tex ... 16_*.tex` -- Fifteen attack-heal chapters, one per voice.
- `chapters/arithmetic/20_synthesis.tex` -- Six-window placement.
- `chapters/arithmetic/21_open_frontiers.tex` -- Three closing conjectures (F1-F3) + F4-F10.
- `appendices/arithmetic/A_primary_source_catalog.tex`
- `appendices/arithmetic/B_source_families_index.tex`
- `appendices/arithmetic/C_three_conjectures_dependency.tex`
- `notes/arithmetic_attack_heal/` -- Raw adversarial transcripts (15 voices).

### Initial status record (2026-04-24)

The branch uses five tags: Theorem / Theorem-waiting /
Conjecture / Heuristic / Falsified. At inscription (2026-04-24):
5 Theorem, 4 Theorem-waiting, 7 Conjecture, 3 Heuristic, 9
Falsified. The Falsified count is feature not defect: each
Falsified claim represents a specific technical joint where the
naive speculation broke, catalogued for pedagogical reference.

### Out of Scope

The branch does NOT claim to replace Caraiani-Scholze,
Fargues-Scholze, or Emerton-Gee. It imports local theorems
(Fargues-Scholze arXiv:2102.13459; Emerton-Gee arXiv:2012.12403)
and assembles them into the $E_{1}$-chiral-algebra presentation
natural to the bar-cobar programme. The novel content is the
assembly, not the components.

The branch does NOT claim $\mathcal{V}^{\mathrm{prim}}$ is a vertex
algebra. It is a Hochschild trace class whose character is an
$L$-function. The reader who wants a VOA must go to the complex
Heisenberg on the archimedean fibre and stop there.

### Label Prefix

All labels use `v4-arith:` prefix to disambiguate from the rest of
Vol IV (`v4-`) and from Vols I-III native cross-references.

### Computation boundary

The arithmetic branch began as a synthesis. New Part C engines require explicit task authorization.
The historical initial branch added no compute engines.

### Provenance

The arithmetic branch records the fifteen-voice adversarial
attack-heal protocol run during 2026-04-23 to 2026-04-24. Raw
transcripts are preserved in `notes/arithmetic_attack_heal/`. These records describe the initial investigation. They impose no fixed iteration count on later research.
