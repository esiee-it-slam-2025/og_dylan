import os
import sys
import time
import random

# ****************************************************************************************************************************************************************
# /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  CLASSES
# ****************************************************************************************************************************************************************
class Creature:
    def __init__(self):
        self.pv = 30
        self.degats = 10
        self.etat = ""

    def attaque(self, cible):
        cible.pv -= self.degats

class Heros(Creature):
    def __init__(self, nom, degats):
        super().__init__()
        self.nom = nom
        self.degats = degats
        self.pm = 5

    def attaque(self, cible):
        print("ATTAQUE BASIQUANNNNCE!!!!!!!!!!!!!!!!!!!!")
        super().attaque(cible)

    def magie(self, cible):
        print("ATTAQUE MAGIQUE DE LA MORT!!!!!!!!!!!!!!!!!!!!")
        if self.pm > 0:
            self.pm -= 1
            cible.pv -= self.degats * 2
        else:
            print("Vous n'avez plus de mana.")

class Monstre(Creature):
    def __init__(self):
        super().__init__()

    def attaque(self, cible):
        print("ATTAQUE BASIQUE DU MONSTRE !!!!!!!!!!!!!!!!!!!!")
        super().attaque(cible)

    def venin(self, cible):
        print("EMPOISONNEMENT MAXIMUUUUUM")
        cible.etat = "Empoisonné"
        cible.pv -= 1


# ****************************************************************************************************************************************************************
# /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  FONCTIONS UTILITAIRES
# ****************************************************************************************************************************************************************
armes = {"Epée": 5, "Arc": 4, "Couteau à beurre": 1}

def verif_int(texte, lim):
    while True:
        valeur = input(texte)
        if valeur.isdigit() and 1 <= int(valeur) <= lim:
            return int(valeur)
        else:
            print("Veuillez entrer un nombre entier entre 1 et", lim)

def choix_armes():
    print("Liste des armes :")
    for index, arme in enumerate(armes, start=1):
        print(f"{index}. {arme}")
    choix = verif_int("\nLequel choisissez-vous ?\n", len(armes))
    return list(armes.values())[choix-1]

def fight(hero, monstre):
    empois = 0
    os.system("cls")
    print(f"Vous combattez un monstre. Il a {monstre.pv} PV.")

    while hero.pv > 0:
        if hero.etat == "Empoisonné":
            print("Vous perdez 1 PV à cause de l'empoisonnement...")
            hero.pv -= 1
            time.sleep(1)
        os.system("cls")
        print("PV restants de ", hero.nom, ":", hero.pv)
        print("PV restants du monstre :", monstre.pv)
        print("\n")
        reponse_action = verif_int("| Que voulez-vous faire?\n| 1 - Attaquer\n|-> ", 1)
        if reponse_action == 1:
            reponse_action = verif_int("| Quelle attaque?\n| 1 - Attaque basique\n| 2 - Attaque magique\n|-> ", 2)
            if reponse_action == 1:
                hero.attaque(monstre)
            else:
                hero.magie(monstre)
            time.sleep(3)
            if monstre.pv > 0 :
                if empois == 0:
                    empoisonne = random.randint(0, 100)
                    if empoisonne > 50:
                        empois = 1
                        monstre.venin(hero)
                        time.sleep(1)     
                        continue
                print("Le monstre réplique et envoie son poing malicieux! -"+str(monstre.degats)+" PV pour vous.")
                time.sleep(1)
                monstre.attaque(hero)
                time.sleep(1)
                os.system("cls")

        if hero.pv <= 0:
            print("Vous avez perdu.")
            print("Fin du jeu.")
            sys.exit()

        if monstre.pv <= 0:
            print("Vous avez gagné le combat !")
            time.sleep(4)
            os.system("cls")
            break

# ****************************************************************************************************************************************************************
# /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  MAIN
# ****************************************************************************************************************************************************************
def intro():
    print("===============================================================")
    print("|| Bienvenue dans le système de combat POO (Punch Out Out) ! ||")
    print("===============================================================")
    os.system("cls")
    nom_hero = input("Quel est votre nom ?\n")
    degats_hero = choix_armes()
    hero = Heros(nom_hero, degats_hero)
    monstre = Monstre()
    fight(hero, monstre)

if __name__ == "__main__":
    intro()
    print("Fin du jeu.")
