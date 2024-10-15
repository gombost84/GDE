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

    def __str__(self):

        foglalasok_print = []

        for foglalas in self.foglalasok:
            foglalasok_print.append(f"{foglalas['nev']} foglalta a következő járatot: {foglalas['jarat'].jarat_informacio()}")

        return "\n".join(foglalasok_print)
