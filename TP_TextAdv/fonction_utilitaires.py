import os,time,sys,random
from donnees import *
from main import *
from lieux import *

# ****************************************************************************************************************************************************************
# /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  FONCTIONS UTILITAIRES
# ****************************************************************************************************************************************************************
def show_menu():
    print("| Que voulez-vous faire?")
    print("| 1 - Lieux\n| 2 - Actions")
    
def verif_int(texte, lim):
    while True:
        valeur = input(texte)
        if valeur.isdigit() and int(valeur) >= 0 and int(valeur) <= lim:
            return int(valeur)
        else:
            print("Veuillez entrer un nombre entier valable.")

def choix_jutsus():
    print("Liste des jutsus :")
    for index, jutsu in enumerate(jutsus, start=1):
        print(f"{index}. {jutsu}")
    choix = verif_int("\nLequel choisissez-vous ?\n", len(jutsus))
    personnage["Jutsu"] = list(jutsus.keys())[choix-1]
    
def create_perso():
    personnage["Age"] = int(input("\nQuel âge as-tu ?\n"))
    personnage["Prénom"] = input("Comment t'appelles-tu ?\n")
    os.system("cls")
    choix_jutsus()
    affich_perso()

def affich_perso():
    print("Voici ton personnage :")
    for attribut, valeur in personnage.items():
        print(f"{attribut} : {valeur}")



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

def proposer_action_lieu(lieu, choix):
    if choix == "lieu":
        print("│ [Lieux] ")
        for li in lieux_AU[lieu]["lieux"]:
            print("|  " + str(lieux_AU[lieu]['lieux'].index(li) + 1) + "- " + li)
    elif choix == "action":
        print("│ [Actions] ")
        for ac in lieux_AU[lieu]["actions"]:
            print("|  " + str(lieux_AU[lieu]['actions'].index(ac) + 1) + "- " + ac)

def fight():
    os.system("cls")
    print("Vous combattez un mannequin d'entrainement. Il a 50 PV.")
    mannequin_pv = 50
    fuir = "non"
    while mannequin_pv > 0 and fuir != "oui":
        mannequin_degat = random.randint(7, 25)
        reponse_action = verif_int("| Que voulez-vous faire?\n| 1 - Attaquer\n| 2 - Manger\n| 3 - Fuir\n", 3)
        if reponse_action == 1:
            print(personnage["Jutsu"] + "!!!!!!\n-"+ str(jutsus[personnage["Jutsu"]])+" PV !!!!\n")
            mannequin_pv -= jutsus[personnage["Jutsu"]]
            time.sleep(3)
            if mannequin_pv > 0 :
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

        if mannequin_pv <= 0:
            print("Vous avez gagné le combat !")
            print("Vous gagnez un badge.")
            print("Vous gagnez 125¥.")
            personnage["Yen"] += 125
            time.sleep(4)
            os.system("cls") 
            personnage["Badges"] += 1
            continue
        
        print("PV restants de ",personnage["Prénom"],":", personnage["PV"])
        print("PV restants du mannequin :", mannequin_pv)
        print("\n")

def affich_eat(inventory):
    print("Liste des plats.")
    for index, plats in enumerate(inventory, start=1):
        print(index,". ",plats)

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

def secret1():
    print("| La malveillance max, vous avez trouvé quelque chose de secret.")
    secret = int(input("| Code secret .... ?"))
    if secret == 1996:
        print("| Vous débloquez un nouveau jutsu..")
        time.sleep(3)
        choix_sus = int(input("| LE SUSANOO PARFAIT !!!!!!\n| Voulez-vous l'équiper?\n|  1- Oui\n|  2- Non\n├─> "))
        if choix_sus == 1:
            jutsus["!!Susanoo Parfait!!"] = 40
            personnage["Jutsu"] = "!!Susanoo Parfait!!"
            print("| Susanoo Parfait équipé. :)")

def start_roul():
    return random.randint(0, 36)

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
        
        for i in range(15):
            num_choisi = start_roul()
            if num_choisi % 2 == 1 and num_choisi != 0:
                print(colors.rouge + str(num_choisi) + colors.init)
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