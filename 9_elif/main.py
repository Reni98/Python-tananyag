#  Elágazások (feltételes utasítások) lehetővé teszik, hogy a program különböző utasításokat hajtson végre különböző feltételek alapján. Az elágazások használata alapvető fontosságú a programozásban, mivel lehetővé teszi a program számára, hogy döntéseket hozzon és különböző utakat kövessen a feltételek szerint.

# Egyszerű (egyágú) elágazások
# Az egyágú elágazások egyszerű feltételes utasítások, amelyek egyetlen feltételt ellenőriznek.
eletkor = 20

if eletkor >= 18:
    print("Felnőtt vagy.")
# Ebben a példában az if utasítás ellenőrzi, hogy az eletkor nagyobb vagy egyenlő-e, mint 18. Ha igen, a program végrehajtja a print utasítást.

# Többágú elágazások
# A többágú elágazások lehetővé teszik, hogy a program több különböző feltételt ellenőrizzen és különböző utasításokat hajtson végre attól függően, hogy melyik feltétel teljesül.
eletkor = 16

if eletkor >= 18:
    print("Felnőtt vagy.")
else:
    print("Kiskorú vagy.")


# Ebben a példában az if utasítás először ellenőrzi, hogy az eletkor nagyobb vagy egyenlő-e, mint 18. Ha igen, a program végrehajtja az első print utasítást. Ha nem, a program végrehajtja az else blokkban található utasítást.

# Elágazások egymásba ágyazása
# Az elágazások egymásba ágyazása azt jelenti, hogy egy elágazást egy másik elágazás belsejében helyezünk el.
eletkor = 19
orszag = "Magyarország"

if eletkor >= 18:
    if orszag == "Magyarország":
        print("Felnőtt vagy Magyarországon.")
    else:
        print("Felnőtt vagy.")
else:
    print("Kiskorú vagy.")

 # Ebben a példában az if eletkor >= 18 feltétel belsejében található egy másik if feltétel, amely ellenőrzi az orszag változó értékét.

#  Az elif utasítás
# Az elif (else if) utasítás lehetővé teszi, hogy több különböző feltételt ellenőrizzünk egymás után, anélkül hogy minden egyes feltételhez külön if-et kellene írni.
nap = "hétfő"

if nap == "hétfő":
    print("Ma hétfő van.")
elif nap == "kedd":
    print("Ma kedd van.")
elif nap == "szerda":
    print("Ma szerda van.")
else:
    print("Ma nem hétfő, kedd vagy szerda van.")
# Ebben a példában az elif utasítások lehetővé teszik, hogy több különböző napot ellenőrizzünk egymás után. Ha egyik feltétel sem teljesül, a program az else blokkban található utasítást hajtja végre.

# Példák és használat
# Egyszerű (egyágú) elágazás
szam = 5

if szam > 0:
    print("A szám pozitív.")

# Többágú elágazás
szam = -5

if szam > 0:
    print("A szám pozitív.")
else:
    print("A szám nem pozitív.")


# Egymásba ágyazott elágazás
szam = -5

if szam >= 0:
    if szam == 0:
        print("A szám nulla.")
    else:
        print("A szám pozitív.")
else:
    print("A szám negatív.")


# elif utasítás
szam = 0

if szam > 0:
    print("A szám pozitív.")
elif szam < 0:
    print("A szám negatív.")
else:
    print("A szám nulla.")

# Miért fontosak az elágazások?
# Döntéshozatal: Lehetővé teszik a program számára, hogy döntéseket hozzon különböző feltételek alapján.
# Rugalmasság: Segítenek a program viselkedésének rugalmas irányításában.
# Olvashatóság: Az elágazások használata javítja a kód olvashatóságát és érthetőségét.