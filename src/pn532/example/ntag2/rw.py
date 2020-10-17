# -*- coding: utf-8 -*-
"""
Write ntags2.

This example shows connecting to the PN532 and writing an NTAG215
type RFID tag
"""

import RPi.GPIO as GPIO  # noqa: N814

import pn532.pn532 as nfc

from pn532.example import parse_mode


def run(mode):
    """Run."""
    try:
        pn532 = mode()

        ic, ver, rev, support = pn532.get_firmware_version()
        print("Found PN532 with firmware version: {0}.{1}".format(ver, rev))

        # Configure PN532 to communicate with NTAG215 cards
        pn532.SAM_configuration()

        print("Waiting for RFID/NFC card to write to!")
        while True:
            # Check if a card is available to read
            uid = pn532.read_passive_target(timeout=0.5)
            print(".", end="")
            # Try again if no card is available.
            if uid is not None:
                break
        print("Found card with UID:", [hex(i) for i in uid])

        # Write block #6
        block_number = 6
        data = bytes([0x00, 0x01, 0x02, 0x03])

        try:
            pn532.ntag2xx_write_block(block_number, data)
            if pn532.ntag2xx_read_block(block_number) == data:
                print("write block %d successfully" % block_number)
        except nfc.PN532Error as e:
            print(e.errmsg)
    finally:
        GPIO.cleanup()


def main():
    """Main."""
    parse_mode("Write ntag2", run)


if __name__ == "__main__":
    main()
