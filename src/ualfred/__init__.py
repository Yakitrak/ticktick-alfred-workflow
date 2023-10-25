# encoding: utf-8
#
# Copyright (c) 2014 Dean Jackson <deanishe@deanishe.net>
#
# MIT Licence. See http://opensource.org/licenses/MIT
#
# Created on 2014-02-15
#

"""A helper library for `Alfred <http://www.alfredapp.com/>`_ workflows."""
# Filter matching rules
# Icons
# Exceptions
from .workflow import (
    ICON_ACCOUNT,
    ICON_BURN,
    ICON_CLOCK,
    ICON_COLOR,
    ICON_COLOUR,
    ICON_EJECT,
    ICON_ERROR,
    ICON_FAVORITE,
    ICON_FAVOURITE,
    ICON_GROUP,
    ICON_HELP,
    ICON_HOME,
    ICON_INFO,
    ICON_NETWORK,
    ICON_NOTE,
    ICON_SETTINGS,
    ICON_SWIRL,
    ICON_SWITCH,
    ICON_SYNC,
    ICON_TRASH,
    ICON_USER,
    ICON_WARNING,
    ICON_WEB,
    MATCH_ALL,
    MATCH_ALLCHARS,
    MATCH_ATOM,
    MATCH_CAPITALS,
    MATCH_INITIALS,
    MATCH_INITIALS_CONTAIN,
    MATCH_INITIALS_STARTSWITH,
    MATCH_STARTSWITH,
    MATCH_SUBSTRING,
    KeychainError,
    PasswordNotFound,
    Workflow,
    manager,
)
from .workflow3 import Variables, Workflow3

__version__ = "2.0.1"

__all__ = [
    "Variables",
    "Workflow",
    "Workflow3",
    "manager",
    "PasswordNotFound",
    "KeychainError",
    "ICON_ACCOUNT",
    "ICON_BURN",
    "ICON_CLOCK",
    "ICON_COLOR",
    "ICON_COLOUR",
    "ICON_EJECT",
    "ICON_ERROR",
    "ICON_FAVORITE",
    "ICON_FAVOURITE",
    "ICON_GROUP",
    "ICON_HELP",
    "ICON_HOME",
    "ICON_INFO",
    "ICON_NETWORK",
    "ICON_NOTE",
    "ICON_SETTINGS",
    "ICON_SWIRL",
    "ICON_SWITCH",
    "ICON_SYNC",
    "ICON_TRASH",
    "ICON_USER",
    "ICON_WARNING",
    "ICON_WEB",
    "MATCH_ALL",
    "MATCH_ALLCHARS",
    "MATCH_ATOM",
    "MATCH_CAPITALS",
    "MATCH_INITIALS",
    "MATCH_INITIALS_CONTAIN",
    "MATCH_INITIALS_STARTSWITH",
    "MATCH_STARTSWITH",
    "MATCH_SUBSTRING",
]
