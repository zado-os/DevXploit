# -*- coding: utf-8 -*-
"""Resolve project paths (shell payloads) from any working directory."""

from __future__ import (absolute_import, division, print_function)

import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHELL_DIR = os.path.join(ROOT_DIR, "shell")

_FALLBACKS = {
    "VulnX.zip": "VulnX.php",
    "VulnX.gif": "VulnX.php",
    "Vulnx.gif": "VulnX.php",
}


def shell_path(filename):
    path = os.path.join(SHELL_DIR, filename)
    if os.path.isfile(path):
        return path
    alt = _FALLBACKS.get(filename)
    if alt:
        alt_path = os.path.join(SHELL_DIR, alt)
        if os.path.isfile(alt_path):
            return alt_path
    return path


def open_shell(filename, mode="rb"):
    return open(shell_path(filename), mode)
