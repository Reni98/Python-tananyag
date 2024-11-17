# Az objektumorientált programozás (OOP) egy népszerű programozási paradigma, amely az adatok és a műveletek csoportosításán alapul objektumokba. Az OOP négy alapvető fogalomra épül: osztályok, objektumok, öröklés és polimorfizmus. Itt bemutatok egy egyszerű példát és magyarázatot, amely bemutatja ezeket a koncepciókat.

# Példa: Állatok és Tevékenységeik
# Képzeljük el, hogy egy programot szeretnénk írni, amely különböző állatokat modellez. Minden állat rendelkezik bizonyos alapvető tulajdonságokkal és tevékenységekkel.

# 1. Osztályok és Objektumok

# Osztályok: Az osztályok az adatok (attribútumok) és a műveletek (metódusok) sablonját jelentik. Az osztályok segítségével példányosítjuk az objektumokat.

# Objektumok: Az objektumok az osztályok példányai, amelyek tartalmazzák az osztály által meghatározott attribútumokat és metódusokat.

# 2. Öröklés

# Az öröklés lehetővé teszi, hogy egy osztály (származtatott osztály) örökölje egy másik osztály (szülő osztály) tulajdonságait és viselkedését. Ez elősegíti a kód újrafelhasználhatóságát és a hierarchikus felépítést.

# 3. Polimorfizmus

# A polimorfizmus lehetővé teszi, hogy ugyanaz a metódus különböző osztályokban eltérően működjön.

# Kód Példa
# Az alábbi példa bemutatja, hogyan alkalmazhatók ezek a koncepciók egy egyszerű állatokat modellező rendszerben:
# Alap osztály
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Minden állatnak saját speak() metódusa van!")

# Származtatott osztály - Dog
class Dog(Animal):
    def speak(self):
        return f"{self.name} mondja: Vau!"

# Származtatott osztály - Cat
class Cat(Animal):
    def speak(self):
        return f"{self.name} mondja: Miaú!"

# Származtatott osztály - Cow
class Cow(Animal):
    def speak(self):
        return f"{self.name} mondja: Bőg!"

# Objektumok létrehozása
dog = Dog("Rex")
cat = Cat("Mia")
cow = Cow("Lúcia")

# Objektumok használata
def animal_speak(animal):
    print(animal.speak())

# Kimenet
animal_speak(dog)  # Kimenet: Rex mondja: Vau!
animal_speak(cat)  # Kimenet: Mia mondja: Miaú!
animal_speak(cow)  # Kimenet: Lúcia mondja: Bőg!

# Magyarázat
# 1. Osztályok és Objektumok:

# Animal Osztály: Ez az alap osztály, amely tartalmaz egy name attribútumot és egy speak metódust. Az speak metódus alapértelmezett implementációja itt nincs, de egy származtatott osztálynak felül kell írnia.

# Dog, Cat, Cow Osztályok: Ezek az osztályok öröklik az Animal osztályt és felülírják a speak metódust a saját specifikus viselkedésük szerint.

# 2. Öröklés:

# Az Dog, Cat és Cow osztályok öröklik az Animal osztályt, így hozzáférnek a name attribútumhoz és a speak metódushoz, de saját verziójukat biztosítják a speak metódusra.

# 3. Polimorfizmus:
# Az animal_speak függvény egy Animal típusú objektumot vár. A különböző állat objektumok különböző speak metódusokat hívnak meg, ezáltal megvalósítva a polimorfizmust. Ugyanaz a metódus (speak) különböző implementációkkal rendelkezik attól függően, hogy melyik állatot példányosítjuk.
# Összegzés
# Az OOP lehetővé teszi az adatok és a műveletek szervezését és strukturálását osztályokba, az öröklés révén a kód újrafelhasználhatóságát növeli, míg a polimorfizmus lehetővé teszi, hogy ugyanaz a metódus különböző típusú objektumokban eltérően működjön. Ez a megközelítés segíti a programok karbantarthatóságát és bővíthetőségét.






