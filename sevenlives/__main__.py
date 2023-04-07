# -*- coding: utf-8 -*-
from sevenlives.game import TheSevenLives

devlop=input("Voulez vous activer le mode dévelopeur ? réponse possible: 'oui' ou 'non' : ")
if devlop=="oui":
    devlop = "dev"
else:
    devlop = "jeu"


jeu=TheSevenLives("7lives", devlop)
print(jeu.getheight())
print(jeu.getwidth())
jeu.run()