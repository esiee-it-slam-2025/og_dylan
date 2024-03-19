import os,time,sys,random
from donnees_personnage import *
from lieux import *
from fonction_utilitaires import *

# ****************************************************************************************************************************************************************
# /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  INTRODUCTION
# ****************************************************************************************************************************************************************
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
    
    emplacement = "Hall"
    while True:
        if emplacement == "Hall":
            emplacement = lieu_hall()
        elif emplacement == "CouloirRDC":
            emplacement = lieu_couloir_rdc()
        elif emplacement == "Classe1A":
            emplacement = lieu_classe_1A()
        elif emplacement == "Couloir1E":
            emplacement = lieu_couloir_1e_etage()
        elif emplacement == "Caféteria":
            emplacement = lieu_cafeteria_1e_etage()
        elif emplacement == "SalleEntrainement":
            emplacement = lieu_salle_entrainement()
        elif emplacement == "Casier":
            emplacement = lieu_casier()
        elif emplacement == "Rue":
            emplacement = lieu_rue()
        elif emplacement == "Aéroport":
            emplacement = lieu_aeroport()

# ****************************************************************************************************************************************************************
# /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  EXECUTION
# ****************************************************************************************************************************************************************

# Pour lancer le jeu, on appelle la fonction d'introduction
if __name__ == "__main__":
    intro()
    print("Fin du jeu.")
