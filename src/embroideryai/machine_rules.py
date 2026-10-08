"""Narrow, source-derived machine-family expansion rules.

Only mappings established by the public research narrative are represented.
Unsupported tags fail closed. These rules do not regenerate Region5 tuples.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


class MachineFamily(StrEnum):
    SCHIFFLI = "schiffli"
    ZTC = "ztc"


@dataclass(frozen=True, slots=True)
class ExpansionPair:
    primary: int
    secondary: int


_SOURCE_A5: dict[MachineFamily, ExpansionPair] = {
    MachineFamily.SCHIFFLI: ExpansionPair(primary=0x17, secondary=0x18),
    MachineFamily.ZTC: ExpansionPair(primary=0x06, secondary=0x07),
}


def expand_source_tag(machine: MachineFamily, source_tag_byte1: int) -> ExpansionPair:
    """Return the proven machine-specific pair for source byte ``0xA5``."""
    if source_tag_byte1 != 0xA5:
        raise LookupError("no public source-derived rule is established for this tag")
    try:
        return _SOURCE_A5[machine]
    except KeyError as error:
        message = "no public source-derived rule is established for this machine"
        raise LookupError(message) from error
