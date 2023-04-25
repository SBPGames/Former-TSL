from typing import Any
import pygame
from sevenlives.mode import Mode
from sevenlives.level import MainLevel
from sevenlives.interface import Mouse

class TheSevenLives:
    def __init__(self, mode: Mode = Mode.PRODUCTION):
        self._mode = mode
        pygame.init()

        if self._mode == Mode.DEVELOPMENT: 
            self._surface = pygame.display.set_mode((
                pygame.display.Info().current_w*3/4,
                pygame.display.Info().current_h*3/4
            ))
        else:
            self._surface = pygame.display.set_mode()

        pygame.display.set_caption("7lives")

        self._level = MainLevel()
        self.clock = pygame.time.Clock()

    def setLevel(self, level):
        self._level = level

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
            else:
                Mouse.update()

                if self._level != None:
                    self._level.update(self.clock.tick())
                    self._level.draw(self._surface)

                pygame.display.update()
                continue

            break