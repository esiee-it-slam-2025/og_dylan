import os
import time

# Dictionnaire initial
stations = {
    "Meinohama": 1.5,
    "Muromi": 0.8, 
    "Fujisaki": 1.1,
    "Nishijin": 1.2,
    "Tojinmachi": 0.8,
    "Ohorikoen (Ohori Park)": 1.1,
    "Akasaka": 0.8,
    "Tenjin": 0.8,
    "Nakasu-Kawabata": 1.0,
    "Gion": 0.7,
    "Hakata": 1.2,
    "Higashi-Hie": 2.1,
    "Fukuokakuko (Airport)": 0.0,
}

# Création de deux listes, une liste clé et une liste valeur du dictionnaire ci-dessus.
stations_cle = list(stations)
stations_valeur = list(stations.values())

# Dictionnaire pour les tarifs, afin de simplifier le code.
tarifs = {
    "Zone 1": {"distance": (0, 3), "plein": 210, "reduit": 110},
    "Zone 2": {"distance": (3.01, 7), "plein": 260, "reduit": 130},
    "Zone 3": {"distance": (7.01, 11), "plein": 300, "reduit": 150},
    "Zone 4": {"distance": (11.01, 15), "plein": 340, "reduit": 170}
}

# Procédure affichant le menu.
def show_actions():
    print("Choisissez une action (1-3) : ")
    print("1 - CONSIGNE TP")
    print("2 - Afficher les trajets")
    print("3 - Quitter le programme")

# Fonction qui vérifie que l'utilisateur entre un entier valide. Elle renvoie l'entier valide.
def verif_int(texte):
    while True:
        valeur = input(texte)
        if valeur.isdigit() and int(valeur) >= 0:
            return int(valeur)
        else:
            print("Veuillez entrer un nombre entier positif.")

# Fonction qui simule un trajet en appelant les différentes fonctions. TP!!!!!!!!!
def add_trajet(trajets):
    os.system("cls")
    billet_adulte = verif_int("Entrez le nombre de billets adultes : ")
    billet_reduit = verif_int("Entrez le nombre de billets à tarif réduit : ")
    print("\n")
    depart = choix_station()
    print("\n")
    destination = choix_station()
    while depart == destination:
        print("La station de départ ne peut pas être la même que la station d'arrivée.")
        destination = choix_station()
    zone = deter_zone(depart, destination)
    voie = deter_voie(depart, destination)
    prix_total = calc_prix(billet_adulte, billet_reduit, zone)
    trajet = (billet_adulte, billet_reduit, zone, prix_total, voie)
    trajets.append(trajet)
    print("\n")
    resume(trajet)

# Fonction qui permet à l'utilisateur de choisir la station de départ et la station de destination. Elle affiche la liste des stations, vérifie que le numéro est valide puis renvoie le nom de la station choisie.
def choix_station():
    print("Liste des stations :")
    for index, station in enumerate(stations_cle, start=1):
        print(index,". ",station)
    while True:
        choix = verif_int("Entrez le numéro de la station : ")
        if 0 < choix <= len(stations) :
            return stations_cle[choix - 1]
        else:
            print("Numéro de station invalide. Veuillez réessayer.")

# Fonction qui détermine la zone tarifaire du trajet. Deux boucles for pour calculer la distance totale et pour chercher à quelle zone la distance correspond. Elle renvoie la zone.
def deter_zone(depart, destination):
    distance_totale = 0
    for station in stations_cle[stations_cle.index(depart):stations_cle.index(destination)]:
        distance_totale += stations[station]
    for zone in tarifs:
        tarif_info = tarifs[zone]
        if tarif_info["distance"][0] <= distance_totale <= tarif_info["distance"][1]:
            return zone

# Fonction qui détermine la voie à prendre en fonction de l'index des gares. Elle compare les deux index et renvoie la voie à prendre.
def deter_voie(depart, destination):
    depart_index = stations_valeur.index(stations[depart])
    destination_index = stations_valeur.index(stations[destination])
    if depart_index < destination_index:
        voie = "Voie 1 (Meinohama > Fukuokafuko)"
    else:
        voie = "Voie 2 (Fukuokafuko > Meinohama)"
    return voie

# Fonction qui calcul le prix total du trajet en allant chercher les prix dans le dictionnaire tarifs. Elle renvoie le prix total.
def calc_prix(nb_adultes, nb_reduits, zone):
    prix_adultes = nb_adultes * tarifs[zone]["plein"]
    prix_reduits = nb_reduits * tarifs[zone]["reduit"]
    return prix_adultes + prix_reduits

######################################### PROCEDURE D'AFFICHAGE ####################################
def resume(trajet):
    nb_adultes, nb_reduits, zone, prix_total, voie = trajet
    print("\nDétails du voyage :")
    print("Nombre de billets adultes : ",nb_adultes)
    print("Nombre de billets à tarif réduit : ",nb_reduits)
    print("Zone tarifaire : ",zone)
    print("Prix total à payer : ",prix_total," euros")
    print("Voie à prendre :",voie)

trajets = []
os.system("cls")

######################################### PROGRAMME MAIN ###########################################
while True:
    print("\n           /////// ")
    print("         ///       ")
    print("  //////////////   ")
    print("      ///          ")
    print("///////            ")
    print("\nBienvenue sur la billetterie du métro municipal de Fukuoka.")
    show_actions()
    action = input()

    if action == "1":
        add_trajet(trajets)
    elif action == "2":
        if not trajets :
            print("Il n'y a pas de trajet à afficher.")
            time.sleep(1)
            os.system("cls")
        else:
            os.system("cls")
            for i, trajet in enumerate(trajets, start=1):
                print(f"\nTrajet {i}:")
                resume(trajet)
                print("\n")
    elif action == "3":
        print("Sortie du programme.\nÀ bientôt !")
        break
    else:
        os.system("cls")
        print("Choix non valide, veuillez entrer un chiffre entre 1 et 3.")
