
class Jarat():

    import datetime

    def __init__(self, jaratszam: int = 0, celallomas: str = "",
                 datumok: list[datetime.datetime] = []):

        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.datumok = datumok
