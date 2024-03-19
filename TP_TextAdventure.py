import os
import time
import sys
import random

personnage = {
    "PV": 70,
    "Badges" : 0,
    "Yen" : 500
}

jutsus = {
    "Rasengan": 20,
    "Chidori": 25,
    "Kirin": 30,
    "Amaterasu": 15,
    "Tsukuyomi": 10,
    "Susanoo": 30,
    "Flying Raijin Jutsu": 20,
    "Eight Trigrams Sixty-Four Palms": 15
}
jutsus_cle = list(jutsus)

plats_stock = {
    "Sushi" : 2,
    "Ramen" : 2,
    "Tempura" : 2,
    "Sashimi" : 2,
    "Udon" : 2,
    "Yakitori" : 2,
    "Okonomiyaki" : 2,
    "Takoyaki" : 2,
    "Tonkatsu" : 2,
    "Miso soup" : 2
}
plat_cle = list(plats_stock)

lieux_AU = {
    "Hall": {
        "lieux": ["Couloir RDC","Casier", "Rue"],
        "actions": ["Observer", "Carte d'identité","Quitter"]
    },
    "CouloirRDC": {
        "lieux": ["Couloir 1e étage", "Classe 1-A"],
        "actions": ["Observer"]
    },
    "Classe1A": {
        "lieux": ["Couloir RDC"],
        "actions": ["Observer", "Demander", "Montrer"]
    },
    "Couloir1E": {
        "lieux": ["Couloir RDC", "Cafétéria", "Salle d'entraînement"],
        "actions": ["Observer"]
    },
    "Caféteria": {
        "lieux": ["Couloir 1e étage"],
        "actions": ["Observer", "Manger", "Acheter"]
    },
    "SalleEntrainement": {
        "lieux": ["Couloir 1e étage"],
        "actions": ["Observer", "Combattre"]
    },
    "Casier":{
        "lieux": ["Hall"],
        "actions": ["Observer", "Changer de jutsus"]
    },
    "Rue":{
        "lieux": ["Hall", "Aéroport"],
        "actions": ["Observer"]
    },
    "Aéroport":{
        "lieux": ["Rue"],
        "actions": ["Observer", "Prendre des vacances"]
    }
}

objets_cles = ["smartphone","Clé"]
inventaire_nourriture = {}

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
    for index, jutsu in enumerate(jutsus_cle, start=1):
        print(index,". ",jutsu)
    jutsu = verif_int("\nLequel choisis-tu ?\n", len(jutsus))
    personnage["Jutsu"] = jutsus_cle[jutsu-1]
    
def create_perso():
    age = int(input("\nQuel âge as-tu ?\n"))
    personnage["Age"] = age
    prenom = input("Comment t'appelles-tu ?\n")
    personnage["Prénom"] = prenom
    os.system("cls")
    choix_jutsus()
    affich_perso()

def affich_perso():
    print("Voici ton personnage :")
    print("Prénom :", personnage["Prénom"])
    print("Âge :", personnage["Age"])
    print("PV :", personnage["PV"])
    print("Jutsu :", personnage["Jutsu"])
    print("Yen : ",personnage["Yen"])
    print("Badges :", personnage["Badges"])

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
        "Aéroport": "L'aéroport est un lieu animé, rempli de voyageurs pressés, de guichets d'enregistrement et du bruit des annonces intercom."
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
                print("Liste des plats de l'inventaire :")
                for index, plat in enumerate(inventaire_nourriture.keys(), start=1):
                    print(f"{index}. {plat}")
                manger = verif_int("Que voulez-vous manger?\n", len(inventaire_nourriture)) 
                plat_selectionne = list(inventaire_nourriture.keys())[manger - 1]
                print("Vous avez mangé "+plat_selectionne+" et vous avez gagné 10 PV.")
                del inventaire_nourriture[plat_selectionne] 
                personnage["PV"] += 10
                time.sleep(2)
                os.system("cls")

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
        
        print("PV restants de ",personnage["Prénom"],":", personnage["PV"])
        print("PV restants du mannequin :", mannequin_pv)
        print("\n")

def affich_eat():
    print("Liste des plats.")
    for index, plats in enumerate(plats_stock, start=1):
        print(index,". ",plats)

def eat():
    print("Que voulez-vous manger ?")
    affich_eat()
    reponse_plat = verif_int("├─>",len(plats_stock))
    plat_selectionne = plat_cle[reponse_plat - 1]
    personnage["PV"] += 10
    plats_stock[plat_selectionne] -= 1
    os.system("cls") 
    print("Vous mangez ",plat_selectionne)
    print("Vous gagnez 10 PV.")
    if plats_stock[plat_selectionne] == 0:
        print("Il n'y aura plus de stock pour ce plat.")
        del plats_stock[plat_selectionne]
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
            jutsus_cle.append("!!Susanoo Parfait!!")
            personnage["Jutsu"] = "!!Susanoo Parfait!!"
            print("| Susanoo Parfait équipé. :)")
            unable_secret = True

