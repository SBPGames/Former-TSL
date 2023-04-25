# -*- coding: utf-8 -*-

import pygame, os
from sevenlives.utils import getAssetFolder
from sevenlives.component.transform import Transform
from sevenlives.component.animate import Animate

class Render():
    ''' défini l'image '''
    
    def __init__(self):
        self.surface=pygame.Surface((0,0))

    def set_entity(self, entity):
        self.entity=entity

    def get_image_path(self):
        return getAssetFolder("entity", self.entity.name, "unique.png")

    def draw(self, surface): # surface représente l'écran
        '''Cette méthode peremet de dessiner l'entité sur l'écran.'''
        if self.entity.has_component(Animate):
            self.entity.give_component(Animate).draw(surface)
        elif os.path.exists(self.get_image_path()) :
            surface.blit(pygame.image.load(self.get_image_path()), self.entity.give_component(Transform).location())

    def update(self, dt):
        pass