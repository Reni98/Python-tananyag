class Bevasarlolista:
    def __init__(self):
        self.lista = []

    def hozzaad(self, elem):
        self.lista.append(elem)

    def eltavolit(self, elem):
        if elem in self.lista:
            self.lista.remove(elem)
        else:
            print(f"{elem} nem található a listában.")

    def ellenoriz(self, elem):
        return elem in self.lista

    def kiir(self):
        print("A bevásárlólista tartalma:", self.lista)

# Példa használat
bevasarlas = Bevasarlolista()
bevasarlas.hozzaad("kenyér")
bevasarlas.hozzaad("tej")
bevasarlas.hozzaad("vaj")
bevasarlas.kiir()
bevasarlas.eltavolit("tej")
bevasarlas.kiir()
print("Van vaj a listában?", bevasarlas.ellenoriz("vaj"))
