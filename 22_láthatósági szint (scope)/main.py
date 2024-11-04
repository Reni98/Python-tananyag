# A láthatósági szint (scope) a programozásban arra utal, hogy egy adott változó, függvény vagy egyéb név hol érhető el a kódon belül. Különböző láthatósági szintek léteznek, például lokális és globális scope. A láthatósági szint meghatározza, hogy a változókat vagy függvényeket hol lehet olvasni vagy módosítani.

# 1. Globális Scope
# A globális scope az a környezet, amely a program teljes területére kiterjed. Ha egy változót a globális scope-ban definiálsz, akkor az a program bármely részéből elérhető.

# Példa:
x = 10  # Globális változó

def print_x():
    print(x)  # A globális x változó elérhető itt is

print_x()  # Output: 10


# 2. Lokális Scope
# A lokális scope azon környezet, amely egy adott blokkra, például egy függvényre korlátozódik. A függvényen belül definiált változók csak a függvényen belül érhetők el.

# Példa:
def my_function():
    y = 5  # Lokális változó
    print(y)  # Elérhető itt

my_function()  # Output: 5
print(y)  # Hiba: y nem elérhető itt

# 3. Globális és Lokális Változók Ütközése
# Ha ugyanazzal a névvel rendelkező változót definiálsz a globális és a lokális scope-ban, a lokális változó "árnyékolja" a globális változót, ami azt jelenti, hogy a lokális scope-ban a globális változó értéke nem elérhető.

# Példa:
x = 10  # Globális változó

def my_function():
    x = 5  # Lokális változó, amely árnyékolja a globális x-et
    print(x)  # Output: 5

my_function()
print(x)  # Output: 10


# 4. A global Kulcsszó Használata
# A global kulcsszó használatával a lokális scope-ban módosíthatod a globális változó értékét.

# Példa:
x = 10  # Globális változó

def modify_global():
    global x  # A globális x változó használata
    x = 20

modify_global()
print(x)  # Output: 20

# 5. A nonlocal Kulcsszó Használata
# A nonlocal kulcsszó lehetővé teszi, hogy módosítsd egy külső (nem globális) változó értékét egy belső függvényből.

# Példa:
def outer_function():
    x = 10  # Külső scope-ban definiált változó

    def inner_function():
        nonlocal x  # Az outer_function x változójának módosítása
        x = 20

    inner_function()
    print(x)  # Output: 20

outer_function()


# Összegzés
# Globális Scope: A program egészében elérhető változók és függvények.
# Lokális Scope: Olyan környezet, amely egy adott blokkra, például egy függvényre korlátozódik.
# Árnyékolás: Ha egy lokális változó azonos nevű, mint egy globális változó, a lokális változó felülírja a globális változót a lokális scope-on belül.
# global és nonlocal kulcsszavak: Ezek segítségével módosíthatod a globális és a külső scope-ban lévő változókat a megfelelő scope-on belül.