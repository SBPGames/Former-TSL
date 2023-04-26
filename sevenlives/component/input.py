# -*- coding: utf-8 -*-

import pygame
from sevenlives.component.transform import Transform

class Input():
    '''Input demande quelque chose'''

    def __init__(self):
        pass

    def set_entity(self, entity):
        self.entity=entity

    def update(self, dt):
        lst_keys_pushed=pygame.key.get_pressed()
   
        if lst_keys_pushed[pygame.K_RIGHT]:
            self.entity.give_component(Transform).set_x_direction(1)
        elif lst_keys_pushed[pygame.K_LEFT]:
            self.entity.give_component(Transform).set_x_direction(-1)
        elif lst_keys_pushed[pygame.K_SPACE]:
            self.entity.give_component(Transform).is_jump=True
        else :
            self.entity.give_component(Transform).set_x_direction(0)        