# A lista az egyik legfontosabb és leggyakrabban használt adatstruktúra Pythonban.Tömbszerűen viselkedik, de számos további funkcionalitással rendelkezik.

# Lista fogalma
# A lista egy olyan adatstruktúra, amely több elemet képes tárolni egyetlen változóban. Az elemek bármilyen adattípusúak lehetnek (számok, karakterláncok, egyéb listák, stb.), és egy listán belül különböző típusú elemek is lehetnek.

# Lista jellemzői
# Indexelhető: Az elemek elérhetők indexek segítségével, ahol az indexelés 0-tól kezdődik.
# Rendezett: Az elemek sorrendje számít, és megőrződik.
# Módosítható (mutábilis): Az elemek hozzáadhatók, eltávolíthatók, és módosíthatók.
                        # Mutábilis: azt jelenti, hogy egy adatstruktúra módosítható, vagyis az elemei megváltoztathatók anélkül, hogy új objektumot kellene létrehozni. Ez magában foglalja az elemek hozzáadását, eltávolítását és módosítását.
# Vegyes típusok: Egy listában különböző típusú elemek is lehetnek.

# Lista létrehozása
# Listát a [] szimbólumok között, az elemek vesszővel elválasztva hozhatunk létre.
# Üres lista
ures_lista = []

# Lista elemekkel
szamok = [1, 2, 3, 4, 5]
szavak = ["alma", "banán", "cseresznye"]
kevert = [1, "kettő", 3.0, True]

# Lista elemeinek elérése és módosítása
# Az elemek indexek segítségével érhetők el. Az indexelés 0-tól kezdődik.

szamok = [1, 2, 3, 4, 5]

# Első elem
elso_elem = szamok[0]  # 1

# Utolsó elem
utolso_elem = szamok[4]  # 5
print(f"Az utolsó elem kiírása: {utolso_elem}")
# Módosítás
szamok[1] = 10  # A második elem most 10


# Negatív indexekkel jobbról balra haladva érjük el az elemeket. Az utolsó elem indexe -1, az utolsó előtti -2, és így tovább.
# Lista létrehozása
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Pozitív indexelés példák
first_fruit = fruits[0]  # Első elem (apple)
second_fruit = fruits[1]  # Második elem (banana)

# Negatív indexelés példák
last_fruit = fruits[-1]  # Utolsó elem (elderberry)
second_last_fruit = fruits[-2]  # Utolsó előtti elem (date)


# Eredmények kiírása
print("Első gyümölcs (pozitív index):", first_fruit)
print("Második gyümölcs (pozitív index):", second_fruit)
print("Utolsó gyümölcs (negatív index):", last_fruit)
print("Utolsó előtti gyümölcs (negatív index):", second_last_fruit)

# Magyarázat
# Lista létrehozása: Létrehoztunk egy fruits nevű listát öt gyümölccsel.
# Pozitív indexelés:
# fruits[0] hozzáfér az első elemhez, ami "apple".
# fruits[1] hozzáfér a második elemhez, ami "banana".
# Negatív indexelés:
# fruits[-1] hozzáfér az utolsó elemhez, ami "elderberry".
# fruits[-2] hozzáfér az utolsó előtti elemhez, ami "date".
# Eredmények kiírása: Az print függvények segítségével kiírjuk az eredményeket a konzolra.

# Lista bejárása
# A listát bejárhatjuk ciklussal, így minden elemhez hozzáférhetünk.

szavak = ["alma", "banán", "cseresznye"]

for szo in szavak:
    print(szo)


# Listák szeletelése
# Egy listából részlistát (szeletet) kaphatunk az elemek indexelésével.
szamok = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Első három elem
elso_harom = szamok[:3]  # [1, 2, 3]


# Középső elemek
kozepso = szamok[3:6]  # [4, 5, 6]


# Utolsó három elem
utolso_harom = szamok[-3:]  # [7, 8, 9]


# Listák összefűzése
# Két vagy több listát összefűzhetünk a + operátor segítségével.
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

egyesitett_lista = lista1 + lista2  # [1, 2, 3, 4, 5, 6]

# Lista elemeinek felcserélése
# Az elemek felcseréléséhez használhatunk indexelést.
# Lista létrehozása
lista = [1, 2, 3, 4, 5]

# Elemek felcserélése
lista[0], lista[4] = lista[4], lista[0]

# Eredmény kiírása
print(lista)  # [5, 2, 3, 4, 1]

# Magyarázat:
# Lista létrehozása: Létrehoztunk egy lista nevű listát.
# Felcserélés: A lista[0] és lista[4] elemek felcserélése a lista[0], lista[4] = lista[4], lista[0] sorban történik.
# Eredmény: A lista most [5, 2, 3, 4, 1].

# Lista ismétlése (szorzás):
# Egy lista elemeit többszörözhetjük a * operátorral.
# Lista létrehozása
lista = [1, 2, 3]

# Lista ismétlése
ismetlodo_lista = lista * 3

