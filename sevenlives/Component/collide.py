# -*- coding: utf-8 -*-

import pygame
from entity import Entity

class Collide(): 
    
    def __init__(self):
        pass

    def verify_collide(self, entity1, entity2):
        pass
        # if entity2.rect.right < entity1.rect.left and entity:
        # # rectB est à gauche return False

        # if rectB.bottom < rectA.top:
        # # rectB est au-dessus return False

        # if rectB.left > rectA.right:
        # # rectB est à droite return False

        # if rectB.top > rectA.bottom:
        # # rectB est en-dessous return False


#  position1 = entity1.location()
#         position2 = entity2.location()
#         dx = position2[0]-position1[0]
#         dy = p2[1]-p1[1]
#         dz = p2[2]-p1[2]
#         d = sqrt(dx*dx+dy*dy+dz*dz)
#         if d>objet1.rayon+objet2.rayon:
#             return False
#         return True

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