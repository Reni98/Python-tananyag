# print("1.Feladat: Kisebb-nagyobb meghatározása.")
# szam1 = int(input("Kérem az első számot: "))
# szam2 = int(input("Kérem a második számot: "))

# if szam1> szam2:
#     print(f"A nagyobb szám {szam1}, a kisebb {szam2}")
# elif szam2> szam1:
#     print(f"A nagyobb szám {szam2}, a kisebb {szam1}")
# else:
#     print("A két szám egyenlő.")


print("2. feladat: Szökőév listázó")
evszam1 = int(input("Kérem az egyik évszámot: "))
evszam2 = int(input("Kérem a másik évszámot:"))
evek = []

if evszam1 < evszam2:
    start = evszam1
    end = evszam2

elif evszam2 < evszam1:
    start = evszam2
    end = evszam1
for ev in range(start,end+1):
    evek.append(ev)

# print(evek)
szokevek = []
for szokoev in evek:
    if szokoev % 4 == 0 and szokoev % 100 != 0:
        szokevek.append(szokoev)
    elif szokoev % 400 == 0:
        szokevek.append(szokoev)

if len(szokevek) == 0:
    print("Nincs szökőév a megadott tartományban")

else:
    str_evek = szokevek
    print(f"Szökőévek: {'; '.join(map(str,str_evek))}")



