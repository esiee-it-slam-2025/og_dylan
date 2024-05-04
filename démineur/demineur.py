import random
import os
import sys
import time
from colorama import init, Fore

init()

# MENU D'ACTIONS
def show_actions():
    print("\nChoisissez une action (1-3) : ")
    print("1 - Découvrir une case.")
    print("2 - Ajouter un drapeau.")
    print("3 - Supprimer un drapeau.")

# VERIFICATION DE L'ENTREE EN DE L'UTILISATEUR
def verif_choix(texte, lim):
    while True:
        valeur = input(texte)
        if len(valeur) == 2 and valeur[0].isdigit() and valeur[1].isalpha() and 1 <= int(valeur[0]) <= lim and 'A' <= valeur[1].upper() <= chr(64 + lim):
            ligne = int(valeur[0])
            colonne = ord(valeur[1].upper()) - ord('A')
            return ligne, colonne
        else:
            print(f"Veuillez entrer une entrée valide (par exemple, '1A' pour la première ligne et la première colonne).")

# CREATION DE GRILLE
def creer_grille(largeur, hauteur):
    return [['~ '] * largeur for _ in range(hauteur)]

# AFFICHAGE DE GRILLE
def affich_grille(grille):
    print('    ', end='')
    for i in range(len(grille[0])):
        print(chr(65 + i), end='  ')
    print("\n  " + "_" * (len(grille[0]) * 3))

    for i, ligne in enumerate(grille, start=1):
        print(f"{i}{' |' if i < 10 else '|'}", end=' ')
        for case in ligne:
            color = Fore.RESET
            if case == '1 ':
                color = Fore.BLUE
            elif case == '2 ':
                color = Fore.GREEN
            elif case != '~':
                color = Fore.RED
            print(f"{color}{case}{Fore.RESET}", end=' ')
        print()

# PLACER LES BOMBES DANS LA GRILLE
def place_bomb(grille,choix_difficulte):
    bombe_counts = {1: 8, 2: 40, 3: 75}
    bombe = bombe_counts.get(choix_difficulte, 0)
    while bombe > 0:
        l = random.randint(0, len(grille) - 1)
        c = random.randint(0, len(grille[0]) - 1)
        if grille[l][c] != 'x ':
            grille[l][c] = 'x '
            bombe -= 1

# COMPTER LES BOMBES AUTOUR DE LA CASE
def compt_bomb_autour_case(grille, lig, col):
    hauteur, largeur = len(grille), len(grille[0])
    bombes_autour = 0
    for delta_lig, delta_col in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
        voisin_lig = lig + delta_lig
        voisin_col = col + delta_col
        if 0 <= voisin_lig < hauteur and 0 <= voisin_col < largeur and grille[voisin_lig][voisin_col] == 'x ':
            bombes_autour += 1
    return bombes_autour

# AFFICHER LE NOMBRE DE BOMBES DANS LA CASE
def compt_bomb_autour(grille):
    for ligne in range(len(grille)):
        for colonne in range(len(grille[0])):
            if grille[ligne][colonne] != 'x ':
                bombes_autour = compt_bomb_autour_case(grille, ligne, colonne)
                grille[ligne][colonne] = str(bombes_autour) + ' '

# FONCTION POUR DEVOILER UNE CASE
def decouv_case(grille, grille_joueur):
    ligne, colonne = verif_choix(f"Choisissez la case à découvrir (ex : '1A' pour la première ligne et la première colonne) : ", len(grille))
    lig, col = ligne - 1, colonne
    if grille[lig][col] == 'x ':
        print("Vous avez perdu.")
        sys.exit()
    decouv_case_recurs(grille, grille_joueur, lig, col)

# FONCTION RECURSIVE POUR DEVOILER TOUTES LES CASES AUTOUR SI ELLES SONT 0
def decouv_case_recurs(grille, grille_joueur, lig, col):
    hauteur, largeur = len(grille), len(grille[0])
    if not (0 <= lig < hauteur and 0 <= col < largeur) or grille_joueur[lig][col] != '~ ':
        return

    bombes_autour = compt_bomb_autour_case(grille, lig, col)
    if bombes_autour == 0:
        grille_joueur[lig][col] = '  '
        for delta_lig, delta_col in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
            decouv_case_recurs(grille, grille_joueur, lig + delta_lig, col + delta_col)
    else:
        grille_joueur[lig][col] = str(bombes_autour) + ' '

