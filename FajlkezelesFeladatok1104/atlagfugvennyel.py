def beolvas(fajlbeolv):
    lista = []
    with open(fajlbeolv, "r", encoding="UTF8") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            adat = line.split(";")

            nev = adat[0]
            atlag = float(adat[1])
            lista.append([nev, atlag])
    return lista

def kiolvas(lista):
    atlagok = []
    for item in lista:
        print(f"{item[0]}, {item[1]}")
        atlagok.append(item[1])
    return atlagok


def atlag(atlagok):
    print(f"Az osztály átlaga: {round(sum(atlagok)/len(atlagok), 2)}")
   
fajlkezel = beolvas("atlag.txt")
fajl_kiolv = kiolvas(fajlkezel)
atlag_szamit = atlag(fajl_kiolv)