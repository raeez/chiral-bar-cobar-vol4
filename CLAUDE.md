# CLAUDE.md -- Vol IV: Realization

> **Inherits `~/ecosystem/INVARIANTS.md`.** That file holds the canonical ecosystem rules: destructive-git forbidden-command list, multi-agent worktree concurrency, standalone-documents discipline, Russian-school voice, every-file-into-the-repo rule, commits-carry-no-LLM-attribution, deep-semantic-merges, intelligence propagation, mathematical-repair doctrine. Read it first. Repo-local rules follow.

---

This file is the canonical reference for Vol IV of the Modular Koszul
Duality programme. It inherits the constitution of Vols I-III and adds
Vol-IV-specific discipline. Read together with the Vol I CLAUDE.md
(primary constitution) and Vol II + Vol III CLAUDE.md (domain-specific
addenda).

Author of record: Raeez Lorgat. No AI attribution appears anywhere in
this repository. No co-authored-by. No generated-by. All commits carry
Raeez Lorgat only.

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
   claims. At installation snapshot (2026-04-16): Vol I 0/2275, Vol II
   0/1134, Vol III 2/283. Vol IV closes these gaps either by inscribing
   a genuine decorator or by explicit scope restriction / status
   downgrade.
2. Engine-claim alignment. Every ProvedHere claim backed by a compute
   engine in Vols I-III carries a cross-reference from Vol IV that
   verifies the engine's expected values come from a source disjoint
   from the engine's own formula.
3. Cross-volume AP5 closure. Every AP5 propagation debt recorded in
   `notes/cross_volume_aps.md` is retired by Vol IV or converted to
   explicit conditional status.

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
- A.2 Master conjectures MC1-MC5 (all proved as of 2026-04-16).
- A.3 Shadow tower, G/L/C/M depth classification, SC-formality.
- A.4 Chiral quantum groups (sl_2 Yangian, affine KM, gl_N, elliptic,
  toroidal formal disk).
- A.5 CY landscape (Phi functor, kappa_BKM universality, CY-A_3, CY-D
  stratification, six routes to H_Muk).
- A.6 Platonic reconstitution chapters (2026-04-16 wave): Koszul
  Reflection Theorem, kappa-conductor K, d_bar = KZ^*(nabla_Arnold),
  quadrichotomy, MC5, S_5 Wick, Phi functor Vol III, infinite
  fingerprint classification.

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
   the intended scope. Rare, but allowed: the Beilinson principle
   prefers a smaller true theorem to a larger false one.

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

Import-time disjointness check: Vol IV imports
`compute.lib.independent_verification` from Vol I (same symbol) plus
`compute/lib/realization_registry.py` local to Vol IV. The two registries
are distinct namespaces; the Vol IV registry forbids any Vol IV entry
whose `verified_against` set collides with the corresponding Vol I
entry's `derived_from` set. This enforces "Vol IV does not pretend that
Vol I's derivation is a Vol IV verification."

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

### Pre-edit checklist

Before any edit to a Vol IV .tex chapter or .py engine:

1. Identify the source claim in Vols I-III (full label, chapter, line).
2. Fetch the original derivation sources (read the .tex proof, read
   the engine formula, not the CLAUDE.md description).
3. Choose verification sources from the primary or secondary disjoint
   catalogs above. Write down the disjoint_rationale.
4. Run the Vol IV decorator import test:
   `pytest compute/tests/test_realization_programme.py -x`.
   A tautological registration fails at collection time.
5. Then write the chapter entry (Part B) + optional compute engine
   (Part C) + optional cross-reference in Part A.

### Label discipline

Vol IV labels carry the prefix `v4-` to avoid collision with the three
upstream volumes. Every `\label{thm:...}` in Vol IV MUST be
`\label{v4-thm:...}`. When referencing a claim from Vols I-III, use the
native cross-volume reference (no prefix change) and include a remark
indicating the home volume.

