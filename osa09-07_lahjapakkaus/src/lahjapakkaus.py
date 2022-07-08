# TEE RATKAISUSI TÄHÄN:
class Lahja:
    def __init__(self, nimi: str, paino: int):
        self.nimi = nimi
        self.paino = paino

    def __str__(self):
        return f"{self.nimi} ({self.paino} kg)"


class Pakkaus:
    def __init__(self):
        self.lista = []

    def lisaa_lahja(self, lahja: Lahja):
        self.lista.append(lahja)

    def yhteispaino(self):
        return sum([alkio.paino for alkio in self.lista])


if __name__ == "__main__":
    kirja = Lahja("Aapiskukko", 2)

    pakkaus = Pakkaus()
    pakkaus.lisaa_lahja(kirja)
    print(pakkaus.yhteispaino())

    cd_levy = Lahja("Pink Floyd: Dark side of the moon", 1)
    pakkaus.lisaa_lahja(cd_levy)
    print(pakkaus.yhteispaino())
