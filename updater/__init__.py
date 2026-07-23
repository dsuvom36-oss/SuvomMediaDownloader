"""
updater/__init__.py

Auto Updater Package

Provides classes for checking, downloading,
and installing application updates.
"""

from .updater import Updater
from .update_checker import UpdateChecker
from .version import Version

__version__ = "1.0.0"

__all__ = [
    "Updater",
    "UpdateChecker",
    "Version",
]
