# -*- coding: utf-8 -*-

from entity import Entity

class Tree():

    '''
    Tree est un arbre.
    Il peut tomber / se brûler'''

    def __init__(self, position):
        self.parent=Entity("tree", position)