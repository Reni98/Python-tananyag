class Allatkert:
    def __init__(self):
        self.allatok = []

    def hozzaad(self, allat):
        self.allatok.append(allat)

    def allat_szam(self):
        return len(self.allatok)

    def keres(self, allat):
        return allat in self.allatok

    def kiir(self):
        print("Az állatkert lakói:", self.allatok)

# Példa használat
kert = Allatkert()
kert.hozzaad("oroszlán")
kert.hozzaad("elefánt")
kert.hozzaad("tigris")
kert.kiir()
print("Állatok száma:", kert.allat_szam())
print("Van tigris az állatkertben?", kert.keres("tigris"))
