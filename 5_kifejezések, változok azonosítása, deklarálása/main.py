#  A kifejezések a programban matematikai műveleteket, logikai összehasonlításokat, változókhoz való hozzáféréseket vagy bármilyen más, értelmesen értelmezett utasításokat jelentenek, amelyek eredményeként egy érték vagy állapot keletkezik.

# A kifejezések kiértékelése során a program futása során ezek az utasítások vagy műveletek végrehajtódnak, és azok eredménye kerül visszaadásra, amelyet további műveletekhez vagy értékadásokhoz lehet használni.

# Egyszerű matematikai kifejezés kiértékelése:
# Kifejezés: 3 + 2 * 5
# Matematikai szabályok érvényesek: szorzás előzi meg az összeadást.
# Eredmény: 3 + 10 = 13
result = 3 + 2 * 5
print(result)  

# Logikai kifejezés kiértékelése:
# Kifejezés: (4 > 2) and (3 < 1)
# 4 > 2 értéke True, 3 < 1 értéke False.

# Logikai 'and' művelet: mindkét feltétel igaznak kell lennie.
# Eredmény: True and False = False
result = (4 > 2) and (3 < 1)
print(result)  

# A logikai 'or' (vagy) művelet két feltétel közül legalább az egyik igaznak kell lennie ahhoz, hogy az összegzett kifejezés igaz legyen.
# Kifejezés: (4 > 2) or (3 < 1)
# 4 > 2 igaz, 3 < 1 hamis.
# Logikai 'or' művelet: legalább az egyik feltétel igaz.
# Eredmény: True or False = True
result = (4 > 2) or (3 < 1)
print(result)

# A logikai 'not' (nem) művelet az adott feltétel logikai értékének ellentettjét adja vissza.
# Kifejezés: not (4 > 2)
# 4 > 2 igaz.
# Logikai 'not' művelet: az igaz értéket megfordítja.
# Eredmény: not True = False
result = not (4 > 2)
print(result)


# Változók és kifejezések kombinációja:
# Változók inicializálása
a = 10
b = 3

# Kifejezések értékelése
# Kifejezés: a + b / 2
# Szabály: osztás előzi meg az összeadást.
# Eredmény: 10 + 1.5 = 11.5
result = a + b / 2
print(result) 

# Függvényhívás és kifejezések:
# Függvény definíció
def double(x):
    return x * 2

# Kifejezés: double(5) + 3
# double(5) értéke: 10
# Eredmény: 10 + 3 = 13
result = double(5) + 3
print(result)

# Kiértékelési szabályok:
# Matematikai műveletek: A szorzás (*), osztás (/), összeadás (+) és kivonás (-) matematikai prioritását követi.

# Logikai műveletek: Logikai 'and', 'or', 'not' műveletek végrehajtása a szabványos logikai szabályoknak megfelelően történik.

# Függvényhívások: A függvények kiértékelése az adott függvény definíciójának megfelelően történik, az argumentumok átadásával.

# Változók és literálok: A változók és literálok közvetlenül értékelődnek ki a megfelelő típusú értékekké.

# Zárójelek: A zárójelek használata meghatározza a kifejezések kiértékelési sorrendjét, módosítva a természetes precedenciát.

#----------------------------------------------------------------------------------------------------------------------------
# Változók azonosítása és deklarálása Pythonban

#Változók azonosítása:
# A változó azonosítása Pythonban a változó nevének megadását jelenti. Fontos szabályok:
# Csak betűkkel (kis- és nagybetűk), számokkal és aláhúzásjellel (_) kezdődhet.
# Nem kezdődhet számmal.
# Nem tartalmazhat szóközt vagy speciális karaktert (kivéve az aláhúzásjel).

# Deklarálás:
# Pythonban a változó deklarálása nem igényel külön típusmegadást. Egyszerűen csak adunk nevet a változónak, és értéket adunk neki az első értékadás során.

# Változó azonosítása és deklarálása
age = 25
name = "Alice"
is_student = True

# Ebben a példában három változót hoztunk létre:

# age: Egész szám típusú változó, értéke 25.
# name: Szöveg típusú változó, értéke "Alice".
# is_student: Logikai típusú változó, értéke True.

# Értékadás:
# Értékadás változónak
x = 10
y = x + 5
print(y)

# Ebben a példában az x változónak először értéket adtunk (10), majd az y változónak az x értékéhez hozzáadtunk még 5-öt.

# Foglalt szavak:
# Pythonban vannak olyan foglalt szavak, amelyeket nem lehet változónevekként használni, mivel ezek a nyelv beépített szimbólumai vagy kulcsszavai.

#  A Python nyelvben vannak olyan foglalt szavak, amelyeket a nyelv szintaktikai elemzéséhez, vezérlési szerkezetekhez vagy beépített funkciókhoz használnak, ezért nem használhatók változónevekként. Ezek a foglalt szavak a következők:

# False      await      else       import     pass
# None       break      except     in         raise
# True       class      finally    is         return
# and        continue   for        lambda     try
# as         def        from       nonlocal   while
# assert     del        global     not        with
# async      elif       if         or         yield
