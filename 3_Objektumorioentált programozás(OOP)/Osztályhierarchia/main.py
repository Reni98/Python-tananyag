# Az osztályhierarchia az objektumorientált programozás (OOP) egyik alapvető fogalma, amely lehetővé teszi az osztályok közötti kapcsolatokat és öröklést. Az osztályhierarchia segítségével osztályokat szervezhetünk alosztályok és szülőosztályok alapján, amely elősegíti a kód újrafelhasználhatóságát és karbantartását.

# Osztályhierarchia Alapfogalmai
# Szülőosztály (Base Class / Parent Class):

# Az osztály, amelyből más osztályok származnak. A szülőosztály tartalmazhat közös attribútumokat és metódusokat, amelyeket az alosztályok örökölnek.
# Alosztály (Derived Class / Child Class):

# Az osztály, amely a szülőosztályból származik. Az alosztály örökli a szülőosztály attribútumait és metódusait, és további specifikus funkciókat vagy adatokat is hozzáadhat.
# Öröklés (Inheritance):

# Az öröklés az a mechanizmus, amely lehetővé teszi, hogy egy alosztály örökölje a szülőosztály attribútumait és metódusait, így elkerülve a kód ismétlését.

# Szülőosztály
class Character:
    def __init__(self, name, health, shield):
        self.name = name
        self.health = health
        self.shield = shield

    def take_damage(self, damage):
        # Csökkenti az életet a bejövő sebzéssel, figyelembe véve a pajzsot
        if self.shield > 0:
            shield_absorption = min(damage, self.shield)
            self.shield -= shield_absorption
            damage -= shield_absorption
        self.health -= damage
        if self.health < 0:
            self.health = 0
        return self.health

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name} - Health: {self.health}, Shield: {self.shield}"

# Alosztály - öröklés a szülőosztályból
class Warrior(Character):
    def __init__(self, name, health, shield, attack_power):
        super().__init__(name, health, shield)
        self.attack_power = attack_power

    def attack(self):
        return self.attack_power

# Alosztály - öröklés a szülőosztályból
class Mage(Character):
    def __init__(self, name, health, shield, magic_power):
        super().__init__(name, health, shield)
        self.magic_power = magic_power

    def cast_spell(self):
        return self.magic_power

# Használat
warrior = Warrior("Thor", 100, 50, 20)
mage = Mage("Gandalf", 80, 30, 40)

print(warrior)  # Kimenet: Thor - Health: 100, Shield: 50
print(mage)    # Kimenet: Gandalf - Health: 80, Shield: 30

# Harcos támadása és varázsló varázslata
print(f"{warrior.name} attacks with power: {warrior.attack()}")  # Kimenet: Thor attacks with power: 20
print(f"{mage.name} casts spell with power: {mage.cast_spell()}")  # Kimenet: Gandalf casts spell with power: 40

# Karakterek sebzése
damage_taken = 60
print(f"{warrior.name} takes {damage_taken} damage.")
warrior.take_damage(damage_taken)
print(warrior)  # Kimenet: Thor - Health: 40, Shield: 0

print(f"{mage.name} takes {damage_taken} damage.")
mage.take_damage(damage_taken)
print(mage)  # Kimenet: Gandalf - Health: 20, Shield: 0

# Ellenőrzés, hogy a karakterek életben vannak-e
print(f"{warrior.name} alive: {warrior.is_alive()}")  # Kimenet: Thor alive: True
print(f"{mage.name} alive: {mage.is_alive()}")        # Kimenet: Gandalf alive: True

# Példa: Játékos Karakterek Osztályhierarchiája
# Képzeljük el, hogy van egy játék, ahol a karakterek különböző típusúak lehetnek, például harcosok és mágusok. Minden karakter rendelkezik élettel és pajzssal, de eltérő támadási képességekkel.

# Magyarázat
# Szülőosztály (Character):

# Az Character osztály tartalmazza a közös attribútumokat, mint a name (név), health (élet) és shield (pajzs).
# Az take_damage metódus kezeli a karakter sebzését, figyelembe véve a pajzsot is. Először a pajzs csökkenti a sebzést, és a maradék sebzés az életre hat.
# Az is_alive metódus ellenőrzi, hogy a karakter még életben van-e.
# Az __str__ metódus a karakter adatait nyomtatja ki.
# Alosztályok (Warrior és Mage):

# Warrior Osztály: A Character osztályból származik, és a harcosok speciális attribútumát, attack_power-t tartalmazza, amely a harcos támadási erejét jelenti. A attack metódus visszaadja a harcos támadási erejét.
# Mage Osztály: A Character osztályból származik, és a mágusok speciális attribútumát, magic_power-t tartalmazza, amely a mágikus képesség erejét jelenti. A cast_spell metódus visszaadja a mágus varázslati erejét.
# Használat:

# Két karaktert hozunk létre: egy harcost és egy mágust, majd kiírjuk az adataikat.
# A karakterek támadási és varázslási képességeit használjuk.
# A take_damage metódussal sebzést adunk a karaktereknek, és ellenőrizzük az új állapotukat.
# Végül ellenőrizzük, hogy a karakterek életben vannak-e.
# Összegzés
# Ez a példa bemutatja, hogyan lehet osztályhierarchiát alkalmazni egy egyszerű játékos karakterek modellálására. Az alap Character osztály tartalmazza a közös tulajdonságokat és funkciókat, míg a Warrior és Mage osztályok speciális képességeket adnak hozzá, tükrözve a játékosok különböző szerepeit. Az öröklés és a szülő- és alosztályok használata segít a kód strukturálásában és egyszerűsíti a karbantartást.