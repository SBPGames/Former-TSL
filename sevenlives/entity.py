# -*- coding: utf-8 -*-
class Entity():
    ''' Les Entités regroupent tous les objets'''
    
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
        
    def update_component(self): # appelle les méthodes de Stinie
        #self.deplacement()
        pass
        
    def remove_component(self, element):
        self.lst_component.remove(element) # à modifier
            
class Girl():                             # Une classe fille et une
    def __init__(self):                   # mère ou une seule classe
        self.attribute= Entity("Marla")   # Humaine
        
class Mother():
    def __init__(self):
        self.attribute= Entity("?")
            
class Squirrel():
    def __init__(self):
        self.attribute= Entity("Scotty")

class Fish():
    def __init__(self):
        self.attribute= Entity("Fisher")
    
class Bird():
    def __init__(self):
        self.attribute= Entity("Piou - Piou")
    
class Pengouin():
    def __init__(self):
        self.attribut_boy= Entity("Linus")
        self.attribut_father= Entity("Unix")
    
class Bee():
    def __init__(self):
        self.attribute= Entity("Mirabelle")           
    
class Cat():
    def __init__(self):
        self.attribute= Entity("?")
    
class Bunny():
    def __init__(self):
        self.attribute= Entity("Thumber")
        
class Hazelnut():
    def __init__(self):
        self.attribute= Entity(None)
        
class Carrot():
    def __init__(self):
        self.attribute= Entity(None)