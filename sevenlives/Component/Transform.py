# -*- coding: utf-8 -*-

import pygame
from entity import Entity

class Transform():
    
    '''
    Gère le déplacement, la taille et la vitesse
    '''
    
    def __init__(self):
        pass

    def set_entity(self, entity):
        self.entity=entity

    def move_right(self):
        self.rect.x += self.velocity # mettre des conditions pour que l'entité reste visible sur l'écran ?

    def move_left(self):
        self.rect.x -= self.velocity

    def jump(self):
        pass

    def fall(self, surface):
        '''Cette méthode est utilisée spour les arbres, les branches, les noisettes ou l'écureuil.'''
        # while self.rect.y>1000 or not self.collision():
        # self.image=pygame.transform.rotozoom(surface, self.velocity, 1)
        # self.rect= self.image.get_rect(center=self.rect.center)
        self.rect.y+=self.velocity

    def modify_velocity(self, new_velocity):
        self.velocity=new_velocity

    def modify_size(self, x, y):
        self.image = pygame.transform.scale(self.image, (x, y))