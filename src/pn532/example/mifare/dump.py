# -*- coding: utf-8 -*-
"""
Mifare dump.

This example shows connecting to the PN532 and reading an M1
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

        # Configure PN532 to communicate with MiFare cards
        pn532.SAM_configuration()

        print("Waiting for RFID/NFC card to read from!")
        while True:
            # Check if a card is available to read
            uid = pn532.read_passive_target(timeout=0.5)
            print(".", end="")
            # Try again if no card is available.
            if uid is not None:
                break
        print("Found card with UID:", [hex(i) for i in uid])

        key_a = b"\xFF\xFF\xFF\xFF\xFF\xFF"
        # Now we try to go through all 16 sectors (each having 4 blocks)
        for i in range(64):
            try:
                pn532.mifare_classic_authenticate_block(
                    uid,
                    block_number=i,
                    key_number=nfc.MIFARE_CMD_AUTH_A,
                    key=key_a,
                )
                print(
                    i,
                    ":",
                    " ".join(
                        [
                            "%02X" % x
                            for x in pn532.mifare_classic_read_block(i)
                        ]
                    ),
                )
            except nfc.PN532Error as e:
                print(e.errmsg)
                break
    finally:
        GPIO.cleanup()


def main():
    """Main."""
    parse_mode("Mifare dump.", run)


if __name__ == "__main__":
    main()
