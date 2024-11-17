# main.py

import payroll_package

def main():
    # Lista a fizetésekről
    salaries = [3000, 4500, 5000, 6000, 3500, 4000]

    # Fizetések átlagának kiszámítása
    average_salary = payroll_package.calculate_average_salary(salaries)
    print(f"Az átlagos fizetés: {average_salary:.2f}")

    # Fizetések összegének kiszámítása
    total_salary = payroll_package.calculate_total_salary(salaries)
    print(f"A fizetések összege: {total_salary:.2f}")

if __name__ == "__main__":
    main()

# Magyarázat
# Csomag Struktúra: A csomagunknak van egy gyökér könyvtára (payroll_package), amely tartalmazza az __init__.py és payroll_utils.py fájlokat.
# __init__.py: Ez a fájl jelzi, hogy a payroll_package könyvtár egy csomag. Ebben a fájlban importáljuk a csomag moduljait, hogy könnyen hozzáférhetőek legyenek.
# payroll_utils.py: Ez a fájl tartalmazza a különböző bérszámfejtési műveleteket, mint például a fizetések átlagának és összegének kiszámítása.
# Csomag Használata: A main.py fájlban importáljuk a payroll_package csomagot és használjuk a benne lévő függvényeket.
# main() függvény: Ebben a függvényben meghívjuk a payroll_package modul függvényeit és kiírjuk az eredményeket.

# Összegzés
# A csomagok lehetővé teszik a kód szervezését és strukturálását, ami különösen hasznos nagyobb projektek esetén. A csomagok használata segít abban, hogy a kódunk tisztább és karbantarthatóbb legyen.