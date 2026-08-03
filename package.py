name = "wacom_gui"
version = "0.0.1"
requires = [
    "PySide6-6.11",
    "python",
]


def commands():
    env.PATH.append("{root}")  # noqa
    env.PYTHONPATH.append("{root}")  # noqa
    alias("wacom_gui", f"python {root}/wacom-gui/wacom-gui.py")  # noqa


description = """
Wacom interface for X11 display.
Fork (PySide6 migration and rez integration) : https://github.com/Ophtis/wacom-gui
"""
help = [["Github", "https://github.com/tb2097/wacom-gui"]]

authors = ["Travis Best travis.best@bronstudios.com", "Sophie Chauvet sophie.chauvet@mathematic.tv"]
