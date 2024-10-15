from Classes.JegyFoglalas import JegyFoglalas
from Classes.LegiTarsasag import LegiTarsasag
from Classes.BelfoldiJarat import BelfoldiJarat
from Classes.NemzetkoziJarat import NemzetkoziJarat


def felhasznaloi_felulet():
    jegyfoglalas_rendszer = JegyFoglalas()
    wizzair = LegiTarsasag("WizzAir")

    # Minta járatok hozzáadása
    belfoldi_jarat = BelfoldiJarat("101", "Budapest", 15000)
    nemzetkozi_jarat = NemzetkoziJarat("202", "London", 50000)
    wizzair.jarat_hozzaadasa(belfoldi_jarat)
    wizzair.jarat_hozzaadasa(nemzetkozi_jarat)

    while True:
        print("\n--- Repülőjegy Foglalási Rendszer ---")
        print("1. Járatok listázása")
        print("2. Jegy foglalása")
        print("3. Foglalás lemondása")
        print("4. Foglalások listázása")
        print("5. Kilépés")
        valasz = input("Válassz egy opciót: ")

        if valasz == "1":
            print("\nElérhető járatok:")
            wizzair.jaratok_listazasa()
        elif valasz == "2":
            nev = input("Add meg a neved: ")
            jaratszam = input("Add meg a foglalni kívánt járat számát: ")

            # Járat kiválasztása és típusának kezelése
            for jarat in wizzair.jaratok:
                if jarat.jaratszam == jaratszam:
                    if isinstance(jarat, BelfoldiJarat):
                        print(f"Belföldi járatra foglalsz: {jarat.celallomas}")
                    elif isinstance(jarat, NemzetkoziJarat):
                        print(f"Nemzetközi járatra foglalsz: {jarat.celallomas}")

                    jegyfoglalas_rendszer.foglalas(jarat, nev)
                    break
            else:
                print("Nincs ilyen járat.")
        elif valasz == "3":
            nev = input("Add meg a neved: ")
            jaratszam = input("Add meg a lemondani kívánt járat számát: ")
            jegyfoglalas_rendszer.foglalas_lemondasa(nev, jaratszam)
        elif valasz == "4":
            jegyfoglalas_rendszer.foglalasok_listazasa()
        elif valasz == "5":
            break
        else:
            print("Érvénytelen választás, próbáld újra.")


if __name__ == "__main__":
    felhasznaloi_felulet()