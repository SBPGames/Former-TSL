"""
Package Interface. It contains all UI elements such as Buttons, KeyTips, etc.

To make working elements that's use the mouse, you need to update it each frames by calling Mouse.update() before any
update of a UI elements.
"""

__all__ = ["Mouse", "Button"]
__author__ = "Xibitol"

from sevenlives.interface.mouse import Mouse
from sevenlives.interface.button import Button