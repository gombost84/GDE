class LegiTarsasag:

    def __init__(self, nev):

        self.nev = nev
        self.jaratok = []

    def jarat_hozzaadasa(self, jarat):

        self.jaratok.append(jarat)

    def __str__(self):

        jaratok_print = []

        for jarat in self.jaratok:
            jaratok_print.append(jarat.jarat_informacio())

        return "\n".join(jaratok_print)
