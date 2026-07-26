"""Vol IV realization registry.

The registry records a pair of source lists for each realized claim.
For a native Vol IV claim, source disjointness is internal to the pair.
For a claim imported from Vol I, II, or III, the comparison list is also
tested against every upstream derivation list visible in the three
source registries, or against the explicit upstream list supplied by
the decorator.
"""

from __future__ import annotations

import importlib.util
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable

# Import upstream HZ-IV infrastructure by explicit file-path spec-loading.
# Vol IV has its own compute.lib package, so plain package imports would
# shadow the source volumes.
_UPSTREAM_REGISTRIES = {
    "Vol I": Path("/Users/raeez/chiral-bar-cobar"),
    "Vol II": Path("/Users/raeez/chiral-bar-cobar-vol2"),
    "Vol III": Path("/Users/raeez/calabi-yau-quantum-groups"),
}


def _load_upstream_registry(volume: str, root: Path):
    module_name = f"vol_iv_upstream_{volume.lower().replace(' ', '_')}"
    if module_name not in sys.modules:
        indep = root / "compute" / "lib" / "independent_verification.py"
        spec = importlib.util.spec_from_file_location(module_name, indep)
        if spec is None or spec.loader is None:
            raise ImportError(
                f"Vol IV realization registry requires {volume} "
                f"independent_verification.py at {indep}; spec load failed"
            )
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
    return sys.modules[module_name]


_upstream_modules = {
    volume: _load_upstream_registry(volume, root)
    for volume, root in _UPSTREAM_REGISTRIES.items()
}

_base_registry = _upstream_modules["Vol I"]
independent_verification = _base_registry.independent_verification
assert_sources_disjoint = _base_registry.assert_sources_disjoint
IndependentVerificationError = _base_registry.IndependentVerificationError


# ---------------------------------------------------------------------------
# Vol IV registry
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class RealizationEntry:
    """Record of one Vol IV realization registration."""

    claim: str
    source_volume: str
    test_qualname: str
    test_file: str
    derived_from: tuple[str, ...]
    verified_against: tuple[str, ...]
    disjoint_rationale: str


_VOL_IV_REGISTRY: list[RealizationEntry] = []


def realization_registry() -> list[RealizationEntry]:
    """Return a copy of the Vol IV realization registry."""
    return list(_VOL_IV_REGISTRY)


def clear_realization_registry() -> None:
    """Clear the registry. Used by the self-test to isolate state."""
    _VOL_IV_REGISTRY.clear()


def realized_claims() -> set[str]:
    """Labels of claims with at least one Vol IV realization entry."""
    return {e.claim for e in _VOL_IV_REGISTRY}


# ---------------------------------------------------------------------------
# Error
# ---------------------------------------------------------------------------


class RealizationError(IndependentVerificationError):
    """Raised when a Vol IV realization entry fails disjointness.

    Inherits from IndependentVerificationError (which inherits from
    AssertionError) so pytest reports it as a test failure at collection
    time, not as a harness crash.
    """


# ---------------------------------------------------------------------------
# Cross-volume disjointness
# ---------------------------------------------------------------------------


def _is_vol_iv_native(claim: str) -> bool:
    """True iff claim label is a Vol IV native label (prefix 'v4-')."""
    return claim.strip().lower().startswith("v4-")


