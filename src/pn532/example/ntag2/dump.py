# -*- coding: utf-8 -*-
"""
Dump ntag2.

This example shows connecting to the PN532 and reading an NTAG215
type RFID tag
"""

import pn532.pn532 as nfc
from pn532.example import parse_mode


def run(mode):
    """Run."""
    with mode() as pn532:
        ic, ver, rev, support = pn532.get_firmware_version()
        print(f"Found PN532 with firmware version: {ver}.{rev}")

        # Configure PN532 to communicate with NTAG215 cards
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

        # Now we try to go through all 135 pages of 4 bytes per page.
        for i in range(135):
            try:
                print(
                    i,
                    ":",
                    " ".join(
                        ["%02X" % x for x in pn532.ntag2xx_read_block(i)]
                    ),
                )
            except nfc.PN532Error as e:
                print(e.errmsg)
                break


def main():
    """Main."""
    parse_mode("Dump ntag2.", run)


if __name__ == "__main__":
    main()
