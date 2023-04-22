"""
Sevenlives's Utils sub-package. It contains some useful functions and classes.
"""
__all__ = ["ScrW", "ScrH", "getAssetFolder"]
__author__ = "Xibitol"

import os, pygame

PROJECT_ROOT = "sevenlives"

def getAssetFolder(subpackage: str, element: str = None):
    assert any(
        [subpackage == d for d in filter(lambda f: f != "__pycache__", os.listdir(PROJECT_ROOT))]
    ), "You have to give a real subpackage name."

    spRoot = os.path.join(PROJECT_ROOT, subpackage)
    return os.path.join(spRoot, element) if element != None else spRoot

def ScrW() -> int:
    return pygame.display.Info().current_w

def ScrH() -> int:
    return pygame.display.Info().current_h