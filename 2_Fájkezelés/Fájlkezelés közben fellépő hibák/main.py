# Fájlkezelés során gyakran találkozhatunk hibákkal, például fájl nem létezése, jogosultsági problémák vagy hibás fájlformátumok. Az alábbiakban bemutatok néhány gyakori fájlkezelési hibát és azok kezelését Pythonban, kezdők számára érthető módon.

# Gyakori Fájlkezelési Hibák és Megoldások

# 1. Fájl Nem Létezik (FileNotFoundError)
# Hiba:
# Ez a hiba akkor fordul elő, amikor próbálunk megnyitni egy fájlt, amely nem létezik.
# try:
#     with open('nfile.txt', 'r') as file:
#         content = file.read()
# except FileNotFoundError:
#     print("Hiba: A fájl nem található.")

# Magyarázat:
# try blokk: Itt próbálkozunk a fájl megnyitásával és olvasásával.
# except FileNotFoundError blokk: Ha a fájl nem található, a Python ezt a hibát dobja. Ekkor a print utasítást futtatjuk, hogy tájékoztassuk a felhasználót.

# 2. Hozzáférési Jogosultságok (PermissionError)
# Hiba:
# Ez a hiba akkor fordul elő, ha nincs megfelelő jogosultságunk a fájl írására vagy olvasására.


# try:
#     # Próbáljuk megnyitni a fájlt írásra
#     with open('/protected_folder/important_file.txt', 'w') as file:
#         file.write("Ez egy teszt.")
# except PermissionError:
#     print("Hiba: Nincs jogosultság a fájl eléréséhez.")


# Magyarázat:
# try blokk: Megpróbálunk írni a fájlba, amelyhez nem lehet hozzáférésünk.
# except PermissionError blokk: Ha a hozzáférési jogosultságok problémát okoznak, ezt a hibát dobja a Python, és a megfelelő hibaüzenetet kapjuk.

# 3. Hibás Fájl Formátum (IOError)
# Hiba:

# Ez a hiba akkor fordulhat elő, ha a fájl formátuma nem megfelelő, vagy a fájl nem olvasható.
# try:
#     with open('corrupt_file.txt', 'r') as file:
#         content = file.read()
# except IOError:
#     print("Hiba: A fájl olvasása közben probléma merült fel.")
# Magyarázat:
# try blokk: Megpróbáljuk olvasni a fájlt.
# except IOError blokk: Ha a fájl formátuma vagy olvasási problémák miatt nem tudjuk olvasni, ezt a hibát kapjuk.

# Fájl írása
try:
    with open('data.txt', 'w') as file:
        file.write("Ez egy fontos adat.\n")
except PermissionError:
    print("Hiba: Nincs jogosultság a fájl írásához.")

# Fájl olvasása
try:
    with open('data.txt', 'r') as file:
        content = file.read()
        print("Fájl tartalma:")
        print(content)
except FileNotFoundError:
    print("Hiba: A fájl nem található.")
except IOError:
    print("Hiba: A fájl olvasása közben probléma merült fel.")


# Magyarázat:

# Írás (write()):
# try blokk: Megpróbálunk adatokat írni a data.txt fájlba.
# except PermissionError blokk: Ha nem rendelkezünk megfelelő jogosultsággal a fájl írására, ezt a hibaüzenetet kapjuk.

# Olvasás (read()):
# try blokk: Megpróbáljuk olvasni a fájlt.
# except FileNotFoundError blokk: Ha a fájl nem létezik, ezt a hibaüzenetet kapjuk.
# except IOError blokk: Ha bármilyen egyéb olvasási probléma merül fel, ezt a hibaüzenetet kapjuk.

# Összegzés
# FileNotFoundError: Fájl nem létezése.
# PermissionError: Hozzáférési jogosultságok problémája.
# IOError: Általános bemeneti/kimeneti hiba, például hibás fájlformátum.