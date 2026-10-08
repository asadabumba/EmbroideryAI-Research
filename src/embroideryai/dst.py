"""Sanitized, independent offline Tajima DST parser.

This public implementation uses documented command behavior and synthetic
fixtures. It is not proprietary native code and has no runtime dependency on
third-party embroidery software.
"""

from __future__ import annotations

from collections import Counter
from typing import Any


class DSTParser:
    HEADER_SIZE = 512
    UNIT_MM = 0.1

    def __init__(self, data: bytes):
        if not isinstance(data, bytes):
            raise TypeError("data must be bytes")
        if len(data) < self.HEADER_SIZE:
            raise ValueError(f"file is smaller than the {self.HEADER_SIZE}-byte header")
        self.data = data

    @staticmethod
    def _bit(value: int, position: int) -> int:
        return (value >> position) & 1

    def read_header(self) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for raw_line in self.data[: self.HEADER_SIZE].split(b"\r"):
            line = (
                raw_line.decode("ascii", errors="ignore")
                .replace("\x00", "")
                .replace("\x1a", "")
                .strip()
            )
            if ":" not in line:
                continue
            key, value = (part.strip() for part in line.split(":", maxsplit=1))
            if not key:
                continue
            try:
                result[key] = int("".join(value.split()))
            except ValueError:
                result[key] = value
        return result

    def decode_dx(self, b0: int, b1: int, b2: int) -> int:
        return (
            self._bit(b2, 2) * 81 - self._bit(b2, 3) * 81
            + self._bit(b1, 2) * 27 - self._bit(b1, 3) * 27
            + self._bit(b0, 2) * 9 - self._bit(b0, 3) * 9
            + self._bit(b1, 0) * 3 - self._bit(b1, 1) * 3
            + self._bit(b0, 0) - self._bit(b0, 1)
        )

    def decode_dy(self, b0: int, b1: int, b2: int) -> int:
        return (
            self._bit(b2, 5) * 81 - self._bit(b2, 4) * 81
            + self._bit(b1, 5) * 27 - self._bit(b1, 4) * 27
            + self._bit(b0, 5) * 9 - self._bit(b0, 4) * 9
            + self._bit(b1, 7) * 3 - self._bit(b1, 6) * 3
            + self._bit(b0, 7) - self._bit(b0, 6)
        )

    @staticmethod
    def command_type(b2: int) -> str:
        if b2 & 0xF3 == 0xF3:
            return "end"
        if b2 & 0xC3 == 0xC3:
            return "color_change"
        if b2 & 0x43 == 0x43:
            return "sequin_mode"
        if b2 & 0x83 == 0x83:
            return "jump"
        return "stitch"

    def parse(self) -> list[dict[str, Any]]:
        result: list[dict[str, Any]] = []
        x = y = 0
        sequin_mode = False
        body = self.data[self.HEADER_SIZE :]
        for index, offset in enumerate(range(0, len(body) - 2, 3)):
            b0, b1, b2 = body[offset : offset + 3]
            command_type = self.command_type(b2)
            if command_type == "sequin_mode":
                sequin_mode = not sequin_mode
            elif command_type == "jump" and sequin_mode:
                command_type = "sequin_eject"
            dx, dy = self.decode_dx(b0, b1, b2), self.decode_dy(b0, b1, b2)
            x, y = x + dx, y + dy
            result.append({
                "index": index,
                "offset": self.HEADER_SIZE + offset,
                "raw": bytes((b0, b1, b2)).hex(" "),
                "dx": dx,
                "dy": dy,
                "x": x,
                "y": y,
                "x_mm": round(x * self.UNIT_MM, 1),
                "y_mm": round(y * self.UNIT_MM, 1),
                "type": command_type,
            })
            if command_type == "end":
                break
        return result

    @staticmethod
    def count_types(commands: list[dict[str, Any]]) -> dict[str, int]:
        return dict(Counter(command["type"] for command in commands))
