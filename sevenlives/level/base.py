"""
Les assets de ce package se situent dans le dossier "assets/level/{level._id}".
"""
import os, pygame
from sevenlives.utils import getAssetFolder
# TODO: Add typing for Entity classes

class Level:
    def __init__(self, id: str, backgroundColor: pygame.Color = pygame.Color(0, 0, 0)):
        self._id = id
        self.backgroundColor = backgroundColor
        self._backgroundLayers: list[pygame.Surface] = []

        if os.path.exists(self.getBackgroundPath()):
            self._backgroundLayers.append(pygame.image.load(self.getBackgroundPath()))
        else:
            i = 0
            while os.path.exists(self.getBackgroundPath(i)):
                self._backgroundLayers.append(pygame.image.load(self.getBackgroundPath(i)))
                i += 1

        self.entities = []

    # Getters
    def getID(self) -> str: return self.id
    def getPath(self) -> str: return getAssetFolder(__package__.split(".")[-1], self._id)
    def getBackgroundPath(self, number: int = None) -> str:
        return os.path.join(self.getPath(), f"{'background' if number == None else number}.png")

    # Functions
    def update(self, deltatime):
        for entity in self.entities:
            entity.update_component(deltatime) # TODO: To see

    def draw(self, surface: pygame.Surface):
        surface.fill(self.backgroundColor)
        for layer in self._backgroundLayers:
            surface.blit(layer, surface.get_rect())

        for entity in self.entities:
            entity.draw() # TODO: To see