from Classes.JegyFoglalas import JegyFoglalas
from Classes.LegiTarsasag import LegiTarsasag
from Classes.BelfoldiJarat import BelfoldiJarat
from Classes.NemzetkoziJarat import NemzetkoziJarat


def felhasznaloi_felulet():

    jegyfoglalas_rendszer = JegyFoglalas()
    wizzair = LegiTarsasag("WizzAir")

    belfoldi_jarat = BelfoldiJarat("101", "Budapest", 15000)
    nemzetkozi_jarat = NemzetkoziJarat("202", "London", 50000)
    nemzetkozi_jarat2 = NemzetkoziJarat("303", "Madrid", 50000)

    wizzair.jarat_hozzaadasa(belfoldi_jarat)
    wizzair.jarat_hozzaadasa(nemzetkozi_jarat)
    wizzair.jarat_hozzaadasa(nemzetkozi_jarat2)

    jegyfoglalas_rendszer.foglalas(belfoldi_jarat, "Tamás")
    jegyfoglalas_rendszer.foglalas(belfoldi_jarat, "Zoltán")
    jegyfoglalas_rendszer.foglalas(nemzetkozi_jarat, "John")
    jegyfoglalas_rendszer.foglalas(nemzetkozi_jarat, "Peter")
    jegyfoglalas_rendszer.foglalas(nemzetkozi_jarat2, "José")
    jegyfoglalas_rendszer.foglalas(nemzetkozi_jarat2, "Julian")

    while True:

        print("\n--- Repülőjegy Foglalási Rendszer ---")
        print("1. Járatok listázása")
        print("2. Jegy foglalása")
        print("3. Foglalás lemondása")
        print("4. Foglalások listázása")
        print("5. Kilépés")

        valasz = input("Válassz egy opciót: ")

        match valasz:

            case "1":
                print("\nElérhető járatok:")
                print(wizzair)

            case "2":
                nev = input("Add meg a neved: ")
                jaratszam = input("Add meg a foglalni kívánt járat számát: ")

                for jarat in wizzair.jaratok:

                    if jarat.jaratszam == jaratszam:

                        if isinstance(jarat, BelfoldiJarat):
                            print(f"Belföldi járatra foglalsz: {jarat.celallomas}")

                        elif isinstance(jarat, NemzetkoziJarat):
                            print(f"Nemzetközi járatra foglalsz: {jarat.celallomas}")

                        jegyfoglalas_rendszer.foglalas(jarat, nev)
                        break

            case "3":
                nev = input("Add meg a neved: ")
                jaratszam = input("Add meg a lemondani kívánt járat számát: ")
                jegyfoglalas_rendszer.foglalas_lemondasa(nev, jaratszam)

            case "4":
                print(jegyfoglalas_rendszer)

            case "5":
                break

            case _:
                print("\nÉrvénytelen menüpont!")


if __name__ == "__main__":
    felhasznaloi_felulet()
