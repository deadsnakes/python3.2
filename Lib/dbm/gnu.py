"""Provide the _gdbm module as a dbm submodule."""

import sys

try:
    from _gdbm import *
except ImportError as msg:
    raise ImportError(str(msg) + ', please install the python%s.%s-gdbm package' % sys.version_info[:2])