# ****************************************************************************************************************************************************************
# /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  LIEUX
# ****************************************************************************************************************************************************************
def lieu_hall():
    os.system("cls")
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("Vous êtes maintenant dans le Hall d'entrée.")
    print("Depuis cet endroit, nous pouvons accéder au couloir du rez-de-chaussée, à la rue et à votre casier.")

    while True:
        print("┌────────────────────────────────────────")
        show_menu()
        choix = verif_int("├─> ",len(lieux_AU["Hall"]))
        if choix == 1:
            proposer_action_lieu("Hall","lieu")
            reponse_lieu = verif_int("├─> ",len(lieux_AU["Hall"]["lieux"]))
            if reponse_lieu == 1:
                return "CouloirRDC"
            elif reponse_lieu == 2:
                return "Casier"
            elif reponse_lieu == 3:
                return "Rue"
        elif choix == 2 :
            proposer_action_lieu("Hall","action")
            reponse_action = verif_int("├─> ",len(lieux_AU["Hall"]["actions"]))
            if reponse_action == 1:
                os.system("cls")
                observ_lieu("Hall")
            elif reponse_action == 2:
                affich_perso()
                time.sleep(3)
                os.system("cls")
            elif reponse_action == 3:
                sys.exit()
        print("└────────────────────────────────────────")


def lieu_couloir_rdc():
    os.system("cls")
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("\nVous voilà arrivé dans le couloir du rez-de-chaussée.")
    print("Depuis ce couloir, nous pouvons accéder à la classe 1-A.")

    while True:
        print("┌────────────────────────────────────────")
        show_menu()
        choix = verif_int("├─> ",len(lieux_AU["CouloirRDC"]))
        if choix == 1:
            proposer_action_lieu("CouloirRDC","lieu")
            reponse_lieu = verif_int("├─> ",len(lieux_AU["CouloirRDC"]["lieux"]))
            return "Couloir1E" if reponse_lieu == 1 else "Classe1A"
        elif choix == 2 :
                proposer_action_lieu("CouloirRDC","action")
                reponse_action = verif_int("├─> ",len(lieux_AU["CouloirRDC"]["actions"]))
                if reponse_action == 1:
                    os.system("cls")
                    observ_lieu("CouloirRDC")
        print("└────────────────────────────────────────")

def lieu_classe_1A():
    os.system("cls")
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("\nVous venez d'entrer dans la classe 1-A.")

    observ_compt = 0
    while True:
        print("┌────────────────────────────────────────")
        show_menu()
        choix = verif_int("├─> ",len(lieux_AU["Classe1A"]))
        if choix == 1:
            proposer_action_lieu("Classe1A","lieu")
            reponse_lieu = verif_int("├─> ",len(lieux_AU["Classe1A"]["lieux"]))
            if reponse_lieu == 1:
                return "CouloirRDC"
        elif choix == 2 :
            proposer_action_lieu("Classe1A","action")
            reponse_action = verif_int("├─> ",len(lieux_AU["Classe1A"]["actions"]))
            if reponse_action == 1:
                os.system("cls")
                observ_lieu("Classe1A")
                observ_compt = observ_compt + 1
                if observ_compt >= 3:
                    print("| A force de regarder, une affiche se distingue des autres....")
                    time.sleep(2)
                    print("| On peut y lire :")
                    print("| Dans les confins du casier, où les secrets se cachent derrière chaque porte, il est chemin à suivre, un choix à faire.\nExplorez les actions disponibles, mais ne vous laissez pas distraire par les chemins familiers. \nCherchez plutôt le chemin moins fréquenté, celui qui dévoile des trésors cachés.\n\nDans un jardin énigmatique, trois roses émergent parmi les pétales. Trouvez le nombre de leurs secrets pour dévoiler la voie. \n\nDans l'année où Conan, le célèbre détective adolescent, a résolu ses premiers mystères, quel nombre révèle le secret dissimulé dans les ombres du passé ?")
                    quitter = input("Appuyez pour quitter..")
            elif reponse_action == 2:
                print("| Le professeur vous donne le passe pour la salle d'entraînement.")
                time.sleep(3)
                os.system("cls") 
                objets_cles.append("Clé")
            elif reponse_action == 3:
                if personnage["Badges"] != 0:
                    print("| Vous montrez vos badges au professeur.")
                    time.sleep(2)
                    os.system("cls") 
                    if personnage["Badges"] == "3":
                        print("| Vous avez réussi le jeu.")
                        print("| Félicitations!")
                        sys.exit()
                print("| Vous n'avez pas de badges pour le moment.")
                time.sleep(3)
                os.system("cls") 
        print("└────────────────────────────────────────")

