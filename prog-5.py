# ------------------------------------------------------------------------
# Laboratoires de programmation mathématique et physique 2
# ------------------------------------------------------------------------
#
# Programme : 7 segments.
#
# ------------------------------------------------------------------------
#Joseph Gabriel
#Ricardo Ono Coimbra
#Roxane Nashroudi

import datetime as dt
import math
import pygame
import sys
import numpy as np

### Constante(s)

NOIR = (0, 0, 0)
GRIS = (200, 200, 200)
ROUGE = (255, 0, 0)

num_afficheur = 0

### Variables Globales
valeur_memorisee = 2


def dessiner_arduino(sortie_arduino, sortie_CD4511, sortie_CD4028, sortie_bouton):
    fenetre.blit(image_arduino, pos_arduino)
    fenetre.blit(image_CD4511, pos_CD4511)
    fenetre.blit(image_bouton, pos_bouton)
    fenetre.blit(image_CD4028, pos_CD4028)


    for j in range(0, 2):
        if j == 0:
            off_ard = 285
            off_cd = 15
            pos_carte = pos_CD4511
            r = range(0, 4)

        if j == 1:
            off_ard = 194
            off_cd = 91
            pos_carte = pos_CD4028
            r = range(4, 8)

        for i in r:
            if sortie_arduino[i] == 0:
                couleur = NOIR
            else:
                couleur = ROUGE

            pygame.draw.line(fenetre, couleur, (pos_arduino[0] + 280, pos_arduino[1] + off_ard),
                            (pos_carte[0] + 7, pos_carte[1] + off_cd), 5)
            off_ard = off_ard + 14
            off_cd = off_cd + 19



    off_cd = 15
    off_aff = 5
    i = 0
    for i in range(0, 7):
        if sortie_CD4511[i] == 0:
            couleur = NOIR
        else:
            couleur = ROUGE
        pygame.draw.line(fenetre, couleur, (pos_afficheur[0] + 591, pos_afficheur[1] + off_aff),
                        (pos_CD4511[0] + 102, pos_CD4511[1] + off_cd), 5)
        off_aff = off_aff + 19
        off_cd = off_cd + 19


    if sortie_bouton == 0:
        couleur = NOIR
    else:
        couleur = ROUGE
    pygame.draw.line(fenetre, couleur, (pos_arduino[0] + 279, pos_arduino[1] + 353),
                        (pos_bouton[0] + 13, pos_bouton[1] + 13), 5)

    i = 0
    off_cd = (102, 111)
    off_aff = 44
    for i in range(0, 6):
        if sortie_CD4028[i] == 0:
            couleur = NOIR
        else:
            couleur = ROUGE
        pygame.draw.line(fenetre, couleur, (pos_CD4028[0] + off_cd[0], pos_CD4028[1] + off_cd[1]),
                        (pos_afficheur[0] + off_aff, pos_CD4028[1] + off_cd[1]), 5)

        pygame.draw.line(fenetre, couleur, (pos_afficheur[0] + off_aff, pos_afficheur[1]),
                        (pos_afficheur[0] + off_aff, pos_CD4028[1] + off_cd[1] - 2), 5)
        off_cd = (off_cd[0], off_cd[1] - 20)
        off_aff = off_aff + 101



def dessiner_afficheur(sortie_CD4511, sortie_CD4028):
    positions_barres = [[32, 14], [89, 20], [87, 88], [28, 150],
                        [17, 88], [19, 20], [30, 82]]

    for j in range(0, 6):
        fenetre.blit(image_afficheur_s, (pos_afficheur[0] + j*101, pos_afficheur[1]))

        if sortie_CD4028[j] == 1:
            latence_mat[j]  = sortie_CD4511
  
        i = 0
        for barre in positions_barres:
                if latence_mat[j][i] == 0:
                    i = i + 1
                    continue
                x_b = j*101 + pos_afficheur[0] + int(round(barre[0]*(image_afficheur_s.get_width()/133)))
                y_b = pos_afficheur[1] + int(round(barre[1]*(image_afficheur_s.get_height()/192)))
                if i == 0 or i == 3 or i == 6:
                    fenetre.blit(barre_horizontale_s, (x_b, y_b))
                else:
                    fenetre.blit(barre_verticale_s, (x_b, y_b))
                i = i + 1
    return

def composant_CD4511(entree):
    tdv = np.array([[1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 1, 1, 0, 0, 1, 1], [1, 0, 1, 1, 0, 1, 1], [1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 1, 1]])
    decimal = 0
    i = 0
    while(i < 4):
        if(entree[3-i] == 1):
            decimal = decimal + pow(2, i)
        i = i + 1
    return tdv[decimal]


def composant_CD4028(entree):
    tdv = np.array([[1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 0, 0, 1]]) 
                   
    return tdv[entree];


def sortie_memorisee(sortie, temps):
    list     = [0, 0, 0, 0]
    position = [0, 0, 0, 0]

    valeur = temps
    i = 3
    while(i >= 0):
        if(valeur > 0):
            list[i] = valeur%2
            valeur  = valeur//2
        if(sortie > 0):
            position[i] = sortie%2
            sortie      = sortie//2
            
        i = i-1
    numpyList = np.array(list+position)
    return numpyList

