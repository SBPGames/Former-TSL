# -*- coding: utf-8 -*-

from entity import Entity

class Girl():

    '''Girl est une petite fille.'''

    def __init__(self, position):
        self.parent=Entity("Marla", position)