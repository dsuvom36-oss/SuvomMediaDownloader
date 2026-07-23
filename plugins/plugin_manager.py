"""
plugins/plugin_manager.py

Plugin Manager
"""

from __future__ import annotations

import importlib
import inspect
import pkgutil
from typing import Dict, List, Optional

from .plugin_base import Plugin


class PluginManager:
    """Loads and manages application plugins."""

    def __init__(self, plugin_package: str = "plugins.installed"):
        self.plugin_package = plugin_package
        self.plugins: Dict[str, Plugin] = {}
        self.enabled_plugins: Dict[str, Plugin] = {}

    # -----------------------------------------------------
    # Discovery
    # -----------------------------------------------------

    def discover_plugins(self) -> List[str]:
        """Return available plugin module names."""

        modules = []

        try:
            package = importlib.import_module(self.plugin_package)

            for _, module_name, ispkg in pkgutil.iter_modules(package.__path__):
                if not ispkg:
                    modules.append(module_name)

        except Exception as exc:
            print(f"Plugin discovery failed: {exc}")

        return sorted(modules)

    # -----------------------------------------------------
    # Loading
    # -----------------------------------------------------

    def load_plugins(self) -> None:
        """Load all discovered plugins."""

        for module_name in self.discover_plugins():
            self.load_plugin(module_name)

    def load_plugin(self, module_name: str) -> Optional[Plugin]:
        """Load a single plugin."""

        try:
            module = importlib.import_module(f"{self.plugin_package}.{module_name}")

            for _, obj in inspect.getmembers(module, inspect.isclass):

                if issubclass(obj, Plugin) and obj is not Plugin:

                    plugin = obj()

                    self.plugins[plugin.name] = plugin

                    plugin.on_load()

                    if plugin.enabled:
                        self.enabled_plugins[plugin.name] = plugin

                    print(f"Loaded plugin: {plugin.name}")

                    return plugin

        except Exception as exc:
            print(f"Failed to load plugin '{module_name}': {exc}")

        return None

    # -----------------------------------------------------
    # Enable / Disable
    # -----------------------------------------------------

    def enable_plugin(self, name: str) -> bool:

        plugin = self.plugins.get(name)

        if plugin is None:
            return False

        if plugin.enabled:
            return True

        plugin.enabled = True
        plugin.on_enable()

        self.enabled_plugins[name] = plugin

        return True

    def disable_plugin(self, name: str) -> bool:

        plugin = self.plugins.get(name)

        if plugin is None:
            return False

        if not plugin.enabled:
            return True

        plugin.enabled = False
        plugin.on_disable()

        self.enabled_plugins.pop(name, None)

        return True

    # -----------------------------------------------------
    # Unload
    # -----------------------------------------------------

    def unload_plugin(self, name: str) -> bool:

        plugin = self.plugins.get(name)

        if plugin is None:
            return False

        try:
            plugin.on_unload()

        finally:
            self.plugins.pop(name, None)
            self.enabled_plugins.pop(name, None)

        return True

    # -----------------------------------------------------
    # Queries
    # -----------------------------------------------------

    def get_plugin(self, name: str) -> Optional[Plugin]:
        return self.plugins.get(name)

    def list_plugins(self) -> List[Plugin]:
        return list(self.plugins.values())

    def list_enabled_plugins(self) -> List[Plugin]:
        return list(self.enabled_plugins.values())

    def is_enabled(self, name: str) -> bool:
        return name in self.enabled_plugins

    # -----------------------------------------------------
    # Shutdown
    # -----------------------------------------------------

    def shutdown(self) -> None:

        for plugin in list(self.plugins.values()):

            try:
                plugin.on_unload()

            except Exception as exc:
                print(f"Plugin shutdown error ({plugin.name}): {exc}")

        self.plugins.clear()
        self.enabled_plugins.clear()
