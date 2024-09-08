# a fő fájlt érdemes main.py nak elnevezni
print("hello 1")
print("hello 2")
print("hello 3")
# Az utasítások abban a sorrendben hajtódtak végre ahogy mi megadtuk, linálisan hajtja végre a Python, egyik után a másikat.

# Szöveg és változók kombinálása
name = "Alice"
age = 30
print("Név:", name)
print("Kor:", age)
print("Név és kor: " + name + ", " + str(age))
print(f"Név és kor: {name}, {age}")

# Speciális karakterek kezelése
print("Első sor\nMásodik sor")
#\t (tabulátor) speciális karakter használatával két oszlopot jelenít meg, a tabulátorral elválasztva őket. A tabulátor karakter egy horizontális térközt ad, amely általában a következő tabulátor pozícióig tolja el a szöveget.
print("Első oszlop\tMásodik oszlop")


#A többsoros szöveg használata """ (három dupla idézőjel) vagy ''' (három szimpla idézőjel) között lehetővé teszi, hogy egyetlen string literálban több sort is megadhassunk anélkül, hogy speciális karaktereket (mint például \n) kellene használnunk. 
# Többsoros szöveg kiírása
multi_line_text = """Ez egy
többsoros
szöveg."""
print(multi_line_text)

#A sep paraméter a print függvényben azt határozza meg, hogy milyen karaktert (vagy karakterláncot) használjon a Python az argumentumok közötti elválasztásra, amikor több elemet adunk meg a print függvénynek.
# Elválasztó karakterek használata
print("alma", "banán", "cseresznye", sep=", ")

# Vége karakterek kezelése
print("Első sor", end=" - ")
print("Második sor")

#-------------------------------------------------------------------------------------------------------------
#A print függvény paraméterezése

# A Python print függvénye különböző paraméterekkel rendelkezik, amelyeket használhatunk a kimenet formázására és irányítására. Ezek a paraméterek a következők:

# sep: Elválasztó karakter az argumentumok között. Alapértelmezett értéke egy szóköz (' ').
# end: Karakter vagy karakterlánc, amely a kimenet végére kerül. Alapértelmezett értéke egy új sor ('\n').
# file: A fájlobjektum, ahová a kimenet íródik. Alapértelmezés szerint a standard kimenetre (általában a képernyő) ír.
# flush: Ha True, akkor az output buffer azonnal kiürítésre kerül. Alapértelmezett értéke False.
# Ha a flush paraméter értékét True-ra állítjuk, a kimenet azonnal íródik a végső kimeneti célba (például a képernyőre vagy fájlba), figyelmen kívül hagyva a bufferelést. Ez akkor lehet hasznos, ha valós idejű vagy közel valós idejű kimenetet szeretnénk látni, például amikor fontos látni a kimenetet azonnal, mint egy log vagy folyamatosan frissülő kijelző esetében.

# Escape karakterek és új sor vezérlőkarakterek
# Escape karakterek: Speciális karakterek, amelyeket a \ (backslash) segítségével adunk meg, és amelyek különleges jelentéssel bírnak.
# \n: Új sor.
# \t: Tabulátor (horizontális térköz).
# \\: Backslash.
# \': Szimpla idézőjel.
# \": Dupla idézőjel.


# A print függvény paraméterezése
# A Python print függvénye különböző paraméterekkel rendelkezik, amelyeket használhatunk a kimenet formázására és irányítására. Ezek a paraméterek a következők:


# Példák
# sep paraméter használata


print("alma", "banán", "cseresznye", sep=", ")



# alma, banán, cseresznye
# end paraméter használata

print("Első sor", end=" - ")
print("Második sor")

# Első sor - Második sor
# file paraméter használata

with open("output.txt", "w") as file:
    print("Ez egy fájlba íródik", file=file)
# flush paraméter használata

import time
import sys

print("Hello", end="", flush=True)
time.sleep(2)
print(", világ!", flush=True)
# Ez a kód azonnal kiírja a "Hello" szöveget, majd két másodperc múlva hozzáfűzi a ", világ!" szöveget.

# Escape karakterek használata
# Új sor és tabulátor

print("Első sor\nMásodik sor")
print("Első oszlop\tMásodik oszlop")



# Backslash és idézőjelek

print("Ez egy backslash: \\")
print("Ez egy szimpla idézőjel: \'")
print("Ez egy dupla idézőjel: \"")


# Ez egy backslash: \
# Ez egy szimpla idézőjel: '
# Ez egy dupla idézőjel: "

# Paraméterátadás fajtái (positional, keyword)

# A Python függvények paramétereit kétféleképpen adhatjuk át: pozíció szerint (positional) és kulcsszóval (keyword).

# Pozíció szerinti paraméterátadás (positional)

print("alma", "banán", "cseresznye", ", ", "\n", sys.stdout, False)
# Ebben az esetben az összes paramétert az adott sorrendben kell megadnunk, és mindegyik pozíciója meghatározza a jelentését. Azonban a print függvényben általában a sep, end, file és flush paramétereket kulcsszóval adjuk meg.

# Kulcsszóval történő paraméterátadás (keyword)

print("alma", "banán", "cseresznye", sep=", ", end=".\n", file=sys.stdout, flush=False)
#Ebben az esetben az egyes paramétereket nevükkel együtt adjuk meg, így az átadás sorrendje tetszőleges lehet.

# Kombinált példa

import sys

# Alapértelmezett viselkedés
print("Alapértelmezett viselkedés:")
print("alma", "banán", "cseresznye")

# Elválasztó és vége karakter használata
print("\nElválasztó és vége karakter használata:")
print("alma", "banán", "cseresznye", sep=", ", end=".\n")

# Több sor és tabulátor
print("\nTöbb sor és tabulátor:")
print("Első sor\nMásodik sor")
print("Első oszlop\tMásodik oszlop")

# Fájlba írás
print("\nFájlba írás:")
with open("output.txt", "w") as file:
    print("Ez egy fájlba íródik", file=file)

# Flush használata
print("\nFlush használata:")
print("Hello", end="", flush=True)
time.sleep(2)
print(", világ!", flush=True)

# Escape karakterek
print("\nEscape karakterek:")
print("Ez egy backslash: \\")
print("Ez egy szimpla idézőjel: \'")
print("Ez egy dupla idézőjel: \"")

# Paraméterek kulcsszóval történő átadása
print("\nParaméterek kulcsszóval történő átadása:")
print("alma", "banán", "cseresznye", sep=", ", end=".\n", file=sys.stdout, flush=False)


