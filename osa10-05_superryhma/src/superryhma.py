# TEE RATKAISUSI TÄHÄN:
class SuperSankari:
    def __init__(self, nimi: str, supervoimat: str):
        self.nimi = nimi
        self.supervoimat = supervoimat

    def __str__(self):
        return f'{self.nimi}, superkyvyt: {self.supervoimat}'


class SuperRyhma:
    def __init__(self, nimi: str, kotipaikka: str):
        self._nimi = nimi
        self._kotipaikka = kotipaikka
        self._jasenet = []

    def nimi(self):
        return self._nimi

    def kotipaikka(self):
        return self._kotipaikka

    def lisaa_jasen(self, ss: SuperSankari):
        self._jasenet.append(ss)

    def tulosta_ryhma(self):
        print(f"{self._nimi}, {self._kotipaikka}\nJäsenet:")
        for r in self._jasenet:
            print(r)


if __name__ == "__main__":
    supermiekkonen = SuperSankari(
        "Supermiekkonen", "Supernopeus, supervoimakkuus")
    nakymaton = SuperSankari("Näkymätön Makkonen", "Näkymättömyys")
    ryhma_z = SuperRyhma("Ryhmä Z", "Kälviä")

    ryhma_z.lisaa_jasen(supermiekkonen)
    ryhma_z.lisaa_jasen(nakymaton)
    ryhma_z.tulosta_ryhma()
