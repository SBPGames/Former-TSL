import pygame
from sevenlives.level import Level
from sevenlives.interface import *

class MainLevel:
    def __init__(self):
        self.__parent = Level("menu")

        origin = pygame.Vector2(pygame.display.Info().current_w*2/3, pygame.display.Info().current_h/2)
        self._buttons: list[Button] = [
            Button("start", origin, self.startClicked),
            Button("continue", origin, self.continueClicked),
            Button("quit", origin, self.quitClicked),
        ]

        space = 40
        origin = origin - pygame.Vector2(0, (sum([button._rect.height + space for button in self._buttons]) - space)/2)
        for (i, button) in enumerate(self._buttons):
            button._rect.topleft = self._buttons[i - 1]._rect.bottomleft + pygame.Vector2(0, space) if i > 0 else origin

        self._cdtText = pygame.font.SysFont("Arial", 15).render(
            "The Seven Lives - A NSI project by Xibitol, Nagisou and Mélody - licensed under GNU GPL v3.",
            True,
            pygame.Color(235, 235, 235)
        )
        self._cdtRect = self._cdtText.get_rect()
        self._cdtRect.bottomleft = pygame.Vector2(10, pygame.display.Info().current_h - 10)

    def update(self, deltatime):
        self.__parent.update(deltatime)

        for button in self._buttons:
            button.update()

    def draw(self, surface: pygame.Surface):
        self.__parent.draw(surface)

        for button in self._buttons:
            button.draw(surface)

        surface.blit(self._cdtText, self._cdtRect)

    # Buttons actions
    def startClicked(self):
        print("Started !")
    def continueClicked(self):
        print("Continued !")
    def quitClicked(self):
        pygame.event.post(pygame.event.Event(pygame.QUIT))
