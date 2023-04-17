# -*- coding: utf-8 -*-

import pygame

class Entity():
    ''' Entité est le père de tous les objets'''
    
    def __init__(self, name, x, y, file_name):
        self.lst_component=[]
        self.name=name
        self.velocity=10
        self.image=pygame.image.load(file_name)
        self.rect= self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        
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

    # def can_do(self, component):
    #     if self.can_do.component==True # si le composant est dans liste :
    #         return False
    #     return True
        
#class Hazelnut():
#    def __init__(self):
#        self.attribute= Entity(None)
#        
#class Carrot():
#    def __init__(self):
#        self.attribute= Entity(None)
        
# si besoin regarder pygame.org

# if __name__ == "__main__":
#     import sys

#     pygame.init()
#     surface = pygame.display.set_mode((960, 540))
#     pygame.display.set_caption("Test window")

#     # Votre initialization de vos objets

#     while True:
#         for event in pygame.event.get():
#             if pygame.QUIT == event.type:
#                 pygame.quit()
#                 sys.exit()
        
#         # Vos fonctions/méthodes à appeller à chaque frame
        
#         pygame.display.update()