# -*- coding: utf-8 -*-

import pygame
from Entity.entity import Entity
from location import Location

class Animate():
    '''Gère les images de chaque entité'''
    
    def __init__(self):
        pass

    def add_image(self, function, file_name):
        '''Cette méthode peremet d'ajouter des images à la liste des images en fonction de la fonction de l'image.'''
        for picture in self.all_images:
            if picture==function and self.all_images[picture]== None:
                self.all_images[picture]=file_name

    def draw(self, surface=pygame.display.set_mode((960, 540)), position=(0,0)): # surface représente l'écran
        '''Cette méthode peremet de dessiner l'entité sur l'écran.'''
        surface.blit(self.image, position)


    def change_image(self, function):
        '''Cette méthode permet de changer à l'écran l'image d'une entité  en fonction de la fonction de l'image.'''
        if self.all_images[function]!= None :
            self.image=pygame.image.load(self.all_images[function])
            self.draw(surface=pygame.display.set_mode((960, 540)), self.location())
        
