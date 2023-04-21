# -*- coding: utf-8 -*-

import pygame
from entity import Entity

class Render():
    ''' défini l'image '''
    
    def __init__(self):
        pass

    def draw(self, surface=pygame.display.set_mode((1920, 1080)), position=(0,0)): # surface représente l'écran
        '''Cette méthode peremet de dessiner l'entité sur l'écran.'''
        surface.blit(self.image, position)

    def transparent(self):
        '''Cette méthode est utilisée quand les animaux sont bléssés ou bien pour les entités de type fire'''
        self.image.set_colorkey((255,255,255)) # pas sûr

    def color(self, num_color):
        '''Cette méthode permet de colorer l'entité.'''
        self.image.set_colorkey(num_color)

    def is_transparent(self):
        '''Cette méthode renvoie True si l'entité est transparente et False sinon.'''
        return self.image.get_colorkey()