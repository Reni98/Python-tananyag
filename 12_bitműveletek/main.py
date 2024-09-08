# A bitműveletek olyan alapvető műveletek, amelyeket a számítógépes rendszerek bináris (bitekből álló) adatokon végeznek. Ezek a műveletek közvetlenül a számok bináris reprezentációján dolgoznak, és általában alacsony szintű programozási nyelvekben, illetve hardveres szinten használatosak.

# Alapvető bitműveletek

# ÉS művelet (&): Az értékek bitenkénti ÉS művelete a bemenetek minden bitjére alkalmazódik. Az eredmény azokon a helyeken lesz 1, ahol mindkét bemenet 1, máshol 0.

a = 5   # binárisen: 101
b = 3   # binárisen: 011
c = a & b
print(c)   # 1 (binárisen: 001)

# VAGY művelet (|): A bitenkénti VAGY művelet az összes bemenet minden bitjére alkalmazódik. Az eredmény azokon a helyeken lesz 1, ahol legalább az egyik bemenet 1.

a = 5   # binárisen: 101
b = 3   # binárisen: 011
c = a | b
print(c)   # 7 (binárisen: 111)


# Kizáró VAGY művelet (^): A bitenkénti kizáró VAGY művelet az összes bemenet minden bitjére alkalmazódik. Az eredmény azokon a helyeken lesz 1, ahol pontosan az egyik bemenet 1, de nem mindkettő.
a = 5   # binárisen: 101
b = 3   # binárisen: 011
c = a ^ b
print(c)   # 6 (binárisen: 110)

# Negáció (~): A bitenkénti negáció operátor megfordítja az egyes bitjeit.
a = 5   # binárisen: 101
c = ~a
print(c)   # -6

# Python bitműveletek
# Pythonban a bitműveletek használata ritkább, mivel általában a magasabb szintű műveletek és az adattípusok használata szokványos. Azonban ha valaki a bináris szinten dolgozik adatokkal, a bitműveletek rendkívül hasznosak és hatékonyak lehetnek.

# Összefoglalás
# A bitműveletek alapvető fontosságúak a hardveres szintű programozásban és alacsony szintű számítógépes nyelvekben. Bár Pythonban nem olyan gyakran használják őket, fontos megérteni az alapokat és tudni, hogyan működnek, különösen akkor, ha alacsony szintű műveleteket kell végezni adatokkal.