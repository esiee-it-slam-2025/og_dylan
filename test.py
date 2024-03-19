
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
        "lieux": ["Hall", "Aéroport","Casino"],
        "actions": ["Observer"]
    },
    "Aéroport":{
        "lieux": ["Rue"],
        "actions": ["Observer", "Prendre des vacances"]
    },
    "Casino":{
        "lieux": ["Rue"],
        "actions": ["Observer", "Jouer"]
    }
}

def proposer_action_lieu(lieu, choix):
    if choix == "lieu":
        print("│ [Lieux] ")
        for li in lieux_AU[lieu]["lieux"]:
            print("|  " + str(lieux_AU[lieu]['lieux'].index(li) + 1) + "- " + li)
    elif choix == "action":
        print("│ [Actions] ")
        for ac in lieux_AU[lieu]["actions"]:
            print("|  " + str(lieux_AU[lieu]['actions'].index(ac) + 1) + "- " + ac)

def verif_int(texte, lim):
    while True:
        valeur = input(texte)
        if valeur.isdigit() and int(valeur) >= 0 and int(valeur) <= lim:
            return int(valeur)
        else:
            print("Veuillez entrer un nombre entier valable.")

def fonc_chang_lieu(taille,lieu):
    proposer_action_lieu(lieu,"lieu")
    reponse_lieu = verif_int("> ", len(lieux_AU[lieu]["lieux"]))
    for i in range (taille+1):
        if reponse_lieu == i :
            return lieux_AU[lieu]["lieux"][i-1]


proposer_action_lieu("Rue","lieu")
a = fonc_chang_lieu(len(lieux_AU["Rue"]["lieux"]),"Rue")
print(a)