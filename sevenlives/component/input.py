# -*- coding: utf-8 -*-

import pygame
from sevenlives.component.transform import Transform

class Input():
    '''Input demande quelque chose'''

    def __init__(self):
        self.dico={
            pygame.K_RIGHT: {"pressed":False, "action": self.move, "argument": pygame.Vector2(1,0)},
            pygame.K_LEFT: {"pressed":False, "action": self.move, "argument": pygame.Vector2(-1,0)},
            pygame.K_UP: {"pressed":False, "action": self.move, "argument": pygame.Vector2(0,1)}
            }

    def set_entity(self, entity):
        self.entity=entity

    def move(self, vector):
        self.entity.give_component(Transform).move_by(vector)
        
    def update(self, dt):
        for event in pygame.event.get():
            if pygame.KEYDOWN==event.type:
                for k, v in self.dico.items():
                    if event.key==k:
                        v["pressed"]=True
            if pygame.KEYUP==event.type:
                for k, v in self.dico.items():
                    if event.key==k:
                        v["pressed"]=False
        for k, v in self.dico.items():
            if v["pressed"]:
                v["action"](v["argument"])
                
        
                
                