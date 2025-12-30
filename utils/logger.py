"""Logging utilities for the simulation system."""

import logging


def get_logger(name: str, level: str = "INFO") -> logging.Logger:
    """Return a configured logger.

    Args:
        name: Logger name, typically __name__.
        level: Log level string.

    Returns:
        Configured logger instance.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.setLevel(level)
    logger.propagate = False
    return logger


def set_root_log_level(level: str = "INFO") -> None:
    """Set root logging level for libraries and app modules.

    Args:
        level: Log level string.
    """
    logging.getLogger().setLevel(level)
