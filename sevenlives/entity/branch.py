# -*- coding: utf-8 -*-

from entity import Entity

class Branch():

    '''
    Branch est une branche.
    Elles peut :
    - tomber
    - se bruler'''
    
    def __init__(self, position):
        self.parent=Entity("branch", position)