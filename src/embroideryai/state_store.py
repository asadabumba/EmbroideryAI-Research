"""Synthetic public model of recovered e4.2 StateStore insertion behavior.

The model captures the proven ``PutStateSetting`` storage key and exact-key
duplicate policy. It is not proprietary native code, an e4.2 writer model, or
a replacement for native machine-state generation.
"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class StateSetting:
    needle_position: int
    state_id: int
    value: int
    sequence: int

    def validate(self) -> None:
        if not 0 <= self.state_id <= 0xFF or not 0 <= self.value <= 0xFF:
            raise ValueError("state_id and value must be bytes")
        if self.sequence < 0:
            raise ValueError("sequence must be nonnegative")


def order_state_settings(settings: Iterable[StateSetting]) -> list[StateSetting]:
    """Model e4.2 storage order by position then ID.

    Newest entries precede older entries for exact equivalent keys. ``value``
    is deliberately absent from the ordering key. The public integer position
    is a sanitized stand-in for the native NeedlePos comparison.
    """
    materialized = list(settings)
    for setting in materialized:
        setting.validate()
    return sorted(
        materialized,
        key=lambda item: (item.needle_position, item.state_id, -item.sequence),
    )
