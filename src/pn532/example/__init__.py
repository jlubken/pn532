# -*- coding: utf-8 -*-
"""Example."""

from argparse import ArgumentParser

from pn532 import (
    PN532_SPI,
    PN532_I2C,
    PN532_UART,
)


def spi():
    """Return default spi device."""
    return PN532_SPI(debug=False, reset=20, cs=4)


def i2c():
    """Return default i2c device."""
    return PN532_I2C(debug=False, reset=20, req=16)


def uart():
    """Return default uart device."""
    return PN532_UART(debug=False, reset=20)


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
