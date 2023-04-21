# -*- coding: utf-8 -*-

import pygame

from Component.sound import Sound
from component import move_right
from Component.transform import move_left
from Component.transform import jump

class Entity():
    ''' Entité est le père de tous les objets'''
    
    def __init__(self, name, position):
        self.lst_component=[]
        self.name=name
        self.velocity=5
        #self.all_images={"first_image":"sevenlives/assets/entity/{"name".id}/{idle/run/burn}/{0/1/2}.png", "move_right":None, "move_left":None, "jump":None, "burnt": None, "other_option":None}
        #self.image= pygame.image.load("sevenlives/assets/entity/{entity.id}.png/") #.convert_alpha()
        # remettre image à bonnes dimensions : self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect= self.image.get_rect()
        self.rect.x=position[0]
        self.rect.y=position[1]
        self.sound=Sound()
        
    def has_component(self, element_class):
        for elt in self.lst_component:
            if isinstance(elt, element_class):
                return True
        return False
    
    def add_component(self, element):
        self.lst_component.append(element)
        
    def update_component(self, right=False, left=False, jump=False, fall=False): # ???
        '''Vérifie pour chaque component qu'il soit dans la liste, et si oui il est exécuté'''
        if right:
            self.move_right()
        elif left:
            self.move_left()
        elif jump:
            self.jump
        elif fall:
            self.fall     
        
    def remove_component(self, element):
        if self.has_component(element):
            self.lst_component.remove(element) # à modifier