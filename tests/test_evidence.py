import json
from pathlib import Path

import pytest

from embroideryai.evidence import EvidenceLevel, EvidenceRecord


def test_synthetic_provenance_fixture_uses_explicit_levels() -> None:
    path = Path(__file__).parent / "fixtures" / "synthetic_provenance.json"
    rows = json.loads(path.read_text(encoding="utf-8"))
    assert {row["level"] for row in rows} == {
        "PROVEN",
        "STRONGLY SUPPORTED",
        "PARTIAL",
        "HYPOTHESIS",
        "NOT PROVEN",
        "INCONCLUSIVE",
    }


def test_proven_record_requires_scope_or_limitations() -> None:
    record = EvidenceRecord("bounded codec grammar", EvidenceLevel.PROVEN, ("synthetic-test",))
    with pytest.raises(ValueError, match="limitations"):
        record.validate()


def test_scoped_proven_record_is_valid() -> None:
    EvidenceRecord(
        "bounded codec grammar",
        EvidenceLevel.PROVEN,
        ("synthetic-test",),
        ("physical encoding only",),
    ).validate()
