"""
tests/test_plugin_manager.py

Unit tests for PluginManager.
"""

from plugins.plugin_manager import PluginManager


def test_plugin_manager_creation():
    manager = PluginManager()

    assert manager is not None
    assert manager.plugins == {}
    assert manager.enabled_plugins == {}


def test_discover_plugins():
    manager = PluginManager()

    plugins = manager.discover_plugins()

    assert isinstance(plugins, list)


def test_load_plugins():
    manager = PluginManager()

    manager.load_plugins()

    assert isinstance(manager.plugins, dict)


def test_list_plugins():
    manager = PluginManager()

    manager.load_plugins()

    plugins = manager.list_plugins()

    assert isinstance(plugins, list)


def test_enabled_plugins():
    manager = PluginManager()

    manager.load_plugins()

    enabled = manager.list_enabled_plugins()

    assert isinstance(enabled, list)


def test_unknown_plugin():
    manager = PluginManager()

    assert manager.get_plugin("Unknown Plugin") is None


def test_enable_unknown_plugin():
    manager = PluginManager()

    assert manager.enable_plugin("Unknown") is False


def test_disable_unknown_plugin():
    manager = PluginManager()

    assert manager.disable_plugin("Unknown") is False
