# -*- coding: utf-8 -*-

import pygame
from entity import Entity

class Component():
    
    def __init__(self):
        pass

# Location

    def location(self):
        return (self.rect.x, self.rect.y)

# Animate : Gère les images à afficher de chaque entité

    def add_image(self, function, file_name):
        '''Cette méthode peremet d'ajouter des images à la liste des images en fonction de la fonction de l'image.'''
        for picture in self.all_images:
            if picture==function and self.all_images[picture]== None:
                self.all_images[picture]=file_name

    def draw(self, surface=pygame.display.set_mode((1920, 1080)), position=(0,0)): # surface représente l'écran
        '''Cette méthode peremet de dessiner l'entité sur l'écran.'''
        surface.blit(self.image, position)


    def change_image(self, function):
        '''Cette méthode permet de changer à l'écran l'image d'une entité  en fonction de la fonction de l'image.'''
        if self.all_images[function]!= None :
            self.image=pygame.image.load(self.all_images[function])
            self.draw(surface=pygame.display.set_mode((1920, 1080)), self.location())

# Render : Modifie l'image de l'entité

    def transparent(self):
        '''Cette méthode est utilisée quand les animaux sont bléssés ou bien pour les entités de type fire'''
        pass

    def color(self):
        '''Cette méthode permet de colorer l'entité.'''
        pass

    def is_transparent(self):
        '''Cette méthode renvoie True si l'entité est transparente et False sinon.'''
        pass

# Collide : détecte des collisions:

    def verify_collide(self, entity1, entity2):
        return entity1.rect.colliderect(entity2.rect)

# Transform : gère le déplacement, la taille, la vitesse

    def move_right(self):
        self.rect.x += self.velocity # mettre des conditions pour que l'entité reste visible sur l'écran ?

    def move_left(self):
        self.rect.x -= self.velocity

    def jump(self):
        pass

    def fall(self, surface):
        '''Cette méthode est utilisée spour les arbres, les branches, les noisettes ou l'écureuil.'''
        while self.rect.y>1000 or not self.collision():
            self.image=pygame.transform.rotozoom(surface, self.velocity, 1)
            self.rect= self.image.get_rect(center=self.rect.center)
            self.rect.y+=self.velocity

    def modify_velocity(self, new_velocity):
        self.velocity=new_velocity

    def modify_size(self, x, y):
        self.image = pygame.transform.scale(self.image, (x, y))