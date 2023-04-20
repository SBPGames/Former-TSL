import pygame
from sevenlives.level import Level

class MainLevel:
    def __init__(self):
        self.__parent = Level("menu")
        self._buttons = [
            # New
            # Continue
            # Credits
            # Quit
        ]

    def update(self, deltatime):
        self.__parent.update(deltatime)

        for button in self._buttons:
            button.update(deltatime);

    def draw(self, surface: pygame.Surface):
        self.__parent.draw(surface)

        for button in self._buttons:
            button.draw(surface);