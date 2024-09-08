# Relációs operátorok: a programozásban olyan speciális operátorok, amelyek segítségével összehasonlításokat végezhetünk különböző értékek között. Ezek az operátorok visszatérnek egy logikai értékkel (True vagy False), attól függően, hogy az összehasonlítás eredménye igaz vagy hamis.

# Relációs operátorok Pythonban
# ==: Egyenlőség operátor, amely azt ellenőrzi, hogy két érték megegyezik-e.
# !=: Nem egyenlőség operátor, amely azt ellenőrzi, hogy két érték nem egyezik-e meg.
# >: Nagyobb operátor, amely azt ellenőrzi, hogy az egyik érték nagyobb-e a másiknál.
# <: Kisebb operátor, amely azt ellenőrzi, hogy az egyik érték kisebb-e a másiknál.
# >=: Nagyobb vagy egyenlő operátor, amely azt ellenőrzi, hogy az egyik érték nagyobb vagy egyenlő-e a másikkal.
# <=: Kisebb vagy egyenlő operátor, amely azt ellenőrzi, hogy az egyik érték kisebb vagy egyenlő-e a másikkal.

# Egész számok összehasonlítása:
x = 5
y = 10

# Egyenlőség
print(x == y)  # False

# Nem egyenlőség
print(x != y)  # True

# Nagyobb
print(x > y)   # False

# Kisebb
print(x < y)   # True

# Nagyobb vagy egyenlő
print(x >= y)  # False

# Kisebb vagy egyenlő
print(x <= y)  # True

# Sztringek összehasonlítása:
szotozsde = "Python"
tanulas = "Python"

# Egyenlőség
print(szotozsde == tanulas)  # True

# Nem egyenlőség
print(szotozsde != tanulas)  # False

# Miért fontosak a relációs operátorok?
# Összehasonlítások végrehajtása: Lehetővé teszik számunkra, hogy összehasonlítsuk két vagy több értékét és döntsük el, hogy azok megegyeznek-e vagy egyik nagyobb/kisebb-e a másiknál.
# Feltételes kifejezések: Alapvető részei a feltételes utasításoknak (if, else, elif), amelyek segítségével programunk döntéseket hozhat az adatok alapján.
# Logikai műveletek: A relációs operátorok fontos szerepet játszanak a logikai műveletekben, mint például az and, or, not, amelyekkel összetett feltételeket hozhatunk létre.


# További fontos információk a relációs operátorokról:
# 1. Logikai értékek visszatérési értékei
# A relációs operátorok mindig egy logikai értéket (True vagy False) adnak vissza az alábbi módon:

# ==: Egyenlőség operátor - Igaz (True), ha az operandusok értékei egyenlőek, különben Hamis (False).
# !=: Nem egyenlőség operátor - Igaz (True), ha az operandusok értékei nem egyenlőek, különben Hamis (False).
# >: Nagyobb operátor - Igaz (True), ha az egyik operandus nagyobb, különben Hamis (False).
# <: Kisebb operátor - Igaz (True), ha az egyik operandus kisebb, különben Hamis (False).
# >=: Nagyobb vagy egyenlő operátor - Igaz (True), ha az egyik operandus nagyobb vagy egyenlő, különben Hamis (False).
# <=: Kisebb vagy egyenlő operátor - Igaz (True), ha az egyik operandus kisebb vagy egyenlő, különben Hamis (False).

# 2. Láncolás és kombináció
# Relációs operátorokat láncolhatunk egymás után vagy kombinálhatunk más logikai operátorokkal (pl. and, or, not), hogy összetettebb feltételeket hozzunk létre:

x = 10
y = 20
z = 30

# Egyszerű relációs operátorok
print(x < y)     # True
print(y == z)    # False

# Összetett relációs operátorok
print(x < y < z)    # True (láncolt reláció)
print(x < y and y < z)  # True (and logikai operátor használata)
print(x < y or y == z)  # True (or logikai operátor használata)

# 3. Fontosság a kifejezésekben
# A relációs operátorok gyakran használatosak feltételes utasításokban (if, elif, else) és ciklusokban, ahol döntéseket hozunk a program folyamatának irányításához:
eletkor = 25

if eletkor >= 18:
    print("Felnőtt")
else:
    print("Kiskorú")

# Ebben a példában az >= relációs operátorral döntjük el, hogy az eletkor változó értéke meghaladja-e a 18-at.

# Miért fontosak?
# Feltételes vezérlés: Segítenek döntéseket hozni a program folyamatában.
# Adatok összehasonlítása: Lehetővé teszik az adatok közötti összehasonlításokat és a logikai műveletek végrehajtását.
# Program struktúrájának irányítása: Alapvető részei a programvezérlésnek és a logikai felépítésnek.