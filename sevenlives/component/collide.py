# -*- coding: utf-8 -*-

import pygame
from sevenlives.entity.entity import Entity

class Collide(): 
    
    def __init__(self):
        pass

    def set_entity(self, entity):
        self.entity=entity

    def collide(self, box: pygame.Rect) -> bool:
        return self.entity.rect.colliderect(box)