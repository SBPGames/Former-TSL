from __future__ import annotations
from typing import Any

class Mode:
    PRODUCTION: Mode = None
    DEVELOPMENT: Mode = None
    __modes = []

    def __init__(self, id: Any, strongChar: int = 1):
        self.__id = id
        self.__strongChar = max(strongChar, 1)

        Mode.__modes.append(self)

    @staticmethod
    def getValues() -> list[Mode]:
        return Mode.__modes

    def getId(self) -> Any:
        return self.__id

    def getNames(self) -> list[str]:
        return [str(self.__id).lower(), str(self.__id).lower()[:self.__strongChar]]

Mode.PRODUCTION = Mode("PRODUCTION", 4)
Mode.DEVELOPMENT = Mode("DEVELOPMENT", 3)