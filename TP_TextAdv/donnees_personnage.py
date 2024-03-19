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
plat_cle = list(plats_stock)

lieux_AU = {
    "Hall": {
        "lieux": ["Couloir RDC","Casier", "Rue"],
        "actions": ["Observer", "Carte d'identité","Quitter"]
    },
    "CouloirRDC": {
        "lieux": ["Couloir 1e étage", "Classe 1-A","Hall"],
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

objets_cles = ["smartphone","Clé"]
inventaire_nourriture = {}