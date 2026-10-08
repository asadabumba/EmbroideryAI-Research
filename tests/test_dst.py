from embroideryai.dst import DSTParser


def _dst_file(*commands: bytes) -> bytes:
    header = b"LA:SYNTHETIC\rST:3\rCO:0\r\x1a"
    return header.ljust(DSTParser.HEADER_SIZE, b" ") + b"".join(commands)


def test_synthetic_dst_coordinates_and_end() -> None:
    data = _dst_file(
        bytes((0x81, 0x00, 0x03)),
        bytes((0x81, 0x00, 0x03)),
        bytes((0x00, 0x00, 0xF3)),
    )
    commands = DSTParser(data).parse()
    assert [(row["x"], row["y"], row["type"]) for row in commands] == [
        (1, 1, "stitch"),
        (2, 2, "stitch"),
        (2, 2, "end"),
    ]


def test_header_and_command_counts() -> None:
    parser = DSTParser(_dst_file(bytes((0, 0, 0xF3))))
    assert parser.read_header()["LA"] == "SYNTHETIC"
    assert parser.count_types(parser.parse()) == {"end": 1}