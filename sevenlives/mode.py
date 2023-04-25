from __future__ import annotations

class Mode:
    __modes = []

    def __init__(self, id, strongChar: int = 1):
        self.__id = id
        self.__strongChar = strongChar if strongChar != None and strongChar > 0 else 1

        Mode.__modes.append(self)

    @staticmethod
    def getValues() -> list[Mode]:
        return Mode.__modes

    def getId(self):
        return self.__id

    def getNames(self) -> list[str]:
        return [str(self.__id).lower(), str(self.__id).lower()[:self.__strongChar]]

Mode.PRODUCTION = Mode("PRODUCTION", 4)
Mode.DEVELOPMENT = Mode("DEVELOPMENT", 3)