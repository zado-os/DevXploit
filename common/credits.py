# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function)

from common.branding import (
    APP_NAME,
    EDITION,
    ORIGINAL_AUTHOR,
    MAINTAINER,
    MAINTAINER_ALIAS,
    REPO_URL,
)

PROJECT_NAME = APP_NAME
SHORT_CREDIT = "[%s %s]" % (MAINTAINER, MAINTAINER_ALIAS)
COPYRIGHT_LINE = "%s %s — %s | %s (%s) | %s" % (
    APP_NAME, EDITION, ORIGINAL_AUTHOR, MAINTAINER, MAINTAINER_ALIAS, REPO_URL,
)
