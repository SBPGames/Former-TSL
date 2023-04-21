# -*- coding: utf-8 -*-

from entity import Entity

class Mother():
    '''
    Mother est la mère de Marla.
    '''
    
    def __init__(self, position):
        self.parent=Entity("mother", position)