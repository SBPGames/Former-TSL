# -*- coding: utf-8 -*-

import pygame, os
from sevenlives.utils import getAssetFolder
from sevenlives.entity.entity import Entity
from sevenlives.component.transform import Transform

class Animate():

    '''Gère les images et les animations de chaque entité'''
    
    def __init__(self):
        self.dico_status={}
        self.status_actual="walk"
        self.index_actual=0
        self.time=0

    # sevenlives/assets/entity/{entity.name}/{idle/run/burn}/{0/1/2}.png 

    def get_assets_folder(self, anim=None):
        return getAssetFolder("entity", self.entity.name, anim)

    def set_entity(self, entity):
        '''Une méthode pour définir l'entité (C'est à cet endroit que l'on charge les images)'''
        self.entity=entity
        for dossier in filter(lambda d: os.path.isdir(self.get_assets_folder(d)), os.listdir(self.get_assets_folder())):
            self.dico_status[dossier]=[]
            for image in os.listdir(self.get_assets_folder(dossier)):
                if image.endswith(".png"):
                    self.dico_status[dossier].append(pygame.image.load(os.path.join(self.get_assets_folder(dossier), image)))

    def draw(self, surface):
        '''Dessine l'image de l'entité'''
        surface.blit(self.dico_status[self.status_actual][self.index_actual], self.entity.give_component(Transform).location())

    def change_status(self, status="idle"):
        '''Une méthode pour changer de status (Via un attribut : status actuel ? + Remettre l'index image à 0)'''
        self.index_actual=0
        self.status_actual=status

    def next_image(self):
        '''Une méthode pour faire avancer l'animation (Index image + 1 ou = 0 si maximum atteint'''
        if self.index_actual<len(self.dico_status[self.status_actual])-1:
            self.index_actual +=1
        else :
            self.index_actual=0

    def update(self, dt):
        self.time+=dt
        if self.time>1/4:
            self.next_image()
            self.time=0