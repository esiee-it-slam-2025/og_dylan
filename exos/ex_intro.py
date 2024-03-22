def func(a, b):
    return (a + b) * 2

nombreA = 1

while True:
    nombreB = input("Entrez une valeur.\n")
    if nombreB.isdigit():
        nombreB = int(nombreB)
        if nombreB > 0:
            break
        else:
            print("Veuillez entrer une valeur supérieure à 0.")
    else:
        print("Veuillez entrer un entier.")

nombreC = func(nombreA, nombreB)


if nombreC > 20:
    print("Résultat énorme !")
else:
    print("Résultat pas ouf..")
    