def gerer_click():
    return 0


def connexion_bouton(sortie_bouton):
    if(sortie_bouton == 0):
        pygame.draw.line(fenetre, NOIR, pin_arduino, pin_bouton, 5)
    else:
        pygame.draw.line(fenetre, ROUGE, pin_arduino, pin_bouton, 5)

    return sortie_bouton

def mettre_a_jour_vecteur_horloge():

    global vecteur_horloge

    heure    = dt.datetime.now().hour    
    minutes  = dt.datetime.now().minute
    secondes = dt.datetime.now().second

    i        = 2
    while( i > 0 ):
        if (heure >= i*10):
            vecteur_horloge[0] = i
            heure -= i*10
        i -= 1
    vecteur_horloge[1] = heure
        
    i        = 6
    while( i > 0 ):
        if (minutes >= i*10):
            vecteur_horloge[2] = i
            minutes -= i*10
        i -= 1
    vecteur_horloge[3] = minutes

    i        = 6
    while( i > 0 ):
        if (secondes >= i*10):
            vecteur_horloge[4] = i
            secondes -= i*10
        i -= 1
    vecteur_horloge[5] = secondes
     

    vecteur_horloge[1] = heure
    print(vecteur_horloge)


#paramètres
dimensions_fenetre = (1100, 600)  # en pixels
images_par_seconde = 25

pos_arduino = (0, 70)
pos_CD4511 = (333, 340)
pos_CD4028 = (333, 128)
pos_afficheur = (500, 350)
pos_bouton = (333, 524)
pos_centre_bouton = (pos_bouton[0] + 51, pos_bouton[1] + 34)
rayon_bouton = 18
pin_arduino = (pos_arduino[0] + 279, pos_arduino[1] + 353)
pin_bouton = (pos_bouton[0] + 13, pos_bouton[1] + 13)

temps_avant     = 0;
latence_mat     = [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]
vecteur_horloge = [0,0,0,0,0,0]
index_v_h       = 0

### Programme

# Initialisation

pygame.init()

temps = 500
sig_horloge     = 0
sig_horloge_num = 0
pygame.time.set_timer(pygame.USEREVENT, temps)

fenetre = pygame.display.set_mode(dimensions_fenetre)
pygame.display.set_caption("Programme 7 segments")

horloge = pygame.time.Clock()

image_afficheur_s = pygame.image.load('images/7_seg_s.png').convert_alpha(fenetre)
barre_verticale_s = pygame.image.load('images/vertical_s.png').convert_alpha(fenetre)
barre_horizontale_s = pygame.image.load('images/horizontal_s.png').convert_alpha(fenetre)
image_afficheur = pygame.image.load('images/7_seg.png').convert_alpha(fenetre)
barre_verticale = pygame.image.load('images/vertical.png').convert_alpha(fenetre)
barre_horizontale = pygame.image.load('images/horizontal.png').convert_alpha(fenetre)
image_arduino = pygame.image.load('images/arduino.png').convert_alpha(fenetre)
image_CD4511 = pygame.image.load('images/CD4511.png').convert_alpha(fenetre)
image_CD4028 = pygame.image.load('images/CD4028.png').convert_alpha(fenetre)
image_bouton = pygame.image.load('images/bouton.png').convert_alpha(fenetre)
couleur_fond = GRIS

temps = 0

# Boucle principale

while True:

    temps_maintenant = pygame.time.get_ticks()
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if(evenement.type == pygame.MOUSEBUTTONDOWN):
            pos = pygame.mouse.get_pos()
            if(((pos_centre_bouton[0] - rayon_bouton) < pos[0] < (pos_centre_bouton[0] + rayon_bouton)) and ((pos_centre_bouton[1] - rayon_bouton) < pos[1] < (pos_centre_bouton[1] + rayon_bouton))):
                valeur_memorisee = valeur_memorisee + 1
        if (evenement.type == pygame.USEREVENT):
            sig_horloge += 0.5
            if(sig_horloge >= 1):
                num_afficheur = num_afficheur + 1
                valeur_memorisee = valeur_memorisee + 1
                sig_horloge = 0

    temps_avant = temps_maintenant

    sortie_bouton = 0
    if (valeur_memorisee >= 10):
        valeur_memorisee = 0
    if (num_afficheur >= 6):
        num_afficheur = 0
    fenetre.fill(couleur_fond)


    mettre_a_jour_vecteur_horloge()

    sortie_CD4511 = composant_CD4511(sortie_memorisee(num_afficheur, vecteur_horloge[num_afficheur]))
    sortie_CD4028 = composant_CD4028(num_afficheur)

    dessiner_arduino(sortie_memorisee(num_afficheur, vecteur_horloge[num_afficheur]), sortie_CD4511, sortie_CD4028, sortie_bouton)
    dessiner_afficheur(sortie_CD4511, sortie_CD4028)







    pygame.display.flip()
    horloge.tick(images_par_seconde)
