import datetime
# print("Ez egy proba sor.\n Ez egy proba sor.")
# print("Ez egy proba sor. \t Ez egy proba sor.")

# nev = "Béla"
# print(f"Szia {type(nev)}!")

# szam = 400
# print(type(szam))

# pi = 3.14
# print(type(pi))

# logikai = False
# print(type(logikai))

# szam = 10
# print(type(szam))
# szam = str(szam)
# print(type(szam))

# szam = "56"
# print(type(szam))
# szam = int(szam)
# print(type(szam))

# szam1 = 30
# szam2 = 12
# osszeg = szam1 + szam2
# print(osszeg)
# print(szam1 + szam2)
# print(szam1-szam2)
# print(szam1*szam2)
# print(szam1/szam2)

# print(szam1%szam2)

# kor = int(input("Add meg a korodat: "))
# print(f"A te korod {kor}")
# print(f"A te korod {type(kor)}")
# ev = datetime.datetime.now()
# print(f"Ebben az évben születtél: {ev.year - kor}")

# nev = input("Add meg a nevedet: ")
# kor = int(input("Add meg a korodat: "))
# print(f"Szia {nev}!\nA korod {kor}")

# kor = int(input("Hány éves vagy: "))

# if kor > 18:
#     print("Remek, ihatsz kólát.")
# if kor == 18:
#     print("Szerencséd van ihatsz már kólát.")
# else:
#     print("Még nem ihatsz kólát.")

# szam = int(input("Adj meg egy számot:"))

# if szam == 12 or szam == 1 or szam == 2:
#     print("Tél.")
# elif szam == 3 or szam == 4 or szam == 5:
#     print("Tavasz.")
# elif szam == 6 or szam == 7 or szam == 8:
#     print("Nyár.")
# elif szam == 9 or szam == 10 or szam == 11:
#     print("Ősz.")

# szam1 = int(input("Add meg az első számot: "))
# szam2 = int(input("Add meg a másik a számot:"))
# muvelet = input("Válassz egy műveletet(+, -, *, /): ")

# if muvelet == "+":
#     osszeg = szam1 + szam2
# elif muvelet == "-":
#     osszeg = szam1- szam2
# elif muvelet == "*":
#     osszeg = szam1 * szam2
# elif muvelet == "/":
#     osszeg = szam1 / szam2

# print(f"Az eredmény: {osszeg}")

# Kérj be egy egész számot, és írd ki
# a kétszeresét,
# a heted részét (2 tizedes jegyre kerekítve),
# páros vagy páratlan.

# Írj be egy pozitív egész számot: 15
# A szám kétszerese: 30
# A szám heted része: 2.14
# 3-mal osztva az egészrész: 5 amaradék: 0
# A szám páratlan

# szam = int(input("Írj be egy pozitív egész számot: "))
# print(f"A szám kétszerese: {szam*2}")
# print(f"A szám heted része: {round(szam/7,2)}")
# print(f"3-mal osztva az egészrész: {round(szam/3)} a maradék: {szam%3}")
# print("Páros" if szam % 2 == 0 else "Páratlan")

# 1.Feladat
# Pizza rendelő program. 
#Az S méretű pizza 1500 Ft, M 2000 Ft, L 2500 FT.
# Kérjük be a felhasználótól, hogy milyen méretű pizzát szeretne rendelni.
# Ha nem a megfelelő paramétereket adja meg, akkor írja ki, hogy érvénytelen.
# Írja ki a választott pizza árát.

small_pizza = 1500
medium_pizza = 2000
large_pizza = 2500

price = 0

pizza = input("Milyen méretű pizzát kérsz(S,M,L):").upper()
if pizza == "S":
    price += small_pizza
if pizza == "M":
    price += medium_pizza
if pizza == "L":
    price += large_pizza

print(f"A választott pizza ára: {price} Ft")

# 2.Feladat
# Kérdezd meg a felhasználótól, hogy milyen feltétet szeretne pluszban, 
#ha sajot plusz 300 FT,
#ha sonkát az 200 Ft, 
#a kukorica 150 Ft. 
#A végén írja ki a program az összeget.

feltet = input("Válassz egy feltétet(sajt, sonka,kukorica): ")
if feltet == "sajt":
    price += 300
elif feltet == "sonka":
    price += 200
elif feltet == "kukorica":
    price += 150

print(f"A fizetendő összeg: {price} Ft")






