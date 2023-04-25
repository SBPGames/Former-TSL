# -*- coding: utf-8 -*-

from sevenlives.entity.entity import Entity

class Squirrel():

    '''
    Squirrel est un éccureuil.
    Il peut :
    - se déplacer à gauche, à droite, sauter
    - manger une noisette
    - disparaître
    - rentrer en collision aved des arbres/ noisettes...
    - se brûler
    '''

    def __init__(self):
        self.parent=Entity("Scotty")

    def give_component(self, component_class):
        return self.parent.give_component(component_class)
        
    def has_component(self, element_class):
       return self.parent.has_component(element_class)
    
    def add_component(self, element):
        self.parent.add_component(element)
        
    def update_component(self, dt):
        '''Vérifie pour chaque component qu'il soit dans la liste, et si oui il est exécuté'''
        self.parent.update_component(dt)
        
    def remove_component(self, element):
        self.parent.remove_component(element)