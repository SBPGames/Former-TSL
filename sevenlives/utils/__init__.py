"""
Sevenlives's Utils sub-package. It contains some useful functions and classes.
"""
__all__ = ["ScrW", "ScrH", "getAssetFolder"]
__author__ = "Xibitol"

import os, pygame

PROJECT_ROOT = "sevenlives"
PROJECT_ASSETS_FOLDER = "assets"

def getAssetFolder(subpackage: str, *path: tuple[str]):
    assert any(
        [subpackage == d for d in filter(lambda f: f != "__pycache__", os.listdir(PROJECT_ROOT))]
    ), "You have to give a real subpackage name."

    return os.path.join(PROJECT_ROOT, PROJECT_ASSETS_FOLDER,
        *filter(lambda v: v != None and len(v) > 0, [subpackage, *path])
    )

def ScrW() -> int:
    return pygame.display.Info().current_w

def ScrH() -> int:
    return pygame.display.Info().current_h