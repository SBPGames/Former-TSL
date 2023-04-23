# -*- coding: utf-8 -*-

from entity import Entity

class Camera():

    '''Camera est une entité qui défini un champ de vision et qui informe si une entité est ou non dans son chmpas de vision.'''

    def __init__(self):
        self.parent=Entity("camera")

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
