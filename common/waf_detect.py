# -*- coding: utf-8 -*-
"""WAF / CDN / security plugin fingerprinting."""

from __future__ import (absolute_import, division, print_function)

import re
import requests
from requests.exceptions import RequestException

SIGNATURES = [
    ("Cloudflare", re.compile(r"cloudflare|cf-ray|__cf_bm", re.I)),
    ("Wordfence", re.compile(r"wordfence|wfvt_", re.I)),
    ("Sucuri", re.compile(r"sucuri|cloudproxy", re.I)),
    ("Akamai", re.compile(r"akamai|ak_bmsc", re.I)),
    ("Imperva", re.compile(r"incapsula|visid_incap", re.I)),
    ("ModSecurity", re.compile(r"mod_security|modsecurity", re.I)),
    ("LiteSpeed", re.compile(r"litespeed|x-litespeed-cache", re.I)),
    ("AWS WAF", re.compile(r"x-amzn|awselb", re.I)),
    ("Barracuda", re.compile(r"barracuda", re.I)),
    ("F5 BIG-IP", re.compile(r"BigIP|F5", re.I)),
]


def detect_waf(url, headers=None, timeout=12):
    found = []
    try:
        r = requests.get(
            url.rstrip("/"),
            headers=headers or {},
            verify=False,
            timeout=timeout,
            allow_redirects=True,
        )
        blob = " ".join(
            str(r.headers.get(h, "")) for h in r.headers
        ) + " " + (r.text or "")[:8000]
        for name, pattern in SIGNATURES:
            if pattern.search(blob):
                found.append(name)
    except RequestException:
        pass
    return found
