class Korok:
    def __init__(self):
        self.korok = []

    def beker(self):
        for i in range(1, 5):
            kor = int(input("Adjon meg egy számot (0,120) között: "))
            self.korok.append(kor)
        print(":".join(map(str,self.korok)))

    def elso_idos(self):
        for k in self.korok:
            if k > 70:
               index = self.korok.index(k)
               return index

    def konzolra_ir(self):
        index = self.elso_idos()
        print(f"Első idős ember korának helye a listában: {index}")

    def fajl_ir(self):
        index = self.elso_idos()
        with open("oreg.txt", "w", encoding="UTF8") as fajl:
            fajl.write(f"Első idős ember korának helye a listában: {index}")



