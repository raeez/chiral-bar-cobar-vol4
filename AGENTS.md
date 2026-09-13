# Volume IV instruction contract

This repository inherits `~/ecosystem/INVARIANTS.md` and `~/ecosystem/AGENTS-HARNESS.md`.
Read their universal safety rules, then their task-relevant sections. The invariants take precedence over the harness and local doctrine.
AGENTS.md and CLAUDE.md share this contract. Read CLAUDE.md before code edits.
For Claude-specific model controls or context loading, consult `~/ecosystem/CLAUDE-HARNESS.md` when those settings affect the task.
System and developer instructions govern the session. Preserve the inherited destructive-Git and no-exfiltration safety floor.

## Scope and custody

Vol IV verifies the Modular Koszul Duality programme in Vols I–III.
Its target is `Real(X,T)=(d,e)`: an independent-verification decorator and an engine with independently derived expected values.
Keep author-of-record attribution to Raeez Lorgat. Add no model coauthor or generated-by attribution.
Use an isolated worktree for nontrivial edits. Preserve concurrent work and the shared checkout's HEAD.
Write only assigned paths. Loading this contract grants no upstream edit, signing, sending, deployment, or publication authority.
Read source volumes as needed. Report required upstream changes to their accountable owner unless the task assigns those paths.
Subagents return evidence and leave integration to the accountable owner. They do not commit or push.
Preserve both sides of substantive divergences through semantic integration. Never discard concurrent mathematical content.

## Manuscript boundary

Reader-facing sources contain mathematics or physics at every scale, including notes, captions, bibliography annotations, and PDF metadata.
Keep task instructions, audit workflow, worktree details, review status, TODO queues, ownership, and model references outside the manuscript.
State theorem, conditional consequence, heuristic, conjecture, and open problem explicitly.
Express missing data mathematically, without drafting history. Builds and prose polish do not replace proof.
Use literal research prose. Avoid mannered language, em dashes, invented terminology, and ornamental transitions.
Pass this boundary to every writing agent and review its returned prose.

## Task routing

- For realization work, read the relevant section of [the mathematical reference](docs/mathematical-reference.md), then the home-volume source proof.
- For decorator or engine changes, read `compute/lib/realization_registry.py` and affected tests in `compute/tests/`.
- For coverage work, read `notes/hziv_coverage.md` and the corresponding Part A and Part B sources.
- For arithmetic work, start with `chapters/arithmetic/98_arithmetic_branch_residual_boundary.tex`, then follow the affected dependencies.
- For layout work, read `main.tex` and the shared package it loads. Inspect only the affected template interface.
- Read adjacent repositories only when a concrete dependency requires them. A read-only lookup does not authorize reconstruction.

## Proof and verification

Read formulas, hypotheses, conventions, and primary sources before changing the corresponding claim.
Record why `derived_from` and `verified_against` are source-disjoint. Renaming a derivation does not create independence.
Expected values must come from an independent route. Numerical agreement alone does not prove a theorem.
Update affected Part A pointers, Part B entries, compute audits, and coverage records together.
Use `v4-` for native labels and `v4-arith:` for arithmetic labels. Keep imported labels and home-volume attribution.
The arithmetic object `\mathcal{V}^{\mathrm{prim}}` is a Hochschild trace class, not a vertex algebra.
New Part C engines for the arithmetic branch require explicit task authorization.
For proof repair, check the strongest plausible failure modes relevant to the claim.
Examples include source collision, signs, ambient category, missing hypotheses, false functoriality, and synchronized engine errors.
Continue useful authorized work while evidence supports a next step. Use effort appropriate to mathematical uncertainty and verification cost.
A bounded investigation may end with an honest unresolved obligation, failed routes, evidence, and the next discriminating step.
This does not complete an unresolved theorem target. Status corrections preserve truth and never substitute for proof repair.
Report source contradictions without inventing a resolution. Continue independent work that the contradiction does not block.
When the user requests parallel work, assign independent claim families or computation checks with clear paths and an integration owner.
Each worker returns claim anchors, sources, exact constants, changed paths, checks, and remaining obligations.

## Local checks and builds

Choose checks by the affected behavior. Instruction-only changes need reference, parity, and diff checks.
Registry changes need `python3 -m pytest compute/tests/test_realization_programme.py -x`.
Run affected compute tests after engine changes. Use `python3 -m pytest compute/tests/ -q` for broader compute changes.
The registry reads predecessor source registries. Report missing dependencies explicitly.
After a coherent manuscript change, run an isolated local build without another permission request.
Do not rebuild after each edit or terminate unrelated processes. Stop only a process whose ownership belongs to this task.

From the assigned worktree, use a unique output directory:

```bash
vol4_build_dir=$(mktemp -d "${TMPDIR:-/tmp}/vol4-build.XXXXXX")
TEXINPUTS="$HOME/latex-template//:${TEXINPUTS:-}" pdflatex -interaction=nonstopmode -halt-on-error -output-directory="$vol4_build_dir" main.tex
```

Repeat compilation only as needed to resolve references. Inspect the log and relevant rendered pages before claiming layout success.
The shared `raeez-math-template.sty` owns typography, theorem environments, claim macros, and diagram styles.
Its sibling-relative symlink can fail in a relocated worktree. The scoped TEXINPUTS above reads the shared package without mutating consumers.
Do not fork the package locally or run consumer installation as an incidental check.
Template deployment belongs to its assigned owner and requires publication authority where applicable.

## Completion

Complete the authorized task with evidence covering its full scope.
Report changed paths, checks and results, remaining mathematical obligations, and exact downstream work requiring another owner.
Do not start persistent goals or publish merely because a local task finishes.
