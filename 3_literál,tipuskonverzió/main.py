# Literál fogalma
# "A literál olyan állandó érték, amely a program kódjába beépül, és azt a továbbiakban (futás közben) nem lehet megváltoztatni. A literálok fajtái:


# Egy másik honlapon Hernyák Zoltán magyarázata a következőképpen írja le a literál a fogalmát:

# "A literál nem más, mint a program szövegében direkt módon beleírt adat."

# Ezeket a literálokat a programozás során konkrét értékként használjuk fel, és azok a program számára értelmezhetőek és használhatóak az adott adattípusukban. A literálok lényegében az adatok alapvető építőkövei, amelyekkel a program működik és dolgozik.

#  A literál pedig egy konkrét adatot jelent, amit közvetlenül megadunk a kódban, és ami általában az inicializálás során szolgál kezdeti értékként.

# Egész literál: Egész számokat reprezentál, például 0, 42, -10.
# Valós literál: Lebegőpontos számokat reprezentál, például 3.14, 2.71828, -0.5.
# Karakterlánc literál: Karakterláncokat (szövegeket) reprezentál, például "hello", 'python', "123".
# Logikai literál: Logikai értékeket reprezentál, vagyis True vagy False.

# Példák literálokra különböző típusokban:
# Egész szám literál: 42
# Lebegőpontos szám literál: 3.14
# Karakterlánc literál: "hello"
# Logikai literál: True vagy False
# Ezek a literálok közvetlenül képviselik az adatot a kódban, és ezeket az értékeket használjuk változók inicializálásához vagy kifejezések értékadásához.

# Miért fontosak a literálok?
# Konzisztencia és olvashatóság: A literálok használata segít abban, hogy egyértelmű legyen, hogy milyen típusú adatot kezelünk a kódban.

# Pontosság: A literálok által közvetített adatok pontosak és megbízhatóak, mivel közvetlenül adjuk meg őket a kódban, nem függünk más változók értékeitől vagy kifejezések eredményeitől.

# Teljesítmény: A literálok használata gyorsabb és hatékonyabb kódolást tesz lehetővé, mivel nincs szükség további kalkulációkra vagy hosszabbításokra az érték kinyerésére.

# Példák
# Ebben az esetben a szam változónak az értéke egy egész szám literál, amely 42.
szam = 42
print(szam)

# Itt a pi változónak az értéke egy lebegőpontos szám literál, amely 3.14.
pi = 3.14
print(pi)

#A nev változónak egy karakterlánc literált adtunk értékül, ami "Alice".
nev = "Alice"
print(nev)

#A igaz_e változónak a True logikai literált adtuk értékül, ami igaz értéket jelent.
igaz_e = True
print(igaz_e)  # Output: True

#---------------------------------------------------------------------------------------------------------
# Típuskonverzió

# A típuskonverzió azt jelenti, hogy egy adott típusú adatot átalakítunk egy másik típusú adattá. Ez lehet automatikus vagy explicit módon történő átalakítás.

# Automatikus típuskonverzió:

# Például egész számot és lebegőpontos számot adunk össze. Ebben az esetben az egész számot automatikusan lebegőpontos számmá konvertálja a Python.

x = 10     # egész szám
y = 3.5    # lebegőpontos szám

eredmeny = x + y
print(eredmeny)   # Output: 13.5

# Itt az x változó (egész szám) értéke automatikusan lebegőpontos számmá konvertálódik a művelet végrehajtása során, hogy megfeleljen a műveleti követelményeknek.



# Explicit típuskonverzió (cast):

# Explicit típuskonverzió során mi kifejezetten megmondjuk a programnak, hogy melyik típusba szeretnénk konvertálni az adatot.

szam = 5
szoveg = str(szam)  # számot karakterlánccá alakítjuk

print(szoveg)   # Output: "5"

# tt az str() függvény segítségével a szam változó értékét karakterláncá (string) konvertáljuk.


# Típuskényszerítés (Type Casting)
# A típuskényszerítés arra utal, hogy egy adott típusú adatot kifejezetten egy másik típusú adattá kényszerítünk. Ez explicit módon történik, és gyakran akkor szükséges, amikor az adatokat különböző típusú műveletekben vagy összehasonlításokban kívánjuk használni.

#Egész számból lebegőpontos szám készítése:
szam1 = 10     # egész szám
szam2 = float(szam1)   # típuskényszerítés: egész számot lebegőpontos számmá konvertálunk

print(szam2)   # Output: 10.0

# Itt a float() függvény segítségével a szam1 változót egész számból lebegőpontos számmá konvertáljuk.

# Karakterláncból egész szám készítése:

szoveg = "42"    # karakterlánc
szam = int(szoveg)   # típuskényszerítés: karakterláncot egész számmá konvertálunk

print(szam)   # Output: 42

# Itt az int() függvény segítségével a szoveg változót karakterlánccá konvertáljuk, majd ezt az értéket egész számmá alakítjuk.

# Összegzés
# A típuskonverzió és típuskényszerítés kulcsfontosságú fogalmak a programozásban, amelyek segítségével kezelhetjük és manipulálhatjuk az adatok típusát és értékét aszerint, hogy milyen műveleteket szeretnénk végezni velük. Fontos megjegyezni, hogy a típuskonverzió automatikusan is megtörténhet bizonyos esetekben, míg a típuskényszerítés explicit módon történik.