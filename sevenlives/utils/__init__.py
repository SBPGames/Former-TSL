"""
Sevenlives's Utils sub-package. It contains some useful functions and classes.
"""
__all__ = ["ScrW", "ScrH", "getAssetFolder"]
__author__ = "Xibitol"

import os, pygame

PROJECT_ROOT = "sevenlives"

def getAssetFolder(subpackage: str, *path: tuple[str]):
    assert any(
        [subpackage == d for d in filter(lambda f: f != "__pycache__", os.listdir(PROJECT_ROOT))]
    ), "You have to give a real subpackage name."

    return os.path.join(PROJECT_ROOT, *filter(lambda p: p != None and len(p) > 0, [subpackage, *path]))

def ScrW() -> int:
    return pygame.display.Info().current_w

def ScrH() -> int:
    return pygame.display.Info().current_h