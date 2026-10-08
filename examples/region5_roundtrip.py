"""Round-trip a synthetic Region5 table without proprietary input data."""

from embroideryai.region5 import Region5Record, decode_region5_records, encode_region5_records

records = [
    Region5Record(-1, 0x10, 0x20),
    Region5Record(127, 0x30, 0x40),
    Region5Record(128, 0x50, 0x60),
]
encoded = encode_region5_records(records)
decoded = decode_region5_records(encoded, len(records))

print(encoded.hex(" "))
for record in decoded:
    print(record)
