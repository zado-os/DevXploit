# -*- coding: utf-8 -*-
"""Multi-signal CMS detection with confidence score."""

from __future__ import (absolute_import, division, print_function)

import re
import requests
from requests.exceptions import RequestException

SIGNALS = {
    "wordpress": [
        (r"wp-content/", 3),
        (r"wp-includes/", 3),
        (r"wordpress", 2),
        (r"xmlrpc\.php", 2),
    ],
    "joomla": [
        (r"/media/system/js/", 3),
        (r"Joomla!", 3),
        (r"option=com_", 2),
        (r"mootools", 1),
    ],
    "prestashop": [
        (r"prestashop", 3),
        (r"/modules/", 2),
        (r"PrestaShop", 2),
    ],
    "drupal": [
        (r"Drupal", 3),
        (r"sites/default", 3),
        (r"drupal\.org", 2),
    ],
    "opencart": [
        (r"route=product", 3),
        (r"OpenCart", 3),
        (r"catalog/view", 2),
    ],
    "magento": [
        (r"Mage\.Cookies", 3),
        (r"Magento", 2),
        (r"/skin/frontend", 2),
    ],
    "lokomedia": [
        (r"lokomedia", 3),
        (r"/smiley/", 2),
    ],
    "laravel": [
        (r"laravel_session", 4),
        (r"/vendor/laravel", 3),
        (r"XSRF-TOKEN", 2),
    ],
    "shopify": [
        (r"cdn\.shopify\.com", 4),
        (r"Shopify\.theme", 3),
    ],
    "moodle": [
        (r"moodle", 3),
        (r"/login/index\.php", 2),
        (r"M\.cfg", 2),
    ],
    "shopware": [
        (r"shopware", 3),
        (r"/backend/", 2),
        (r"sw-cache-hash", 2),
    ],
}

CLASS_MAP = {
    "wordpress": "Wordpress",
    "joomla": "Joomla",
    "prestashop": "Prestashop",
    "drupal": "Drupal",
    "opencart": "Opencart",
    "magento": "Magento",
    "lokomedia": "Lokomedia",
    "lokomedia2": "Lokomedia2",
    "laravel": "Framework",
    "shopify": "Framework",
    "moodle": "Framework",
    "shopware": "Framework",
}


def detect_cms_scored(url, headers=None, extra_html=""):
    try:
        html = extra_html or requests.get(
            url.rstrip("/"),
            headers=headers or {},
            verify=False,
            timeout=12,
        ).text or ""
    except RequestException:
        html = extra_html or ""

    scores = {}
    for cms, patterns in SIGNALS.items():
        s = 0
        for rx, weight in patterns:
            if re.search(rx, html, re.I):
                s += weight
        if s:
            scores[cms] = s

    if not scores:
        return "Unknown", 0, []

    best = max(scores, key=scores.get)
    max_score = scores[best]
    confidence = min(99, int(100 * max_score / (max_score + 6)))
    ranked = sorted(scores.items(), key=lambda x: -x[1])
    return CLASS_MAP.get(best, best.capitalize()), confidence, ranked
