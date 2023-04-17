# -*- coding: utf-8 -*-

import pygame

pygame.init()

# générer fenêtre du jeu

pygame.display.set_caption("Affichage du jeu test")
pygame.display.set_mode((1000,800))


run=True

while run :
    #si joueur ferme fenêtre
    for event in pygame.event.get():
        #fermeture fenêtre
        if event.type == pygame.QUIT:
            run=False
            pygame.quit()