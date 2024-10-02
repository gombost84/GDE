
class Jarat():

    def __init__(self, jaratszam: int, celallomas: str):

        self.jaratszam = jaratszam
        self.celallomas = celallomas


class BelfoldiJarat(Jarat):

    def __init__(self, jegyar: int, elerhetohelyek: int, *args):

        super().__init__(*args)
        self.jegyar = jegyar
        self.elerhetohelyek = elerhetohelyek


class NemzetKozijarat(Jarat):

    def __init__(self, jegyar: int, elerhetohelyek: int, *args):

        super().__init__(*args)
        self.jegyar = jegyar
        self.elerhetohelyek = elerhetohelyek


class LegiTarsasag():

    belfoldijaratok = []
    nemzetkozijaratok = []

    def __init__(self, nev: str):

        self.nev = nev

    def belfoldihozzadasa(self, *data):

        self.belfoldijaratok.append(BelfoldiJarat(*data))

    def nemzetkozihozzaadasa(self, *data):

        self.nemzetkozijaratok.append(NemzetKozijarat(*data))


if __name__ == '__main__':

    RyanAir = LegiTarsasag("RyanAir")
    RyanAir.belfoldihozzadasa(1000, 50, 300, "Debrecen")
    RyanAir.nemzetkozihozzaadasa(10000, 200, 400, "London")

    print(vars(RyanAir.belfoldijaratok[0]))
    print(RyanAir.belfoldijaratok[0].jaratszam)

    print(vars(RyanAir.nemzetkozijaratok[0]))
    print(RyanAir.nemzetkozijaratok[0].jaratszam)
