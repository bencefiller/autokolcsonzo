from Auto import Szemelyauto, Teherauto
from Autokolcsonzo import Autokolcsonzo

def main_menu():
    print("\n--- Autókölcsönző ---")
    print("1. Bérlések listázása")
    print("2. Autó bérlése")
    print("3. Bérlés lemondása")
    print("4. Kilépés")

def main():
    kolcsonzo = Autokolcsonzo("Példa Autókölcsönző")

    kolcsonzo.auto_hozzaad(Szemelyauto("ABC-123", "Toyota Corolla", 10000))
    kolcsonzo.auto_hozzaad(Teherauto("DEF-456", "Ford Transit", 15000))
    kolcsonzo.auto_hozzaad(Szemelyauto("GHI-789", "Opel Astra", 9000))
    kolcsonzo.auto_hozzaad(Teherauto("JKL-012", "Volkswagen Transporter", 14000))

    kolcsonzo.berel("ABC-123", "2025-06-20")
    kolcsonzo.berel("DEF-456", "2025-06-15")
    kolcsonzo.berel("GHI-789", "2025-06-12")
    kolcsonzo.berel("JKL-012", "2025-06-09")

    while True:
        main_menu()
        choice = input("Válassz egy műveletet: ")
        if choice == "1":
            print("Aktuális bérlések:")
            for r in kolcsonzo.listaz_berleseket():
                print("-", r)

        elif choice == "2":
            datum = input("Add meg a bérlés dátumát (pl. 2025-06-01): ")
            print("Elérhető autók ezen a napon:")
            for auto in kolcsonzo.foglalhato_autok(datum):
                print("-", auto.info())
            rendszam = input("Add meg az autó rendszámát: ")
            eredmeny = kolcsonzo.berel(rendszam, datum)
            if eredmeny == "mult":
                print("Nem lehet múltbeli dátumra foglalni.")
            elif eredmeny:
                print(f"Sikeres bérlés! Ár: {eredmeny} Ft")
            else:
                print("Az autó nem elérhető vagy már foglalt.")

        elif choice == "3":
            rendszam = input("Add meg a lemondandó autó rendszámát: ")
            datum = input("Add meg a lemondandó bérlés dátumát (pl. 2025-06-01): ")
            if kolcsonzo.lemond(rendszam, datum):
                print("Sikeres lemondás.")
            else:
                print("Hiba: Nem található ilyen bérlés.")

        elif choice == "4":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás.")

if __name__ == "__main__":
    main()
