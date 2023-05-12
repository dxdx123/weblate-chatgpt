#!/usr/bin/env python

# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Setup script for customization demo."""

from setuptools import setup, find_packages

setup(
    name="weblate_holdon",
    version="0.0.1",
    author="Your name",
    author_email="yourname@example.com",
    description="holdOn plugin for Weblate",
    license="GPLv3+",
    keywords="Weblate holdon plugin",
    packages=["weblate_holdon"],
)