Atomic grep before label creation:

    grep -rn '\\label{v4-' /Users/raeez/chiral-bar-cobar-vol4/
    grep -rn '\\label{<candidate>}' /Users/raeez/chiral-bar-cobar \
        /Users/raeez/chiral-bar-cobar-vol2 \
        /Users/raeez/calabi-yau-quantum-groups

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
IV decorators. Snapshot (2026-04-16, installation):

    Vol I:   0 / 2275 covered   (target: 2275 / 2275)
    Vol II:  0 / 1134 covered   (target: 1134 / 1134)
    Vol III: 2 /  283 covered   (target:  283 /  283)

At Vol IV installation, three Vol IV decorators are installed (Part B
seed):

1. `thm:realization-programme-definition` (defines Real).
2. `thm:realization-existence-for-platonic-theorems` (Real exists for
   the seven Platonic theorems of the programme).
3. `thm:realization-completeness-programme` (Real extends to the
   non-degenerate locus).

Progress is tracked in `notes/hziv_coverage.md` (to be created per
campaign). Each campaign targets a batch of Vol I-III claims, inscribes
Vol IV decorators, and updates the coverage snapshot.

### Prose standard

Vol IV inherits the Vol I prose standard in full: no em dashes, no AI
slop tokens, no hedging where the math is clear, no passive voice
where active is available. Before any Edit, mental-grep the banned
tokens: moreover, furthermore, additionally, notably, crucially,
remarkably, interestingly, delve, leverage, tapestry, cornerstone,
landscape (as metaphor), journey, navigate (non-geometric). Em dash
(---, U+2014) forbidden; use colon, semicolon, period.

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

Vol IV inscribes the following openings at installation time. These
are NOT gaps in Vol IV; they are scope restrictions inherited from
Vols I-III, recorded here for operational clarity.

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

These are not defects of Vol IV; they are honest scope boundaries.

## Build

```
cd /Users/raeez/chiral-bar-cobar-vol4
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pytest compute/tests/ -q
```

Vol IV inherits the Vol I build discipline: kill competing pdflatex
before running; serialize builds across volumes on the same machine.

## Shared LaTeX Template

Vol IV consumes the shared mathematics template from `~/latex-template`.
The repo-root symlink is:

```
raeez-math-template.sty -> ../latex-template/raeez-math-template.sty
```

`main.tex` loads `\usepackage{raeez-math-template}` immediately after
`\documentclass` and exposes the standard `\mainpreambleonly` guard used
by the template deployment harness. Typography, theorem-like
environments, claim-status macros, stable anchors, Unicode fallbacks,
and shared TikZ styles live in the template. Do not fork them locally
unless the shared template itself is being repaired.

Template deployment is checked from the template repo:

```
cd /Users/raeez/latex-template
make install-consumer-symlinks
make check
```

## Session Protocol

1. Read this file.
2. Read `AGENTS.md` when operating in a Codex / GPT-5-family harness;
   it mirrors this file on substance and adds Codex-specific load order.
3. Read the corresponding Vol I, II, or III CLAUDE.md section for the
   claim class being realized.
4. Before inscribing a Vol IV decorator, read the SOURCE chapter and
   its proof in the home volume -- never from memory, never from
   CLAUDE.md description.
5. Write the Part B entry + compute engine + Part A index update in
   the same session.
6. Run the Vol IV decorator test. Tautology fails at collection.
7. Update `notes/hziv_coverage.md` with the new coverage snapshot.

## Git Attribution

All Vol IV commits authored by Raeez Lorgat. No co-authored-by. No
AI attribution anywhere in the repository. No generated-by. This rule
is constitutional; violating it is a PRE-COMMIT hook failure.

## Long-Form Proof Harness

For Claude Code, Codex CLI, and any GPT-5.5 / GPT-5-Codex-class agent,
frontier mathematics runs in maximum-effort mode. Use the deepest
host-exposed model and reasoning budget. If the host offers a
GPT-5.5 Pro / Heavy or `xhigh` setting, use it for theorem repair,
cross-volume synthesis, source-disjoint verification, adversarial
review, and primary-source reconstruction. The private ChatGPT Pro
harness is not public; this is the open local analogue.

