import argparse,os,random,re
from datetime import datetime
from donnees import articles, interviews

# ****************************************************************************************************************************************************************
# /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  CLASSES
# ****************************************************************************************************************************************************************
# Classe parente ElementJournal
class ElementJournal():
    date = ""
    edition = ""
    auteur = ""
    titre = ""
    contenu = ""
    def __init__(self, date, edition, auteur, titre, contenu):
        self.date = date
        self.edition = edition
        self.auteur = auteur
        self.titre = titre
        self.contenu = contenu

    def afficher_details(self):
        print(f"Date: {self.date}")
        print(f"Auteur: {self.auteur}")
        print(f"Contenu: {self.contenu}")
        print(f"Édition: {self.edition}")

# Classe Article, enfante de ElementJournal
class Article(ElementJournal):
    def __init__(self, date, edition, auteur, titre, contenu):
        super().__init__(date, edition, auteur, titre, contenu)

# Classe Interview, enfante de ElementJournal
class Interview(ElementJournal):
    invite = ""
    def __init__(self, date, edition, auteur, invite, contenu):
        super().__init__(date, edition, auteur, invite, contenu)
        self.invite = invite

    def afficher_details(self):
        super().afficher_details()
        print(f"Invité: {self.invite}")

# Classe Generateur, importer les articles venant de donnees.py et afficher
class Generateur():
    def __init__(self, date, edition):
        self.date = date
        self.edition = edition

    def importer(self, articles, interviews):
        elements = []
        for donnees_art in articles:
            if donnees_art["date"] == self.date and (donnees_art["edition"] == self.edition):
                article = Article(donnees_art["date"], donnees_art["edition"], donnees_art["auteur"], donnees_art["titre"], donnees_art["contenu"])
                elements.append(article)

        for donnees_int in interviews:
            if donnees_int["date"] == self.date and (donnees_int["edition"] == self.edition):
                interview = Interview(donnees_int["date"], donnees_int["edition"], donnees_int["auteur"], donnees_int["invite"], donnees_int["contenu"])
                elements.append(interview)

        return elements

    def afficher(self, elements):
        print(f"==================================")
        print(f"*-*-*-*-*-* LeLutécien *-*-*-*-*-*")
        print(f"==================================")
        if elements:
            random.shuffle(elements)
            num = 1
            print("\n")
            for element in elements:
                print("Article n°",num)
                print("+" + "="*28 + "+")
                element.afficher_details()
                print("+" + "="*28 + "+") 
                num += 1
                print('\n')
        else:
            print(f"Il n'y a pas d'articles à cette date '{self.date}'")
            exit(1)

    def afficher_credit(self):
        with open("credits.txt", "r",encoding="utf-8") as file:
            credit_content = file.read()
        print("Crédits :")
        print(credit_content)

# ****************************************************************************************************************************************************************
# /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  MAIN
# ****************************************************************************************************************************************************************
if __name__ == "__main__":
    os.system("cls")

    parser = argparse.ArgumentParser(description="Génère le journal du jour selon une date et une région.")
    parser.add_argument("date", help="Date du journal à générer, sous le format 'annee-mois-jour'")
    parser.add_argument("edition", help="Édition du journal à générer", choices=["national", "idf", "paca"])

    args = parser.parse_args()

    try:
        date_str = args.date
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError as error:
        print(f"Erreur : La date '{date_str}' ne correspond pas au format 'AAAA-MM-JJ'")
        exit(1)

    generateur = Generateur(args.date, args.edition)

    elements = generateur.importer(articles, interviews)

    generateur.afficher(elements)
    generateur.afficher_credit()
