# Az input függvény a Python programozási nyelv egyik beépített függvénye, amely felhasználói adatbevitelre szolgál. Az input függvény használata során a program megáll, és várja, hogy a felhasználó begépeljen egy értéket, majd ezt az értéket visszaadja sztring (string) formában.

# Szintaxis
input("prompt")
# prompt: (nem kötelező) egy szöveg, amelyet a felhasználónak jelenít meg a program a bevitel előtt. Ez a szöveg segít a felhasználónak megérteni, hogy mit kell beírnia.

# Kérünk egy nevet a felhasználótól
nev = input("Kérlek, add meg a neved: ")
print("Szia, " + nev + "!")

# Ebben a példában a program megkéri a felhasználót, hogy adja meg a nevét, majd köszönti a felhasználót a megadott névvel.

# Számok beolvasása
# Mivel az input függvény mindig sztringet ad vissza, ha számot szeretnénk beolvasni, akkor az adatot először át kell alakítanunk megfelelő típusúra, például integerre (egész számra) vagy float-ra (lebegőpontos számra).

# Egész szám beolvasása

# Kérünk egy számot a felhasználótól
kor = int(input("Kérlek, add meg az életkorodat: "))
# print("Te " + str(kor) + " éves vagy.")
# print("Te " + kor + " éves vagy.")
print(f"Te  {kor}  éves vagy.")

# Ebben a példában a felhasználó életkorát kérjük be. Mivel az életkor egy egész szám, az input függvény visszaadott értékét az int függvénnyel alakítjuk át.

# A példában a str(kor) azért van használva, hogy az int típusú kor változót sztringgé alakítsa, így a print függvényben lévő sztringekkel együtt ki lehessen írni. A Pythonban a + operátor két sztring összefűzésére használható, de nem lehet egy sztringet és egy számot közvetlenül összefűzni, mert az hibát okozna.

# Lebegőpontos szám beolvasása
# Kérünk egy számot a felhasználótól
magassag = float(input("Kérlek, add meg a magasságodat méterben: "))
print("A magasságod " + str(magassag) + " méter.")

# Itt a felhasználó magasságát kérjük be, amely egy lebegőpontos szám, így az input függvény visszaadott értékét a float függvénnyel alakítjuk át.

# Összetett példa
# Az alábbi példa egy egyszerű számológépet valósít meg, amely két számot kér be a felhasználótól, majd kiírja azok összegét.

# Első szám bekérése
szam1 = float(input("Add meg az első számot: "))

# Második szám bekérése
szam2 = float(input("Add meg a második számot: "))

# Összeg kiszámítása
osszeg = szam1 + szam2

# Eredmény kiírása
print(f"A két szám összege: {osszeg}")

# Ebben a példában két számot kérünk be a felhasználótól, átalakítjuk őket lebegőpontos számokká, majd kiszámítjuk és kiírjuk az összegüket.

# Hibakezelés
# Az adatbevitel során érdemes figyelni a hibákra, például ha a felhasználó nem számot ad meg, amikor azt várnánk. Ezt try-except blokk használatával kezelhetjük.

try:
    szam = float(input("Adj meg egy számot: "))
    print("A megadott szám: " + str(szam))
except ValueError:
    print("Hiba: Nem számot adtál meg.")

# Ebben a példában, ha a felhasználó nem számot ad meg, a program nem omlik össze, hanem egy hibaüzenetet jelenít meg.