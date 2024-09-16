# Mi a random Modul?
# A random modul a Python beépített könyvtárának része, és segít véletlenszerű számok generálásában, valamint véletlenszerű elemek kiválasztásában.

# Hogyan Importáljuk a random Modult?
# Minden használat előtt először importálni kell a modult. Ezt a következőképpen tehetjük meg:
import random

# Példák a random Modul Használatára

# 1. Véletlenszerű Egész Szám Generálása
# Ha szeretnénk egy véletlenszerű egész számot generálni egy megadott tartományból, használhatjuk a random.randint() függvényt.

# Generáljunk egy véletlenszerű egész számot 1 és 10 között
random_number = random.randint(1, 10)

print(f"Véletlenszerű egész szám 1 és 10 között: {random_number}")

# Mit csinál ez a kód?
# random.randint(1, 10): Véletlenszerű egész számot generál 1 és 10 között, beleértve mindkét határt.
# print(...): Kiírja a generált véletlenszerű számot.

# 2. Véletlenszerű Lebegőpontos Szám Generálása
# A random.uniform() függvénnyel véletlenszerű lebegőpontos számot generálhatunk két érték között.
# Generáljunk egy véletlenszerű lebegőpontos számot 1.5 és 5.5 között
random_float = random.uniform(1.5, 5.5)

print(f"Véletlenszerű lebegőpontos szám 1.5 és 5.5 között: {random_float}")

# Mit csinál ez a kód?
# random.uniform(1.5, 5.5): Véletlenszerű lebegőpontos számot generál 1.5 és 5.5 között.
# print(...): Kiírja a generált véletlenszerű lebegőpontos számot.

# 3. Véletlenszerű Elem Kiválasztása Listából
# A random.choice() függvény segítségével véletlenszerűen választhatunk ki egy elemet egy listából.
# Egy lista gyümölcsökkel
fruits = ['alma', 'banán', 'cseresznye', 'datolya']

# Véletlenszerű gyümölcs kiválasztása a listából
random_fruit = random.choice(fruits)

print(f"Véletlenszerűen kiválasztott gyümölcs: {random_fruit}")

# Mit csinál ez a kód?
# random.choice(fruits): Véletlenszerűen kiválaszt egy gyümölcsöt a fruits listából.
# print(...): Kiírja a kiválasztott gyümölcs nevét.

# 4. Lista Véletlenszerű Rendezése
# A random.shuffle() függvénnyel véletlenszerűen megkeverhetjük a lista elemeit.
# Egy lista gyümölcsökkel
fruits = ['alma', 'banán', 'cseresznye', 'datolya']

# Véletlenszerűen megkeverjük a lista elemeit
random.shuffle(fruits)

print(f"Véletlenszerűen kevert lista: {fruits}")

# Mit csinál ez a kód?
# random.shuffle(fruits): Véletlenszerűen megkeveri a fruits lista elemeit.
# print(...): Kiírja a kevert lista elemeit.

# 5. Véletlenszerű Minta Kiválasztása
# A random.sample() függvény segítségével kiválaszthatunk egy mintát a lista elemeiből anélkül, hogy ismétlődnének az elemek.
# Egy lista gyümölcsökkel
fruits = ['alma', 'banán', 'cseresznye', 'datolya', 'eper']

# Véletlenszerűen kiválasztunk 3 gyümölcsöt a listából
random_sample = random.sample(fruits, 3)

print(f"Véletlenszerűen kiválasztott gyümölcsök: {random_sample}")

# Mit csinál ez a kód?

# random.sample(fruits, 3): Véletlenszerűen kiválaszt 3 gyümölcsöt a fruits listából.
# print(...): Kiírja a kiválasztott gyümölcsöket.

# Összegzés
# random.randint(a, b): Véletlenszerű egész számot generál az a és b tartomány között.
# random.uniform(a, b): Véletlenszerű lebegőpontos számot generál az a és b tartomány között.
# random.choice(seq): Véletlenszerűen kiválaszt egy elemet a seq sorozatból.
# random.shuffle(lst): Véletlenszerűen megkeveri a lista elemeit.
# random.sample(population, k): Véletlenszerűen kiválaszt k elemet a population sorozatból, ismétlés nélkül.

# Játékokban Véletlenszerű Események
# A játékokban gyakran használunk véletlenszerű eseményeket, például dobókockát, loot rendszert, vagy véletlenszerű kihívásokat.

# Példa: Véletlenszerű Dobókocka

# Tegyük fel, hogy szeretnénk szimulálni egy dobókocka dobását. Ez hasznos lehet játékokban vagy tesztekben.
import random

def roll_dice():
    return random.randint(1, 6)

# Dobjuk el a dobókockát
result = roll_dice()
print(f"A dobókocka eredménye: {result}")

# Mit csinál ez a kód?

# random.randint(1, 6): Véletlenszerű egész számot generál 1 és 6 között, ami a dobókocka lehetséges eredménye.
# print(...): Kiírja a dobókocka dobásának eredményét.