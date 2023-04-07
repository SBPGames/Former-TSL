# -*- coding: utf-8 -*-
class Entity():
    ''' Entité est le père de tous les objets'''
    
    def __init__(self, name):
        self.lst_component=[]
        self.name=name
        
    def has_component(self, element_class):
        for elt in self.lst_component:
            if isinstance(elt, element_class):
                return True
        return False
    
    def add_component(self, element):
        self.lst_component.append(element)
        
    def update_component(self): # appelle les méthodes de Stinie + les miennes
        #self.deplacement()
        pass
        
    def remove_component(self, element):
        self.lst_component.remove(element) # à modifier   
        
#class Hazelnut():
#    def __init__(self):
#        self.attribute= Entity(None)
#        
#class Carrot():
#    def __init__(self):
#        self.attribute= Entity(None)
        
# si besoin regarder pygame.org