def lieu_couloir_1e_etage():
    os.system("cls")
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("\nVous êtes à présent dans le couloir du 1e étage.")
    print("On y trouve la cafétéria et la salle d'entraînement.")
    
    while True:
        print("┌────────────────────────────────────────")
        show_menu()
        choix = verif_int("├─> ",len(lieux_AU["Couloir1E"]))
        if choix == 1:
            i = 0
            proposer_action_lieu("Couloir1E","lieu")
            reponse_lieu = verif_int("├─> ",len(lieux_AU["Couloir1E"]["lieux"]))
            if reponse_lieu == 1:
                return "CouloirRDC"
            elif reponse_lieu == 2:
                return "Caféteria"
            elif reponse_lieu == 3:
                if "Clé" in objets_cles:
                        i = 1
                if i == 1 :
                    return "SalleEntrainement"
                else:
                    print("| Endroit inaccessible.")
                    time.sleep(2)
                    os.system("cls")
        elif choix == 2 :
            proposer_action_lieu("Couloir1E","action")
            reponse_action = verif_int("├─> ",len(lieux_AU["Couloir1E"]["actions"]))
            if reponse_action == 1:
                os.system("cls")
                observ_lieu("Couloir1E")
        print("└────────────────────────────────────────")

def lieu_cafeteria_1e_etage():
    os.system("cls")
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("\nVous passez les portes de la cafétéria, vous sentez cette odeur alléchante.")

    while True:
        print("┌────────────────────────────────────────")
        show_menu()
        choix = verif_int("├─> ",len(lieux_AU["Caféteria"]))
        if choix == 1:
            proposer_action_lieu("Caféteria","lieu")
            reponse_lieu = verif_int("├─> ",len(lieux_AU["Caféteria"]["lieux"]))
            if reponse_lieu == 1:
                return "Couloir1E"
        elif choix == 2 :
            proposer_action_lieu("Caféteria","action")
            reponse_action = verif_int("├─> ",len(lieux_AU["Caféteria"]["actions"]))
            if reponse_action == 1:
                os.system("cls")
                observ_lieu("Caféteria")
            elif reponse_action == 2:
                eat()
            elif reponse_action == 3:
                os.system("cls")
                if personnage["Yen"] < 75 :
                    print("| Vous n'avez pas assez d'argents...")
                else:
                    print("| Que souhaitez-vous acheter ? 75¥ unité.")
                    affich_eat()
                    reponse_plat = verif_int("├─>", len(plats_stock))
                    plat_selectionne = plat_cle[reponse_plat - 1]
                    if plats_stock[plat_selectionne] > 0:
                        if plat_selectionne in inventaire_nourriture:
                            inventaire_nourriture[plat_selectionne] += 1
                        else:
                            inventaire_nourriture[plat_selectionne] = 1
                        plats_stock[plat_selectionne] -= 1
                        print("| Vous avez acheté le plat : ",plat_selectionne)
                        personnage["Yen"] -= 75
                        print("| Solde mis à jour : ",personnage["Yen"])
                        time.sleep(2)
                        if plats_stock[plat_selectionne] == 0:
                            print("| Il n'y aura plus de stock pour ce plat.")
                            time.sleep(2)
                            del plats_stock[plat_selectionne]
                            plat_cle.remove(plat_selectionne)

        print("└────────────────────────────────────────")

def lieu_salle_entrainement():
    os.system("cls")
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("\nVous pénétrez dans la salle d'entraînement. Une atmosphère pesante s'est installée dans cette pièce.")

    while True:
        print("┌────────────────────────────────────────")
        show_menu()
        choix = verif_int("├─> ", len(lieux_AU["SalleEntrainement"]))
        if choix == 1:
            proposer_action_lieu("SalleEntrainement","lieu")
            reponse_lieu = verif_int("├─> ", len(lieux_AU["SalleEntrainement"]["lieux"]))
            if reponse_lieu == 1:
                return "Couloir1E"
        elif choix == 2:
            proposer_action_lieu("SalleEntrainement","action")
            reponse_action = verif_int("├─> ", len(lieux_AU["SalleEntrainement"]["actions"]))
            if reponse_action == 1:
                os.system("cls")
                observ_lieu("SalleEntrainement")
            elif reponse_action == 2:
                fight()
        print("└────────────────────────────────────────")

