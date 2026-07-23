"""
plugins/plugin_base.py

Base Plugin Class
"""

from __future__ import annotations

from abc import ABC
from typing import Any, Dict


class Plugin(ABC):
    """
    Base class for all plugins.
    """

    # Metadata (override in subclasses)
    name: str = "Unnamed Plugin"
    version: str = "1.0.0"
    author: str = "Unknown"
    description: str = ""
    enabled: bool = True

    def __init__(self) -> None:
        self.context: Dict[str, Any] = {}

    # --------------------------------------------------
    # Lifecycle Hooks
    # --------------------------------------------------

    def on_load(self) -> None:
        """
        Called after the plugin is loaded.
        """
        pass

    def on_enable(self) -> None:
        """
        Called when the plugin is enabled.
        """
        pass

    def on_disable(self) -> None:
        """
        Called when the plugin is disabled.
        """
        pass

    def on_unload(self) -> None:
        """
        Called before the plugin is unloaded.
        """
        pass

    # --------------------------------------------------
    # Context
    # --------------------------------------------------

    def set_context(self, **kwargs: Any) -> None:
        """
        Store shared objects (services, event bus, etc.).
        """
        self.context.update(kwargs)

    def get_context(self, key: str, default: Any = None) -> Any:
        """
        Retrieve a shared object.
        """
        return self.context.get(key, default)

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def info(self) -> Dict[str, Any]:
        """
        Return plugin metadata.
        """
        return {
            "name": self.name,
            "version": self.version,
            "author": self.author,
            "description": self.description,
            "enabled": self.enabled,
        }

    # --------------------------------------------------
    # Utility
    # --------------------------------------------------

    def log(self, message: str) -> None:
        """
        Simple plugin logger.
        """
        print(f"[{self.name}] {message}")

    # --------------------------------------------------
    # Representation
    # --------------------------------------------------

    def __repr__(self) -> str:
        return (
            f"<Plugin "
            f"name='{self.name}' "
            f"version='{self.version}' "
            f"enabled={self.enabled}>"
        )
