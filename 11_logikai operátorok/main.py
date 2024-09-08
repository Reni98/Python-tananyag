# A logikai operátorok (and, or, not) Pythonban arra szolgálnak, hogy logikai kifejezéseket összekapcsoljunk vagy megfordítsunk. Ezek az operátorok segítenek összetett feltételek létrehozásában, amelyeket például if-elif-else szerkezetekben használhatunk.

# Logikai operátorok
# and: Mindkét kifejezésnek igaznak kell lennie ahhoz, hogy az összetett kifejezés igaz legyen.
# or: Elég, ha legalább az egyik kifejezés igaz ahhoz, hogy az összetett kifejezés igaz legyen.
# not: Megfordítja a kifejezés logikai értékét. Ha a kifejezés igaz, hamis lesz, és fordítva.

# Példák
# and operátor
# Az and operátor akkor ad vissza igaz értéket, ha mindkét operandusa igaz.
x = 5
y = 10

if x > 0 and y > 0:
    print("Mindkét szám pozitív.")

# Ebben a példában a kifejezés csak akkor igaz, ha mindkét feltétel (x > 0 és y > 0) teljesül.

# or operátor
# Az or operátor akkor ad vissza igaz értéket, ha legalább az egyik operandusa igaz.

x = -5
y = 10

if x > 0 or y > 0:
    print("Legalább az egyik szám pozitív.")
# Ebben a példában a kifejezés igaz, mert a második feltétel (y > 0) igaz, függetlenül attól, hogy az első feltétel (x > 0) hamis.

# not operátor
# A not operátor megfordítja a kifejezés logikai értékét.

x = 5

if not x > 10:
    print("A szám nem nagyobb, mint 10.")

# Ebben a példában a kifejezés x > 10 hamis, tehát a not x > 10 igaz lesz, és a feltétel teljesül.

# Összetett példák
# Több feltétel ellenőrzése
x = 5
y = 15
z = 10

if x < y and y < z:
    print("x kisebb y-nál és y kisebb z-nél.")
else:
    print("Legalább az egyik feltétel hamis.")

# Ebben a példában a feltétel x < y igaz, de a feltétel y < z hamis, ezért az and operátorral összekapcsolt kifejezés hamis lesz, és a else ág fut le.

# Alternatív feltételek ellenőrzése
x = 5
y = -10

if x > 0 or y > 0:
    print("Legalább az egyik szám pozitív.")
else:
    print("Egyik szám sem pozitív.")
# Ebben a példában az or operátorral összekapcsolt feltétel igaz, mert az első feltétel (x > 0) igaz, így a print utasítás a if ágban fut le.

# Negáció használata(A negáció használata azt jelenti, hogy egy logikai kifejezés eredményét megfordítjuk. )
x = 5

if not (x < 0):
    print("A szám nem negatív.")
# Ebben a példában a not operátor a kifejezés x < 0 értékét fordítja meg. Mivel x < 0 hamis, a not (x < 0) igaz lesz, és a feltétel teljesül.

# Összefoglalás
# A logikai operátorok (and, or, not) segítenek összetett logikai feltételek létrehozásában és értékelésében. Ezek használata különösen fontos, amikor több feltételt kell együttesen ellenőriznünk egy programban. 
