import random
import string
#1.Feladat
#Sorsolás: Készíts egy egyszerű sorsolást, ahol a felhasználók nevei közül választhatsz ki véletlenszerűen egyet.
# nevek = ['Anna', 'Béla', 'Cecil', 'Dávid', 'Emma']
# nev = random.choice(nevek)
# print(f"A választott név: {nev}")
# print(f"A választott nevek: {random.sample(nevek,2)}")

#2.Feladat
#Véletlenszerű mondatok generálása: Készíts egy egyszerű mondatgenerátort, amely véletlenszerűen kiválaszt szavakat különböző listákból.
# alany = ['A macska', 'A kutya', 'A kisfiú', 'A tanár']
# ige = ['fut', 'ugrik', 'alszik', 'játszik']
# targy = ['a labdával', 'a fűben', 'a házban', 'a barátokkal']
# print(f"{random.choice(alany)} {random.choice(ige)} {random.choice(targy)}")

# 3.Feladat
# Jelszó generálása
karakterek = string.ascii_letters + string.digits
jelszo = "".join(random.choice(karakterek) for i in range(8))
print(jelszo)

with open("password.txt","w") as file:
    file.write(f"{jelszo}; ")

# 4.Feladat
# kő papír olló
# lista=['kő','papír','olló']
# gep = random.choice(lista)
# user = input("Válassz egyet(kő papír olló):")

# if user == gep:
#     print("Döntetetlen.")
# elif user == "kő" and gep == "olló" or user == "olló" and gep=="papír" or user== "papír" and gep == "kő":
#     print("Győztél!")
# else:
#     print("Vesztettél!")

# print(f"A gép választotta: {gep}, választásod: {user}")

# 5.Feladat
# Készíts egy programot ami bekér 1 és 200 között 15db számot és hozzá kell adni a számokat egy listához ha páros,
# és addig kell a listához adni a számokat, amíg nincs meg az 15db.
# Írasd ki a lista hosszát, hogy le tudjuk ellenőrizni, hogy meg van-e az 15 db.
# Írd ki a számokat pontos vesszővel elválasztva.

# szamok = []
# while len(szamok)<15:
#     szam = int(input("Adj meg egy számot 1-200 között: "))
#     if szam % 2 == 0:
#         szamok.append(szam)

# print(f"A lista hossza: {len(szamok)}.")
# print('; '.join(map(str,szamok)))

# szamok = []
# while len(szamok)<15:
#     szam = random.randint(1,200)
#     if szam % 2 == 0:
#         szamok.append(szam)

# print(f"A lista hossza: {len(szamok)}.")
# print('; '.join(map(str,szamok)))

# with open("numbers.txt", "w") as file:
#     file.write('; '.join(map(str,szamok)))

# fajl = open('szamok.txt', 'w')  # Fájl megnyitása írásra
    
# fajl.close()  

with open("movies.txt", "r") as file:
    lines = file.readlines()

    for i in lines:
        i = i.strip()
        szoveg = i.split(",")
        print(",".join(szoveg))
