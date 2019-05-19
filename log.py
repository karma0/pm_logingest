"""
Python logging facilities.
"""

import os
import logging

def create_logger(name):
    """Generic logger for application.  Configure logging from the returned
    resource.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(os.environ.get('LOGLEVEL', logging.INFO))
    return logger

logger = create_logger(__name__)
"""Global logger for application to use."""
