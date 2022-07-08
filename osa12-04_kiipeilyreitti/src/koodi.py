class Kiipeilyreitti:
    def __init__(self, nimi: str, pituus: int, grade: str):
        self.nimi = nimi
        self.pituus = pituus
        self.grade = grade

    def __str__(self):
        return f"{self.nimi}, pituus {self.pituus} metriä, grade {self.grade}"


def pituuden_mukaan(reitit: list):
    def pituus(a: Kiipeilyreitti):
        return a.pituus
    return sorted(reitit, key=pituus, reverse=True)


def vaikeuden_mukaan(reitit: list):
    def vaikeus(a: Kiipeilyreitti):
        return (a.grade, a.pituus)
    return sorted(reitit, key=vaikeus, reverse=True)


if __name__ == "__main__":
    r1 = Kiipeilyreitti("Pieniä askelia", 13, "6A+")
    r2 = Kiipeilyreitti("Kantti", 38, "6A+")
    r3 = Kiipeilyreitti("Bukowski", 9, "6A+")
    vastaus = vaikeuden_mukaan([r1, r2, r3])

    reitit = [r1, r2, r3]

    for reitti in vaikeuden_mukaan(reitit):
        print(reitti)
