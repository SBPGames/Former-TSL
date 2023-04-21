"""
Buttons's image asset is "0.png" in "assets/interface/button/{button._id}".
"""
import os, pygame
from typing import Callable
from sevenlives.interface import Mouse

BUTTONS_ASSETS_PATH = "sevenlives/assets/interface/button"

class Button:
    def __init__(self,
        id: str,
        pos: pygame.Vector2,
        size: tuple[int, int] = (200, 50),
        callback: Callable[[], None] = lambda: None,

        color: pygame.Color = pygame.Color(51, 51, 51),
        text: str = None,
        textColor: pygame.Color = pygame.Color(235, 235, 235)
    ):
        self._id = id
        self._clicked = False
        self._callback = callback

        if os.path.exists(self._getButtonImgPath()):
            image = pygame.image.load(self._getButtonImgPath())
            size = image.get_rect().size

        self._rect = pygame.Rect(pos.x, pos.y, size[0], size[1])
        self._surface = pygame.Surface(self._rect.size)

        if image != None:
            self._surface.blit(image, image.get_rect(center=self._surface.get_rect().center))
        else:
            self._surface.fill(color)
            font = pygame.font.SysFont("Arial", int(self._rect.h/2))
            textSurf = font.render(text if text != None else self._id.capitalize(), False, textColor)
            self._surface.blit(textSurf, textSurf.get_rect(center=self._surface.get_rect().center))

    def isClicked(self) -> bool:
        return self._clicked
    def _getButtonImgPath(self) -> str:
        return f"{BUTTONS_ASSETS_PATH}/{self._id}/0.png"

    def update(self):
        self._surface.set_alpha(255)

        if self._rect.collidepoint(*Mouse.getPos()):
            self._surface.set_alpha(127)

            if Mouse.isReleased() and self._rect.collidepoint(*Mouse.getPressedPos()):
                self._clicked = True
                self._callback()

    def draw(self, surface: pygame.Surface):
        surface.blit(self._surface, self._rect)