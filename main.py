# 1.Feladat
# Pizza rendelő program. 
# Az S méretű pizza 1500 Ft, M 2000 Ft, L 2500 FT.
# Kérjük be a felhasználótól, hogy milyen méretű pizzát szeretne rendelni. 
# Ha nem a megfelelő paramétereket adja meg, akkor írja ki, hogy érvénytelen. 
# Írja ki a választott pizza árát.

# small_pizza = 1500
# medium_pizza = 2000
# large_pizza = 2500

# price = 0

# pizza = input("Válassz egy pizza méretet(S, M, L):").upper()
# if pizza == "S":
#     price += small_pizza
# elif pizza == "M":
#     price += medium_pizza
# elif pizza == "L":
#     price += large_pizza
# else:
#     print("Nem helyes értéket adtál meg.")


# 2.Feladat
# Kérdezd meg a felhasználótól, hogy milyen feltétet szeretne pluszban,
# ha sajot plusz 300 FT,
# ha sonkát az 200 Ft, a kukorica 150 Ft. A végén írja ki a program az összeget.

# sajt = 300
# sonka = 200
# kukorica = 150

# feltet = input("Válassz feltétet(sajt, sonka,kukorica): ")
# if feltet == "sajt":
#     price += sajt
# elif feltet == "sonka":
#     price += sonka
# elif feltet == "kukorica":
#     price += kukorica

# print(f"A fizetendő összeg {price} Ft")

# bemenet = ""
# while bemenet.lower() != "exit":
#     bemenet = input("Írj be valamit (vagy írd be: exit a kilépéshez): ")
#     print("Te ezt írtad be:", bemenet)

# 3.Feladat
# While használatának gyakorlására feladat. 
# Addig kell bekérni a felhasználótól a korát ameddig nem számot ad meg.

# igaze = False

# while not igaze:
#     kor = input("Add meg a korod: ")
#     if kor.isdigit():
#         kor = int(kor)
#         print(f"A korod {kor}")
#         igaze = True
#         exit()
#     else:
#         print("Nem számot adtál meg.")

# 4.Feladat
# Számot kell bekérni a felhasználótól és addig fusson a program amíg el nem éri az összeg a 100-at, írja ki mindig az aktuál összeget, ha teljesül a feltétel lépjen ki a programból.

osszeg = 0
while osszeg < 100:
    szam = int(input("Adj meg egy számot: "))
    osszeg += szam
print(osszeg)


