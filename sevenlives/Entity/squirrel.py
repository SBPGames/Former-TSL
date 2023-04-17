# -*- coding: utf-8 -*-

import pygame 
from entity import Entity

class Squirrel():

    '''
    Squirrel est un éccureuil.
    Il peut :
    - se déplacer à gauche, à droite, sauter
    - manger une noisette
    - disparaître
    - rentrer en collision aved des arbres/ noisettes...
    - se brûler
    '''

    def __init__(self):
        self.attribute= Entity("Scotty")
        