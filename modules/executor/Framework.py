#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function)

from modules.exploits.framework_exploits import FRAMEWORK_RUNNERS, FRAMEWORK_CHAINS
from modules.exploits.exploit_scanner import run_exploit_scan
from modules.gathering.host_gathering import GatherHost


class Framework(object):
    """Generic executor for Laravel / Shopify / Moodle / Shopware."""

    def __init__(self, url=None, headers=None, port=None, fw_type="laravel"):
        self.url = url
        self.headers = headers
        self.port = port
        self.fw_type = (fw_type or "laravel").lower()

    def exploit(self, output_dir=None):
        cls = FRAMEWORK_RUNNERS.get(self.fw_type, FRAMEWORK_RUNNERS["laravel"])
        chain = FRAMEWORK_CHAINS.get(self.fw_type, [])
        inst = cls(self.url, self.headers)
        label = self.fw_type.capitalize()
        return run_exploit_scan(
            label, inst, chain, output_dir=output_dir, target_url=self.url
        )

    def webinfo(self):
        GatherHost(self.url, self.headers).web_host()

    def serveros(self):
        GatherHost(self.url, self.headers).os_server()
