# Az osztály (class) egy alapvető fogalom az objektumorientált programozásban (OOP), amely lehetővé teszi a programozók számára, hogy adatokat és műveleteket egyesítsenek egyetlen entitásba, amit objektumnak nevezünk. Az osztályok segítségével definiálhatunk új típusokat és struktúrákat, amelyek az adatok és az azokkal végzett műveletek együttesét tartalmazzák.

# Osztályok Alapfogalmai
# Osztály Definíciója:

# Az osztály egy sablon az objektumok létrehozásához. Az osztály meghatározza, hogy milyen adatokat (attribútumokat) és milyen műveleteket (metódusokat) tartalmaznak az általa létrehozott objektumok.
# Attribútumok:

# Az attribútumok az osztályhoz tartozó adatokat jelentik. Ezek a változók az objektum állapotát reprezentálják.
# Metódusok:

# A metódusok olyan függvények, amelyek az osztályon belül vannak definiálva és az osztály objektumainak viselkedését határozzák meg.
# Konstruktor:

# A konstruktor (az __init__ metódus) az osztály példányosításakor automatikusan meghívódik, és az objektum kezdeti állapotát állítja be.
# Példa: Egyszerű Osztály
# Az alábbiakban bemutatok egy egyszerű példát, amely egy osztályt definiál, és azt használja az osztály objektumainak létrehozására.

# Osztály definíció
class Person:
    def __init__(self, name, age):
        # Konstruktor, amely inicializálja az attribútumokat
        self.name = name
        self.age = age

    def greet(self):
        # Metódus, amely üdvözli az embert
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    def have_birthday(self):
        # Metódus, amely növeli az életkort egy évvel
        self.age += 1

# Objektum létrehozása
person1 = Person("Alice", 30)
person2 = Person("John", 35)

# Használat
print(person1.greet())        # Kimenet: Hello, my name is Alice and I am 30 years old.
person1.have_birthday()
print(person2.greet())        # Kimenet: Hello, my name is John and I am 35 years old.

# Magyarázat
# Osztály Definíció:

# Az Person osztályt a class kulcsszóval definiáljuk. Az osztály két attribútumot tartalmaz: name és age. A konstruktor (__init__ metódus) az objektum létrehozásakor inicializálja ezeket az attribútumokat.
# Konstruktor:

# Az __init__ metódus az osztály példányosításakor automatikusan meghívódik. Beállítja az name és age attribútumokat a Person objektum esetében.
# Metódusok:

# greet: Ez a metódus visszaad egy üdvözlő üzenetet, amely tartalmazza a name és age attribútumok értékét.
# have_birthday: Ez a metódus növeli az age attribútum értékét egy évvel, szimulálva ezzel a születésnapot.
# Objektum Létrehozása:

# Az person1 változó egy új Person objektumot példányosít a "Alice" névvel és 30 éves korral.
# Metódusok Használata:

# Az person1.greet() metódus meghívása egy üdvözlő üzenetet ad vissza.
# A person1.have_birthday() metódus meghívása növeli az age értékét egy évvel, majd az új üdvözlő üzenet újra meghívásával látjuk, hogy az életkor frissült.

# Összegzés
# Az osztályok egy kulcsfontosságú építőkockát jelentenek az objektumorientált programozásban. Lehetővé teszik az adatok és a műveletek egyesítését, valamint az új típusok és struktúrák létrehozását. Az osztályok segítenek a kód organizálásában, újrafelhasználhatóságában és karbantartásában, amely különösen fontos komplexebb projektek esetén.


# https://okt.inf.szte.hu/szkriptnyelvek/gyakorlat/python/object/