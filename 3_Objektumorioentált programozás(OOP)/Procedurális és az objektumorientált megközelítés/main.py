# A procedurális és az objektumorientált (OOP) megközelítések két különböző programozási paradigma, amelyek különböző módon kezelik a problémákat és a kód szerkezetét. 

# 1. Procedurális Programozás
# A procedurális programozás a funkciókra és eljárásokra összpontosít. Az adatokat és a műveleteket külön kezeljük, és a kódot függvények (procedúrák) segítségével szervezzük. A cél az, hogy az adatokat és az azokkal végzett műveleteket (algoritmusokat) külön-külön kezeljük.
# Procedurális megközelítés

# Függvény a számjegyek összegzésére
def sum_of_digits(number):
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total

# Használat
number = 12345
print(f"A számjegyek összege: {sum_of_digits(number)}")  # Kimenet: A számjegyek összege: 15
# Magyarázat:
# A sum_of_digits függvény egy adott számjegyek összegét számolja ki. Az adat és a funkció (algoritmus) külön vannak kezelve.
# A procedurális programozás fókusza az algoritmusokon van, és az adatokat globálisan kezelhetjük.

# 2. Objektumorientált Programozás (OOP)
# Az objektumorientált programozás az adatokat és a műveleteket egyesíti objektumokban. Az objektumok az osztályok példányai, amelyek tartalmazzák az adatok és a műveletek (metódusok) összesítését. Az OOP négy fő koncepcióra épül: osztályok, objektumok, öröklés és polimorfizmus.

# Példa: Egyszerű Számjegyek Összegzése OOP
# Magyarázat:
# A DigitSumCalculator osztály egy számot tárol és tartalmaz egy metódust (sum_of_digits), amely a számjegyek összegét számolja ki.
# Az OOP megközelítésben az adat (number) és a művelet (sum_of_digits) együtt van kezelve egy objektumban. Az osztály az adat és a metódusok összesítésére szolgál, ami segít a kód struktúrájának javításában.

# Különbségek Összefoglalása

# 1. Adat- és Műveletkezelés:
# Procedurális: Az adatokat és a funkciókat külön kezeljük. A funkcionalitás globálisan elérhető, és az adatokat az algoritmusokon keresztül manipuláljuk.
# OOP: Az adatokat és a funkciókat egyesítjük objektumokban. Az objektumok a kódot és az adatot együtt kezelik, amely elősegíti a kód újrafelhasználhatóságát és karbantartását.

# 2. Modularitás és Karbantarthatóság:
# Procedurális: A kód nem mindig könnyen karbantartható, ha a projekt bővül, mivel az adatok és az algoritmusok szétszórtan helyezkednek el.
# OOP: Az objektumok és osztályok struktúrája elősegíti a kód modularitását, így a karbantartás és a bővítés egyszerűbbé válik.

# 3. Öröklés és Polimorfizmus:
# Procedurális: Az öröklés és polimorfizmus nem alkalmazható. Az algoritmusok a kód egészében egységesek.
# OOP: Az öröklés és polimorfizmus segítségével a kódot hierarchikus módon szervezhetjük, és az objektumok viselkedése változhat az osztályok és objektumok alapján.

# 4. Kód Újrafelhasználhatóság:
# Procedurális: A kód újrafelhasználhatósága korlátozott lehet, mivel a függvények globálisan hozzáférhetők.
# OOP: Az osztályok és objektumok révén a kód könnyen újrafelhasználható és bővíthető, mivel a funkcionalitás egy helyen van összegyűjtve.

# Összegzés
# A procedurális programozás és az objektumorientált programozás eltérő megközelítéseket kínálnak a problémák kezelésére. Míg a procedurális programozás a funkciókra és algoritmusokra összpontosít, az OOP az adatokat és a műveleteket egyesíti objektumokba, amely segít a kód jobb struktúrázásában és karbantartásában. Az OOP általában rugalmasabb és jobban kezelhető a nagyobb, komplexebb projektek esetében.