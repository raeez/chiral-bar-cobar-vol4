# Native Vol. IV arithmetic consumer construction

This is a constructed candidate, awaiting fresh review of its exact bytes.
It is not a whole-native acceptance, an arithmetic-primary realization, or a proof of RH.

The source root is `research-candidates/vol4_prime026/native004/` in the assigned worktree.
The report root is `reports/research/vol4_prime026/native004/`.
The complete source freeze contains 129 files. Its aggregate is
`2dfffa30781c42a8335e4c2d92cbbc624cb4410f9648045d559b0310d90aa51c`.
`source-freeze.json` states the aggregate encoding and every file hash.
`native.patch` records the full native delta against the preceding frozen construction.
The prior construction and its partial records remain unchanged.

## Mathematical constructions

1. The finite-prime pairing on each support interval is a bounded self-adjoint sum of compressed translations. The exact comparison uses its absolute value and sign. Compression makes these forms compatible on the full compact test algebra.
2. A two-dimensional translated-bump space has both signs. Its positive line has an explicit norm-preserving map to an ordinary L2 line. Its negative line excludes a positive Hilbert representation of the full finite-prime form.
3. Zero evaluation maps the compact test algebra into the Hilbert space indexed by actual zero occurrences. Reflection across the critical line defines a signed Hermitian form. This gives the complete Weil comparison with both polar moments, the gamma sign, and the prime weights retained. Its translation and differential intertwiners are explicit.
4. The normal diagonal zero operator has a Hilbert–Schmidt inverse. The normalized genus-one determinant is `(1/2) exp(Bs) det_2(1-s Theta_Z^-1)`, with `B=-1-gamma/2+log(4pi)/2`. Its value and logarithmic derivative at zero remove the exponential ambiguity. No unsupported complex-power prescription remains in Ch56's determinant proof.
5. Ch61 distinguishes the auxiliary density `g=Re psi+log pi` from the arithmetic density `k=log pi-Re psi`. Their quadratic forms differ by `2 log pi ||f||²` and a sign. Compact dilation and modulation examples determine both gamma signs. The full Weil inequality retains the exact correction.
6. Ch74 constructs a space of rapidly exponentially decaying tests, proves compact-test density and continuity of every explicit-formula term, and derives the Gaussian error-function series with a summable analytic error bound. The normalized gamma average strictly decreases. Its positive range is below its unique threshold.
7. Ch73 constructs the complete de Branges sampling map under the real-zero hypothesis. The proof includes the kernel expansion, boundary limits, orthonormality, completeness, and the exact `pi m_gamma` weights. Gaussian Fourier transforms fail the direct Hardy-space condition. Sampling multiplicity weights do not produce determinant eigenvalue multiplicities.
8. Ch79 gives the exact sign dictionary and the subtracted time-variable gamma integral. Its Poisson identity uses the Fourier transform. A compact two-bump example refutes replacing that transform by reciprocal substitution.
9. Ch90 proves the continuous-versus-atomic spectral obstruction, the correctly typed conjugacy formula, and the actual zero exponential on the occurrence carrier. The exponential counting pushforward is not locally finite. The ordinary multiplicative product fails its factor-to-one condition. Arithmetic purity concerns `F_Z`; continuous scaling purity is unconditional.
10. Ch60's direct positive-closure claims and compact-test criterion are corrected. Ch87 now names the constructed signed zero carrier and its map instead of asserting an unspecified adele-class L2 construction. Ch98 uses the actual compact/Fourier algebra isomorphism and separates arithmetic purity from continuous scaling purity.

The map to the zero carrier uses the zero divisor as input. It is not a construction from the arithmetic primary sector. The de Branges positive comparison assumes real zeros before constructing its Hilbert norm. The exact finite-prime negative square excludes the proposed unrestricted positive transfer, but does not refute every separately defined restricted modular subspace.

## Preserved accepted arguments

The complete Ch57 and Ch80 source files remain byte-identical to the earlier bounded PASS:

- Ch57 SHA-256 `959caa71b54ef6d6041f98caeb8ff6193f46d4646afcc07fb293244db36a2422`.
- Ch80 SHA-256 `a223804ab1fc543234f72a7c0eee4e35a1b51f22c72fd3d061e38238f205c058`.

