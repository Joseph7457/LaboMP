#  ██████   ██████  ███    ██ ██    ██ ███████ 
#  ██   ██ ██    ██ ████   ██ ██    ██ ██      
#  ██████  ██    ██ ██ ██  ██ ██    ██ ███████ 
#  ██   ██ ██    ██ ██  ██ ██ ██    ██      ██ 
#  ██████   ██████  ██   ████  ██████  ███████ 

"""
https://patorjk.com/software/taag/#p=display&c=bash&f=ANSI%20Regular&t=INITIALISATION

"""
#  ██      ██ ██████  ██████   █████  ██ ██████  ██ ███████ 
#  ██      ██ ██   ██ ██   ██ ██   ██ ██ ██   ██ ██ ██      
#  ██      ██ ██████  ██████  ███████ ██ ██████  ██ █████   
#  ██      ██ ██   ██ ██   ██ ██   ██ ██ ██   ██ ██ ██      
#  ███████ ██ ██████  ██   ██ ██   ██ ██ ██   ██ ██ ███████ 

import pygame
import math

#   ██████  ██████  ███    ██ ███████ ████████  █████  ███    ██ ████████ ███████ 
#  ██      ██    ██ ████   ██ ██         ██    ██   ██ ████   ██    ██    ██      
#  ██      ██    ██ ██ ██  ██ ███████    ██    ███████ ██ ██  ██    ██    █████   
#  ██      ██    ██ ██  ██ ██      ██    ██    ██   ██ ██  ██ ██    ██    ██      
#   ██████  ██████  ██   ████ ███████    ██    ██   ██ ██   ████    ██    ███████ 


noir  = (0  ,  0,  0)
blanc = (255,255,255)
rouge = (255,  0,  0)
bleu  = (  0,  0,255)
vert  = (  0,255,  0)
fond  = (230,230,230)


#  ███████ ███████ ███    ██ ███████ ████████ ██████  ███████ 
#  ██      ██      ████   ██ ██         ██    ██   ██ ██      
#  █████   █████   ██ ██  ██ █████      ██    ██████  █████   
#  ██      ██      ██  ██ ██ ██         ██    ██   ██ ██      
#  ██      ███████ ██   ████ ███████    ██    ██   ██ ███████


(largeur, hauteur) = (1000, 800)
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.flip()


#  ████████ ███████ ███    ███ ██████  ███████ 
#     ██    ██      ████  ████ ██   ██ ██      
#     ██    █████   ██ ████ ██ ██████  ███████ 
#     ██    ██      ██  ██  ██ ██           ██ 
#     ██    ███████ ██      ██ ██      ███████ 

horloge = pygame.time.Clock()


#  ██████   ██████  ████████  ██████  ██████  
#  ██   ██ ██    ██    ██    ██    ██ ██   ██ 
#  ██████  ██    ██    ██    ██    ██ ██████  
#  ██   ██ ██    ██    ██    ██    ██ ██   ██ 
#  ██   ██  ██████     ██     ██████  ██   ██ 


angle_moteur = 0

position_cercle_exterieur     = [ 500 , 400 ]
position_cerclounet_interne   = [ 0 , 0 ]

rayon_cercle_exterieur   = 100
rayon_cerclounet_interne = 15

couleur_cercle_externe     = (80,80,80)
couleur_cerclounet_interne = (180,155,180)

distance_cerclounet = 0.7 * rayon_cercle_exterieur

def calculer_position_cerclounet_interne():
    global position_cerclounet_exterieur

    position_cerclounet_interne[0] =  position_cercle_exterieur[0] + ( math.cos(angle_moteur) * distance_cerclounet )
    position_cerclounet_interne[1] =  position_cercle_exterieur[1] + ( math.sin(angle_moteur) * distance_cerclounet )

def afficher_rotor():

    calculer_position_cerclounet_interne()

    pygame.draw.circle(fenetre, couleur_cercle_externe, position_cercle_exterieur, rayon_cercle_exterieur )
    pygame.draw.circle(fenetre, (0,0,0) , position_cercle_exterieur, rayon_cercle_exterieur, 8 )

    pygame.draw.circle(fenetre, couleur_cerclounet_interne, position_cerclounet_interne, rayon_cerclounet_interne )
    pygame.draw.circle(fenetre, (0,0,0), position_cerclounet_interne, rayon_cerclounet_interne, 6 )


