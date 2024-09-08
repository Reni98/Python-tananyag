# Ha van egy alkalmazásunk és üdvözölni szeretnénk a látogatot, akkor nem lehet mindig az, hogy Miki, hanem létrehozunk egy változot amivel az aktuális látogatot tudjuk üdvözölni.

# létrehozunk egy kulcsot aminek az lesz a neve, hogy felhasználónév, legfoglalunk a memóriában egy helyet, amiben eltudunk menteni különböző adatokat, most a Levit mentettük el. Utána a print függvényben hivatkozunk erre a memória területre felhasznalonev kulccsal, memóriában lévő anyagot a print függvény megkapja. Mivel a Levi szót mentettük abba, így azt kapja meg. Mivel ez egy változó képes változásra. 

felhasznalonev = "Levi"
print(felhasznalonev)
felhasznalonev = "Miki"
print(felhasznalonev)

# Változók Pythonban
# A változók Pythonban azonosítók, amelyeket az értékek (pl. számok, sztringek, listák stb.) tárolására használunk. A változókat értékeikkel együtt definiáljuk, és ezeket később hivatkozásokként használhatjuk a programunkban.

# Változó definíciója
# A változók Pythonban dinamikusan típusosak, ami azt jelenti, hogy típusdeklaráció nélkül is létrehozhatjuk őket, és bármikor hozzárendelhetünk más típusú értéket hozzájuk. A változókat az = operátorral hozzuk létre és inicializáljuk.

# "típusdeklaráció nélkül" kifejezés azt jelenti, hogy a Python programozási nyelvben nem szükséges előre meghatároznunk vagy deklarálnunk (megadnunk) a változók típusát, mielőtt azokat használnánk. Ez a Python dinamikus típusú nyelv jellemzője.

# Példa változók deklarálására típusdeklaráció nélkül

# Sztring típusú változó
nev = "John"

# Egész szám típusú változó
eletkor = 30

# Lebegőpontos szám típusú változó
pi = 3.14

# Logikai típusú változó
igaz_e = True

# Ebben a példában minden változó definiálása során csak az értékét adtuk meg ("John", 30, 3.14, True), de nem kellett előre meghatároznunk, hogy milyen típusú lesz az adott változó. A Python maga határozza meg dinamikusan a változó típusát az érték alapján.

# Dinamikus típusosság előnyei
# Rugalmasabb kód: Nem kell foglalkoznunk a változó típusának előre megadásával vagy típuskonverziókkal.
# Egyszerűbb és gyorsabb fejlesztés: Könnyebben és gyorsabban lehet fejleszteni, mivel nem kell figyelni a típusdeklarációkra.
# Javítja az olvashatóságot: Azonosítóink többet mondhatnak az embereknek

# Típuskonverzió: (vagy más néven "típusátalakítás") egy olyan folyamatot jelent a programozásban, amikor egy adott típusú adatot átalakítunk vagy konvertálunk egy másik típusú adattá.

# Típusdeklaráció: fogalma a programozásban arra utal, hogy egy változó vagy egy függvény paramétere milyen típusú adatot vár, vagy hogy egy változó milyen típusú adatot tárolhat.


# Pythonban azonban nem szükséges típusdeklarációt megadni a változóknak. Ez azt jelenti, hogy nem kell előre meghatároznunk, hogy egy változó milyen típusú adatot fog tárolni. A változók típusa automatikusan meghatározódik az alapján, hogy milyen értéket kapnak. Ez a dinamikus típusosság jellemzője Pythonban.