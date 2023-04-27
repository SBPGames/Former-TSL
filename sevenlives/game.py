import pygame
from sevenlives.utils import ScrW, ScrH
from sevenlives.mode import Mode
from sevenlives.interface import Mouse

class TheSevenLives:
    WINDOW_WIDTH = 640
    WINDOW_HEIGHT = 360

    def __init__(self, mode: Mode = Mode.PRODUCTION):
        self._mode = mode
        pygame.init()

        if self._mode == Mode.DEVELOPMENT: self._surface = pygame.display.set_mode((ScrW()*3/4, ScrH()*3/4))
        else: self._surface = pygame.display.set_mode()
        pygame.display.set_caption(f"7lives{' - DEVELOPMENT MODE' if self._mode == Mode.DEVELOPMENT else ''}")

        self._clock = pygame.time.Clock()
        self._level = None

    def setLevel(self, level):
        self._level = level

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
            else:
                screen = pygame.Surface(pygame.Vector2(TheSevenLives.WINDOW_WIDTH, TheSevenLives.WINDOW_HEIGHT))
                screen.fill("black")

                Mouse.update()
                if self._level != None:
                    self._level.update(self._clock.get_time()/1000)
                    self._level.draw(screen)

                self._surface.blit(pygame.transform.scale(screen, self._surface.get_rect().size), screen.get_rect())
                pygame.display.flip()
                self._clock.tick(60)
                continue

            break