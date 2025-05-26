# SPDX-License-Identifier: MIT OR CC0-1.0

from typing import Any, Callable, Dict, Optional, Self, Tuple, Union

# Type aliases:

# A value which converts to bool
_Bool = Union[bool, int, float]
# An object which support the buffer API
_Buffer = Any
# An 8-tuple used by the RTC functions
_DatetimeTuple = Tuple[int, int, int, int, int, int, int, int]


PWRON_RESET = 1
WDT_RESET = 3


class ADC:
    CORE_TEMP = 4

    def __init__(self, pin: int) -> None:
        pass

    def read_u16(self) -> int:
        return 0

    def read_uv(self) -> int:
        return 0


class Pin:
    IN = 0
    OUT = 1
    OPEN_DRAIN = 2

    PULL_UP = 1
    PULL_DOWN = 2

    def __init__(
            self,
            id: int,
            mode: int = -1,
            pull: Optional[int] = None,
            value: Optional[int] = None,
            drive: int = IN,
            alt: int = -1) -> None:
        pass

    def value(self, v: Optional[int] = None) -> int:
        return 0


class Signal:
    def __init__(self, pin: Pin, invert: bool = False) -> None:
        pass

    def value(self, x: Optional[_Bool] = None) -> Optional[int]:
        pass

    def on(self) -> None:
        pass

    def off(self) -> None:
        pass


class PWM:
    def __init__(
        self,
        pin: Pin,
        freq: int = 0,
        duty_u16: int = 32768
    ) -> None:
        pass

    def freq(self, f: int = 0) -> Optional[int]:
        return 0

    def duty_u16(self, f: int = 0) -> Optional[int]:
        return 0

    def deinit(self) -> None:
        pass


class I2C:
    def __init__(
            self,
            id: int,
            scl: int,
            sda: int,
            freq: int = 400000,
            timeout: int = 50000) -> None:
        pass

    def deinit(self) -> None:
        pass

    def scan(self) -> None:
        pass

    def start(self) -> None:
        pass

    def stop(self) -> None:
        pass

    def readinto(self, buf: _Buffer, nack: bool = True) -> int:
        return 0

    def write(self, buf: _Buffer) -> int:
        return 0

    def readfrom(self, addr: int, nbytes: int, stop: bool = True) -> bytes:
        return b''

    def readfrom_into(
            self, addr: int, buf: _Buffer, stop: bool = True) -> int:
        return 0

    def writeto(
            self, addr: int, buf: _Buffer, stop: bool = True) -> int:
        return 0

    def readfrom_mem(
            self, addr: int, memaddr: int, nbytes: int,
            addrsize: int = 8) -> bytes:
        return b''

    def readfrom_mem_into(
            self, addr: int, memaddr: int, buf: _Buffer,
            addrsize: int = 8) -> None:
        pass

    def writeto_mem(
            self, addr: int, memaddr: int, buf: _Buffer,
            addrsize: int = 8) -> None:
        pass


class SPI:
    LSB = 0
    MSB = 1

    def __init__(
        self,
        id: int = 0,
        baudrate: int = 500000,
        polarity: int = 0,
        phase: int = 0,
        bits: int = 0,
        firstbit: int = MSB,
        sck: Optional[Pin] = None,
        mosi: Optional[Pin] = None,
        miso: Optional[Pin] = None
    ) -> None:
        pass

    def init(
        self,
        baudrate: int = 500000,
        polarity: int = 0,
        phase: int = 0,
        bits: int = 0,
        firstbit: int = MSB,
        sck: Optional[Pin] = None,
        mosi: Optional[Pin] = None,
        miso: Optional[Pin] = None
    ) -> None:
        pass

    def deinit(self) -> None:
        pass

    def read(self, nbytes: int, write: int = 0x00) -> bytes:
        return b''

    def readinto(self, buf: _Buffer, write: int = 0x00) -> None:
        pass

    def write(self, buf: _Buffer) -> None:
        pass

    def write_readinto(self, buf: _Buffer, read_buf: _Buffer) -> None:
        pass


class UART:
    CTS = 1
    RTS = 2

    def __init__(
        self,
        id: int,
        baudrate: int = 9600,
        bits: int = 8,
        parity: Optional[bool] = False,
        stop: int = 1,
        tx: Optional[Pin] = None,
        rx: Optional[Pin] = None
    ) -> None:
        pass

    def init(
        self,
        baudrate: int = 9600,
        bits: int = 8,
        parity: Optional[bool] = False,
        stop: int = 1,
        rts: Optional[Pin] = None,
        cts: Optional[Pin] = None,
        txbuf: int = -1,
        rxbuf: int = -1,
        timeout: int = -1,
        timeout_char: int = -1,
        flow: int = 0
    ) -> None:
        pass

    def deinit(self) -> None:
        pass

    def any(self) -> bool:
        return False

    def read(self, nbytes: int = -1) -> bytes:
        return b''

    def readinto(
        self,
        buf: _Buffer,
        nbytes: int = -1
    ) -> Optional[int]:
        return None

    def readline(self) -> Optional[bytes]:
        return None

    def write(self, buf: _Buffer) -> Optional[int]:
        return None

    def sendbreak(self) -> None:
        pass

    def flush(self) -> None:
        pass

    def txdone(self) -> bool:
        return True


class RTC:
    def __init__(self, id: int = 0) -> None:
        pass

    def datetme(
        self, t: Optional[_DatetimeTuple] = None
    ) -> Optional[_DatetimeTuple]:
        return None


class Timer:
    ONE_SHOT = 0
    PERIODIC = 1

    def __init__(self, id: int = 0) -> None:
        pass

    def init(
        self,
        callback: Callable[[Self], None],
        mode: int = PERIODIC,
        freq: int = -1,
    ) -> None:
        pass

    def deinit(self) -> None:
        pass


class WDT:
    def __init__(self, id: int = 0, timeout: int = 5000) -> None:
        pass

    def feed(self) -> None:
        pass


SoftI2C: I2C  # Re-use the type
SoftSPI: SPI  # Re-use the type

# TODO: class I2S
# TODO: class USBDevice


bitstream: Callable[
    [Pin, int, Tuple[int, int, int, int], _Buffer], None]
bootloader: Callable[[], None]
# Undocumented: dht_readinto
disable_irq: Callable[[], None]
enable_irq: Callable[[], None]
# Unavailable: hard_reset: Callable[[], None]
idle: Callable[[], None]
mem8: Dict[int, int]
mem16: Dict[int, int]
mem32: Dict[int, int]
reset: Callable[[], None]
reset_cause: Callable[[], int]
soft_reset: Callable[[], None]
time_pulse_us: Callable[[Pin, int, int], int]
unique_id: Callable[[], bytes]


def deepsleep(time_ms: int = -1) -> None:
    pass


def lightsleep(time_ms: int = -1) -> None:
    pass


def freq(hz: Optional[int] = None) -> Optional[int]:
    pass
