#!/usr/bin/python36
#1b-dic.py
# Jeu du plus ou moins
# Author: Loris Catallo
# Date: 23/10/2018
from random import *

i=0

nbpif = randint(0, 100)
print("Bienvenue dans ce jeu du Plus ou moins")
nb1=int(input("Veuillez rentrer un nombre : "))


while nb1 != nbpif:
  if nb1 < nbpif:
     print("C'est plus !")
  if nb1 > nbpif:
     print("C'est moins !")
  nb1=int(input("Veuillez rentrer un nombre :"))
  i = i + 1
print("Nombre de coups necessaires :")
print(i)
print("Au revoir et bonne fin de journee, du con")

