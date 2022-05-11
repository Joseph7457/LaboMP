#Ricardo Ono Coimbra #La belle
#Joseph Gabriel      #La bête
#Roxane Nashroudi    #Et le truand
import math
import pygame
import sys
import random
pygame.init()

# Constantes

BLEUCLAIR = (127, 191, 255)
NOIR      = (0,0,0)
ROUGE     = (255,0,0)
A = 2
B = 5
C = 20
k = 8.9876 * pow(10,9)


LARGEUR = 900
HAUTEUR = 600
dimensions_fenetre = (LARGEUR, HAUTEUR) # en pixels
images_par_seconde = 50
objets = []
champ_electrique_v = 10

CLIC = 100
RAYON = 10
NOIR = (0,0,0)

mobile_est_present         = False
mobile_x                   = dimensions_fenetre[0]/2
mobile_y                   = dimensions_fenetre[1]/2
mobile_vx                  = 0
mobile_vy                  = 0
mobile_charge              = 10**(-10)
mobile_masse               = 10**(-10)
mobile_energie_cinetique   = 0

champ_magnetique = 1
#mobile_energie_potentielle = 0

#potentiel_souris = 0

temps_maintenant = pygame.time.get_ticks()

police  = pygame.font.SysFont("monospace", 16)


def calculer_potentiel(x, y):
    potentiel = 0

    for o in objets:
        r = math.sqrt( (x - o[0])**2 + (y - o[1])**2 )
        if(r != 0):
            potentiel += k*o[2]/r

    r = math.sqrt( (x - mobile_x)**2 + (y - mobile_y)**2 )
    if(r != 0):
        potentiel += k*mobile_charge/r
    return potentiel



"""def calculer_energie_potentielle(x, y, charge):
    energie = 0
    if mobile_est_present:
        for o in objets:
            r = math.sqrt( (mobile_x - o[0])**2 + (mobile_y - o[1])**2 )
            if(r != 0):
                energie += k*o[2]*charge/r
        return energie/10
    else:
        return 0
"""


def calculer_energie_cinetique(masse, vx, vy):

    if mobile_est_present:
        norme = math.sqrt( vx * vx + vy * vy)
        energie = masse * norme * norme / 2
        return energie/10
    else:
        return 0



def mettre_a_jour_mobile(t):
    global mobile_x, mobile_y, mobile_vx, mobile_vy, mobile_est_present

    Fx = 0
    Fy = 0
    champElectrique     = calculer_champ_electrique(mobile_x,mobile_y)

    if(champElectrique):

        Fx += champElectrique[0] * mobile_charge
        Fy += champElectrique[1] * mobile_charge

    else:
        mobile_est_present   = False

    v = norme_vecteur(mobile_vx, mobile_vy);
    angle = calculer_angle(mobile_vx, mobile_vy)   
    Fl = mobile_charge * v * champ_magnetique
    Fla = angle + math.pi/2

    Flx = Fl * math.cos(Fla)
    Fly = Fl * math.sin(Fla)
    Fx += Flx
    Fy += Fly
    acceleration        = [ Fx/mobile_masse, Fy/mobile_masse ]

    print(" ")
    print("v: " + str(v))
    print("vx: " + str(mobile_vx))
    print("vy: " + str(mobile_vy))
    print("va: " + str(angle))
    print("Fl : " + str(Fl))
    print("Flx : " + str(Flx))
    print("Fly : " + str(Fly))
    print("Fla : " + str(Fla))
    print("Fx: " + str(Fx))
    print("Fy" + str(Fy)) 
    print("Acceleration X " + str(acceleration[0]))
    print("Acceleration Y " + str(acceleration[1])) 

    
    mobile_vx           +=  acceleration[0] * t
    mobile_vy           +=  acceleration[1] * t
    mobile_x            +=  mobile_vx * t 
    mobile_y            +=  mobile_vy * t


