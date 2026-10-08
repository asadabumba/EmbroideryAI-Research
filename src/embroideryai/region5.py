"""Deterministic codec for the proven physical Region5 record grammar.

This module implements physical encoding only. It does not infer native machine
semantics and is not a production embroidery writer.
"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Region5Record:
    """One physical Region5 record.

    ``first`` is a signed int32 encoded through its uint32 representation as
    canonical ULEB128. ``second`` and ``third`` are raw bytes. ``encoded_width``
    is populated by decoding and is ignored when encoding.
    """

    first: int
    second: int
    third: int
    encoded_width: int | None = None

    def validate(self) -> None:
        if not -(2**31) <= self.first <= 2**31 - 1:
            raise ValueError(f"first field is not an int32: {self.first}")
        if not 0 <= self.second <= 0xFF or not 0 <= self.third <= 0xFF:
            raise ValueError("second and third fields must be bytes")


def encode_uleb32(value: int) -> bytes:
    """Encode a uint32 using its unique canonical ULEB128 spelling."""
    if type(value) is not int or not 0 <= value <= 0xFFFFFFFF:
        raise ValueError(f"value is not a uint32: {value!r}")
    output = bytearray()
    while True:
        byte = value & 0x7F
        value >>= 7
        output.append(byte | (0x80 if value else 0))
        if not value:
            return bytes(output)


def _decode_uleb32(data: bytes, start: int, record_index: int) -> tuple[int, int]:
    position = start
    value = 0
    shift = 0
    for _ in range(5):
        if position >= len(data):
            raise ValueError(f"record {record_index}: truncated ULEB32")
        byte = data[position]
        position += 1
        value |= (byte & 0x7F) << shift
        if byte < 0x80:
            break
        shift += 7
    else:
        raise ValueError(f"record {record_index}: ULEB32 exceeds five bytes")

    spelling = data[start:position]
    if value > 0xFFFFFFFF or spelling != encode_uleb32(value):
        raise ValueError(f"record {record_index}: noncanonical/out-of-range ULEB32")
    return value, position


def decode_region5_records(data: bytes, count: int) -> list[Region5Record]:
    """Decode exactly ``count`` physical records and reject trailing data."""
    if type(count) is not int or count < 0:
        raise ValueError("record count must be a nonnegative integer")

    position = 0
    records: list[Region5Record] = []
    for record_index in range(count):
        start = position
        unsigned, position = _decode_uleb32(data, position, record_index)
        if position + 2 > len(data):
            raise ValueError(f"record {record_index}: missing raw byte fields")
        signed = unsigned if unsigned < 0x80000000 else unsigned - 0x100000000
        records.append(
            Region5Record(
                first=signed,
                second=data[position],
                third=data[position + 1],
                encoded_width=position - start,
            )
        )
        position += 2

    if position != len(data):
        raise ValueError(f"{len(data) - position} trailing region5 bytes after {count} records")
    return records


def encode_region5_records(records: Iterable[Region5Record]) -> bytes:
    """Encode physical records without assigning semantic meaning to fields."""
    output = bytearray()
    for record in records:
        record.validate()
        output.extend(encode_uleb32(record.first & 0xFFFFFFFF))
        output.extend((record.second, record.third))
    return bytes(output)
