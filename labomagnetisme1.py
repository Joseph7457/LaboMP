
import math
import pygame
import sys

# Constantes

BLEUCLAIR = (127, 191, 255)
NOIR      = (0,0,0)
ROUGE     = (255,0,0)
#k = 8 987 600 000

# La norme de ce vecteur est égale à k|q|r2, où r est la distance qui sépare p et p′, 
# Paramètres

dimensions_fenetre = (1600, 900)  # en pixels
images_par_seconde = 25
objets = []

def ajouter_objet(x,y,z):
    objets.append((x,y,z))

ajouter_objet(800,200,1000000)
ajouter_objet(800,700,-1000000)

def print_objets():
    for o in objets:
        print(o)   


def dessiner_objets():
    for o in objets:
        if (o[2]<0):
            pygame.draw.circle(fenetre, NOIR , (o[0], o[1]), 10)
        else:
            pygame.draw.circle(fenetre, ROUGE, (o[0], o[1]), 10)

def dessiner_champ(pas):
    print("ton travail commence ici")
    x = -pas
    while(x < dimensions_fenetre[0] + pas):
        y = -pas
        while(y < dimensions_fenetre[1] + pas):
            print(x)
            print(y)
            print(" ")
            y += pas
        x += pas

dessiner_champ(50)


print_objets()
# Initialisation

pygame.init()

fenetre = pygame.display.set_mode(dimensions_fenetre)
pygame.display.set_caption("Programme 1")

horloge = pygame.time.Clock()
couleur_fond = BLEUCLAIR

# Dessin

fenetre.fill(couleur_fond)

while True:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    dessiner_objets()

    pygame.display.flip()
    horloge.tick(images_par_seconde)
