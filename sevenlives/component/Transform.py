# -*- coding: utf-8 -*-

import pygame

class Transform():
    
    '''
    Gère le déplacement, la taille et la vitesse
    '''
    
    def __init__(self, vector):
        self.rect=pygame.Rect(vector.x, vector.y, 0, 0)
        self.velocity=1

    def set_entity(self, entity):
        self.entity=entity

    def location(self):
        return (self.rect.x, self.rect.y)

    def set_entity(self, entity):
        self.entity=entity

    def move_by(self, dt, vector:pygame.Vector2): # système gravité --> variable gravity + attribut jump boléen je saute ou pas
        vector=vector.normalize()
        self.rect.topleft += self.velocity*vector*dt

    # def modify_size(self, x, y):
    #     self.image = pygame.transform.scale(self.image, (x, y))

    def update(self, dt):
        pass