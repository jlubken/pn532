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
    extras_require={
        "all": TEST_REQUIRES,
        "test": TEST_REQUIRES,
    },
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.7.7,!=3.8.*,!=3.9.*",
    setup_requires=SETUP_REQUIRES,
    tests_require=TEST_REQUIRES,
    use_scm_version={"local_scheme": "dirty-tag"},
)
