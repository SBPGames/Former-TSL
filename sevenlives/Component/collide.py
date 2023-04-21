# -*- coding: utf-8 -*-

import pygame
from entity import Entity

class Collide(): 
    
    def __init__(self):
        pass

    def verify_collide(self, entity1, entity2):
        return entity1.rect.colliderect(entity2.rect)