# -*- coding: utf-8 -*-
"""Setup"""

from setuptools import find_packages, setup

INSTALL_REQUIRES = (
    "pip>=20.2.3",
    "RPi.GPIO>=0.7.0",
    "setuptools>=50.3.0",
    "wheel>=0.35.1",
)

SETUP_REQUIRES = ("setuptools_scm[toml]>=4.1.2",)

TEST_REQUIRES = (
    "black",
    "pre-commit",
)

setup(
    entry_points={
        "console_scripts": [
            "pn532.mifare.dump = pn532.example.mifare.dump:main",
            "pn532.mifare.rw = pn532.example.mifare.rw:main",
            "pn532.ntag2.dump = pn532.example.ntag2.dump:main",
            "pn532.ntag2.rw = pn532.example.ntag2.rw:main",
            "pn532.get.uid = pn532.example.uid:main",
            "pn532.gpio.read = pn532.example.gpio.read:main",
            "pn532.gpio.write = pn532.example_gpio.write:main",
            "pn532.uart.hex = pn532.example.uart.hex:main",
        ]
    },
    extras_require={
        "all": TEST_REQUIRES,
        "test": TEST_REQUIRES,
    },
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.7.3,!=3.8.*,!=3.9.*",
    setup_requires=SETUP_REQUIRES,
    tests_require=TEST_REQUIRES,
    use_scm_version={"local_scheme": "dirty-tag"},
)
