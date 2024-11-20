class Gombak:
    def __init__(self):
        self.gombak = []

    def fajl_beolvas(self,fajlnev):
        with open(fajlnev,"r", encoding="UTF8") as fajl:
            sorok = fajl.readlines()

            for sor in sorok[1:]:
                sor = sor.strip()
                sor = sor.split("@")

                nev = sor[0]
                nemzetseg = sor[1]
                evszak = sor[2]
                self.gombak.append([nev,nemzetseg,evszak])

    def gombak_szama(self):
        print(f"  A gombák száma:{len(self.gombak)}")

    def papsapka(self):
        for i in self.gombak:
            if i[1] == "papsapkagombák ":
                neve=i[0]
                break
        print(f" Az első papsapkagomba neve: {neve}")

    def tinoru(self):
        db= 0
        for n in self.gombak:
            if n[1] == "tinóru":
                db+=1
        print(f"A tinóru gombák száma: {db}")

