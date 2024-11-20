import random

class Szam:
    def __init__(self):
        self.szam = random.randint(1,50)

    def kiiras(self):
        print(f"A generált szám: {self.szam}")
        if self.szam % 5 == 0:
            print("A szám öttel osztható!")
        elif self.szam % 3 == 0:
            print("A szám hárommal osztható!")
        elif self.szam % 5  == 0 and self.szam%3== 0:
            print("A szám öttel és hárommal is osztható!")