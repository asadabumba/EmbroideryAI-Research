from __future__ import annotations

import pytest

from embroideryai.region5 import (
    Region5Record,
    decode_region5_records,
    encode_region5_records,
    encode_uleb32,
)


@pytest.mark.parametrize(
    ("signed", "encoded", "width"),
    [
        (0, bytes.fromhex("00"), 1),
        (127, bytes.fromhex("7f"), 1),
        (128, bytes.fromhex("80 01"), 2),
        (16_383, bytes.fromhex("ff 7f"), 2),
        (16_384, bytes.fromhex("80 80 01"), 3),
        (0x7FFFFFFF, bytes.fromhex("ff ff ff ff 07"), 5),
        (-0x80000000, bytes.fromhex("80 80 80 80 08"), 5),
        (-1, bytes.fromhex("ff ff ff ff 0f"), 5),
    ],
)
def test_canonical_first_field(signed: int, encoded: bytes, width: int) -> None:
    record = encoded + bytes((0xA5, 0x5A))
    assert encode_uleb32(signed & 0xFFFFFFFF) == encoded
    assert decode_region5_records(record, 1) == [Region5Record(signed, 0xA5, 0x5A, width)]
    assert encode_region5_records([Region5Record(signed, 0xA5, 0x5A)]) == record


@pytest.mark.parametrize(
    ("payload", "message"),
    [
        (bytes.fromhex("80"), "truncated ULEB32"),
        (bytes.fromhex("80 00 aa bb"), "noncanonical/out-of-range"),
        (bytes.fromhex("80 80 80 80 80 00 aa bb"), "exceeds five bytes"),
        (bytes.fromhex("ff ff ff ff 1f aa bb"), "noncanonical/out-of-range"),
        (bytes.fromhex("01 aa"), "missing raw byte fields"),
        (bytes.fromhex("01 aa bb cc"), "trailing region5 bytes"),
    ],
)
def test_rejects_ambiguous_or_truncated_records(payload: bytes, message: str) -> None:
    with pytest.raises(ValueError, match=message):
        decode_region5_records(payload, 1)


@pytest.mark.parametrize("count", [-1, True, 1.0, "1"])
def test_rejects_invalid_record_count(count: object) -> None:
    with pytest.raises(ValueError, match="record count"):
        decode_region5_records(b"", count)  # type: ignore[arg-type]


def test_raw_byte_order_and_count_are_exact() -> None:
    records = [
        Region5Record(-1, 0x10, 0x20),
        Region5Record(127, 0x30, 0x40),
        Region5Record(128, 0x50, 0x60),
    ]
    encoded = encode_region5_records(records)
    assert encoded == bytes.fromhex("ff ff ff ff 0f 10 20 7f 30 40 80 01 50 60")
    assert [r.encoded_width for r in decode_region5_records(encoded, 3)] == [5, 1, 2]
