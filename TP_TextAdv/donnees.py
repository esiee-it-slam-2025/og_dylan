# Dictionnaire pour le personnage
personnage = {
    "Prénom" : None,
    "Âge" : None,
    "PV": 70,
    "Jutsu" : None,
    "Badges" : 0,
    "Yen" : 500,
}

# Dictionnaire pour le mannequin
mannequin = {
    "PV" : 50,
    "DMG_min" : 7,
    "DMG_max" : 25
}

# Dictionnaire pour les pouvoirs
jutsus = {
    "Rasengan": {
        "dégat" : 20,
        "niveau" : 5,
    },
    "Chidori": {
        "dégat": 25,
        "niveau": 0,
    },
    "Kirin": {
        "dégat": 30,
        "niveau": 0,
    },
    "Amaterasu": {
        "dégat": 15,
        "niveau": 0,
    },
    "Tsukuyomi": {
        "dégat": 10,
        "niveau": 0,
    },
    "Susanoo": {
        "dégat": 30,
        "niveau": 0,
    },
    "Flying Raijin Jutsu": {
        "dégat": 20,
        "niveau": 0,
    },
    "Eight Trigrams Sixty-Four Palms": {
        "dégat": 15,
        "niveau": 0,
    }
}

# Dictionnaire pour les plats en stocks
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

# Dictionnaire pour afficher les différents lieux, leurs lieux possibles d'accès et leurs actions
lieux_AU = {
    "Hall": {
        "lieux": ["Aller au Couloir RDC","Ouvrir son Casier", "Sortir du Lycée AU"],
        "actions": ["Observer", "Carte d'identité","Quitter"]
    },
    "CouloirRDC": {
        "lieux": ["Monter au Couloir 1e étage", "Entrer en Classe 1-A","Retourner au Hall"],
        "actions": ["Observer"]
    },
    "Classe1A": {
        "lieux": ["Sortir de la Classe 1-A"],
        "actions": ["Observer", "Demander le pass d'entraînement", "Montrer les badges"]
    },
    "Couloir1E": {
        "lieux": ["Descendre au Couloir RDC", "Entrer dans la Cafétéria", "Entrer dans la Salle D'entraînement"],
        "actions": ["Observer"]
    },
    "Caféteria": {
        "lieux": ["Sortir de la Caféteria"],
        "actions": ["Observer", "Manger", "Acheter"]
    },
    "SalleEntrainement": {
        "lieux": ["Sortir de la Salle D'entraînement"],
        "actions": ["Observer", "Combattre","Améliorer son jutsu"]
    },
    "Casier":{
        "lieux": ["Fermer son Casier"],
        "actions": ["Observer", "Changer de jutsus"]
    },
    "Rue":{
        "lieux": ["Entrer dans le Lycée AU", "Aller à l'Aéroport","Aller au Casino"],
        "actions": ["Observer"]
    },
    "Aéroport":{
        "lieux": ["Sortir de l'Aéroport"],
        "actions": ["Observer", "Prendre des vacances"]
    },
    "Casino":{
        "lieux": ["Sortir du Casino"],
        "actions": ["Observer", "Jouer"]
    }
}

# Liste objet clé
objets_cles = []

# Dictionnaire inventaire nourriture
inventaire_nourriture = {}

# Class pour changer la couleur du texte dans la console
class colors:
    init = '\033[0m'
    rouge = '\033[31m'
    bleu = '\033[34m'
    vert = '\033[32m'