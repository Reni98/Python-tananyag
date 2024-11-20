class Jatekos:
    def __init__(self, nev):
        self.nev = nev
        self.pontszam = 0

    def pontot_hozzaad(self, pont):
        self.pontszam += pont

    def pontot_csokkent(self, pont):
        if self.pontszam - pont >= 0:
            self.pontszam -= pont
        else:
            print(f"{self.nev} pontszáma nem lehet negatív!")

    def kiir(self):
        print(f"{self.nev} pontszáma: {self.pontszam}")

# Példa használat
jatekos = Jatekos("Anna")
jatekos.pontot_hozzaad(10)
jatekos.kiir()
jatekos.pontot_csokkent(5)
jatekos.kiir()
jatekos.pontot_csokkent(10)
jatekos.kiir()
