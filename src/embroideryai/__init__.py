"""Public, offline EmbroideryAI research utilities."""

from .evidence import EvidenceLevel, EvidenceRecord
from .machine_rules import ExpansionPair, MachineFamily, expand_source_tag
from .region5 import Region5Record, decode_region5_records, encode_region5_records
from .state_store import StateSetting, order_state_settings

NATIVE_SEMANTICS_PROVEN = False
PRODUCTION_AUTHORITY = False

__all__ = [
    "EvidenceLevel",
    "EvidenceRecord",
    "ExpansionPair",
    "MachineFamily",
    "NATIVE_SEMANTICS_PROVEN",
    "PRODUCTION_AUTHORITY",
    "Region5Record",
    "StateSetting",
    "decode_region5_records",
    "encode_region5_records",
    "expand_source_tag",
    "order_state_settings",
]
