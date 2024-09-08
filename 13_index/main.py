# Index fogalma
# Az index Pythonban a lista elemeinek sorszámozását jelöli. A listák indexelése 0-tól kezdődik, azaz az első elem indexe 0, a második elem indexe 1, és így tovább. Negatív indexek is használhatók, amelyek a lista végéről kezdve számolnak vissza. Például -1 az utolsó elem indexe, -2 az utolsó előtti elem indexe, és így tovább.

# Lista létrehozása
lista = ["alma", "körte", "szilva", "banán", "barack"]

# Pozitív indexek használata
print(lista[0])    # "alma" (az első elem)
print(lista[2])    # "szilva" (a harmadik elem)
print(lista[4])    # "barack" (az ötödik elem)

# Negatív indexek használata
print(lista[-1])   # "barack" (az utolsó elem)
print(lista[-2])   # "banán" (az utolsó előtti elem)
print(lista[-5])   # "alma" (az első elem)

# Magyarázat:
# A lista nevű listában az elemek sorrendje: "alma", "körte", "szilva", "banán", "barack".
# A pozitív indexekkel a lista elemeihez hozzáférünk. Például lista[0] az első elemet adja vissza, lista[2] a harmadik elemet, stb.
# A negatív indexekkel a lista végéről indulva érhetünk el elemeket. Például lista[-1] az utolsó elemet adja vissza, lista[-2] az utolsó előtti elemet, stb.

# Fontosság
# Indexelés kezdete: Pythonban a lista indexelése 0-tól kezdődik.
# Negatív indexek: Használhatók a lista végéről való visszaszámláláshoz, ami gyakran kényelmes, ha az utolsó elemre vagy az utolsó előtti elemre van szükségünk.
# Hiba elkerülése: Fontos figyelni, hogy az indexek ne lépjenek túl a lista határain, mert ez IndexError kivételt eredményezhet.