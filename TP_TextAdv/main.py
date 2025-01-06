import os
import time
import tkinter as tk
from PIL import Image, ImageTk
from donnees import *
from lieux import *
from fonction_utilitaires import *

# Classe pour afficher les images en fonction des lieux et naviguer dans le jeu
class Interface:
    def __init__(interface):
        interface.img = tk.Tk()
        interface.img.title("~~~~~~~~~~~~~~~~~~~~~~~~~~~LYCEE AU~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        interface.img_display = tk.Label(interface.img)
        interface.img_display.pack()

        interface.emplacement = "Hall"
        interface.maj_lieu(interface.emplacement)

    def maj_lieu(interface, nom_lieu):
        chemin_image = f"images/{nom_lieu}.jpg" # <---------------------- VEUILLEZ CHANGER LE CHEMIN D'ACCES ICI POUR POUVOIR AFFICHER LES IMAGES
        image = Image.open(chemin_image)

        image_resized = image.resize((720, 480), Image.Resampling.BILINEAR )
        photo = ImageTk.PhotoImage(image_resized)

        interface.img_display.config(image=photo)
        interface.img_display.image = photo

    def chang_lieu(interface, nouvel_emplacement):
        interface.emplacement = nouvel_emplacement
        interface.maj_lieu(interface.emplacement)

    def lancer(interface):
        interface.img.mainloop()

# LE MAIN
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

    interface = Interface()
    lieux = {
        "Hall": lieu_hall,
        "CouloirRDC": lieu_couloir_rdc,
        "Classe1A": lieu_classe_1A,
        "Couloir1E": lieu_couloir_1e_etage,
        "Caféteria": lieu_cafeteria_1e_etage,
        "SalleEntrainement": lieu_salle_entrainement,
        "Casier": lieu_casier,
        "Rue": lieu_rue,
        "Aéroport": lieu_aeroport,
        "Casino": lieu_casino
    }

    while True:
        emplacements = lieux[interface.emplacement]()
        interface.chang_lieu(emplacements)

if __name__ == "__main__":
    intro()
    print("Fin du jeu.")