The signed comparison is a separate included source following Ch57. Identity of preserved bytes is a propagation check, not a new mathematical review.

## Remaining native defects

Whole-native closure remains incomplete. The source copy preserves additional consumers requiring mathematical repair:

- Ch71 and Ch72 continue to attach arithmetic gamma positivity to the auxiliary high-frequency condition. Ch71 also requires a review of its claimed Stirling remainder and threshold proof.
- Ch75 continues to infer gamma positivity from its integral-energy bound. Its asserted strict relation between restricted cones requires an actual construction on the stated test carrier.
- Ch76 retains the auxiliary-kernel identification in its Mellin–Barnes argument.
- Ch77's use of pointwise Hadamard logarithmic derivatives as a Weil kernel requires a carrier and pole analysis.
- Ch78 uses the old integral kernel and calls a map to a test-space dual a self-adjoint Hilbert operator without a complete domain construction.
- Ch89 and Ch94 still propagate the former surface/scaling and arithmetic-purity identifications. The continuous operator cannot replace the zero-occurrence operator in the RH-equivalent purity statement.
- Existing production-style tables and source-independence narration elsewhere in the native manuscript remain outside a bounded firewall verdict. Ch60 still contains such inherited material. The complete native book also retains layout overflows.

`unchanged-consumer-references.json` records every detected reference from unchanged native files to changed-source labels. `residual-consumer-anchors.json` retains exact lines for the families above. These inventories identify investigation points; a matching line is not itself a mathematical verdict.

## Evidence and reproducibility

Run from the assigned worktree:

```
/opt/homebrew/bin/python3 reports/research/vol4_prime026/native004/calculations.py
python3 reports/research/vol4_prime026/native004/build.py reader
python3 reports/research/vol4_prime026/native004/build.py native
/opt/homebrew/bin/python3 reports/research/vol4_prime026/native004/render.py reader
/opt/homebrew/bin/python3 reports/research/vol4_prime026/native004/render.py native
```

The reader has 67 pages, zero undefined references, zero duplicate labels, and zero overfull boxes. Its PDF SHA-256 is `6d864168bab186ee4f206dafc9c81d47568f97230bac9641b2e1e61c9500977c`.

The native build has 1032 pages, zero undefined references, and zero duplicate labels. It retains 139 horizontal and three vertical overfull boxes. Its PDF SHA-256 is `5c23e0c02e9f13a9b89ec34ee40aae269997ef365bb309f61452f2b2ef94fcca`.

The final render check covers 26 reader pages and 30 native pages. New mathematical passages have no clipping or overlap. The native-wide layout and manuscript-boundary gates remain open.

Both builds disable shell escape and confine outputs to this report directory. The builder records commands, environments, return codes, hashes, and every compiler input/output. The source freeze is checked against the final compiler inputs. The native template is a frozen byte copy of the preceding build input. No shared template was changed.

The exact rational matrix computation verifies the two finite-prime signs after suppressing their positive scalar factor. High-precision Gaussian quadrature checks the independently derived error-function series within the proved tail bound. Decimal roots and quadrature are diagnostic. The TeX supplies every general sign, convergence, and comparison argument.

An independent first stage was frozen before receiving the writer's formulas. The later exchange supplied the full de Branges proof for semantic integration. `primary-evidence.json` records that ordering and the source hashes. This constructive lane is not an independent acceptance review of the integrated native bytes.

The first reader/native attempt exposed memoir's rejection of the legacy `rm` font command. A subsequent native attempt exposed duplicate equation labels. Both were repaired; the failed logs remain under `failed-build001/`. The final native comma-separated reference also required splitting because the inherited reference macro did not resolve a label list. No failed check was treated as a pass.

Required mathematical runtime: gpt-6-astra with ultra reasoning. Independent observed runtime metadata were unavailable, so the requirement remains unverified, with no observed mismatch. No formal proof assistant was used. No novelty claim is made.

There was no staging, commit, push, central PDF write, application opening, or change outside the two assigned directories. Root retains review, integration, and publication authority.
