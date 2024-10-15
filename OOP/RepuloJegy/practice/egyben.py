from abc import ABC, abstractmethod


class Jarat(ABC):

    def __init__(self, jaratszam, celallomas, jegyar):

        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar

    @abstractmethod
    def jarat_informacio(self):
        pass


class BelfoldiJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar):
        super().__init__(jaratszam, celallomas, jegyar)

    def jarat_informacio(self):
        return f"Belföldi Járat - {self.jaratszam}: {self.celallomas}, \
        Ár: {self.jegyar} Ft"


class NemzetkoziJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar):
        super().__init__(jaratszam, celallomas, jegyar)

    def jarat_informacio(self):
        return f"Nemzetközi Járat - {self.jaratszam}: {self.celallomas}, \
            Ár: {self.jegyar} Ft"


class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []

    def jarat_hozzaadasa(self, jarat):
        self.jaratok.append(jarat)

    def jaratok_listazasa(self):
        for jarat in self.jaratok:
            print(jarat.jarat_informacio())


class JegyFoglalas:
    def __init__(self):
        self.foglalasok = []

    def foglalas(self, jarat, nev):
        self.foglalasok.append({'nev': nev, 'jarat': jarat})
        print(f"{nev} foglalta a következő járatot: {jarat.jarat_informacio()}")
        return jarat.jegyar

    def foglalas_lemondasa(self, nev, jaratszam):
        for foglalas in self.foglalasok:
            if foglalas['nev'] == nev and \
              foglalas['jarat'].jaratszam == jaratszam:
                self.foglalasok.remove(foglalas)
                print(f"{nev} lemondta a {jaratszam} számú járatot.")
                return True
        print(f"Nincs ilyen foglalás: {nev} - {jaratszam}")
        return False

    def foglalasok_listazasa(self):
        if not self.foglalasok:
            print("Nincs aktuális foglalás.")
        else:
            for foglalas in self.foglalasok:
                print(f"{foglalas['nev']} foglalta a következő járatot: \
                      {foglalas['jarat'].jarat_informacio()}")


def felhasznaloi_felulet():
    jegyfoglalas_rendszer = JegyFoglalas()
    wizzair = LegiTarsasag("WizzAir")

    # Minta járatok hozzáadása
    belfoldi_jarat = BelfoldiJarat("101", "Debrecen", 15000)
    nemzetkozi_jarat = NemzetkoziJarat("202", "London", 50000)
    nemzetkozi_jarat = NemzetkoziJarat("303", "Madrid", 50000)
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