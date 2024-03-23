import os,time,random
from donnees import *
from main import *
from lieux import *

# ****************************************************************************************************************************************************************
# /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  FONCTIONS UTILITAIRES
# ****************************************************************************************************************************************************************

# fonction pour afficher le menu
def show_menu():
    print("| Que voulez-vous faire?")
    print("| 1 - Lieux\n| 2 - Actions")

# fonction pour vérifier les int  
def verif_int(texte, lim):
    while True:
        valeur = input(texte)
        if valeur.isdigit() and int(valeur) >= 0 and int(valeur) <= lim:
            return int(valeur)
        else:
            print("Veuillez entrer un nombre entier entre 0 et",lim)

# fonction pour initialiser les pouvoirs au début
def init_jutsu():
    print("Un jutsu aléatoire va être associé à votre personnage.")
    time.sleep(2)
    for boucle in range(20):
        os.system("cls")
        jutsu = random.randint(0, len(jutsus)-1)
        print(list(jutsus.keys())[jutsu])
        time.sleep(0.05)
    print("Votre jutsu a été tiré au sort ! Il s'agit de",list(jutsus.keys())[jutsu],".")
    personnage["Jutsu"] = list(jutsus.keys())[jutsu]
    time.sleep(0.5)
    print("Il inflige",list(jutsus.values())[jutsu]["dégat"],"dégats aux adversaires.")
    time.sleep(2)

# fonction pour changer de pouvoirs
def choix_jutsus():
    print("Liste des jutsus :")
    for index, jutsu in enumerate(jutsus, start=1):
        print(f"{index}. {jutsu}")
    choix = verif_int("\nLequel choisissez-vous ?\n", len(jutsus))
    personnage["Jutsu"] = list(jutsus.keys())[choix-1]

# fonction pour créer le personnage au début du programme 
def create_perso():
    personnage["Age"] = int(input("\nQuel âge as-tu ?\n"))
    personnage["Prénom"] = input("Comment t'appelles-tu ?\n")
    os.system("cls")
    init_jutsu()
    affich_perso()

# fonction pour afficher le personnage
def affich_perso():
    print("Voici ton personnage :")
    for attribut, valeur in personnage.items():
        print(f"{attribut} : {valeur}")


# fonction pour observer les lieux
def observ_lieu(lieu):
    descriptions_lieux = {
        "Hall": "Le hall d'entrée est spacieux et accueillant, orné de portraits décoratifs et de bancs confortables pour se reposer.",
        "CouloirRDC": "Le couloir du RDC est lumineux et vibrant, avec des casiers alignés le long des murs et des portes menant aux salles de classe.",
        "Classe1A": "La salle de classe 1-1 est chaleureuse et accueillante, décorée de belles affiches et de dessins créatifs sur les murs. Un professeur attend patiemment sur son bureau",
        "Couloir1E": "Le couloir du 1e étage offre une atmosphère calme et sereine, éclairé par la lumière naturelle des fenêtres et orné de décorations minimalistes.",
        "Caféteria": "La cafétéria est animée, emplie du bruit joyeux des étudiants et du doux parfum des plats fraîchement préparés.",
        "SalleEntrainement": "La salle d'entraînement résonne des efforts des élèves, empreinte d'une énergie motivante et de détermination.",
        "Casier": "Pas grand chose à dire à part que c'est votre casier. Il est rempli de poussière et de parchemins.",
        "Rue": "La rue est animée par l'activité environnante, avec des passants qui vont et viennent, des voitures qui klaxonnent et des enseignes lumineuses clignotantes.",
        "Aéroport": "L'aéroport est un lieu animé, rempli de voyageurs pressés, de guichets d'enregistrement et du bruit des annonces intercom.",
        "Casino": "Le casino est un endroit animé et lumineux, rempli du son des machines à sous, du cliquetis des jetons de jeu et de l'excitation des joueurs."
    } 

    print(descriptions_lieux[lieu])
    time.sleep(4)
    os.system("cls")   

# fonction pour proposer les actions et les lieux possibles d'accès
def proposer_action_lieu(lieu, choix):
    if choix == "lieu":
        print("│ [Lieux] ")
        for li in lieux_AU[lieu]["lieux"]:
            print("|  " + str(lieux_AU[lieu]['lieux'].index(li) + 1) + "- " + li)
    elif choix == "action":
        print("│ [Actions] ")
        for ac in lieux_AU[lieu]["actions"]:
            print("|  " + str(lieux_AU[lieu]['actions'].index(ac) + 1) + "- " + ac)

