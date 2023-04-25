# -*- coding: utf-8 -*-

import pygame

class Transform():
    
    '''
    Gère le déplacement, la taille et la vitesse.
    '''
    
    def __init__(self, vector:pygame.Vector2, speed=10):
        self.rect=pygame.Rect(vector.x, vector.y, 0, 0)
        self.velocity=pygame.Vector2(0,0)
        self.gravity=9.81
        self.jump=False
        self.speed=speed

    def set_entity(self, entity):
        self.entity=entity

    def location(self):
        return (self.rect.x, self.rect.y)

    def move_by(self, vector:pygame.Vector2):
        '''Modifie la vitesse du déplacement de l'entité'''
        print(vector)
        futur_velocity=self.velocity+vector*self.speed
        vector_max=pygame.Vector2(self.speed, self.speed)
        if futur_velocity.length()<vector_max.length():
            self.velocity+=vector*self.speed
        else :
            self.velocity=vector_max

    def update(self, dt, jump=False):
        '''La méthode update permet de mettre à jour le déplacement de l'entité.'''
        new_location=self.velocity*dt
        self.rect.move_ip(new_location.x, new_location.y)
        
        self.velocity.x -= dt if self.velocity.x > 0 else 0
#        if jump :
#            self.rect.topleft += self.velocity*self.gravity
#            if self.gravity > 1 :
#                self.gravity=self.gravity/dt
#        self.velocity=pygame.Vector2(0,0)
        
        
        
        
        
        