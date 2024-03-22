import os
import time
import random

jutsus = {
    "Rasengan": {
        "dégat": 20,
        "niveau": 0,
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

personnage = {
    "PV": 70,
    "Badges": 0,
    "Yen": 500,
    "Jutsu": "Susanoo"
}

nom_jutsu = list(jutsus.keys())[0]  # Sélectionner un jutsu spécifique

jutsus[nom_jutsu]["niveau"] += 1
jutsus[nom_jutsu]["dégat"] += 5
print(nom_jutsu, "amélioré !")
print("Il est maintenant niveau", jutsus[nom_jutsu]["niveau"], "et inflige", jutsus[nom_jutsu]["dégat"], "DMG!!")
personnage["Yen"] -= 300