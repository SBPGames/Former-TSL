import os, pygame
from sevenlives.utils import ScrW, ScrH
from sevenlives.level import Level
from sevenlives.interface import Button

class MainLevel:
    def __init__(self):
        self.__parent = Level("menu")
        self._buttons: list[Button] = [
            Button("start", pygame.Vector2(0, 0), self.startClicked),
            Button("continue", pygame.Vector2(0, 0), self.continueClicked),
            Button("quit", pygame.Vector2(0, 0), self.quitClicked),
        ]

        space = pygame.Vector2(0, 40)
        origin = pygame.Vector2(ScrW()*2/3, ScrH()/2 - self._buttons[0]._rect.h)

        # Logo
        self._logo = pygame.image.load(os.path.join(self.__parent.getPath(), "logo.png"))
        self._logoRect = self._logo.get_rect()
        self._logoRect.bottomleft = origin - space - pygame.Vector2((self._logoRect.w - self._buttons[0]._rect.w)/2, 0)

        # Buttons
        for (i, button) in enumerate(self._buttons):
            button._rect.topleft = self._buttons[i - 1]._rect.bottomleft + space if i > 0 else origin

        # Credits
        self._cdtText = pygame.font.SysFont("Arial", 15).render(
            "The Seven Lives - A NSI project by Xibitol, Nagisou and Mélody - licensed under GNU GPL v3.",
            True,
            pygame.Color(235, 235, 235)
        )
        self._cdtRect = self._cdtText.get_rect()
        self._cdtRect.bottomleft = pygame.Vector2(10, ScrH() - 10)

    def update(self, deltatime):
        self.__parent.update(deltatime)

        for button in self._buttons:
            button.update()

    def draw(self, surface: pygame.Surface):
        self.__parent.draw(surface)

        for button in self._buttons:
            button.draw(surface)

        surface.blit(self._cdtText, self._cdtRect)
        surface.blit(self._logo, self._logoRect)

    # Buttons actions
    def startClicked(self):
        pass
    def continueClicked(self):
        pass
    def quitClicked(self):
        pygame.event.post(pygame.event.Event(pygame.QUIT))
