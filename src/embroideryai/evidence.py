"""Public evidence vocabulary for scoped, fail-closed research claims.

This is an independent provenance model, not a representation of proprietary
native classes or runtime state.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


class EvidenceLevel(StrEnum):
    PROVEN = "PROVEN"
    STRONGLY_SUPPORTED = "STRONGLY SUPPORTED"
    PARTIAL = "PARTIAL"
    HYPOTHESIS = "HYPOTHESIS"
    NOT_PROVEN = "NOT PROVEN"
    INCONCLUSIVE = "INCONCLUSIVE"


@dataclass(frozen=True, slots=True)
class EvidenceRecord:
    claim: str
    level: EvidenceLevel
    provenance: tuple[str, ...]
    limitations: tuple[str, ...] = ()

    def validate(self) -> None:
        if not self.claim.strip():
            raise ValueError("claim must not be empty")
        if not self.provenance:
            raise ValueError("at least one provenance item is required")
        if self.level is EvidenceLevel.PROVEN and not self.limitations:
            raise ValueError("PROVEN claims must state their scope or limitations")
