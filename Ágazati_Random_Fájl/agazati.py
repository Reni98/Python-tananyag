# print("1. feladat: Kisebb-nagyobb meghatározása")
# szam1 = int(input("Kérem az első számot:"))
# szam2= int(input("Kérem a második számot:"))

# if szam1 > szam2:
#     print(f"A nagyobb szám {szam1}, a kisebb {szam2}")
# elif szam1<szam2:
#     print(f"A nagyobb szám {szam2}, a kisebb {szam1}")
# else:
#     print("A két szám egyenlő.")

print("2.feladat: Szökőév listázó")
evszam1 = int(input("Kérem az egyik évszámot:"))
evszam2 = int(input("Kérem a másik évszámot:"))

if evszam1 < evszam2:
    start = evszam1
    end = evszam2
elif evszam2 < evszam1:
    start = evszam2
    end = evszam1
evszamok = []

for ev in range(start,end+1):
    evszamok.append(ev)

szokoevek= []

for szokoev in evszamok:
    if szokoev % 4 == 0 and szokoev % 100 != 0:
        szokoevek.append(szokoev)
    elif szokoev % 400 == 0:
        szokoevek.append(szokoev)
        

if len(szokoevek)==0:
    print("Nincs szökőév a megadott tartományban!")
else:
    print(f"Szökőévek: {'; '.join(map(str,szokoevek))}")