class Konyvtar:
    def __init__(self):
        self.konyvek=[]

    def hozzad(self,konyv_cim):
        self.konyvek.append(konyv_cim)

    def kiir(self):
        print(f"A könyvtárban található könyvek: ")
        for konyv in self.konyvek:
            print("_", konyv)

    def kezdAval(self):
        for k in self.konyvek:
            if k.startswith("A"):
                print(k)

konyvtar = Konyvtar()
konyvtar.hozzad("Alice csodaországban")
konyvtar.hozzad("Egyri Csillagok")
konyvtar.hozzad("Harry Potter")

konyvtar.kiir()
konyvtar.kezdAval()