"""
plugins/__init__.py

Plugin package for Suvom Media Downloader.

This package provides the plugin framework used to
discover, load, enable, disable, and manage plugins.
"""

from .plugin_base import Plugin
from .plugin_manager import PluginManager

__version__ = "1.0.0"

__all__ = [
    "Plugin",
    "PluginManager",
]
