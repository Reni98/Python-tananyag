def beolvas(fajlbeolv):
    with open(fajlbeolv, "r", encoding="UTF8") as file:
        lista = []
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
            lista.append([nev,varos,orszag, magassag, emelet,epult])
        return lista
    
def kiir(lista):
    for item in lista:
        print(f"{item[0]}, {item[1]}, {item[2]}, {item[3]},{item[4]},{item[5]},")
    
def varosok(lista):
    varos_ok = []
    for item in lista:
        if item[1] not in varos_ok:
            varos_ok.append(item[1])
    print(";".join(varos_ok))
    print(len(varos_ok))

fajlkezeles = beolvas("epuletek.txt")
fajl_kiir = kiir(fajlkezeles)
varos_kiir = varosok(fajlkezeles)