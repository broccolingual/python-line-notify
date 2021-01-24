from .exceptions import NoTokenError
from .client import Client
from .utils import *

from .__version__ import __title__, __url__, __version__
from .__version__ import __author__, __author_email__, __license__

import logging
from logging import NullHandler

logging.getLogger(__name__).addHandler(NullHandler())