# Projet JO 2024 - Système de Billetterie
Cette application de billetterie pour les Jeux Olympiques 2024 permet aux utilisateurs d'acheter, gérer et vérifier des billets pour les différents événements olympiques.


## Prérequis

Python 3.x
WampServer (ou équivalent pour MySQL)
Visual Studio Code avec l'extension Live Server

## Installation et configuration
1. Environnement de développement
	- Installer Python - Télécharger et installer depuis python.org
	- Installer WampServer - Télécharger et installer depuis www.wampserver.com

2. Dépendances Python
	- `pip install django-cors-headers`
	- `pip install djangorestframework`
	- `pip install mysqlclient`
	- `pip install Pillow`

3. Configuration de la base de données
	- Ouvrir phpMyAdmin via WampServer
	- Créer une nouvelle base de données nommée api_joticket

4. Préparation de l'application Django
	- Générer les migrations
	`py manage.py makemigrations`

	- Appliquer les migrations
	`py manage.py migrate`

	- Importer le fichier SQL fourni avec le projet

# Lancement de l'application
## Démarrer le backend

`cd admin`

`py manage.py runserver`

Le serveur Django sera accessible à l'adresse http://127.0.0.1:8000/

# Lancer l'application frontend

1. Ouvrir le projet dans Visual Studio Code
2. Faire un clic droit sur mobile/index.html
3. Sélectionner "Open with Live Server"

L'application frontend s'ouvrira dans votre navigateur par défaut.

# Structure du projet

- mobile/ - Application web destinée aux utilisateurs
- scanner/ - Outil de vérification des billets (scan de QR code)
- admin/ - Backend Django et interface d'administration

# Fonctionnalités principales

- Inscription et connexion des utilisateurs
- Visualisation des événements et achat de billets
- Personnalisation du profil utilisateur
- Génération et téléchargement de billets (PDF et QR Code)
- Vérification de l'authenticité des billets via QR Code
- Interface d'administration pour gérer les événements