# Eredmény kiírása
print(ismetlodo_lista)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Magyarázat:
# Lista létrehozása: Létrehoztunk egy lista nevű listát.
# Ismétlés: A lista * 3 háromszor ismétli meg a lista elemeit.
# Eredmény: Az ismétlődő lista most [1, 2, 3, 1, 2, 3, 1, 2, 3].

# Fontosabb lista metódusok
# append(x): Hozzáadja az x elemet a lista végéhez.
# extend(iterable): Kiterjeszti a listát az iterable elemeivel.
# insert(i, x): Beilleszti az x elemet az i index helyére.
# remove(x): Eltávolítja az első x értékű elemet a listából.
# pop([i]): Eltávolítja és visszaadja az i indexű elemet (alapértelmezettként az utolsó elemet).
# index(x[, start[, end]]): Visszaadja az első x értékű elem indexét.
# count(x): Megszámolja, hogy az x elem hányszor fordul elő a listában.
# sort(key=None, reverse=False): Rendezi a listát.
# reverse(): Megfordítja a lista elemeinek sorrendjét.

# 1. append(x)
# A append() metódus hozzáadja az x elemet a lista végéhez.
lista = [1, 2, 3]
lista.append(4)
print(lista)  # [1, 2, 3, 4]

# 2. extend(iterable)
# A extend() metódus hozzáadja egy iterálható objektum (mint egy lista, tuple, vagy string) összes elemét a lista végéhez.
lista = [1, 2, 3]
lista.extend([4, 5, 6])
print(lista)  # [1, 2, 3, 4, 5, 6]

# 3. insert(i, x)
# Az insert() metódus az x elemet az i index helyére illeszti be. Az eredeti elemek egy pozícióval jobbra tolódnak.
lista = [1, 2, 3]
lista.insert(1, 10)
print(lista)  # [1, 10, 2, 3]


# 4. remove(x)
# A remove() metódus eltávolítja az első x értékű elemet a listából. Ha az elem nem található, ValueError-t dob.

lista = [1, 2, 3, 2, 4]
lista.remove(2)
print(lista)  # [1, 3, 2, 4]

# 5. pop([i])
# A pop() metódus eltávolítja és visszaadja az i indexű elemet. Ha az i index nincs megadva, az utolsó elemet távolítja el és adja vissza.

lista = [1, 2, 3, 4]
elem = lista.pop()
print(elem)  # 4
print(lista)  # [1, 2, 3]

elem = lista.pop(1)
print(elem)  # 2
print(lista)  # [1, 3]

# Különbség
# remove(x): Érték alapján történik az eltávolítás, azaz meg kell adnunk az elem konkrét értékét (x), amelyet eltávolítani szeretnénk.

# pop(i): Index alapján történik az eltávolítás. Meg kell adnunk az elem indexét (i), amelyet eltávolítani szeretnénk. Ha nem adunk meg indexet, az utolsó elemet távolítja el.

# Fontos megjegyzés: A remove(x) csak az x értékű első előfordulását távolítja el, míg a pop(i) konkrét index alapján törli az elemet. Tehát a remove() metódus nem használható konkrét index megadására, mivel nem ismeri a lista indexeit, csak az értékeket.

# 6. index(x[, start[, end]])
# Az index() metódus visszaadja az első x értékű elem indexét. Opcionálisan megadható egy kezdő (start) és egy vég (end) index.
lista = [1, 2, 3, 2, 4]
index = lista.index(2)
print(index)  # 1

index = lista.index(2, 2)  # Kezdő index megadása
print(index)  # 3

# lista = [1, 2, 3, 1, 4, 3, 4,1,5]
# index = lista.index(4)
# print(index)  # 4

# index = lista.index(1,4,8)  # Kezdő index megadása
# print(index)  # 7

# 7. count(x)
# A count() metódus megszámolja, hogy az x elem hányszor fordul elő a listában.
lista = [1, 2, 3, 2, 4, 2]
db = lista.count(2)
print(f"A 2-es elem {db}-szor fordul elő a listában.")  # 3

# 8. sort(key=None, reverse=False)
# A sort() metódus rendezi a listát. Opcionálisan megadható egy kulcs (key) függvény és egy reverse logikai érték, amely fordított sorrendet ad.
lista = [3, 1, 4, 1, 5, 9, 2]
lista.sort()
print(lista)  # [1, 1, 2, 3, 4, 5, 9]

# lista.sort(reverse=True)
# print(lista)  # [9, 5, 4, 3, 2, 1, 1]
lista.reverse()
print(lista)  

# Kulcs megadása
lista = ["alma", "banán", "cseresznye", "barack"]
lista.sort(key=len)
print(lista)  # ['alma', 'banán', 'cseresznye']

# 9. reverse()
# A reverse() metódus megfordítja a lista elemeinek sorrendjét.
lista = [1, 2, 3, 4, 5]
lista.reverse()
print(lista)  # [5, 4, 3, 2, 1]

