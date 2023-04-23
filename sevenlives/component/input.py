# -*- coding: utf-8 -*-

import pygame, os
from sevenlives.entity.entity import Entity
from sevenlives.component.transform import Transform

class Input():
    '''Input demande quelque chose'''

    def __init__(self):
        pass

    def set_entity(self, entity):
        self.entity=entity

    def key_down(self, key, dt): #bouton appuyé
        if key==pygame.K_RIGHT:
            self.entity.give_component(Transform).move_by(dt, pygame.Vector2(1,0))
        # if:
        # if:

    def update(self, dt):
        for event in pygame.event.get():
            if pygame.KEYDOWN == event.type:
                self.key_down(event.key, dt)