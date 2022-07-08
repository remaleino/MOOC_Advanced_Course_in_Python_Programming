class Suoritus:
    def __init__(self, opiskelijan_nimi: str, kurssi: str, arvosana: int):
        self.opiskelijan_nimi = opiskelijan_nimi
        self.kurssi = kurssi
        self.arvosana = arvosana

    def __str__(self):
        return f"{self.opiskelijan_nimi}, arvosana kurssilta {self.kurssi} {self.arvosana}"


def hyvaksytyt(suoritukset: list):
    return list(filter(lambda x: x.arvosana > 0, suoritukset))


def suoritus_arvosanalla(suoritukset: list, arvosana: int):
    return list(filter(lambda x: x.arvosana == arvosana, suoritukset))


def kurssin_suorittajat(suoritukset: list, kurssi: str):
    l = list(map(lambda z: z.opiskelijan_nimi, filter(
        lambda x: x.kurssi == kurssi and x.arvosana > 0, suoritukset)))
    return sorted(l)


if __name__ == "__main__":
    s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
    s2 = Suoritus("Olivia Ohjelmoija", "Tietoliikenteen perusteet", 5)
    s3 = Suoritus("Pekka Python", "Tietoliikenteen perusteet", 0)
    s4 = Suoritus("Niilo Nörtti", "Tietoliikenteen perusteet", 3)

    for suoritus in kurssin_suorittajat([s1, s2, s3, s4], "Tietoliikenteen perusteet"):
        print(suoritus)
