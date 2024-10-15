from Classes.Jarat import Jarat


class BelfoldiJarat(Jarat):

    def __init__(self, jaratszam, celallomas, jegyar):

        super().__init__(jaratszam, celallomas, jegyar)

    def jarat_informacio(self):

        return f"Belföldi Járat - {self.jaratszam}: {self.celallomas}, \
        Ár: {self.jegyar} Ft"
