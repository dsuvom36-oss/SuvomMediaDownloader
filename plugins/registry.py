"""
plugins/registry.py

Plugin Registry
"""

from __future__ import annotations

from typing import Dict, List, Optional

from .plugin_base import Plugin


class PluginRegistry:
    """
    Stores and manages registered plugins.
    """

    def __init__(self):
        self._plugins: Dict[str, Plugin] = {}

    # -------------------------------------------------
    # Register
    # -------------------------------------------------

    def register(self, plugin: Plugin) -> None:
        """
        Register a plugin.
        """
        self._plugins[plugin.name] = plugin

    # -------------------------------------------------
    # Unregister
    # -------------------------------------------------

    def unregister(self, name: str) -> bool:
        """
        Remove a plugin from the registry.
        """
        if name in self._plugins:
            del self._plugins[name]
            return True
        return False

    # -------------------------------------------------
    # Lookup
    # -------------------------------------------------

    def get(self, name: str) -> Optional[Plugin]:
        """
        Get a plugin by name.
        """
        return self._plugins.get(name)

    def exists(self, name: str) -> bool:
        """
        Check whether a plugin exists.
        """
        return name in self._plugins

    # -------------------------------------------------
    # Lists
    # -------------------------------------------------

    def all(self) -> List[Plugin]:
        """
        Return all registered plugins.
        """
        return list(self._plugins.values())

    def names(self) -> List[str]:
        """
        Return all plugin names.
        """
        return sorted(self._plugins.keys())

    def enabled(self) -> List[Plugin]:
        """
        Return enabled plugins.
        """
        return [plugin for plugin in self._plugins.values() if plugin.enabled]

    def disabled(self) -> List[Plugin]:
        """
        Return disabled plugins.
        """
        return [plugin for plugin in self._plugins.values() if not plugin.enabled]

    # -------------------------------------------------
    # Utilities
    # -------------------------------------------------

    def count(self) -> int:
        """
        Number of registered plugins.
        """
        return len(self._plugins)

    def clear(self) -> None:
        """
        Remove every registered plugin.
        """
        self._plugins.clear()

    # -------------------------------------------------
    # Magic Methods
    # -------------------------------------------------

    def __contains__(self, name: str) -> bool:
        return name in self._plugins

    def __len__(self) -> int:
        return len(self._plugins)

    def __iter__(self):
        return iter(self._plugins.values())
