import LegiTarsasag


if __name__ == '__main__':

    RyanAir = LegiTarsasag.LegiTarsasag("RyanAir")

    with open("adatok.txt", "r") as file:
        for line in file:
            x = line.split()
            if x[0] == "b":
                RyanAir.belfoldihozzadasa(x[1:])
            if x[0] == "n":
                RyanAir.nemzetkozihozzaadasa(x[1:])
