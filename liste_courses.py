import os
import time

liste_course = {
    "pates": 2,
    "sauce tomate": 1,
    "parmesan": 1
}


def show_actions():
    print("Choisissez une action (1-4) : ")
    print("1 - Ajouter un article")
    print("2 - Supprimer un article")
    print("3 - Modifier la quantité d'un article")
    print("4 - Quitter le programme")

def affich_list():
    print("\nListe de courses actuelle :")
    position = 1
    for article in liste_course:
        quantite = liste_course[article]
        print(str(position)+". "+article+" : "+str(quantite))
        position += 1
    print()

def add_article():
    article = input("Entrez le nom de l'article à ajouter : ")
    quantite = int(input("Entrez la quantité pour "+article+" : "))
    liste_course[article] = quantite
    print(article+" a été ajouté à la liste.")
    time.sleep(1.5)
    os.system("cls") 

def supp_article():
    affich_list()
    choix = int(input("Entrez le numéro de l'article à supprimer : ")) - 1
    choix = verif_input(choix)
    list_cle = list(liste_course)
    article = list_cle[choix]
    del liste_course[article]
    print(article+" a été supprimé de la liste.")
    time.sleep(1.5)
    os.system("cls")

def modif_list():
    affich_list()
    choix = int(input("Entrez le numéro de l'article dont vous voulez modifier la quantité : ")) - 1
    choix = verif_input(choix)
    list_cle = list(liste_course)
    article = list_cle[choix]
    quantite = int(input("Entrez la nouvelle quantité pour " + article + " : "))
    liste_course[article] = quantite
    print("La liste a maintenant " + str(quantite) + " " + article)
    time.sleep(1.5)
    os.system("cls")

def verif_list():
    total = len(liste_course)
    if total == 0:
        return False
    return True

def verif_input(a):
    while a < 0 and a > len(liste_course):
        a = int(input("Veuillez entrer une valeur entre 0 et "+len(liste_course)))
    return a

def list_vide():
    print("\nVotre liste est vide.")
    time.sleep(1.5)
    os.system("cls")

while True:
    os.system("cls") 
    print("Bienvenue dans la liste de courses.\n")
    show_actions()
    action = input()

    if action == "1":
        add_article()
    elif action == "2":
        if verif_list(): 
            supp_article()
        else:
            list_vide()
    elif action == "3":
        if verif_list(): 
            modif_list()
        else:
            list_vide()
    elif action == "4":
        print("À bientôt !")
        break
    else:
        os.system("cls")
        print("Choix non valide, veuillez entrer un chiffre entre 1 et 4.")

    affich_list()  
