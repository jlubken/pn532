# -*- coding: utf-8 -*-
"""
GPIO Write.

This example shows connecting to the PN532 and writing the GPIOs.
"""

import RPi.GPIO as GPIO  # noqa: N814

from pn532.example import parse_mode


def run(mode):
    """Run."""
    try:
        pn532 = mode()

        ic, ver, rev, support = pn532.get_firmware_version()
        print("Found PN532 with firmware version: {0}.{1}".format(ver, rev))

        print("Before:")
        p3, p7, i0i1 = pn532.read_gpio()
        for i in range(6):
            print("P3%d: %s" % (i, True if (p3 >> i & 1) else False))
        for i in [1, 2]:
            print("P7%d: %s" % (i, True if (p7 >> i & 1) else False))
        for i in [0, 1]:
            print("I%d: %s" % (i, True if (i0i1 >> i & 1) else False))
        # Same as pn532.write_gpio(p3=0b00010101)
        pn532.write_gpio("P30", True)
        pn532.write_gpio("P31", False)
        # pn532.write_gpio('P32', True)    # RESERVED (Must be HIGH)
        pn532.write_gpio("P33", False)
        # pn532.write_gpio('P34', True)    # RESERVED (Must be HIGH)
        pn532.write_gpio("P35", False)
        # Same as pn532.write_gpio(p7=0b00000100)
        pn532.write_gpio("P71", False)
        pn532.write_gpio("P72", True)
        print("After:")
        p3, p7, i0i1 = pn532.read_gpio()
        for i in range(6):
            print("P3%d: %s" % (i, True if (p3 >> i & 1) else False))
        for i in [1, 2]:
            print("P7%d: %s" % (i, True if (p7 >> i & 1) else False))
        for i in [0, 1]:
            print("I%d: %s" % (i, True if (i0i1 >> i & 1) else False))
        print("Note:")
        print(
            "1.  All Pins are set to the default state after hardware reset."
        )
        print("2.  P71/P72 are always HIGH in SPI mode.")
        print("3.  DO NOT reset the P32 and P34 pins.")
    finally:
        GPIO.cleanup()


def main():
    """Main."""
    parse_mode("Write GPIO.", run)


if __name__ == "__main__":
    main()