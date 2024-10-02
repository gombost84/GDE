from LegiTarsasag import LegiTarsasag


if __name__ == '__main__':

    RyanAir = LegiTarsasag("RyanAir")
    RyanAir.belfoldihozzadasa(1000, 50, 300, "Debrecen")
    RyanAir.nemzetkozihozzaadasa(10000, 200, 400, "London")

    print(vars(RyanAir.belfoldijaratok[0]))
    print(RyanAir.belfoldijaratok[0].jaratszam)

    print(vars(RyanAir.nemzetkozijaratok[0]))
    print(RyanAir.nemzetkozijaratok[0].jaratszam)
