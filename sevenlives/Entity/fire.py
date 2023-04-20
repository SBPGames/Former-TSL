# -*- coding: utf-8 -*-

import pygame 
from entity import Entity

class Fire():

    def __init__(self):
        pass

    def create_fire(self, x, y, file_name):
        fire = Entity('Fire', x, y, file_name)