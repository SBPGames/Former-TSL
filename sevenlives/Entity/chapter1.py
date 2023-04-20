# -*- coding: utf-8 -*-

import pygame
from entity import Entity

class Squirrel1():
    '''
    Squirrel est un éccureuil.
    Il peut :
    - se déplacer à gauche, à droite, sauter
    - manger une noisette
    - disparaître
    - rentrer en collision aved des arbres/ noisettes...
    - se brûler ?
    '''

    def __init__(self):
        pass

    def create_scotty(self, x, y, image_scotty):
        scotty=Entity("Scotty", x, y, image_scotty)

class Hazelnut1():
    '''Hazelnut est une noisette.
    Elle peut :
    - brûler
    - se faire manger par un éccureuil'''

    def __init__(self):
        pass
    
    def create_hazelnut(self, x, y, hazelnut_image):
        hazelnut=Entity("hazelnut", x, y, hazelnut_image)

class Tree1():

    def __init__(self):
        pass

class Branch1():

    def __init__(self):
        pass

class Fire1():

    def __init__(self):
        pass

class Bubble1():

    def __init__(self):
        pass