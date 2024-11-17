# Az objektum-orientált programozás (OOP) egyik alapvető fogalma az objektum, amely egy adott osztály példányát jelenti. Az objektumok olyan adatokkal rendelkeznek, amelyek az osztály attribútumai, és olyan funkciókat biztosítanak, amelyek az osztály metódusai.

# Példa: Egy egyszerű Car (Autó) osztály
# Képzeljük el, hogy egy egyszerű autómodellezést készítünk. Egy autó rendelkezik egy márkájával és sebességével, valamint képes gyorsítani és fékezni.

# Osztály definíció
class Car:
    def __init__(self, brand, speed=0):
        self.brand = brand  # Autó márkája
        self.speed = speed  # Autó sebessége

    def accelerate(self, increase):
        # Sebesség növelése
        self.speed += increase
        print(f"The {self.brand} car accelerated to {self.speed} km/h.")

    def brake(self, decrease):
        # Sebesség csökkentése, minimálisan 0-ra állítva
        self.speed -= decrease
        if self.speed < 0:
            self.speed = 0
        print(f"The {self.brand} car slowed down to {self.speed} km/h.")

    def __str__(self):
        return f"Car brand: {self.brand}, Speed: {self.speed} km/h"

# Objektum példányosítása
my_car = Car("Toyota", 50)  # Létrehozunk egy Toyota márkájú autót, ami 50 km/h sebességgel rendelkezik

# Objektum használata
print(my_car)  # Kimenet: Car brand: Toyota, Speed: 50 km/h
my_car.accelerate(20)  # Kimenet: The Toyota car accelerated to 70 km/h.
my_car.brake(30)       # Kimenet: The Toyota car slowed down to 40 km/h.
print(my_car)  # Kimenet: Car brand: Toyota, Speed: 40 km/h


# Magyarázat
# Osztály Definíció (Car):

# Konstruktor (__init__ metódus): Az osztály inicializálásához használjuk, amikor új autóobjektumot hozunk létre. A konstruktor beállítja az brand (márka) és a speed (sebesség) attribútumokat. Alapértelmezett sebesség értéke 0, ha nem adunk meg.
# Metódusok:
# accelerate: Növeli az autó sebességét a megadott increase értékkel.
# brake: Csökkenti az autó sebességét a megadott decrease értékkel. Ha a sebesség 0 alá csökken, akkor 0-ra állítjuk.
# __str__: A szöveges reprezentáció, amely megjeleníti az autó márkáját és sebességét, amikor a print funkcióval kiíratjuk az objektumot.

# Objektum példányosítása:
# my_car: Létrehozunk egy Car típusú objektumot a Toyota márkával és 50 km/h sebességgel. Ez az objektum a my_car nevű változóhoz van rendelve.
# Objektum használata:

# print(my_car): A print függvény meghívásakor az __str__ metódust használja, amely megjeleníti az autó márkáját és sebességét.
# my_car.accelerate(20): Az accelerate metódus növeli az autó sebességét 20 km/h-val.
# my_car.brake(30): A brake metódus csökkenti az autó sebességét 30 km/h-val.

# Összegzés
# Az objektum az osztály példánya, és tartalmazza az osztály által definiált adatokat és funkciókat. Az objektumok lehetővé teszik, hogy az adatokat és a funkciókat logikailag összekapcsoljuk, és kezeljük őket egyértelmű módon. Az objektumok az osztály attribútumait és metódusait használják a program különböző részein történő manipuláláshoz és adatkezeléshez.