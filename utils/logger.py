"""
Logging utilities for Project AEGIS.
"""

from __future__ import annotations

import logging


def get_logger(name: str) -> logging.Logger:
    """
    Create and return a configured logger.

    Args:
        name: Usually use __name__ from the calling module.

    Returns:
        A configured Logger instance.
    """
    logger = logging.getLogger(name)

    # Prevent adding duplicate handlers if called multiple times
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%H:%M:%S",
    )

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Prevent messages from being printed twice
    logger.propagate = False

    return logger