Long runs are normal. A 30-60 minute agent run is acceptable when a
proof obligation requires it. The agent first loads the relevant
context (`CLAUDE.md`, `AGENTS.md`, target chapter, home-volume source
chapter, dependencies, bibliography, compute files, and registry
entries), builds an internal outline, then works through independent
routes: worked example, formal argument, primary source, computation,
and cross-volume consistency. Private scratch stays private; the
deliverable is the checked proof trace and the exact remaining
obstruction.

After every proposed repair, run an attack-heal loop: source collision,
sign/convention check, ambient-category check, missing hypothesis,
false functoriality, unproved equivalence, numerical constant, and
engine-test synchronization. Heal and attack again until the theorem
closes or the exact obstruction is named for the next repair cycle. Do
not downgrade the manuscript to close the loop. Subagents provide
evidence, not authority; the main thread integrates by deep semantic
merge.

## Do Not

1. Do not treat old throughput cautions as a prohibition on swarms.
   When the user explicitly asks for a large adversarial or
   cross-volume swarm, it is allowed. Partition work by disjoint
   Vol I/II/III claim families, source catalogs, compute engines, or
   arithmetic-branch proof obligations.
2. Do not register a tautological verification. `derived_from` and
   `verified_against` must be source-disjoint.
3. Do not propagate claim-status wording when mathematics is waiting.
4. Do not invent formulas from memory. Read source chapters and primary
   literature.
5. Do not run `pdflatex` after every edit.
6. Do not add AI attribution anywhere.
7. Do not `git stash` or amend commits.
8. Do not fork the shared LaTeX template locally for typography,
   theorem styles, claim-status macros, or diagram styles.
9. Do not confuse this file with a configuration manual. It is a
   mathematician's working manifesto for Vol IV.

## Branch and Worktree Reconciliation

When branches or worktrees differ, always perform a deep semantic
merge. Never discard one side of a divergence without reading it.
Never use `git reset --hard`, `git checkout --`, or `git restore` to
clobber work as a shortcut. Read both sides in context and construct a
merged result that preserves the mathematical content, prose
improvements, and structural refinements from both sides. When a
line-level conflict is semantic, choose the stronger theorem, tighter
citation, or more rigorous proof by reading the surrounding chapter.

## Appendices

- `appendices/realization_catalog.tex` -- Full realization index (Part A).
- `appendices/disjoint_source_catalog.tex` -- Source catalogs used
  across Parts B and C.
- `appendices/hziv_coverage_snapshots.tex` -- Historical coverage
  snapshots from each campaign.

(To be created as Vol IV expands.)

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

### Load-Bearing Theorem

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
- `appendices/arithmetic/B_fifteen_voices_attack_heal_index.tex`
- `appendices/arithmetic/C_three_conjectures_dependency.tex`
- `notes/arithmetic_attack_heal/` -- Raw adversarial transcripts (15 voices).

### Status Discipline

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

### Build

Arithmetic branch compiles via the standard `main.tex` build:

    cd /Users/raeez/chiral-bar-cobar-vol4
    pdflatex -interaction=nonstopmode main.tex
    pytest compute/tests/ -q

The arithmetic branch adds no new `compute/` engines (it is a
synthesis, not a computation); Part C of Vol IV remains unchanged
by this addition.

### Provenance

The arithmetic branch records the fifteen-voice adversarial
attack-heal protocol run during 2026-04-23 to 2026-04-24. Raw
transcripts are preserved in `notes/arithmetic_attack_heal/`. Each
voice channelled a distinct combination of the elite Russian school
and the mathematical physics elite; each executed at least five
attack-heal cycles; the fifteen independent trajectories converged on
the common Hochschild-trace-class object described above.
