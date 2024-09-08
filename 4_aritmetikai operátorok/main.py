# Az aritmetikai operátorok alapvetően matematikai műveleteket végeznek különböző adattípusokon, például egész számokon (integer), lebegőpontos számokon (float), vagy akár karakterláncokon (string). 

# Összeadás (+): Két értéket ad össze.

x = 5
y = 3
eredmeny = x + y
print(eredmeny)  

# Kivonás (-): Két értékből kivon egyet.

x = 5
y = 3
eredmeny = x - y
print(eredmeny)  

# Szorzás (*): Két értéket szoroz.

x = 5
y = 3
eredmeny = x * y
print(eredmeny)  

# Osztás (/): Egy értéket oszt egy másikkal, és lebegőpontos eredményt ad vissza.

x = 10
y = 3
eredmeny = x / y
print(eredmeny)  

# Maradékos osztás (%): Egy értéket oszt egy másikkal, és csak a maradékot adja vissza.

x = 10
y = 3
maradek = x % y
print(maradek)  

# Hatványozás ():** Egy számot emel egy másik szám hatványára.

x = 2
hatvany = x ** 3
print(hatvany)  

#------------------------------------------------------------------------------------------------------------------------------------
# A rövidített értékadások (augmented assignment operators) arra szolgálnak, hogy rövidített formában hajtsanak végre egy műveletet egy változón, és az eredményt újra a változóba helyezzék. Ez olvashatóbbá és rövidebbé teszi a kódokat, különösen akkor, ha egy változó értékét többször módosítani kell azonos művelettel.

# += 
# Ez az operátor az aktuális változó értékéhez hozzáad egy másik értéket, majd az eredményt visszaadja és elmenti a változóba.

x = 5
x += 3   # Ez ekvivalens a x = x + 3 kifejezéssel
print(x)  

# -= 
# Ez az operátor az aktuális változó értékéből kivon egy másik értéket, majd az eredményt visszaadja és elmenti a változóba.

y = 10
y -= 2   # Ez ekvivalens a y = y - 2 kifejezéssel
print(y)

# *=

z = 3
z *= 4   # Ez ekvivalens a z = z * 4 kifejezéssel
print(z) 

# /=
w = 20
w /= 5   # Ez ekvivalens a w = w / 5 kifejezéssel
print(w) 

# %=
n = 15
n %= 4   # Ez ekvivalens a n = n % 4 kifejezéssel
print(n) 

# **=
m = 2
m **= 3   # Ez ekvivalens a m = m ** 3 kifejezéssel
print(m)