def _cross_volume_disjointness_ok(
    claim: str,
    verified_against: Iterable[str],
    upstream_derived_from: Iterable[str] | None = None,
) -> tuple[bool, str]:
    """Check Vol IV verified_against is disjoint from Vols I-III
    derived_from for the same claim label.

    Returns (True, reason) on pass; (False, reason) on fail.

    For Vol IV native labels (prefix "v4-"), the check is skipped and
    returns (True, "native").

    For non-native (Vol I/II/III) labels, enforcement proceeds by two
    channels:
      1. Opportunistic: query each upstream HZ-IV registry via
         entries_for and intersect every upstream entry's derived_from
         with verified_against. Any overlap fails. If no upstream test
         module has been imported in the current process, this channel
         supplies no evidence.
      2. Explicit: if the decorator author passes upstream_derived_from,
         intersect it with verified_against directly. This channel is
         mandatory for load-bearing enforcement when the upstream
         registry may not be populated at collection time.

    At least one of the two channels must yield positive evidence
    (explicit upstream or an opportunistic hit) for the check to be
    classified as enforcing rather than vacuous.
    """
    if _is_vol_iv_native(claim):
        return True, "native"

    verified_set = {s.strip().lower() for s in verified_against}

    explicit_checked = False
    if upstream_derived_from is not None:
        explicit_checked = True
        upstream_set = {s.strip().lower() for s in upstream_derived_from}
        overlap = verified_set & upstream_set
        if overlap:
            return False, (
                f"Vol IV verified_against overlaps explicit upstream "
                f"derived_from at {sorted(overlap)!r}"
            )

    opportunistic_checked = False
    for volume, module in _upstream_modules.items():
        try:
            upstream_entries = module.entries_for(claim)
        except Exception:
            upstream_entries = []
        for entry in upstream_entries:
            opportunistic_checked = True
            upstream_set = {s.strip().lower() for s in entry.derived_from}
            overlap = verified_set & upstream_set
            if overlap:
                return False, (
                    f"Vol IV verified_against overlaps {volume} registered "
                    f"derived_from for claim={claim!r} at "
                    f"{sorted(overlap)!r}"
                )

    if explicit_checked or opportunistic_checked:
        return True, "enforced"

    # Neither channel yielded data. This is a genuine gap: the author
    # did not supply upstream_derived_from and no upstream registry has
    # imported the upstream test for this claim. A cross-volume
    # realization without upstream derivation evidence is vacuous, so it
    # must fail at decoration time.
    return False, "missing upstream derived_from evidence"


# ---------------------------------------------------------------------------
# Decorator
# ---------------------------------------------------------------------------


def realization_decorator(
    *,
    claim: str,
    source_volume: str,
    derived_from: Iterable[str],
    verified_against: Iterable[str],
    disjoint_rationale: str,
    upstream_derived_from: Iterable[str] | None = None,
) -> Callable:
    """Register a Vol IV realization pair for claim.

    Parameters match @independent_verification in Vol I with two
    additions: source_volume tracks which source volume the
    claim originally lives in (Vol I, Vol II, Vol III, or Vol IV for
    Vol IV's own theorems); upstream_derived_from is the explicit
    derivation catalog of the upstream volume's own inscription of
    the claim, supplied by the author so that cross-volume
    disjointness can be enforced even when the upstream test has not
    been imported in the current pytest collection.

    The decorator:
      1. Calls assert_sources_disjoint on derived_from vs
         verified_against (same as Vol I HZ-IV);
      2. Calls _cross_volume_disjointness_ok to confirm verified_against
         is also disjoint from the upstream volume's derived_from for
         the same claim label, using opportunistic source-registry
         lookup and the explicit upstream_derived_from argument;
      3. Registers a RealizationEntry in _VOL_IV_REGISTRY;
      4. Wraps the test with the Vol I @independent_verification
         decorator so the same Vol I-level registry also records it.
    """
    derived_tuple = tuple(derived_from)
    verified_tuple = tuple(verified_against)

    assert_sources_disjoint(derived_tuple, verified_tuple, claim=claim)

    ok, reason = _cross_volume_disjointness_ok(
        claim, verified_tuple, upstream_derived_from=upstream_derived_from,
    )
    if not ok:
        raise RealizationError(
            f"Vol IV realization for claim={claim!r} fails cross-volume "
            f"disjointness: {reason}. Choose verified_against disjoint "
            f"from the upstream volume's derived_from."
        )

    def decorator(test_fn: Callable) -> Callable:
        entry = RealizationEntry(
            claim=claim,
            source_volume=source_volume,
            test_qualname=test_fn.__qualname__,
            test_file=test_fn.__code__.co_filename,
            derived_from=derived_tuple,
            verified_against=verified_tuple,
            disjoint_rationale=disjoint_rationale,
        )
        _VOL_IV_REGISTRY.append(entry)

        # Also register against the base HZ-IV registry so existing
        # coverage queries see this verification.
        wrapped = independent_verification(
            claim=claim,
            derived_from=derived_tuple,
            verified_against=verified_tuple,
            disjoint_rationale=disjoint_rationale,
        )(test_fn)
        return wrapped

    return decorator


# ---------------------------------------------------------------------------
# Coverage query
# ---------------------------------------------------------------------------


def coverage_snapshot() -> dict[str, int]:
    """Coverage snapshot: number of Vol IV realization entries per source volume.

    Returns a dictionary mapping source_volume -> entry count.
    """
    snapshot: dict[str, int] = {}
    for entry in _VOL_IV_REGISTRY:
        snapshot[entry.source_volume] = snapshot.get(entry.source_volume, 0) + 1
    return snapshot
