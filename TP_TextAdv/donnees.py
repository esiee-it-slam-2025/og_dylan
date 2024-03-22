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
        "actions": ["Observer", "Combattre"]
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

objets_cles = ["smartphone"]
inventaire_nourriture = {}

class colors:
    init = '\033[0m'
    rouge = '\033[31m'
    bleu = '\033[34m'