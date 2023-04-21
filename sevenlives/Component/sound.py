# -*- coding: utf-8 -*-

import pygame
from entity import Entity

class Sound():

    ''' défini les différents sons de chaque personnages'''

    def __init__(self):
        self.sounds={} # pygame.mixer.Sound("file_name")

    def set_entity(self, entity):
        self.entity=entity

    def play(self, sound_name):
        self.sounds[sound_name].play()