# -*- coding: utf-8 -*-
"""
Get uid.

This example shows connecting to the PN532 with I2C (requires clock
stretching support), SPI, or UART. SPI is best, it uses the most pins but
is the most reliable and universally supported.
After initialization, try waving various 13.56MHz RFID cards over it!
"""

import RPi.GPIO as GPIO  # noqa: N814

from pn532.example import parse_mode


def run(mode):
    """Run."""
    try:
        pn532 = mode()

        ic, ver, rev, support = pn532.get_firmware_version()
        print("Found PN532 with firmware version: {0}.{1}".format(ver, rev))

        # Configure PN532 to communicate with MiFare cards
        pn532.SAM_configuration()

        print("Waiting for RFID/NFC card...")
        while True:
            # Check if a card is available to read
            uid = pn532.read_passive_target(timeout=0.5)
            print(".", end="")
            # Try again if no card is available.
            if uid is None:
                continue
            print("Found card with UID:", [hex(i) for i in uid])
    except Exception as e:
        print(e)
    finally:
        GPIO.cleanup()


def main():
    """Main."""
    parse_mode("Get uid.", run)


if __name__ == "__main__":
    main()
