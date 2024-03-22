import os,time,sys,random
from donnees import *
from main import *
from fonction_utilitaires import *

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
            if reponse_lieu == 1:
                return "Couloir1E"
            if reponse_lieu == 2:
                return "Classe1A"
            if reponse_lieu == 3:
                return "Hall"
            
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
                if "Clé" not in objets_cles:
                    print("| Le professeur vous donne le passe pour la salle d'entraînement.")
                    time.sleep(3)
                    os.system("cls") 
                    objets_cles.append("Clé")
                else:
                    print("Vous avez déjà la clé.")
                    os.system("cls")
                    time.sleep(2)
            elif reponse_action == 3:
                if personnage["Badges"] != 0:
                    print("| Vous montrez vos badges au professeur.")
                    time.sleep(2)
                    os.system("cls") 
                    if personnage["Badges"] == "3":
                        print("| Vous avez réussi le jeu.")
                        print("| Félicitations!")
                        sys.exit()
                    else:
                        print("| Professeur : Vous avez ",personnage["Badges"]," badges ! Continuez ainsi :)")
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
                eat(plats_stock)
            elif reponse_action == 3:
                os.system("cls")
                if personnage["Yen"] < 75 :
                    print("| Vous n'avez pas assez d'argents...")
                else:
                    print("| Que souhaitez-vous acheter ? 75¥ unité.")
                    affich_eat(plats_stock)
                    reponse_plat = verif_int("├─>", len(plats_stock))
                    plat_selectionne = list(plats_stock.keys())[reponse_plat-1]
                    if plats_stock[plat_selectionne] > 0:
                        if plat_selectionne in inventaire_nourriture:
                            inventaire_nourriture[plat_selectionne] += 1
                        else:
                            inventaire_nourriture[plat_selectionne] = 1
                        plats_stock[plat_selectionne] -= 1
                        print("| Vous avez acheté le plat : ",plat_selectionne)
                        personnage["Yen"] -= 75
                        print("| Solde mis à jour :",personnage["Yen"],"¥")
                        time.sleep(2)
                        if plats_stock[plat_selectionne] == 0:
                            print("| Il n'y aura plus de stock pour ce plat.")
                            time.sleep(2)
                            del plats_stock[plat_selectionne]

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
            elif reponse_action == 3:
                upgrade_jutsu()
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
                    unable_secret = True
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
            elif reponse_lieu == 3:
                return "Casino"
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

def lieu_casino():
    os.system("cls")
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("\nVous pénétrez dans le casino. Gare à votre porte-feuille!")

    while True:
        print("┌────────────────────────────────────────")
        show_menu()
        choix = verif_int("├─> ", len(lieux_AU["Casino"]))
        if choix == 1:
            proposer_action_lieu("Casino", "lieu")
            reponse_lieu = verif_int("├─> ", len(lieux_AU["Casino"]["lieux"]))
            if reponse_lieu == 1:
                return "Rue"
        elif choix == 2:
            proposer_action_lieu("Casino", "action")
            reponse_action = verif_int("├─> ", len(lieux_AU["Casino"]["actions"]))
            if reponse_action == 1:
                os.system("cls")
                observ_lieu("Casino")
            elif reponse_action == 2:
                os.system("cls")
                print("Bienvenue dans le monde de l'ARGENT.\nIci, tu peux soit partir en slip, soit en costard.")
                time.sleep(2)
                jeu_de_roulette()
                time.sleep(2)
        print("└────────────────────────────────────────")