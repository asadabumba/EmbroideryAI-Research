# Region5 physical format

## Proven record grammar

A Region5 table contains a known record count from the surrounding document structure. Each record is:

```text
canonical ULEB32(uint32(int32 first_field))
+ raw u8 second_field
+ raw u8 third_field
```

The signed first field is converted to its two's-complement uint32 representation before ULEB encoding. Negative values therefore use canonical five-byte spellings.

## Examples

| Signed first field | Encoded bytes |
|---:|---|
| `0` | `00` |
| `127` | `7f` |
| `128` | `80 01` |
| `16384` | `80 80 01` |
| `-1` | `ff ff ff ff 0f` |
| `-2147483648` | `80 80 80 80 08` |

After the ULEB field, the next two bytes are raw and are not ULEB continuations.

## Decoder invariants

The public decoder rejects:

- truncated ULEB values;
- encodings longer than five bytes;
- noncanonical spellings;
- values outside uint32;
- missing raw bytes;
- invalid record counts;
- trailing bytes after the declared number of records.

## What this proves

This grammar proves physical parsing and encoding. It does not establish the semantic origin of the three fields or authorize generation of native records from arbitrary designs.
