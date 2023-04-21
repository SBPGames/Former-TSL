# -*- coding: utf-8 -*-

from entity import Entity

class Hazelnut():

    '''Hazelnut est une noisette.
    Elle peut :
    - brûler
    - se faire manger par un éccureuil'''

    def __init__(self, position):
        self.parent=Entity("hazelnut", position)