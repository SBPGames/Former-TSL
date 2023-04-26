# -*- coding: utf-8 -*-

import pygame

class Transform():
    
    '''
    Gère le déplacement, la taille et la vitesse.
    '''
    
    def __init__(self, vector:pygame.Vector2, speed=5):
        self.rect=pygame.Rect(vector.x, vector.y, 0, 0)
        self.velocity=pygame.Vector2(0,0)
        self.gravity=9.81
        self.is_jump=False
        self.speed=speed
        self.x_direction=0

    def set_entity(self, entity):
        self.entity=entity

    def location(self):
        return (self.rect.x, self.rect.y)
    
    def set_x_direction(self, x:int):
        self.x_direction=x if x in [-1, 1] else 0

    # def move_towards(self, vector:pygame.Vector2):
    #     '''Modifie la vitesse du déplacement de l'entité'''
    #     vector=vector.normalize()
    #     futur_velocity=self.velocity+vector*self.speed
    #     vector_max=pygame.Vector2(self.speed, self.speed)
    #     if futur_velocity.length()<vector_max.length():
    #         self.velocity+=vector*self.speed
    #     else :
    #         self.velocity=vector_max

    def jump(self, vector=pygame.Vector2(0,-1)):
        self.velocity+=vector*self.gravity

    def update(self, dt, jump=False):
        '''La méthode update permet de mettre à jour le déplacement de l'entité.'''
        new_location=self.velocity*dt
        self.rect.move_ip(self.x_direction*self.speed*dt, new_location.y)



    # Gérer le saut dans Transform
        
        
        
        