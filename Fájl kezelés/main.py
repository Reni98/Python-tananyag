#Fájlba írás
# Fájl megnyitása írásra:

# Egy fájl megnyitásához használjuk az open() függvényt.
# Az első paraméter a fájl neve, a második az üzemmód (itt: 'w' - írás).
# Ha a fájl nem létezik, a program létrehozza. Ha már létezik, felülírja a tartalmát.

fajl = open('szamok.txt', 'w')  # Fájl megnyitása írásra
# Adatok írása a fájlba:

# A következő példában a program 1-től 10-ig számokat ír a fájlba, 10 sorban, minden sorban 10 számot.
# Az íráshoz a print() függvényt használjuk, ahol megadjuk a fájl nevét (file=fajl), ahová írni szeretnénk.
for i in range(10):
    sor = [str(i*10 + i1) for i1 in range(1, 11)]
    print(' '.join(sor), file=fajl)  # A sorokat a fájlba írja
# Fájl bezárása:

# A fájl írása után mindig zárjuk be a fájlt a close() függvénnyel, hogy biztosak legyünk abban, hogy az adatok valóban elmentődtek.
fajl.close()  # Fájl lezárása

# Fájl olvasása
# Fájl megnyitása olvasásra:

# Olvasáshoz használjuk az open() függvényt 'r' üzemmóddal (olvasás).
fajl = open('szamok.txt', 'r')  # Fájl megnyitása olvasásra
# Adatok olvasása a fájlból:

# A readlines() függvény minden sort beolvas, és egy listát ad vissza, ahol minden sor egy listaelem.
sorok = fajl.readlines()  # Sorok beolvasása a fájlból
for sor in sorok:
    print(sor.strip())  # A sorokat kiírjuk a képernyőre, a felesleges szóközöket eltávolítva
# Fájl lezárása:

# Olvasás után is zárjuk be a fájlt.
fajl.close()  # Fájl lezárása olvasás után
