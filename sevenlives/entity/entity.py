# -*- coding: utf-8 -*-

import pygame

class Entity():
    
    ''' Entité est le père de tous les objets'''
    
    def __init__(self, name):
        self.lst_component=[]
        self.name=name
        #self.all_images={"first_image":"sevenlives/assets/entity/{"name".id}/{idle/run/burn}/{0/1/2}.png", "move_right":None, "move_left":None, "jump":None, "burnt": None, "other_option":None}
        #self.image= pygame.image.load("sevenlives/assets/entity/{entity.id}.png/") #.convert_alpha()
        # remettre image à bonnes dimensions : self.image = pygame.transform.scale(self.image, (32, 32))
        
    def give_component(self, component_class):
        if self.has_component(component_class):
            for component in self.lst_component:
                if isinstance(component, component_class):
                    return component
        
    def has_component(self, element_class):
        for elt in self.lst_component:
            if isinstance(elt, element_class):
                return True
        return False
    
    def add_component(self, element):
        element.set_entity(self)
        self.lst_component.append(element)
        
    def update_component(self, dt):
        '''Vérifie pour chaque component qu'il soit dans la liste, et si oui il est exécuté'''
        for component in self.lst_component:
            component.update(dt)
    # def update_component(self, dt):
    #     '''Vérifie pour chaque component qu'il soit dans la liste, et si oui il est exécuté'''
    #     for component in self.lst_component:
    #         component.update(dt)
        # '''Vérifie pour chaque component qu'il soit dans la liste, et si oui il est exécuté'''
        # for component in self.lst_component:
        #     component.update(dt)   
        
    def remove_component(self, element):
        if self.has_component(element):
            self.lst_component.remove(element) # à modifier