import os, pygame

LEVELS_ASSETS_PATH = "assets/level"

class Level:
    def __init__(self, id: str, backgroundColor: pygame.Color = pygame.Color(255, 0, 0)):
        self._id = id
        self.entities = []
        self.backgroundColor = backgroundColor
        self.backgroundLayers: list[pygame.Surface] = []

        if os.path.exists(self.getBackgroundPath()):
            self.append(pygame.image.load(self.getBackgroundPath()))
        else:
            i = 0
            while os.path.exists(self.getBackgroundPath(i)):
                self.append(pygame.image.load(self.getBackgroundPath(i)))
                i += 1

        self.buttons = [
            # Start/Continue
            # New Game
            # Credits
            # Quit
        ]

    # Getters
    def getID(self) -> str: return self.id
    def getBackgroundPath(self, number: int) -> str:
        return f"{LEVELS_ASSETS_PATH}/{self._id}/{'background' if number == None else number}.png"

    # Functions
    def update(self, deltatime):
        for entity in self.entities:
            entity.update_component() # TODO: To see

    def draw(self, surface: pygame.Surface):
        displayInfo = pygame.display.Info() # FIXME: Get it from Game class
        screenRect = pygame.Rect(0, 0, displayInfo.current_w, displayInfo.current_h)

        pygame.draw.rect(surface, self.backgroundColor, screenRect)
        for layer in self.backgroundLayers:
            layer.blit(surface, screenRect)

if __name__ == "__main__":
    # See for tests
    pass