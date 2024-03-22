teams_points = {
    "Paris SG": 85,
    "Lens": 84,
    "Marseille": 73,
    "Rennes": 68,
    "Lille": 67,
    "Monaco": 65,
    "Lyon": 62,
}
list_cle = list(teams_points)
list_valeur = list(teams_points.values())

UCL = []
EL = []

i = 0
for x in teams_points:
    if i < 2 :
        UCL.append(x)
    elif i >= 2 and i <5:
        EL.append(x)
    i = i+1

print(UCL)
print(EL)

def int_to_rank(choix):
    if choix == 1:
        return "1er"
    if choix == 2:
        return "2ème"
    if choix == 3:
        return "3ème"
    if choix == 4:
        return "4ème"
    if choix == 5:
        return "5ème"
    if choix == 6:
        return "6ème"
    if choix == 7:
        return "7ème"

def affich_info(num_equipe):
    print("Nom de l'équipe : "+list_cle[num_equipe-1])
    print("Classement : "+int_to_rank(num_equipe))
    print("Total de points la saison dernière : "+str(list_valeur[num_equipe-1]))
    for x in UCL:
        if x == list_cle[num_equipe-1]:
            print("Compétition joué la saison suivante : Ligue des Champions")
    for x in EL :
        if x == list_cle[num_equipe-1]:
            print("Compétition joué la saison suivante : Ligue Europa")
        
def verif_choix_int(c,nbr):
    while(True):
        if c < 1 or c > nbr : 
                c = int(input("Erreur, saisissez une valeur entre 1 et "+str(nbr)+".\n"))
        else :
            return c


choix_infos = int(input("\nInfos entre :\n1 - Equipe\n2 - Competition\n"))
choix_infos = verif_choix_int(choix_infos,2)
print("\n")


if choix_infos == 1:
    i = 1
    print("De quelle équipe voulez-vous des informations ?\n")
    for team in teams_points:
        print(str(i) + " - " + team)
        i = i + 1
    choix_infos_equipe = int(input())
    choix_infos_equipe = verif_choix_int(choix_infos_equipe,len(list_cle))
    affich_info(choix_infos_equipe)

if choix_infos == 2:
    print("Quelle compétition voulez-vous regarder ?\nUCL - Ligue des champions\nEL - Ligue Europa")
    while(True):
        choix_infos_competition = input()
        if choix_infos_competition != "UCL" and choix_infos_competition != "EL": 
            print("Quelle compétition voulez-vous regarder ?\n1 - Ligue des champions\n2 - Ligue Europa")
        else :
            break
    if choix_infos_competition == "UCL":
        print("Les équipes françaises en course seront :")
        print(UCL)
    else:
        print("Les équipes françaises en course seront :")
        print(EL)


    





