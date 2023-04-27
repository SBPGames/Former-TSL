# -*- coding: utf-8 -*-

import pygame, os
from sevenlives.component.location import Location

class Render():
    ''' défini l'image '''
    
    def __init__(self):
        self.surface=pygame.Surface((0,0))

    def set_entity(self, entity):
        self.entity=entity

    def get_image_path(self):
        return f"sevenlives/assets/entity/{self.entity.name}/unique.png"

    def draw(self, surface): # surface représente l'écran
        '''Cette méthode peremet de dessiner l'entité sur l'écran.'''
        if os.path.exists(self.get_image_path()) :
            surface.blit(pygame.image.load(self.get_image_path()), self.entity.give_component(Location).location())
        #surface.blit(self.surface, self.entity.give_component(Location).location())

    def transparent(self):
        '''Cette méthode est utilisée quand les animaux sont bléssés ou bien pour les entités de type fire'''
        self.image.set_colorkey((255,255,255)) # pas sûr

    def color(self, num_color):
        '''Cette méthode permet de colorer l'entité.'''
        self.image.set_colorkey(num_color)

    def is_transparent(self):
        '''Cette méthode renvoie True si l'entité est transparente et False sinon.'''
        return self.image.get_colorkey()
    
    def update(self, dt):
        pass