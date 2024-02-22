number_list1 = (2, 5, 8, 7, 6, 12, 14, 18)
number_list2 = (132, 80, 28, 371, 223, 42, 75, 375)
number_list3 = (61, 18, 36, 16, 8, 55, 74, 11)
number_list4 = (3, 15, 1, 12, 8, 6, 15, 23)
number_list5 = (22, 53, 180, 70, 13, 39, 21, 42)


def trouver_nombre(lis):
    for i in range(len(lis)):
        nbr = lis[i]
        if i == 0:
            if nbr % 2 != 0:
                if nbr == lis[i + 1] // 5:
                    print(nbr)
                    return nbr
                    
        elif i == len(lis) - 1:
            if nbr / 2 == lis[i - 1]:
                print(nbr)
                return nbr

        elif nbr % 2 != 0:
            if nbr == lis[i + 1] // 5 :
                print(nbr)
                return nbr
        else:
            if nbr / 2 == lis[i - 1]:
                print(nbr)
                return nbr

n1 = trouver_nombre(number_list1)/3
n2 = trouver_nombre(number_list2)/3
n3 = trouver_nombre(number_list3)/3
n4 = trouver_nombre(number_list4)/3
n5 = trouver_nombre(number_list5)/3

print("Le mot de passe est :", n1, ";", n2, ";", n3, ";", n4, ";", n5, ".")

        