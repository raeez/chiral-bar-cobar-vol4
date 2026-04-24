# Vol IV HZ-IV Coverage Progress

Canonical tracker for the realization campaign. Each campaign batch
records (claims targeted, decorators installed, upstream source audit,
open obligations) in chronological order beneath the installation
snapshot. Coverage is programme-wide: Vol IV counts its own native
theorems; the upstream gaps are Vol I, Vol II, Vol III decorator
installation.

## Installation Snapshot (2026-04-24)

| Volume  | ProvedHere Claims | Decorated | Coverage |
|---------|------------------:|----------:|---------:|
| Vol I   |              2275 |         0 |     0.0% |
| Vol II  |              1134 |         0 |     0.0% |
| Vol III |               283 |         2 |     0.7% |
| Vol IV  |                 3 |         3 |   100.0% |
| total   |              3695 |         5 |     0.14% |

The Vol IV count of 3 is the three self-realized anchors of the
realization programme chapter:

- `v4-thm:realization-programme-definition`
- `v4-thm:realization-existence-for-platonic-theorems`
- `v4-thm:realization-completeness-programme`

Each is backed by a decorator in
`compute/tests/test_realization_programme.py` with disjoint
`derived_from` and `verified_against` catalogs and a
`disjoint_rationale` recorded at decoration time. The tautological
self-test in the same file confirms the decorator's disjointness guard
fires on any overlap.

## Load-Bearing Infrastructure Note (2026-04-24)

The cross-volume disjointness check in
`compute/lib/realization_registry.py::_cross_volume_disjointness_ok`
was upgraded from advisory to enforcing on 2026-04-24. It now proceeds
through two channels: (i) opportunistic lookup of the Vol I HZ-IV
registry via `entries_for(claim)` and intersection of any upstream
entry's `derived_from` with the Vol IV `verified_against` set; (ii)
explicit `upstream_derived_from` keyword on `realization_decorator`
which the author supplies for Vol I/II/III claim labels so the check
fires even when the upstream test has not been imported in the current
pytest collection. The three native Vol IV decorators remain
unaffected: native `v4-` labels short-circuit the cross-volume check
by design (Vol IV's own claims do not have an upstream volume).

## Campaigns

### Campaign 0 — Installation (2026-04-24)

- Target: Vol IV self-realized theorems (three Platonic anchors).
- Decorators installed: 3.
- Build: `pdflatex` produces `main.pdf` at 142 pages; `pytest
  compute/tests/ -q` reports `4 passed in 0.01s` (three realization
  tests plus the tautological self-test).
- Status: complete.

## Open Campaigns

The realization programme's remaining 3690 claims are partitioned
across three upstream volumes. Each campaign below is a finite
enumeration whose termination is guaranteed by
`v4-thm:realization-completeness-programme`.

- Vol I (2275 claims): primary disjoint catalogs are
  Pridham-Toen-Vezzosi DAG VIII.2, Lurie HA 5.3
  (infinity,2)-centralizer theory, and the Vols I-III independent test
  infrastructure. Per the realization programme chapter's four-case
  analysis, each Vol I claim lives under one of: Platonic
  specialization (case 1), standard-landscape family verification
  (case 2), CY converged route (case 3), or 3D HT QFT inscription
  (case 4).
- Vol II (1134 claims): primary is Costello-Gwilliam factorization
  algebra on `R x C` for 3D HT QFT inscriptions; secondary includes
  Ben-Zvi-Francis-Nadler, Mok 2025, Schiffmann-Vasserot.
- Vol III (283 claims): primary is Hua-Keller N=1 Calabi-Yau
  categorification for CY converged routes; secondary includes the
  five conditional CY-C bridges tracked under AP-CY60.

Scope restrictions inherited from Vols I-III (admissible logarithmic
CKL lane, super-Yangian FM230 chain-level chiral coproduct, five of
six CY-C bridges awaiting convergence) are tracked as scope-restricted
entries per `v4-sec:scope-restrictions` and do not count toward the
Vol IV coverage denominator.

## Arithmetic Realization Branch (2026-04-24)

The Arithmetic Realization Branch inscribed 2026-04-24 is a parallel
realization track: the programme's five theorems (A, B, C, D, H) over
the Arakelov-compactified arithmetic curve
$\overline{\mathrm{Spec}\,\mathbb{Z}}$ in addition to $C/\mathbb{C}$.
Status distribution at inscription per CLAUDE.md: 5 Theorem, 4
Theorem-waiting, 7 Conjecture, 3 Heuristic, 9 Falsified. The branch
uses a five-tag system distinct from the Vols I-III ProvedHere/
Conjectured/Conditional/... tag system; it does not enter the
HZ-IV coverage denominator for Vols I-III and is tracked
separately.
