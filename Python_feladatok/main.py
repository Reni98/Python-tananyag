"""
jegyek = [2,3,4,5,2,5,2,5,3,1,4,4,5,3,2,5,5]
for i in range(1,6):
    db = 0
    for szam in jegyek:
        if i == szam:
            db+=1
    print(f"Az érdemjegyből: {i}, {db} db van.")
"""

lista = ["alma", "eper", "körte", "cseresznye","körte","körte","eper","eper","eper",]
rendezett_lista=[]
for i in range(len(lista)):
    db=0
    if lista[i] not in rendezett_lista:
        for list in lista:
            if lista[i] == list:
                db+=1
        print(f"A szóból: {lista[i]}, {db}van")
        rendezett_lista.append(lista[i])

# 1. Feladat
#     Írd ki a képernyőre a számokat szóközzel elválasztva 1 - től 15 - ig! Valósítsd meg for ciklussal, while -ciklussal és 1 soros megoldással is !
#     Figyelj arra, hogy az utolsó számot követően ne írja ki a vesszőt!

#     Minta:
#     1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
#     1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
#     1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15

for i in range(3):
    for j in range(1,16):
        if j == 15:
            print(j)
        else:
            print(j, end=", ")

# 2. Feladat
# Feladat leírása: Írj programot, amely lépcsőzetesen írja ki a számokat 1-től 15-ig. A kimenet formája egy lépcsőzetes alakzatot fog formálni, ahol minden sorban egyre több szám jelenik meg.
	
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9 10
# 1 2 3 4 5 6 7 8 9 10 11
# 1 2 3 4 5 6 7 8 9 10 11 12
# 1 2 3 4 5 6 7 8 9 10 11 12 13
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 

