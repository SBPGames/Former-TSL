"""
Sevenlives's Utils sub-package. It contains some useful functions and classes.
"""
__all__ = ["ScrW", "ScrH"]
__author__ = "Xibitol"

import pygame

def ScrW() -> int:
    return pygame.display.Info().current_w

def ScrH() -> int:
    return pygame.display.Info().current_h