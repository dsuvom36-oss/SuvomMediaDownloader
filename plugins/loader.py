"""
plugins/loader.py

Plugin Loader
"""

from __future__ import annotations

from pathlib import Path
from typing import List

from .plugin_manager import PluginManager


class PluginLoader:
    """
    Helper class responsible for discovering and
    loading plugins through the PluginManager.
    """

    def __init__(
        self,
        manager: PluginManager,
        plugin_directory: Path | None = None,
    ):
        self.manager = manager
        self.plugin_directory = plugin_directory or Path(__file__).parent / "installed"

    # -------------------------------------------------
    # Discovery
    # -------------------------------------------------

    def discover(self) -> List[str]:
        """
        Discover available plugin names.
        """
        return self.manager.discover_plugins()

    # -------------------------------------------------
    # Loading
    # -------------------------------------------------

    def load_all(self) -> None:
        """
        Load every discovered plugin.
        """
        self.manager.load_plugins()

    def load(self, plugin_name: str):
        """
        Load a single plugin.
        """
        return self.manager.load_plugin(plugin_name)

    # -------------------------------------------------
    # Enable / Disable
    # -------------------------------------------------

    def enable(self, plugin_name: str) -> bool:
        """
        Enable a plugin.
        """
        return self.manager.enable_plugin(plugin_name)

    def disable(self, plugin_name: str) -> bool:
        """
        Disable a plugin.
        """
        return self.manager.disable_plugin(plugin_name)

    # -------------------------------------------------
    # Unload
    # -------------------------------------------------

    def unload(self, plugin_name: str) -> bool:
        """
        Unload a plugin.
        """
        return self.manager.unload_plugin(plugin_name)

    # -------------------------------------------------
    # Information
    # -------------------------------------------------

    def plugins(self):
        """
        Return all loaded plugins.
        """
        return self.manager.list_plugins()

    def enabled_plugins(self):
        """
        Return enabled plugins.
        """
        return self.manager.list_enabled_plugins()

    def exists(self, plugin_name: str) -> bool:
        """
        Check whether a plugin is loaded.
        """
        return self.manager.get_plugin(plugin_name) is not None

    # -------------------------------------------------
    # Shutdown
    # -------------------------------------------------

    def shutdown(self) -> None:
        """
        Shutdown the plugin system.
        """
        self.manager.shutdown()
