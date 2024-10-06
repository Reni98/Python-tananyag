# 1. Fájl Megnyitása és Olvasása (open(), readline(), readlines())
# 1. Fájl létrehozása és írása
# with open('example.txt', 'w') as file:
#     file.write("Első sor\n")
#     file.write("Második sor\n")
#     file.write("Harmadik sor\n")

# # 2. Fájl olvasása readline() használatával
# print("Olvasás readline()-nal:")
# with open('example.txt', 'r') as file:
#     print(file.readline(), end='')  # Első sor
#     print(file.readline(), end='')  # Második sor
#     print(file.readline(), end='')  # Harmadik sor

# # 3. Fájl olvasása readlines() használatával
# print("\nOlvasás readlines()-sal:")
# with open('example.txt', 'r') as file:
#     lines = file.readlines()  # Listába olvas minden sort
#     for line in lines:
#         print(line, end='')  # Minden sort kiíratunk


# Magyarázat
# Fájl Létrehozása és Írása (write()):

# Az open('example.txt', 'w') megnyitja a example.txt nevű fájlt írásra ('w' mód). Ha a fájl nem létezik, létrehozza. Ha létezik, felülírja a tartalmát.
# A file.write("szöveg\n") függvénnyel adatokat írunk a fájlba.
# Fájl Olvasása readline() Használatával:

# Az open('example.txt', 'r') megnyitja a fájlt olvasásra ('r' mód).
# A file.readline() függvénnyel egy sor olvasható be a fájlból. Ha többször hívjuk, a következő sorokat olvassa be.
# Fájl Olvasása readlines() Használatával:

# A file.readlines() függvény az egész fájlt beolvassa, és minden sort egy listában tárol. Minden egyes sor a listában egy elem.

# 2. Fájl Írása és Olvasása (open(), write(), read())

# 1. Fájl írása
with open('data.txt', 'w') as file:
    file.write("Ez egy teszt.\n")
    file.write("Második sor.\n")
    file.write("Harmadik sor.\n")

# 2. Fájl olvasása
print("Fájl tartalma:")
with open('data.txt', 'r') as file:
    content = file.read()  # Az egész fájlt beolvassuk egyszerre
    print(content)         # A fájl tartalmát kiírjuk

# Magyarázat
# Fájl Írása (write()):

# Az open('data.txt', 'w') fájl írásra nyitása. Ha a fájl nem létezik, létrehozza; ha létezik, felülírja.
# Fájl Olvasása (read()):

# Az open('data.txt', 'r') fájl olvasásra nyitása.
# A file.read() az egész fájlt beolvassa egyetlen stringben. Az így kapott stringet kiírjuk.
# Összegzés
# open(): Használjuk fájlok megnyitására olvasásra ('r'), írásra ('w'), vagy egyéb módokra.
# readline(): Egy sort olvas be a fájlból.
# readlines(): Az összes sort beolvassa és listában tárolja.
# write(): Adatokat ír a fájlba.
# Ezek a műveletek segítenek fájlokat kezelni és adatokat olvasni/írni, ami gyakori feladat a programozás során.