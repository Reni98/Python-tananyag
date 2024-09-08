# A ciklusok olyan programozási struktúrák, amelyek lehetővé teszik, hogy egy adott kódrészletet többször végrehajtsunk. Két fő ciklusfajtát különböztetünk meg Pythonban: a while és a for ciklusokat. 

# 1. while ciklus
# A while ciklus addig ismétel egy kódrészletet, amíg a megadott feltétel igaz (True). Ha a feltétel hamis (False), a ciklus befejeződik.

# Példa: while ciklus használata
szam = 1

while szam <= 5:
    print(szam)
    szam += 1

# Ebben a példában a ciklus addig fut, amíg a szam változó értéke kisebb vagy egyenlő, mint 5.  Minden egyes iteráció után a szam változó értéke eggyel növekszik. 

# Mikor használjunk while ciklust?
# Ismétlés, amíg egy feltétel igaz: Olyan helyzetekben, amikor nem tudjuk előre, hány alkalommal kell végrehajtani a ciklust, de van egy feltétel, amely alapján eldönthetjük, hogy folytatni kell-e vagy sem (pl. felhasználói bemenetek ellenőrzése).
# Végtelen ciklusok: Olyan esetekben, amikor a ciklust folyamatosan futtatni szeretnénk, amíg egy megszakító esemény be nem következik.

# 2. for ciklus
# A for ciklus egy iterálható objektum (pl. lista, tuple, string) elemein megy végig, és minden iterációban végrehajt egy kódrészletet az aktuális elemre.
# Példa: for ciklus használata
nevek = ["Anna", "Béla", "Cecília"]

for nev in nevek:
    print(nev)

# Ebben a példában a for ciklus a nevek listán iterál, és minden iterációban a nev változó az aktuális listabeli nevet tartalmazza.

# Mikor használjunk for ciklust?
# Iterálás egy kollekción: Olyan helyzetekben, amikor egy kollekció (pl. lista, tuple, dictionary, string) elemein szeretnénk végigmenni.
# Meghatározott számú ismétlés: Olyan esetekben, amikor előre tudjuk, hányszor kell végrehajtani a ciklust (pl. egy adott számú ismétlés range segítségével).

# Összehasonlítás 
# while ciklus
# Előnye: Rugalmas, mert addig fut, amíg a feltétel igaz.
# Hátránya: Könnyű végtelen ciklust létrehozni, ha nem gondoskodunk a feltétel hamissá válásáról.
# for ciklus
# Előnye: Kényelmes és olvasható, amikor egy kollekción iterálunk vagy meghatározott számú ismétlést végzünk.
# Hátránya: Kevésbé rugalmas olyan helyzetekben, amikor egy bonyolult feltételt kell ellenőrizni minden iteráció előtt.

# Példák konkrét feladatokra
# while ciklus használata felhasználói bemenet ellenőrzésére
bemenet = ""

while bemenet.lower() != "exit":
    bemenet = input("Írj be valamit (vagy írd be: exit a kilépéshez): ")
    print("Te ezt írtad be:", bemenet)

# Ebben a példában a ciklus addig fut, amíg a felhasználó be nem írja az "exit" szót.
# A .lower() metódus arra szolgál, hogy egy sztring (karakterlánc) minden betűjét kisbetűssé alakítsa. 

# for ciklus használata listán való iterálásra
szamok = [1, 2, 3, 4, 5]

for szam in szamok:
    print(szam)

# Ebben a példában a for ciklus a szamok listán iterál, és minden számot kiír.

# for ciklus használata meghatározott számú ismétlésre
for i in range(1, 6):
    print(i)

# Ebben a példában a for ciklus a range függvényt használja, hogy 1-től 5-ig iteráljon, és minden számot kiírjon.

# Összefoglalás
# A while és for ciklusok közötti választás a feladat természetétől függ. A while ciklusok jobbak olyan helyzetekben, amikor egy feltételtől függ a ciklus futása, míg a for ciklusok ideálisak kollekciókon való iterálásra vagy előre meghatározott számú ismétlésre. 


# Range függvény
# A range függvényt Pythonban arra használjuk, hogy egy sorozatot generáljunk, amely számokból áll, és amelyen könnyen végig tudunk iterálni egy for ciklus segítségével. A range függvény különösen hasznos, amikor előre meghatározott számú ismétlést szeretnénk végrehajtani.

# Szintaxis és használat
# A range függvény különböző módokon használható attól függően, hogy hány argumentumot adunk meg:

# range(stop): Egy paraméterrel.
# range(start, stop): Két paraméterrel.
# range(start, stop, step): Három paraméterrel.

for i in range(5):
    print(i)
# Ez a ciklus 0-tól 4-ig (5 kizárva) iterál


for i in range(1, 6):
    print(i)
# Ez a ciklus 1-től 5-ig (6 kizárva) iterál

for i in range(1, 10, 2):
    print(i)
# Ez a ciklus 1-től 9-ig iterál (10 kizárva), és az alábbi értékeket írja ki, minden lépésnél 2-vel növekedve


# Gyakorlati példa
# A range függvényt gyakran használják ciklusokban, ahol meghatározott számú ismétlést kell végrehajtani. Például:
# Összeg számítása 1-től 5-ig
osszeg = 0
for i in range(1, 6):
    osszeg += i
print("Az összeg 1-től 5-ig:", osszeg)
# Ez a ciklus kiszámítja az 1-től 5-ig terjedő számok összegét

# Számok kiírása visszafelé
for i in range(10, 0, -1):
    print(i)
# Ez a ciklus 10-től 1-ig (0 kizárva) iterál visszafelé

# Páros számok kiírása
for i in range(0, 11, 2):
    print(i)
# Ez a ciklus 0-tól 10-ig (11 kizárva) iterál

# Összefoglalás
# A range függvény egy rendkívül hasznos eszköz Pythonban, amely lehetővé teszi számsorozatok könnyű generálását és iterálását.