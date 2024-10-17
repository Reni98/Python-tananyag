import random
# 1.Feladat
# Ha egy szabályos pénzérmét feldobunk, akkor egyenlő eséllyel lehet fej (F) vagy írás (I)
#  az eredmény. 
# Szimulálj öt pénzfeldobást, ahol azonos esélye van a fejnek és az írásnak is! 
# Az eredményt írasd ki txt fájlba.
# Kérj be a felhasználótól egy tippet, majd szimulálj egy pénzfeldobást és írasd ki, 
# hogy eltalálta-e vagy sem!

# F I I F I
# Kérek egy tippet (F/I): F
# A tipp F, a dobás eredménye I volt.
# Ön nem találta el!

# dobas=["F","I"]
# dobasok=[]
# for i in range(5):
#     dob = random.choice(dobas)
#     dobasok.append(dob)
# print(" ".join(dobasok))
# feldobas= random.choice(dobasok)
# tipp = input("Kérek egy tippet (F/I):")
# with open("penzdobas.txt", "a") as file:
#     file.write(f"A tipp {tipp},a dobás eredménye {feldobas} volt.")
#     if tipp == feldobas:
#         file.write("Eltaláltad!")
#         print("Eltaláltad!")
#     else:
#         file.write("Nem találtad el!")
#         print("Nem találtad el!")
# names=[]
# with open("nevek.txt","r") as file:
#     lines= file.readline().split(";")

#     for line in lines:
#         line = line.strip()       
#         names.append(line)


# names.sort()
# print(" ".join(names))

# with open("rendezett_nevek.txt","w") as fajl:
#     fajl.write(" ".join(names))

# Olvassuk be a szamok.txt fájlból az adatokat. Majd mentsük el a fájlba de már növekvő sorrendbe.
# numbers = []
# with open("random_szamok.txt", "r") as file:
#     lines = file.readlines()
#     for i in lines:
#         i = i.strip()
#         szam = i.split(",")
#         numbers.extend(szam)

#     numbers=[int(num) for num in numbers]

#     numbers.sort()
#     with open("rendezett_random_szamok.txt", "w") as fajl:
#         fajl.write(",".join(map(str, numbers)))

names = []
with open("osztalyatlag.txt", "r") as file:
    lines = file.readlines()
    for i in lines:
        i = i.strip()
        nev,atl = i.split(";")
        names.append((nev,float(atl)))


negyesfelettiek=[]
eredmenyek = 0
for nev, atl in names:
    eredmenyek += atl
    if atl > 4:
        negyesfelettiek.append(nev)
print(negyesfelettiek)
with open("atlag.txt", "w") as fajl:
    fajl.write(f"Az átlag: {eredmenyek/len(names)}")
    fajl.write(";".join(map(str,negyesfelettiek)))
