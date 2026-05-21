# -*- coding: utf-8 -*-
"""Multi-target parallel scanning."""

from __future__ import (absolute_import, division, print_function)

from concurrent.futures import ThreadPoolExecutor, as_completed

from common.colors import good, bad, run, W
from modules.detector import CMS


def normalize_url(line):
    line = (line or "").strip()
    if not line or line.startswith("#"):
        return None
    if line.startswith("http"):
        return line
    return "https://" + line


def scan_one(url, headers, scan_kwargs):
    try:
        CMS(url=url, headers=headers, **scan_kwargs).instanciate()
        return url, True, ""
    except Exception as exc:
        return url, False, str(exc)[:120]


def run_batch(urls, headers, threads=3, **scan_kwargs):
    urls = [normalize_url(u) for u in urls]
    urls = [u for u in urls if u]
    if not urls:
        print(" {0} No valid URLs in input".format(bad))
        return
    print(" {0} Batch scan — {1} target(s), {2} thread(s)".format(run, len(urls), threads))
    ok = 0
    with ThreadPoolExecutor(max_workers=max(1, threads)) as pool:
        futures = {
            pool.submit(scan_one, u, headers, scan_kwargs): u for u in urls
        }
        for fut in as_completed(futures):
            url, success, err = fut.result()
            if success:
                ok += 1
                print(" {0} Done: {1}".format(good, url))
            else:
                print(" {0} Fail: {1} — {2}".format(bad, url, err))
    print("{0} −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−".format(W))
    print(" {0} Batch finished: {1}/{2} OK".format(good, ok, len(urls)))