# FONCTION PLACER DRAPEAU POUR GAGNER
def place_flag(grille_joueur):
    ligne, colonne = verif_choix(f"Choisissez la case où placer un drapeau (ex : '1A' pour la première ligne et la première colonne) : ", len(grille_joueur))
    lig, col = ligne - 1, colonne
    if grille_joueur[lig][col] == '~ ':
        grille_joueur[lig][col] = 'F '
        return True
    print("Vous ne pouvez pas placer un drapeau sur un chiffre ou sur un autre drapeau.")
    time.sleep(2)

# FONCTION POUR SUPPRIMER UN DRAPEAU EN CAS D'ERREUR
def supp_flag(grille_joueur):
    ligne, colonne = verif_choix(f"Choisissez la case où supprimer un drapeau (ex : '1A' pour la première ligne et la première colonne) : ", len(grille_joueur))
    lig, col = ligne - 1, colonne
    if grille_joueur[lig][col] == 'F ':
        grille_joueur[lig][col] = '~ '
        return True
    print("Il n'y a pas de drapeaux à cette position.")
    time.sleep(2)

# FONCTION POUR VERIFIER LA VICTOIRE
def verif_victoire(grille, grille_joueur):
    for lig in range(len(grille)):
        for col in range(len(grille[0])):
            if grille[lig][col] == 'x ':
                if grille_joueur[lig][col] != 'F ':
                    return
    print("Vous avez trouvé toutes les bombes, félicitations !")
    recommencer = 0
    while recommencer < 1 or recommencer > 2:
        recommencer = int(input("voulez-vous recommencer ?\n1- Oui\n2- Non\n"))
    if recommencer == 1 :
        main()
    sys.exit()

def main():
    os.system("cls")
    # CHOIX DE LA DIFFICULTE
    choix_difficulte = 0
    while choix_difficulte < 1 or choix_difficulte > 3:
        choix_difficulte = int(input("Quelle difficulté choisissez-vous ?\n1- Facile\n2- Normal\n3- Difficile\n"))
    if choix_difficulte == 1:   
        largeur = hauteur = 9
        drapeau = 8
    elif choix_difficulte == 2:
        largeur = hauteur = 16
        drapeau = 40
    else:
        largeur = 24
        hauteur = 16
        drapeau = 75

    # INITIALISATION DE LA PARTIE
    grille = creer_grille(largeur, hauteur)
    grille_joueur = creer_grille(largeur, hauteur)
    place_bomb(grille,choix_difficulte)
    compt_bomb_autour(grille)
    drapeau_actuel = drapeau

    # BOUCLE DE JEU
    while True:
        os.system("cls")
        print("\n         /////////// ")
        print("       //        ///   ")
        print("     //        ///     ")
        print("   //        ///       ")
        print(" ////////////          ")
        print("\nBienvenue sur le jeu du démineur.\n")

        affich_grille(grille_joueur)

        verif_victoire(grille, grille_joueur)

        show_actions()

        print(f"\nVous avez {drapeau_actuel} drapeaux à placer.")

        action = input()
        if action == "1":
            decouv_case(grille, grille_joueur)
        elif action == "2":
            if drapeau_actuel > 0 :
                if place_flag(grille_joueur):
                    drapeau_actuel -= 1
            else:
                print("Vous n'avez plus de drapeaux à placer.")
                time.sleep(2)
        elif action == "3":
            if drapeau_actuel != drapeau:
                if supp_flag(grille_joueur):
                    drapeau_actuel += 1
        else:
            os.system("cls")
            print("Choix non valide, veuillez entrer un chiffre entre 1 et 3.")
            time.sleep(1)

if __name__ == "__main__":
    main()
    print("Fin du jeu.")