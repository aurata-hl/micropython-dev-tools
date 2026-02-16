# SPDX-License-Identifier: MIT OR CC0-1.0

from typing import Callable

time: Callable[[], int]

ticks_ms: Callable[[], int]
ticks_us: Callable[[], int]

sleep_ms: Callable[[int], None]
sleep_us: Callable[[int], None]

ticks_add: Callable[[int, int], int]
ticks_diff: Callable[[int, int], int]
