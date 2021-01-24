__title__ = 'python_line_notify'
__author__ = 'Broccolingual'
__author_email__ = 'broccolingual@gmail.com'
__url__ = 'https://github.com/broccolingual/python-line-notify'
__license__ = 'MIT'
__copyright__ = 'Copyright 2021-present Broccolingual'
__version__ = '1.1.5'

from .exceptions import NoTokenError
from .client import Client
from .utils import *

import logging
from logging import NullHandler

logging.getLogger(__name__).addHandler(NullHandler())