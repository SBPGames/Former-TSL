"""
Les assets de ce package se situent dans le dossier "assets/level/{level._id}".
"""
import os, pygame
from sevenlives.utils import getAssetFolder
# TODO: Add typing for Entity classes

class Level:
    def __init__(self, id: str, backgroundColor: pygame.Color = pygame.Color(0, 0, 0)):
        self._id = id
        self._position = pygame.Vector2(0, 0)
        size = pygame.Vector2(640, 360)
        self.backgroundColor = backgroundColor
        self._backgroundLayers: list[pygame.Surface] = []

        # Backgrounds loading
        if os.path.exists(self.getBackgroundPath()):
            self._backgroundLayers.append(pygame.image.load(self.getBackgroundPath()))
        else:
            i = 0
            while os.path.exists(self.getBackgroundPath(i)):
                self._backgroundLayers.append(pygame.image.load(self.getBackgroundPath(i)))
                i += 1

        if len(self._backgroundLayers) > 0:
            size = self._backgroundLayers[0].get_size()

        # Surface creation
        self._surface = pygame.Surface(size)

        # Entities loading
        self.entities = []

    # GETTERS
    def getID(self) -> str: return self.id
    def getPath(self) -> str: return getAssetFolder(__package__.split(".")[-1], self._id)
    def getBackgroundPath(self, number: int = None) -> str:
        return os.path.join(self.getPath(), f"{'background' if number == None else number}.png")
    def _getInternalSurface(self): return self._surface

    # FUNCTIONS
    def update(self, deltatime):
        for entity in self.entities:
            entity.update_component(deltatime) # TODO: To see

    def _drawInternally(self, visibleRect: pygame.Rect):
        self._getInternalSurface().fill(pygame.Color(0, 0, 0))

        for layer in self._backgroundLayers:
            self._getInternalSurface().blit(layer, layer.get_rect())

        for entity in self.entities:
            entity.draw(self._getInternalSurface()) # TODO: To see
    def draw(self, surface: pygame.Surface, hasToDraw=True):
        if hasToDraw:
            self._drawInternally(surface.get_rect(topleft=self._position))
        surface.blit(self._getInternalSurface(), self._position)