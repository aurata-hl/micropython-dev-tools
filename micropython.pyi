# SPDX-License-Identifier: MIT OR CC0-1.0

from typing import Any, Callable, Optional, TypeVar

_N = TypeVar("_N", int, float)

alloc_emergency_exception_buf: Callable[[int], None]
heap_lock: Callable[[], None]
heap_locked: Callable[[], bool]
heap_unlock: Callable[[], None]
kbd_intr: Callable[[int], None]
schedule: Callable[[Callable[[Any], Any], Any], Any]
stack_use: Callable[[], None]


def const(number: _N) -> _N:
    return number


def mem_info(verbose: bool = False) -> None:
    pass


def opt_level(level: int = -1) -> Optional[int]:
    pass


def qstr_info(verbose: bool = False) -> None:
    pass
