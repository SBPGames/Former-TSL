import pygame

class Mouse:
    _pressed = False
    _pressedPos: pygame.Vector2 = None
    _wasPressed = False
    _released = False

    @staticmethod
    def isPressed() -> bool: return Mouse._pressed
    @staticmethod
    def wasPressed() -> bool: return Mouse._wasPressed
    @staticmethod
    def isReleased() -> bool: return Mouse._released

    @staticmethod
    def getPos() -> pygame.Vector2: return pygame.Vector2(*pygame.mouse.get_pos())
    @staticmethod
    def getPressedPos() -> pygame.Vector2: return Mouse._pressedPos.copy() if Mouse.isPressed() else Mouse._pressedPos

    @staticmethod
    def update():
        Mouse._wasPressed = Mouse.isPressed()

        Mouse._pressed = pygame.mouse.get_pressed()[0]
        if Mouse.isPressed() and Mouse._pressedPos == None: Mouse._pressedPos = pygame.Vector2(Mouse.getPos())
        elif not Mouse.wasPressed(): Mouse._pressedPos = None

        Mouse._released = not Mouse.isPressed() and Mouse.wasPressed()