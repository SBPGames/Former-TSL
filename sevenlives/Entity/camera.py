# -*- coding: utf-8 -*-

from entity import Entity

class Camera():

    '''Camera est une entité qui défini un champ de vision et qui informe si une entité est ou non dans son chmpas de vision.'''

    def __init__(self, position):
        self.parent=Entity("camera", position)
