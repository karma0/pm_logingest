"""
Python logging facilities.
"""

import os
import logging


def create_logger(name=__name__):
    """
    Generic logger for application.  Configure logging from the returned
    resource.
    """
    log = logging.getLogger(name)
    level = os.environ.get('LOGLEVEL', 'INFO')
    log.setLevel(getattr(logging, level, logging.INFO))
    return log

logger = create_logger()
"""Global logger for application to use."""
