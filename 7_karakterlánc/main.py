
# 1. Karakterláncok összefűzése
# A karakterláncok összefűzésére a + operátort használjuk.

nev = "John"
koszones = "Hello, " + nev + "!"
print(koszones)

# 2. Karakterláncok replikációja
# A karakterláncok replikációjára a * operátort használjuk, amely megismétli a karakterláncot a megadott számú alkalommal.

szoveg = "Hello! "
ismetel = szoveg * 5
print(ismetel)

# 3. Karakterláncok indexelése és szeletelése
# Indexelés
# Az indexelés egy adott karakter elérését jelenti egy sztring (karakterlánc) esetén. Az indexelésnél egy konkrét karaktert érünk el a sztringből, és a szintaxisa szoveg[index], ahol index egy egész szám, ami megadja a karakter pozícióját a sztringben. Az indexek 0-tól kezdődnek.
# A karakterláncokban az egyes karakterek elérésére indexelést használunk. 
szoveg = "Python"
elso_karakter = szoveg[0]
utolso_karakter = szoveg[-2]
print(elso_karakter)
print(utolso_karakter)

# A negatív indexeket használva a Python karakterláncokat hátulról kezdi el indexelni. Tehát:

# Az utolsó karakter indexe -1.
# Az utolsó előtti karakter indexe -2, és így tovább.

# +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#    0   1   2   3   4   5
#   -6  -5  -4  -3  -2  -1

# Szeletelés
# A szeletelés (slicing) lehetővé teszi, hogy egy részt válasszunk ki egy sztringből. A szeletelés során egy intervallumot adunk meg, ami két indexből áll: szoveg[start:end]. Ez az intervallum tartalmazza szoveg karaktereit az start indextől (beleértve) az end indexig (kizárólag).
# A szeleteléssel a karakterlánc egy részét érhetjük el.
szoveg = "Python"
reszlet = szoveg[1:4]
print(reszlet)

# szoveg = "Python"
# reszlet = szoveg[1:4] # 'yth' (a 1-es indextől a 4-es indexig, de a 4-es index már nem tartozik bele)
# A szoveg[1:4] kifejezés nem indexelés, hanem szeletelés, mert egy részét választjuk ki a sztringnek. Ez azt jelenti, hogy az szoveg sztringből az 1-es indextől (beleértve) a 4-es indexig (kizárólag) vágunk ki egy részt. Tehát az eredmény yth lesz, mert ez a sztring tartalmazza az 1-es, 2-es és 3-as indexű karaktereket.

# Összefoglalva:

# Indexelés: Egy adott karakter elérése a sztringben egyetlen index segítségével.
# Szeletelés: Egy rész kiválasztása a sztringből egy intervallum segítségével, ami két indexből áll.

# 4. Karakterlánc hossza
# A len függvény használatával megkaphatjuk egy karakterlánc hosszát.

szoveg = "Python"
hossz = len(szoveg)
print(hossz)


# 5. Karakterláncok összehasonlítása
# A sztringek összehasonlíthatók a ==, !=, <, >, <=, >= operátorokkal.
szoveg1 = "Alma"
szoveg2 = "Banán"
print(szoveg1 == szoveg2)  # Hamis
print(szoveg1 < szoveg2)   # Igaz (Ábécé sorrendben)

# 6. Karakterláncok keresése és helyettesítése
# A find, replace és hasonló függvényekkel kereshetünk és helyettesíthetünk részeket a karakterláncokban.


szoveg = "Hello, World!"
hely = szoveg.find("World")
print(hely)  # 7

# szoveg.find("World")

# Ez a sor meghatározza, hogy hol kezdődik a "World" szó az eredeti szoveg változóban. A find metódus visszaadja az első előfordulás indexét, ha megtalálható a sztringben, vagy -1-et, ha nem található meg.

# A szoveg értéke: "Hello, World!"
# A find metódus visszaadja a 7-es indexet, mert "World" a 7-es pozíciótól kezdődik a sztringben.

uj_szoveg = szoveg.replace("World", "Python")
print(uj_szoveg)

# szoveg.replace("World", "Python")

# Ez a sor létrehoz egy új sztringet (uj_szoveg), amelyben a "World" szót "Python"-ra cseréli a szoveg változóban. Ez az eredmény kimenetben megjelenik, amikor kiírjuk az uj_szoveg változót.

# Az uj_szoveg értéke: "Hello, Python!"

# 7. Karakterláncok szétválasztása és egyesítése
# A split és join függvényekkel szétválaszthatunk és egyesíthetünk karakterláncokat.
szoveg = "Python is fun"
szavak = szoveg.split()
print(szavak)  # ['Python', 'is', 'fun']

# A 'Python', 'is', 'fun' formátum, amit a print(szavak) eredményez, a listák által használt formátum Pythonban. Ez azt jelenti, hogy a split() metódus által visszaadott eredményt egy listában kapjuk meg. A lista elemeit vesszőkkel választja el, és a lista elemei szögletes zárójelek közé vannak helyezve.

egyesitett_szoveg = " ".join(szavak)
print(egyesitett_szoveg)

# Az egyesitett_szoveg változóban a join metódus által létrehozott sztring található, amely tartalmazza a szavak listában található szavakat, szóközökkel elválasztva.

# Miért hasznos?
# Ez a technika gyakran hasznos, ha több sztringet vagy szavakat kell egyesíteni egyetlen sztringgé, és lehetővé teszi a szövegek könnyebb formázását vagy kimenetek előállítását.