# fonction pour le combat dans la salle d'entrainement
def fight():
    os.system("cls")
    print(f"Vous combattez un mannequin d'entrainement. Il a {mannequin["PV"]} PV.")
    fuir = "non"

    # ajout de deux variables pour éviter le bug de float.
    min_dmg = int(mannequin["DMG_min"])
    max_dmg = int(mannequin["DMG_max"])

    while mannequin["PV"] > 0 and fuir != "oui":
        print("PV restants de ",personnage["Prénom"],":", personnage["PV"])
        print("PV restants du mannequin :", mannequin["PV"])
        print("\n")
        mannequin_degat = random.randint(min_dmg, max_dmg)
        reponse_action = verif_int("| Que voulez-vous faire?\n| 1 - Attaquer\n| 2 - Manger\n| 3 - Fuir\n", 3)
        if reponse_action == 1:
            print(personnage["Jutsu"] + "!!!!!!\n-" + str(jutsus[personnage["Jutsu"]]["dégat"]) + " PV !!!!\n")
            mannequin["PV"] -= jutsus[personnage["Jutsu"]]["dégat"]
            time.sleep(3)
            if mannequin["PV"] > 0 :
                print("Le mannequin réplique et envoie son poing malicieux! -"+str(mannequin_degat)+" PV pour vous.")
                time.sleep(2)
                os.system("cls") 
                personnage["PV"] -= mannequin_degat
        elif reponse_action == 2:
            if not inventaire_nourriture :
                print("Il n'y a pas de nourriture dans l'inventaire.")
                time.sleep(1)
                os.system("cls")
            else:
                eat(inventaire_nourriture)
                print("Le mannequin réplique et envoie son poing malicieux! -"+str(mannequin_degat)+" PV pour vous.")
                time.sleep(2)
                os.system("cls") 
                personnage["PV"] -= mannequin_degat

        elif reponse_action == 3:
            print("Vous décidez de fuir le combat..")
            fuir = "oui"

        if personnage["PV"] <= 0:
            print("Vous avez perdu.")
            print("Fin du jeu.")
            sys.exit()

        if mannequin["PV"] <= 0:
            print("Vous avez gagné le combat !")
            print("Vous gagnez un badge.")
            print("Vous gagnez 125¥.")
            personnage["Yen"] += 125
            personnage["Badges"] += 1
            time.sleep(4)
            os.system("cls") 
            #Amélioration du mannequin, augmentation de la difficulté à chaque victoire
            mannequin["PV_init"] *= 1.08
            mannequin["PV"] = mannequin["PV_init"]
            mannequin["DMG_min"] *= 1.25
            mannequin["DMG_max"] *= 1.25
            break
        

# fonction pour afficher les plats disponibles
def affich_eat(inventory):
    print("Liste des plats.")
    for index, plats in enumerate(inventory, start=1):
        print(index,". ",plats)

# fonction pour manger lors du combat
def eat(inventory):
    print("Que voulez-vous manger ?")
    affich_eat(inventory)
    reponse_plat = verif_int("├─>",len(inventory))
    plat_selectionne = list(inventory.keys())[reponse_plat-1]
    personnage["PV"] += 10
    if plat_selectionne in inventory:
        inventory[plat_selectionne] -= 1
        os.system("cls") 
        print("Vous mangez ",plat_selectionne)
        print("Vous gagnez 10 PV.")
        if inventory[plat_selectionne] == 0:
            print("Il n'y aura plus de stock pour ce plat.")
            del inventory[plat_selectionne]
    else:
        print("Ce plat n'est plus disponible.")
    time.sleep(2)
    os.system("cls")

# fonction pour le easter egg
def secret1():
    print("| La malveillance max, vous avez trouvé quelque chose de secret.")
    secret = int(input("| Code secret .... ?"))
    if secret == 1996:
        print("| Vous débloquez un nouveau jutsu..")
        time.sleep(3)
        choix_sus = int(input("| LE SUSANOO PARFAIT !!!!!!\n| Voulez-vous l'équiper?\n|  1- Oui\n|  2- Non\n├─> "))
        if choix_sus == 1:
            jutsus["!!Susanoo Parfait!!"] = {
                "dégat": 40, 
                "niveau": 0
            }
            personnage["Jutsu"] = "!!Susanoo Parfait!!"
            print("| Susanoo Parfait équipé. :)")

