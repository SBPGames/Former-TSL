# -*- coding: utf-8 -*-

import pygame 
from entity import Entity

class Fire():

    '''Fire est du feu.
    La seul fonction du feu est de brûler les autrs entités.'''

    def __init__(self, position):
        fire = Entity('fire', position)