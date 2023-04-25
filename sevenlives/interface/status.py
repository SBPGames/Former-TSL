from __future__ import annotations

class UIStatus:
    IDLE: UIStatus = None
    CLICKED: UIStatus = None
    __status = []

    def __init__(self, id):
        self.__id = id

        UIStatus.__status.append(self)

    @staticmethod
    def getValues() -> list[UIStatus]:
        return UIStatus.__status

    def getId(self):
        return self.__id

UIStatus.IDLE = UIStatus("idle")
UIStatus.CLICKED = UIStatus("clicked")