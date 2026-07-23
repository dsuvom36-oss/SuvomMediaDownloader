"""
plugins/installed/example_plugin.py

Example Plugin
"""

from plugins import Plugin


class ExamplePlugin(Plugin):
    """
    Example plugin demonstrating the plugin lifecycle.
    """

    name = "Example Plugin"
    version = "1.0.0"
    author = "Suvom Project Limited"
    description = "Example plugin bundled with the application."
    enabled = True

    # -------------------------------------------------
    # Lifecycle
    # -------------------------------------------------

    def on_load(self) -> None:
        self.log("Plugin loaded.")

    def on_enable(self) -> None:
        self.log("Plugin enabled.")

    def on_disable(self) -> None:
        self.log("Plugin disabled.")

    def on_unload(self) -> None:
        self.log("Plugin unloaded.")

    # -------------------------------------------------
    # Example Action
    # -------------------------------------------------

    def hello(self) -> str:
        """
        Example public method.
        """
        message = "Hello from Example Plugin!"
        self.log(message)
        return message

    # -------------------------------------------------
    # Information
    # -------------------------------------------------

    def info(self):
        data = super().info()
        data["type"] = "Example"
        return data
