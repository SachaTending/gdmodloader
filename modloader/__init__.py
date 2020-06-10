"""ModLoader for Geometry Dash, written in Python and Rust."""

__version__ = "0.1.0"

import gd
from gd.version import make_version_details

from modloader.logging import *
from modloader.state import *


version_info = make_version_details(__version__)
