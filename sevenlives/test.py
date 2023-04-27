# -*- coding: utf-8 -*-

import pygame
import time

pygame.init()
surface = pygame.display.set_mode((1020, 900))
pygame.display.set_caption("Test window")


run=True
while run :
    #si joueur ferme fenêtre
    surface.blit(pygame.image.load("sevenlives\Ecureuil_1.png") , (0,0) )
    pygame.display.flip()
    time.sleep(0.2)
    surface.fill(0)
    surface.blit(pygame.image.load("sevenlives\Ecureuil_mouv.png"), (54,11))
    print()
    pygame.display.flip()
    time.sleep(0.2)
    surface.fill(0)
    for event in pygame.event.get():
        #fermeture fenêtre
        if event.type == pygame.QUIT:
            run=False
            pygame.quit()


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

# Images/Police d'écritures/Sons : sevenlives/assets
# Assets niveaux : sevenlives/assets/level/[niveau]/*
# Assets Entités : sevenlives/assets/entity/[entité]/*
# Assets UI : sevenlives/assets/UI/*

# def detecter_collision(objet1,objet2,parametres):
#         p1 = objet1.position
#         p2 = objet2.position
#         dx = p2[0]-p1[0]
#         dy = p2[1]-p1[1]
#         dz = p2[2]-p1[2]
#         d = sqrt(dx*dx+dy*dy+dz*dz)
#         if d>objet1.rayon+objet2.rayon:
#             return -1
#         return 0