def lieu_casier():
    unable_secret = False
    os.system("cls")
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("\nVous ouvrez votre casier.")

    while True:
        print("┌────────────────────────────────────────")
        show_menu()
        choix = verif_int("├─> ", len(lieux_AU["Casier"]))
        if choix == 1:
            proposer_action_lieu("Casier","lieu")
            reponse_lieu = verif_int("├─> ", len(lieux_AU["Casier"]["lieux"]))
            if reponse_lieu == 1:
                return "Hall"
        elif choix == 2:
            proposer_action_lieu("Casier","action")
            reponse_action = verif_int("├─> ", len(lieux_AU["Casier"]["actions"])+1)
            if reponse_action == 1:
                os.system("cls")
                observ_lieu("Casier")
            elif reponse_action == 2:
                choix_jutsus()
                affich_perso()
                time.sleep(2)
                os.system("cls")    
            elif reponse_action == 3:
                if not unable_secret:
                    secret1()
                else:
                    print("| Ce chemin n'existe plus..")
        print("└────────────────────────────────────────")

def lieu_rue():
    os.system("cls")
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("Vous êtes dans la rue.")
    print("Depuis cette rue, vous pouvez accéder au hall et à l'aéroport.")

    while True:
        print("┌────────────────────────────────────────")
        show_menu()
        choix = verif_int("├─> ",len(lieux_AU["Rue"]))
        if choix == 1:
            proposer_action_lieu("Rue","lieu")
            reponse_lieu = verif_int("├─> ",len(lieux_AU["Rue"]["lieux"]))
            if reponse_lieu == 1:
                return "Hall"
            elif reponse_lieu == 2:
                return "Aéroport"
        elif choix == 2 :
            proposer_action_lieu("Rue","action")
            reponse_action = verif_int("├─> ",len(lieux_AU["Rue"]["lieux"]))
            if reponse_action == 1:
                os.system("cls")
                observ_lieu("Rue")
        print("└────────────────────────────────────────")

def lieu_aeroport():
    os.system("cls")
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("\nVous êtes à l'aéroport. Vous pouvez accéder à la rue.")

    while True:
        print("┌────────────────────────────────────────")
        show_menu()
        choix = verif_int("├─> ", len(lieux_AU["Aéroport"]))
        if choix == 1:
            proposer_action_lieu("Aéroport", "lieu")
            reponse_lieu = verif_int("├─> ", len(lieux_AU["Aéroport"]["lieux"]))
            if reponse_lieu == 1:
                return "Rue"
        elif choix == 2:
            proposer_action_lieu("Aéroport", "action")
            reponse_action = verif_int("├─> ", len(lieux_AU["Aéroport"]["actions"]))
            if reponse_action == 1:
                os.system("cls")
                observ_lieu("Aéroport")
            elif reponse_action == 2:
                choix = verif_int("| Le voyage en Corée du Sud coûte 2500¥\n| Souhaitez-vous voyager?\n|  1 - Oui\n|  2 - Non\n├─> ",2)
                if choix == 1 and personnage["Yen"] >= 2500:
                    print("Nous nous envolons pour la Corée du Sud")
                else:
                    print("Vous n'avez pas assez d'argent... il vous manque ",(2500-personnage["Yen"]),"¥")


        print("└────────────────────────────────────────")

# ****************************************************************************************************************************************************************
# /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  INTRODUCTION
# ****************************************************************************************************************************************************************
def intro():
    os.system("cls")
    print("      ////////    ///  ///")
    print("      ///  ///    ///  ///")
    print("      ////////    ///  ///")
    print("      ///  ///    ////////")
    print("===============================")
    print("|| Bienvenue au lycée A.U. ! ||")
    print("===============================")
    print("Commençons par créer ton personnage.")
    create_perso()
    time.sleep(2)
    os.system("cls")
    
    emplacement = "Hall"
    while True:
        if emplacement == "Hall":
            emplacement = lieu_hall()
        elif emplacement == "CouloirRDC":
            emplacement = lieu_couloir_rdc()
        elif emplacement == "Classe1A":
            emplacement = lieu_classe_1A()
        elif emplacement == "Couloir1E":
            emplacement = lieu_couloir_1e_etage()
        elif emplacement == "Caféteria":
            emplacement = lieu_cafeteria_1e_etage()
        elif emplacement == "SalleEntrainement":
            emplacement = lieu_salle_entrainement()
        elif emplacement == "Casier":
            emplacement = lieu_casier()
        elif emplacement == "Rue":
            emplacement = lieu_rue()
        elif emplacement == "Aéroport":
            emplacement = lieu_aeroport()

# ****************************************************************************************************************************************************************
# /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  EXECUTION
# ****************************************************************************************************************************************************************

# Pour lancer le jeu, on appelle la fonction d'introduction
if __name__ == "__main__":
    intro()
    print("Fin du jeu.")
