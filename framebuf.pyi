# SPDX-License-Identifier: MIT OR CC0-1.0

import array
from typing import Any, Optional

# An object with buffer API
Buffer = Any


GS2_HMSB = 5
GS4_HMSB = 2
GS8 = 6
MONO_HLSB = 3
MONO_HMSB = 4
MONO_VLSB = 0
MVLSB = 0
RGB565 = 1


class FrameBuffer:
    def __init__(
            self,
            buffer: Buffer,
            width: int, height: int,
            format: int,
            stride: int = -1) -> None:
        pass

    def fill(self, c: int) -> None:
        pass

    def pixel(self, x: int, y: int, c: int = -1) -> int:
        return -1

    def hline(self, x: int, y: int, w: int, c: int) -> None:
        pass

    def vline(self, x: int, y: int, h: int, c: int) -> None:
        pass

    def line(self, x1: int, y1: int, x2: int, y2: int, c: int) -> None:
        pass

    def rect(
            self,
            x: int, y: int, w: int, h: int, c: int,
            f: bool = False) -> None:
        pass

    def ellipse(
            self,
            x: int, y: int, xr: int, yr: int, c: int,
            f: bool = False, m: int = 3) -> None:
        pass

    def poly(
            self, x: int, y: int, coords: array.array[int],
            c: int, f: bool = False) -> None:
        pass

    def text(
            self, s: str, x: int, y: int,
            c: int = 1) -> None:
        pass

    def scroll(
            self, xstep: int, ystep: int) -> None:
        pass

    def blit(
            self, fbuf: FrameBuffer,
            x: int, y: int, key: int = -1,
            palette: Optional[FrameBuffer] = None) -> None:
        pass