#   █████  ██ ███    ███  █████  ███    ██ ████████ 
#  ██   ██ ██ ████  ████ ██   ██ ████   ██    ██    
#  ███████ ██ ██ ████ ██ ███████ ██ ██  ██    ██    
#  ██   ██ ██ ██  ██  ██ ██   ██ ██  ██ ██    ██    
#  ██   ██ ██ ██      ██ ██   ██ ██   ████    ██    


espacement = 130

taille_aimant = [200, 300]
rayon_cercle = rayon_cercle_exterieur * 1.5

position_aimant_gauche = [ position_cercle_exterieur[0] - espacement - taille_aimant[0]/2, position_cercle_exterieur[1] - taille_aimant[1]/2]
position_aimant_droit  = [ position_cercle_exterieur[0] + espacement - taille_aimant[0]/2, position_cercle_exterieur[1] - taille_aimant[1]/2]
position_cercle        = [ position_cercle_exterieur[0] , position_cercle_exterieur[1]]

couleur_aimant_gauche = rouge
couleur_aimant_droit  = bleu
couleur_cercle        = fond



def afficher_aimants():

    pygame.draw.rect  (fenetre, couleur_aimant_gauche, pygame.Rect(position_aimant_gauche, taille_aimant)) 
    pygame.draw.rect  (fenetre, couleur_aimant_droit , pygame.Rect(position_aimant_droit, taille_aimant)) 
    pygame.draw.circle(fenetre, fond                 , position_cercle, rayon_cercle)
 



#  ██████   ██████   ██████  ██      ███████ ███████ ███    ██ 
#  ██   ██ ██    ██ ██    ██ ██      ██      ██      ████   ██ 
#  ██████  ██    ██ ██    ██ ██      █████   █████   ██ ██  ██ 
#  ██   ██ ██    ██ ██    ██ ██      ██      ██      ██  ██ ██ 
#  ██████   ██████   ██████  ███████ ███████ ███████ ██   ████


en_cours = True


#  ███████ ██    ██ ███████ ███    ██ ███████ ███    ███ ███████ ███    ██ ████████ 
#  ██      ██    ██ ██      ████   ██ ██      ████  ████ ██      ████   ██    ██    
#  █████   ██    ██ █████   ██ ██  ██ █████   ██ ████ ██ █████   ██ ██  ██    ██    
#  ██       ██  ██  ██      ██  ██ ██ ██      ██  ██  ██ ██      ██  ██ ██    ██    
#  ███████   ████   ███████ ██   ████ ███████ ██      ██ ███████ ██   ████    ██  


def gestion_evenement():
    global en_cours

    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            en_cours = False


#  ██ ███    ██ ██ ████████ ██  █████  ██      ██ ███████  █████  ████████ ██  ██████  ███    ██ 
#  ██ ████   ██ ██    ██    ██ ██   ██ ██      ██ ██      ██   ██    ██    ██ ██    ██ ████   ██ 
#  ██ ██ ██  ██ ██    ██    ██ ███████ ██      ██ ███████ ███████    ██    ██ ██    ██ ██ ██  ██ 
#  ██ ██  ██ ██ ██    ██    ██ ██   ██ ██      ██      ██ ██   ██    ██    ██ ██    ██ ██  ██ ██ 
#  ██ ██   ████ ██    ██    ██ ██   ██ ███████ ██ ███████ ██   ██    ██    ██  ██████  ██   ████

calculer_position_cerclounet_interne()
print(position_cerclounet_interne)


#  ██████   ██████  ██    ██  ██████ ██      ███████ 
#  ██   ██ ██    ██ ██    ██ ██      ██      ██      
#  ██████  ██    ██ ██    ██ ██      ██      █████   
#  ██   ██ ██    ██ ██    ██ ██      ██      ██      
#  ██████   ██████   ██████   ██████ ███████ ███████ 

pygame.init
while(en_cours):

    delta_time = horloge.tick(60)
    gestion_evenement()

    fenetre.fill(fond)
    afficher_aimants()
    afficher_rotor()
    pygame.display.flip()

