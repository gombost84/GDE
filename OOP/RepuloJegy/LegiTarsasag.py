import BelfoldiJarat
import NemzetkoziJarat


class LegiTarsasag():

    belfoldijaratok = []
    nemzetkozijaratok = []

    def __init__(self, nev: str):

        self.nev = nev

    def belfoldihozzadasa(self, data):

        self.belfoldijaratok.append(BelfoldiJarat(data))

    def nemzetkozihozzaadasa(self, data):

        self.nemzetkozijaratok.append(NemzetkoziJarat(data))
