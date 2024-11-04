#A függvények az egyik alapvető építőkövei a Python programozásnak
# Függvények Alapjai
# Mi az a Függvény?
# A függvény egy önálló kódrészlet, amely egy adott feladatot hajt végre. A függvényeket általában arra használjuk, hogy a kódunkat modulárissá és újrahasználhatóvá tegyük. Függvényekkel kódot csoportosíthatunk és elkerülhetjük a kód ismétlését.

# Függvény Jellemzői
# Definiálás: A függvényeket a def kulcsszóval definiáljuk.
# Név: Minden függvénynek neve van, amelyet a hívásakor használunk.
# Paraméterek: A függvények paramétereket (vagy argumentumokat) fogadhatnak, amelyek a függvény működéséhez szükségesek.
# Visszatérési érték: A függvények egy értéket is visszaadhatnak a return kulcsszóval.
# Dokumentáció: A függvényekhez docstringet (dokumentáló szöveget) is hozzáadhatunk, amely leírja a függvény működését.

# 1. Egyszerű Függvény
# Egy egyszerű függvény, amely nem fogad paramétereket és nem ad vissza értéket.
def say_hello():
    print("Hello, World!")

# Függvény hívása
say_hello()  # Output: Hello, World!

# Magyarázat:

# def say_hello():: A def kulcsszóval definiáljuk a say_hello nevű függvényt.
# print("Hello, World!"): A függvény tartalma, amely üdvözlő üzenetet ír ki a képernyőre.
# say_hello(): A függvény hívása, amely végrehajtja a benne lévő kódot.

# 2. Paramétereket Fogadó Függvény
# Egy függvény, amely paramétereket fogad és visszaad egy értéket.
def add_numbers(a, b):
    return a + b

# Függvény hívása
result = add_numbers(5, 3)
print(result)  # Output: 8

# Magyarázat:

# def add_numbers(a, b):: A függvény két paramétert (a és b) fogad.
# return a + b: A függvény visszaadja a két paraméter összegét.
# result = add_numbers(5, 3): A függvény hívása, ahol az 5 és 3 értékeket átadjuk a a és b paramétereknek.

# 3. Alapértelmezett Értékek
# Függvény alapértelmezett paraméterértékekkel.
def greet(name="Guest"):
    print(f"Hello, {name}!")

# Függvény hívása alapértelmezett értékkel
greet()  # Output: Hello, Guest!

# Függvény hívása megadott értékkel
greet("Alice")  # Output: Hello, Alice!

# Magyarázat:

# name="Guest": Az alapértelmezett érték, amelyet akkor használunk, ha a függvényt paraméter nélkül hívjuk.
# print(f"Hello, {name}!"): Az üdvözlő üzenet tartalmazza a paraméter értékét.

# 4. Többsoros Dokumentációs Szöveg (Docstring)
# Dokumentációs szöveg hozzáadása a függvényhez.
def multiply(x, y):
    """
    Visszaadja az x és y szorzataként kapott értéket.

    :param x: Az első szám
    :param y: A második szám
    :return: Az x és y szorzata
    """
    return x * y

# Függvény hívása
print(multiply(4, 5))  # Output: 20

# Dokumentációs szöveg megtekintése
print(multiply.__doc__)

# Magyarázat:

# """ ... """: A docstring, amely a függvény működését és paramétereit dokumentálja.
# multiply.__doc__: A docstring megtekintése a függvényhez.

# További Függvény Jellemzők
# Változó Számú Argumentumok:

# Használhatjuk a *args és **kwargs szintaxist, hogy változó számú pozicionált és kulcs-érték páros argumentumokat fogadjunk.
def print_args(*args):
    for arg in args:
        print(arg)

print_args(1, 2, 3, "hello")  # Output: 1 2 3 hello

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Alice", age=30)  # Output: name: Alice  age: 30

# Lambda Függvények:
# Mikor Használunk Lambda Függvényt?
# Egyszerű Függvények Létrehozása:

# Ha csak egy egyszerű kifejezésre van szükséged, amely nem igényel több sor kódot.
# Például, ha csak egyszer használod a függvényt, vagy nem szükséges a függvény nevének tárolása.
# Függvények Paramétereként:

# Ha olyan függvényeket használunk, amelyek paraméterként fogadnak más függvényeket, mint például az map(), filter() vagy sorted() függvények.
# Lambda függvények ideálisak, amikor a függvényt csak egyszer és csak egy helyen használjuk.
# Rövid Kódot Szeretnénk Írni:

# Lambda függvények rövidebb szintaxist kínálnak, mint a normál függvénydefiníciók, amelyeket hasznos lehet rövid, egy soros kifejezésekhez.

# Az egyszerű, névtelen függvények, amelyeket lambda kulcsszóval hozhatunk létre.
add = lambda a, b: a + b
print(add(3, 4))  # Output: 7

# Összegzés
# Függvények: Olyan kódrészletek, amelyek ismételten felhasználhatóak, és amelyek paramétereket fogadhatnak és értékeket adhatnak vissza.
# Jellemzők:
# Definiálás def kulcsszóval.
# Paraméterek fogadása és visszatérési érték.
# Dokumentációs szöveg a """ ... """ szintaxissal.
# Alapértelmezett paraméterértékek.
# Változó számú argumentumok kezelése *args és **kwargs használatával.
# Lambda függvények az egyszerű, névtelen függvényekhez.