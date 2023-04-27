# -*- coding: utf-8 -*-

import pygame

class Location():
    
    def __init__(self, vector):
        self.rect=pygame.Rect(vector.x, vector.y, 0, 0)

    def set_entity(self, entity):
        self.entity=entity

    def location(self):
        return (self.rect.x, self.rect.y)
    
    def update(self, dt):
        pass