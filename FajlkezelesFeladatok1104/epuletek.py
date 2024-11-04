lista = []
varosok = []
legrebbi = float("inf")
legregebbi_epulet = None
with open("epuletek.txt", "r", encoding="UTF8") as file:
    lines = file.readlines()

    for line in lines[1:]:
        line = line.strip()
        adat = line.split(";")

        nev = adat[0]
        varos = adat[1]
        orszag = adat[2]
        magassag = int(adat[3])
        emelet = int(adat[4])
        epult = int(adat[5])
        lista.append([nev, varos, orszag, magassag, emelet, epult])

for item in lista:
    #print(f"{item[0]}, {item[1]}, {item[2]}, {item[3]}, {item[4]}, {item[5]}")
    if item[1] not in varosok:
        varosok.append(item[1])
    if item[5] < legrebbi:
        legrebbi = item[5]
        legregebbi_epulet = item[0]

print(f"{legregebbi_epulet}, {legrebbi}")
print(";".join(varosok))
print(f"Városok száma: {len(varosok)}")

