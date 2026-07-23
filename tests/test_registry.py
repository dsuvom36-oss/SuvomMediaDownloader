"""
tests/test_registry.py
"""

from plugins.plugin_base import Plugin
from plugins.registry import PluginRegistry


class DummyPlugin(Plugin):
    name = "Dummy Plugin"


def test_registry_creation():
    registry = PluginRegistry()

    assert registry.count() == 0


def test_register_plugin():
    registry = PluginRegistry()

    plugin = DummyPlugin()

    registry.register(plugin)

    assert registry.count() == 1


def test_get_plugin():
    registry = PluginRegistry()

    plugin = DummyPlugin()

    registry.register(plugin)

    assert registry.get("Dummy Plugin") is plugin


def test_exists():
    registry = PluginRegistry()

    plugin = DummyPlugin()

    registry.register(plugin)

    assert registry.exists("Dummy Plugin")


def test_unregister():
    registry = PluginRegistry()

    plugin = DummyPlugin()

    registry.register(plugin)

    assert registry.unregister("Dummy Plugin")

    assert registry.count() == 0


def test_names():
    registry = PluginRegistry()

    registry.register(DummyPlugin())

    assert "Dummy Plugin" in registry.names()


def test_clear():
    registry = PluginRegistry()

    registry.register(DummyPlugin())

    registry.clear()

    assert registry.count() == 0


def test_enabled():
    registry = PluginRegistry()

    plugin = DummyPlugin()

    registry.register(plugin)

    assert len(registry.enabled()) == 1


def test_disabled():
    registry = PluginRegistry()

    plugin = DummyPlugin()
    plugin.enabled = False

    registry.register(plugin)

    assert len(registry.disabled()) == 1
