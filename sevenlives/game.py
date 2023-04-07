# -*- coding: utf-8 -*-
import pygame
import sys

class TheSevenLives:
    def __init__(self,titre,mode="jeu"):
        assert mode=="dev" or mode=="jeu"
        
        pygame.init()
        
        if mode=="dev":
            pygame.display.set_mode((1024,576))
        else:
            pygame.display.set_mode()
        
        pygame.display.set_caption(titre)
        
        self.clock=pygame.time.Clock()
    
    def update(self,delta_time):
        pass
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
            delta_time=self.clock.tick()
            self.update(delta_time)
            pygame.display.update()
    def getwidth(self):
        return pygame.display.Info().current_w
    def getheight(self):
        return pygame.display.Info().current_h