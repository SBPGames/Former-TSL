# -*- coding: utf-8 -*-

import pygame
from sevenlives.entity.entity import Entity

class Collide(): 
    
    def __init__(self):
        pass

    def set_entity(self, entity):
        self.entity=entity

    def collide(self, entity1, entity2):
        return entity1.rect.colliderect(entity2.rect)