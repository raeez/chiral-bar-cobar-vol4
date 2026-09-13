# CoHA and Euler statement repairs: candidate 003

This candidate repairs the two blocking statements in the complete candidate 002 review. The complete latest return was read from its completed task status before manuscript editing. Its bounded Euler, trace, Hall, PBW, normalization, potential, primary-source and render checks are retained as evidence for the unchanged mathematics; they do not accept the defective 002 statements or certify the whole book.

Only chapters/arithmetic/15b_coha_euler_comparison.tex changes. All other manuscript files from candidate 002 are byte-identical, including the accepted integral-centre proof 15a. Frozen 001 and frozen 002 sources, evidence, inputs, diffs, renders and PDFs remain untouched.

The three source hunks are:

1. The edgeless-CoHA exclusion requires a nonempty finite prime set. The text explicitly computes the empty case: its only representation is zero, and both the CoHA and the prime monoid algebra are Q.
2. The ordinary polynomial-algebra conclusion requires the generator tower to supercommute and to be even. It no longer permits evenness by itself to imply multiplicativity. The preceding if-and-only-if criterion and its universal-property proof are unchanged.
3. The immediate closing sentence restricts the edgeless exclusion to a nonempty prime set.

The primary comparisons and all calculations remain those frozen in candidate 002. In particular, a PBW object isomorphism does not supply actual supercommutativity, and a nonzero even Hall commutator is compatible with even grading. The arithmetic Hochschild-trace-to-BPS realization, compatible prime-set transitions, and trace comparison remain separate open constructions.

No new mathematical test was introduced for these statement repairs. The prior exact calculation scripts/results and primary PDFs remain available through the protected candidate 002 manifest. The build and source-identity checks verify the changed candidate itself.

Build from the worktree root:

```sh
python3 reports/research/MINING-2026-09-13/coha-euler-003/build_vol4.py 1
```

The isolated build directory was initialized with the frozen 002 reference/contents state. The build pins the absolute actual book entrypoint, uses worktree-first TEXINPUTS and the canonical shared template, and records the actual compiler inputs. The first pass produced 1044 pages, zero undefined references, no rerun request, and no overfull box in the changed source. The 156 pre-existing overfull boxes elsewhere remain outside scope.

The render manifest compares all 20 affected or adjacent pages from candidate 002 against new 003. Changed rasters and their transitions are visually inspected before freezing. The freeze records full-source inputs, actual compiler inputs, source and phase diffs, the exact PDF, and rendered pages. This is a candidate for renewed independent review, not acceptance or publication.

No staging, commit, merge, push, publication, shared-checkout change or shared-template change occurs. All writes are within the assigned isolated worktree.
