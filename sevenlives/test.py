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