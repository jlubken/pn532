# -*- coding: utf-8 -*-
"""Example."""

from argparse import ArgumentParser
from contextlib import contextmanager

from RPi.GPIO import GPIO  # noqa: N814

from pn532 import (
    PN532_SPI,
    PN532_I2C,
    PN532_UART,
)


@contextmanager
def spi(debug=False, reset=20, cs=4):
    """Yield a spi device."""
    try:
        yield PN532_SPI(debug=debug, reset=reset, cs=cs)
    finally:
        GPIO.cleanup()


@contextmanager
def i2c(debug=False, reset=20, req=16):
    """Yield a i2c device."""
    try:
        yield PN532_I2C(debug=debug, reset=reset, req=req)
    finally:
        GPIO.cleanup()


@contextmanager
def uart(debug=False, reset=20):
    """Yield a uart device."""
    try:
        yield PN532_UART(debug=debug, reset=reset)
    finally:
        GPIO.cleanup()


def mode(value):
    """Mode."""
    modes = {
        "i2c": i2c,
        "spi": spi,
        "uart": uart,
    }
    return modes.get(value, spi)


def parse_mode(description, run):
    """Parse mode."""
    parser = ArgumentParser(description=description)
    parser.add_argument("mode", type=mode, default=spi)
    args = parser.parse_args()
    run(args.mode)
