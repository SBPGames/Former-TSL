# -*- coding: utf-8 -*-

import pygame
from Entity.entity import Entity

class Animate():
    ''' défini quelle image choisir '''
    
    def __init__(self):
        pass

    def draw(self, screen, position): # screen représente l'écran
        screen.blit(self.image, self.rect)