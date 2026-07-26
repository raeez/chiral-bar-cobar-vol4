# Vol IV HZ-IV Coverage

This note records realized claims, not intended claims. A claim is counted
only when a Vol IV realization decorator has been imported and its
`derived_from` and `verified_against` lists are disjoint.

## Current Imported Registry

As of the present compute import, `coverage_snapshot()` gives:

| Source volume | Decorated claims |
|---|---:|
| Vol IV | 8 |

The eight imported Vol IV labels are:

- `v4-thm:realization-formalism-definition`
- `v4-thm:realization-existence-for-platonic-theorems`
- `v4-thm:realization-completeness-programme`
- `v4-arith:w6-h:thm:c-ar-residue`
- `v4-arith:w6-h:thm:li-coefficients`
- `v4-arith:w6-h:thm:N-T-rvm`
- `v4-arith:w6-h:thm:first-three-zeros`
- `v4-arith:w6-h:thm:psi-quarter`

The realization criterion in
`chapters/realization/realization_programme.tex` is not an enumeration
theorem. Membership in the non-degenerate locus does not realize a
claim. A Vol I, II, or III claim is realized only when an explicit pair
`(d,e)` is present, the comparison source is disjoint from the upstream
derivation source, and the expected value is obtained independently of
the formula being tested.

## Registry Invariant

For a native `v4-` claim, Vol IV checks disjointness of its own two
source lists. For an imported Vol I-III claim, Vol IV also checks the
comparison list against upstream derivation sources. The registry loads
the independent-verification modules from:

- `/Users/raeez/chiral-bar-cobar`
- `/Users/raeez/chiral-bar-cobar-vol2`
- `/Users/raeez/calabi-yau-quantum-groups`

If no upstream registry entry is visible, the decorator must carry
`upstream_derived_from`; otherwise the imported realization fails at
decoration time.

## Arithmetic Constant Entries

The five arithmetic entries are finite numerical realizations. Their
scope is exactly the recorded constants:

- `c^{Ar}=2`
- `lambda_1,...,lambda_4`
- `N(100)` and `N(1000)`
- the first three zeta zero ordinates
- `psi(1/4)`

The `N(T)` entry is a finite comparison at `T=100,1000`: `mpmath.nzeros`
supplies the contour count, while the von Mangoldt leading term rounded
to the nearest integer agrees at those two heights. It is not a theorem
that the leading term alone computes `N(T)` at arbitrary height.