def tableau_de_bord(champ_electrique_v, ec):
    texte_1 = "champ electrique: {0:.2f} V/m".format(champ_electrique_v)
    image_1 = police.render(texte_1, True, NOIR)
    fenetre.blit(image_1, (dimensions_fenetre[0]//20, dimensions_fenetre[1]//20))
    texte_2 = "champ magnétique: {0:.2f} T".format(champ_magnetique)
    image_2 = police.render(texte_2, True, NOIR)
    fenetre.blit(image_2, (dimensions_fenetre[0]//20, 2*dimensions_fenetre[1]//20))
    texte_3 = "energie cinétique: {0:.2f} µJ".format(ec)
    image_3 = police.render(texte_3, True, NOIR)
    fenetre.blit(image_3, (dimensions_fenetre[0]//20, 3*dimensions_fenetre[1]//20))


    """texte_2 = "energie potentielle: {0:.2f} ".format(ep)
    image_2 = police.render(texte_2, True, NOIR)
    fenetre.blit(image_2, (dimensions_fenetre[0]//20, (dimensions_fenetre[1]//20) + 50 ))

    texte_3 = "energie totale: {0:.2f} ".format(ep+ec)
    image_3 = police.render(texte_3, True, NOIR)
    fenetre.blit(image_3, (dimensions_fenetre[0]//20, (dimensions_fenetre[1]//20) + 100))

    texte_4 = "potentiel souris: {0:.2f} ".format(ps)
    image_4 = police.render(texte_4, True, NOIR)
    fenetre.blit(image_4, (dimensions_fenetre[0]//20, (dimensions_fenetre[1]//20) + 150))"""


def dessiner_mobile():
    if (mobile_est_present):
        if(mobile_charge >= 0 ):
            couleur = (255,0,0)
        else:
            couleur = (0,0,0)

        pygame.draw.circle(fenetre, couleur, (mobile_x, mobile_y), 10, 4)



"""def ajouter_objet(x,y,z, vx, vy):
    objets.append([x,y,z, vx, vy])"""

"""def print_objets():
    for o in objets:
        print(o)"""


def dessiner_objets():
    for o in objets:
        if (o[2]<0):
            pygame.draw.circle(fenetre, NOIR , (o[0], o[1]), RAYON)
        else:
            pygame.draw.circle(fenetre, ROUGE, (o[0], o[1]), RAYON)


"""def bouger_objets():
    for o in objets:
        o[0] += o[3]
        o[1] += o[4]

        if (o[0] < 0):
            o[0] = LARGEUR
        if (o[0] > LARGEUR):
            o[0] = 0

        if (o[1] < 0):
            o[1] = HAUTEUR
        if (o[1] > HAUTEUR):
            o[1] = 0"""

        #print(o)
def calculer_angle(vx, vy):
 
    if(vx == 0):
        if(vy > 0):
            return math.pi/2
        else:
            return -math.pi/2
    else:
        return (math.atan(vy/vx))

    """
    On a : tan b^ = [AC][AB] = 57.
On obtient la valeur de b^ en utilisant la fonction inv tan de la calculatrice.
b^ = 35° (à un degré près par défaut).

"""


def norme_vecteur(x, y):
    a = x*x + y*y
    return math.sqrt(a)

def normer_vecteur(tailleMax, v):
    norme   = math.sqrt(v[0]*v[0] + v[1]*v[1])
    vecteur = [0,0]
    if (norme !=0):
        vecteur = [ v[0]*tailleMax/norme, v[1]*tailleMax/norme ]
    return vecteur


def calculer_champ_electrique(x,y):

    norme = 0
    v = [0,0]

    for o in objets:
        r     = math.sqrt( (x-o[0]) * (x-o[0]) + (y-o[1]) * (y-o[1]) )
        if(r > 20):
            norme = k * abs(o[2]) / (r*r)
        else:
            return None
        angle = math.atan2( (y-o[1]), (x-o[0]) )

        if (o[2]<0):
            vtemp = (-norme * math.cos(angle) , -norme * math.sin(angle))
        else:
            vtemp = (norme * math.cos(angle) , norme * math.sin(angle))


        v[0] += vtemp[0]
        v[1] += vtemp[1]

    return (0, -champ_electrique_v)


# print_objets()
# Initialisation


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
        elif evenement.type == pygame.KEYDOWN:

            x_souris, y_souris = pygame.mouse.get_pos()

            if (evenement.key == pygame.K_UP and champ_electrique_v <= 100):
                champ_electrique_v += 1
            elif (evenement.key == pygame.K_DOWN and champ_electrique_v >= -100):
                champ_electrique_v -= 1
            elif (evenement.key == pygame.K_SPACE and champ_electrique_v >= -100):
                mobile_x                   = dimensions_fenetre[0]/2
                mobile_y                   = dimensions_fenetre[1]/2
                mobile_vx                  = 0  
                mobile_vy                  = 0


    #mobile_x           = dimensions_fenetre[0]/2
    #mobile_y           = dimensions_fenetre[1]/2
    mobile_est_present = True

    fenetre.fill(couleur_fond)

    #position_souris = pygame.mouse.get_pos()
    delta_time = pygame.time.get_ticks() - temps_maintenant  
    t_seconde  = delta_time / 1000
    print("t = " + str(t_seconde))
    mettre_a_jour_mobile(t_seconde)

    mobile_energie_cinetique   = calculer_energie_cinetique(mobile_masse, mobile_vx, mobile_vy)
    ec = mobile_energie_cinetique * pow(10,6)

    tableau_de_bord(champ_electrique_v, ec)
    #mobile_energie_potentielle = calculer_energie_potentielle(mobile_x, mobile_y, mobile_charge)

    temps_maintenant = pygame.time.get_ticks()


    dessiner_mobile()
    #bouger_objets()
    dessiner_objets()


    pygame.display.flip()
    horloge.tick(images_par_seconde)

