# AGENTS.md — chiral-bar-cobar-vol4

> **Inherits `~/ecosystem/INVARIANTS.md`** — canonical ecosystem rules (model-agnostic): destructive-git forbidden list, multi-agent worktree concurrency, standalone-documents discipline, Russian-school voice, every-file-into-the-repo rule, no-LLM-attribution in commits, deep-semantic-merges, intelligence propagation, open-source whitelist, mathematical-repair doctrine.
> **Inherits `~/ecosystem/AGENTS-HARNESS.md`** — canonical Codex / GPT-5-family harness calibration: reasoning-effort per task class, agentic eagerness, tool-use discipline, tool preambles, persistence and stop conditions, verbosity control, uncertainty handling, long-context outlining, self-reflection rubric, scope discipline, error-handling, git-and-worktree restatement for Codex defaults, frontend quality, no-LLM-commit-attribution, voice.
> **Mirrors the repo's `CLAUDE.md`** on substance. Before editing code in this repo, `read_file ./CLAUDE.md` — it carries the repo-local layout, commands, doctrine, and conventions. `AGENTS.md` and `CLAUDE.md` must not diverge in facts; they may differ in structure and voice.
>
> **Load order.** `INVARIANTS.md` → `AGENTS-HARNESS.md` → this repo's `CLAUDE.md` → this file's repo-local section (if any). The closest `AGENTS.md` in the directory tree wins per `agents.md`; explicit principal chat instructions outrank everything.
>
> **Model target.** Deepest host-exposed GPT-5.5 / GPT-5-Codex-family model, `reasoning_effort=xhigh` for any non-trivial mathematical work (never lower than `high`). Terse, declarative voice per `INVARIANTS.md §IV`. No LLM attribution on commits (`INVARIANTS.md §VI`).

---

## Repo-local (Codex / GPT-5 specific)

## What this repository is for

This repository is Vol IV of the Modular Koszul Duality programme:
the realization and verification capstone for Vols I-III. The target
object is the realization pair

```text
Real(X, T) = (d, e)
```

where `d` is an HZ-IV independent-verification decorator with disjoint
derivation and verification sources, and `e` is a compute engine whose
expected values are obtained independently of the formula it tests.

If you are an agent here, progress means converting a ProvedHere claim
from Vol I, II, or III into a realized claim, or honestly restricting
or downgrading it when no disjoint verification path exists.

## The mathematics you are working on

- Part A indexes every Vol I-III ProvedHere claim.
- Part B installs Vol IV decorators and the source-disjointness rationale.
- Part C audits compute engines and expected-value provenance.
- The arithmetic realization branch studies the Hochschild trace class
  `\mathcal{V}^{\mathrm{prim}}` over
  `\overline{\mathrm{Spec}\,\mathbb{Z}}`.
- The native label prefixes are `v4-` and `v4-arith:`. Never create an
  unprefixed Vol IV theorem label.

## Agent rules

1. Read `./CLAUDE.md` before any mathematical edit. It is the full
   Vol IV constitution.
2. Read the source chapter in the home volume before realizing a claim.
   Do not work from memory or from a scaffolding summary.
3. Never register a tautological verification. `derived_from` and
   `verified_against` must be disjoint, and the rationale must name why.
4. Write the Part A pointer, Part B decorator, compute audit, and
   coverage update in the same session when the claim requires all four.
5. Do not build after every edit. Run targeted tests after compute or
   registry changes; build at session end when the manuscript changed.
6. No AI attribution anywhere. Commits carry Raeez Lorgat only.
7. No `git stash`, no amend, no destructive checkout/reset/restore.
8. Claim-status changes are not repairs. Heal the proof, statement, or
   construction; if that cannot be done, name the exact obstruction.

## Shared LaTeX template

Vol IV consumes the shared template through the repo-root symlink
`raeez-math-template.sty -> ../latex-template/raeez-math-template.sty`.
`main.tex` loads it immediately after `\documentclass`, and exposes the
standard `\mainpreambleonly` guard used by the template harness.

The template deployment contract lives in `~/latex-template`:

```bash
cd ~/latex-template
make install-consumer-symlinks
make check
```

Do not fork typography, theorem styles, claim-status macros, or shared
TikZ styles locally unless the shared template itself is being repaired.

## Build and test

```bash
cd ~/chiral-bar-cobar-vol4
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pytest compute/tests/ -q
```

For template-level deployment checks, use `~/latex-template/scripts/check-template-harness`.

## User-authorized max-effort swarm protocol

When the user explicitly asks for a large adversarial, rescue, review,
or cross-volume swarm, treat that as authorization to use the largest
useful swarm the runtime can support. Partition by disjoint Vol I/II/III
claim families, source catalogs, compute engines, or arithmetic-branch
proof obligations. Name the integration owner.

Every attack-heal agent must return a compact, checkable report:
claim attacked, failure mode or proof, file anchors, primary-source
anchors, exact constants, claim-status recommendation, files changed,
tests run, and remaining open questions. Subagents provide evidence,
not authority. The main thread integrates by deep semantic merge.

## Research-grade Codex / GPT-5 scaffolding

| Parameter | Setting | Rationale |
|---|---|---|
| `reasoning_effort` | `xhigh` for non-trivial mathematics, never below `high` | Vol IV verifies an entire cross-volume proof corpus; false verification is worse than no verification. |
| `model` | Deepest host-exposed GPT-5.5 / GPT-5-Codex-family model | Long-context theorem repair and source-disjoint audit. |
| `verbosity` | As the proof requires | Final answers stay short; proof traces are not abridged when they are the deliverable. |
| Tool use | Parallel reads for TeX, compute, and cross-volume anchors | Load the whole claim neighborhood before writing. |
| Persistence | Absolute within scope | Close the verification or name the open proof obligation precisely. |
| Self-reflection rubric | Required before any inscription | Use `~/ecosystem/AGENTS-HARNESS.md §VIII`. |

### Long-form proof harness

For theorem repair, source-disjoint verification, arithmetic synthesis,
or cross-volume consistency, long runs are normal. Load `CLAUDE.md`,
this file, the target chapter, the source chapter in Vol I/II/III,
compute files, cited primary sources, and registry entries before the
first mathematical edit. Build an internal outline; do not write from
memory.

After every proposed repair, attack the strongest failure mode:
source collision, sign/convention mismatch, false functoriality,
missing hypothesis, engine-test synchronization, or scope leakage from
the arithmetic branch into the original realization programme. Heal,
then attack again until no fatal objection survives.

### Codex load order

1. `./CLAUDE.md`.
2. `~/ecosystem/INVARIANTS.md` and `~/ecosystem/AGENTS-HARNESS.md`.
3. `main.tex`, then the target `chapters/**.tex` or `appendices/**.tex`.
4. `compute/lib/realization_registry.py` and `compute/tests/` for any
   decorator or engine edit.
5. Home-volume source chapters in `~/chiral-bar-cobar`,
   `~/chiral-bar-cobar-vol2`, and `~/calabi-yau-quantum-groups`.
6. Adjacent math papers `~/igusa-cusp-form` and `~/topological-strings`
   when a modular, BKM, BCOV, or arithmetic trace claim crosses them.

## Escalation

Stop and report when a proof obligation cannot be discharged honestly,
when Vol IV disagrees with a source theorem in Vol I-III, when a compute
engine disagrees with manuscript prose, or when completing the task
requires overwriting work outside this repo or `~/latex-template`.
