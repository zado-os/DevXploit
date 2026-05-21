# -*- coding: utf-8 -*-
"""DevXploit startup banner — modern terminal branding."""

from __future__ import (absolute_import, division, print_function)

from common.colors import (
    bannerblue,
    bannerblue2,
    W,
    G,
    end,
    msf_red,
    msf_dim,
)
from common.branding import (
    APP_NAME,
    APP_VERSION,
    EDITION,
    MAINTAINER,
    MAINTAINER_ALIAS,
    REPO_URL,
    APP_TAGLINE,
)
from modules.exploits.exploit_scanner import exploit_module_total


def _logo_lines():
    """Compact block logo — readable on 80-col terminals."""
    c1, c2, c3 = bannerblue, bannerblue2, W
    return [
        c1 + "  ╔══════════════════════════════════════════════════════════╗" + end,
        c1 + "  ║" + c2 + "  ▄▄▄▄▄  █▀▀▄ █░█░█ █░█ █▀▀▄ █▀▀ █▀▀▄ █▀▀ █▀▀▄ █▀▀ █▀▀  " + c1 + "║" + end,
        c1 + "  ║" + c2 + "  █░░█░█ █▄▄▀ ▀▄▀▄▀ ▀▄▀ █▄▄▀ █▀▀ █▄▄▀ █░░ █▄▄▀ █▀▀ █▀▀  " + c1 + "║" + end,
        c1 + "  ║" + c3 + "       ◈  " + G + APP_NAME + W + "  ·  " + c2 + EDITION + c3 + "  ◈              " + c1 + "║" + end,
        c1 + "  ╚══════════════════════════════════════════════════════════╝" + end,
    ]


def banner():
    total = exploit_module_total()
    print(msf_red + "       =[ %s v%s — %s ]=" % (APP_NAME, APP_VERSION, EDITION) + end)
    print(msf_dim + "+ -- --=[ %s ]=--" % APP_TAGLINE + end)
    print(msf_dim + "+ -- --=[ %d exploit modules loaded ]=--" % total + end)
    print("")
    for line in _logo_lines():
        print(line)
    print("")
    print(W + "  resource (repo) => " + G + REPO_URL + end)
    print(
        W + "  author          => "
        + G + MAINTAINER + W + " / " + MAINTAINER_ALIAS + end
    )
    print("")
