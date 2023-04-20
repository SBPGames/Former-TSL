"""
Les assets de ce package se situent dans le dossier "assets/level/{level._id}".
"""
import os, pygame

LEVELS_ASSETS_PATH = "sevenlives/assets/level"

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
    def getBackgroundPath(self, number: int = None) -> str:
        return f"{LEVELS_ASSETS_PATH}/{self._id}/{'background' if number == None else number}.png"

    # Functions
    def update(self, deltatime):
        for entity in self.entities:
            entity.update_component(deltatime) # TODO: To see

    def draw(self, surface: pygame.Surface):
        screenRect = pygame.Rect(0, 0, surface.get_width(), surface.get_height())

        surface.fill(self.backgroundColor)
        for layer in self._backgroundLayers:
            surface.blit(pygame.transform.scale(layer, screenRect.size), screenRect)

        for entity in self.entities:
            entity.draw() # TODO: To see