# -*- coding: utf-8 -*-

from entity import Entity

class Bubble():

    '''Bubble sont est une bulle.
    Elle peut apparaaître/disparaître'''

    def __init__(self, position):
        self.parent=Entity("bubble", position)