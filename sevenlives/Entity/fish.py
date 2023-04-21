# -*- coding: utf-8 -*-

import pygame 
from entity import Entity

class Fish():

    '''
    Fish est un poisson qui n'apparaîtera qu'au chapitre 2.
    '''

    def __init__(self, position):
        self.parent=Entity("fish", position)