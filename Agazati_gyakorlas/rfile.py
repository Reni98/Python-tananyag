import random

game = False
# while not game:
#     user = int(input("Adj meg egy számot 1-5 között: "))
#     computer = random.randint(1,5)

#     if user > computer:
#         print("Nagyobb számot adtál meg.")
#     elif user < computer:
#         print("Kisebb számot adtál meg.")
#     elif user == computer:
#         print("Győztél!")
#         game = True

#Sorsolás: Készíts egy egyszerű sorsolást, ahol a felhasználók nevei közül választhatsz ki véletlenszerűen egyet.
nevek = ['Anna', 'Béla', 'Cecil', 'Dávid', 'Emma']

nev = random.choice(nevek)
print(f"A kiválasztot név: {nev}")


#Véletlenszerű mondatok generálása: Készíts egy egyszerű mondatgenerátort, amely véletlenszerűen kiválaszt szavakat különböző listákból.
alany = ['A macska', 'A kutya', 'A kisfiú', 'A tanár']
ige = ['fut', 'ugrik', 'alszik', 'játszik']
targy = ['a labdával', 'a fűben', 'a házban', 'a barátokkal']