# fonction pour choisir un chiffre aléatoire
def start_roul():
    return random.randint(0, 36)

# fonction pour jouer au casino
def jeu_de_roulette():
    while personnage["Yen"] > 0:
        print("Vous allez jouer au jeu de la roulette !")
        print("Vous pouvez parier sur un numéro entre 0 et 36, ou sur une couleur (rouge ou noir).")
        print("Votre solde actuel est de ",personnage["Yen"]," ¥ ")
        mise = verif_int("Combien voulez-vous parier ? (Entrez 0 pour quitter) : ",personnage["Yen"])

        if mise == 0:
            print("Merci d'avoir joué ! À la prochaine !")
            break

        choix = input("Sur quel numéro ou couleur voulez-vous parier ? (0-36, Rouge, Noir) : ").lower()

        if choix.isdigit():
            numero_choisi = int(choix)
            if numero_choisi < 0 or numero_choisi > 36:
                print("Numéro invalide. Veuillez choisir un numéro entre 0 et 36.")
                continue
        elif choix == "rouge" or choix == "noir":
            couleur_choisie = choix
        else:
            print("Choix invalide. Veuillez choisir un numéro entre 0 et 36, ou Rouge ou Noir.")
            continue
        
        for boucle in range(15):
            num_choisi = start_roul()
            if num_choisi % 2 == 1 and num_choisi != 0:
                print(colors.rouge + str(num_choisi) + colors.init)
            elif num_choisi == 0:
                print(colors.vert + str(num_choisi) + colors.init)
            else:
                print(colors.bleu + str(num_choisi) + colors.init)
            time.sleep(0.3)
            os.system("cls")

        print("La roulette s'est arrêtée sur le numéro ",num_choisi,".")
        time.sleep(2)
        if choix.isdigit():
            if num_choisi == numero_choisi:
                print("Vous avez gagné !")
                personnage["Yen"] += mise * 36
            else:
                print("Vous avez perdu !")
                personnage["Yen"] -= mise
        elif couleur_choisie == "rouge":
            if num_choisi % 2 == 1 and num_choisi != 0:
                print("Vous avez gagné !")
                personnage["Yen"] += mise
            else:
                print("Vous avez perdu !")
                personnage["Yen"] -= mise
        elif couleur_choisie == "noir":
            if num_choisi % 2 == 0:
                print("Vous avez gagné !")
                personnage["Yen"] += mise
            else:
                print("Vous avez perdu !")
                personnage["Yen"] -= mise
    if personnage["Yen"] <= 0:
        print("Votre solde est épuisé. N'oubliez pas, le casino est toujours gagnant ! :)")

# fonction pour améliorer les pouvoirs
import os
import time

def upgrade_jutsu():
    os.system("cls")
    if personnage["Yen"] >= 300:
        print("Liste des jutsus :")
        for index, (nom_jutsu, details) in enumerate(jutsus.items(), start=1):
            print(f"{index}. {nom_jutsu} : Lv{details['niveau']}")
            print()

        choix = verif_int("Quel jutsu voulez-vous améliorer?\n", len(jutsus))
        print("Solde actuel :", personnage["Yen"])
        nom_jutsu = list(jutsus.keys())[choix - 1]

        niveau_actuel = jutsus[nom_jutsu]["niveau"]

        if niveau_actuel == 5:
            print("Ce jutsu ne peut pas être amélioré. Il est déjà niveau max.")
            time.sleep(2)
        else:
            augmentation_degat = (niveau_actuel * 2) + 5
            jutsus[nom_jutsu]["niveau"] += 1
            jutsus[nom_jutsu]["dégat"] += augmentation_degat
            print(nom_jutsu, "amélioré !")
            print("Il est maintenant niveau", jutsus[nom_jutsu]["niveau"], "et inflige", jutsus[nom_jutsu]["dégat"], "DMG!!")
            personnage["Yen"] -= 300
            print("Solde actualisé :", personnage["Yen"])
            time.sleep(2)
        os.system("cls")
    else:
        print("Solde insuffisant.\nSolde actuel :", personnage["Yen"])
        time.sleep(2)

            