from functools import reduce


class Suoritus:
    def __init__(self, kurssi: str, arvosana: int, opintopisteet: int):
        self.kurssi = kurssi
        self.arvosana = arvosana
        self.opintopisteet = opintopisteet

    def __str__(self):
        return f"{self.kurssi} ({self.opintopisteet} op) arvosana {self.arvosana}"


def kaikkien_opintopisteiden_summa(lista: list):
    return reduce(lambda summa, a: a.opintopisteet + summa, lista, 0)


def hyvaksyttyjen_opintopisteiden_summa(lista: list):
    return reduce(lambda summa, a: a.opintopisteet + summa, list(filter(lambda a: a.arvosana > 0, lista)), 0)


def keskiarvo(lista: list):
    return (reduce(lambda summa, a: a.arvosana + summa, filter(lambda x: x.arvosana > 0, lista), 0)/len(list(filter(lambda x: x.arvosana > 0, lista))))


if __name__ == "__main__":
    s1 = Suoritus("Ohjelmoinnin perusteet", 5, 5)
    s2 = Suoritus("Ohjelmoinnin jatkokutssi", 0, 4)
    s3 = Suoritus("Tietorakenteet ja algoritmit", 3, 10)
    summa = keskiarvo([s1, s2, s3])
    print(summa)
