# TEE RATKAISUSI TÄHÄN:
class Lottorivi:
    def __init__(self, k: int, llista: list):
        self.k = k
        self.lista = llista

    def osumien_maara(self, pelattu_rivi: list):
        return len([a for a in pelattu_rivi if a in self.lista])

    def osumat_paikoillaan(self, pelattu_rivi: list):
        return [a if a in self.lista else -1 for a in pelattu_rivi]


if __name__ == "__main__":
    oikea = Lottorivi(8, [1, 2, 3, 10, 20, 30, 33])
    oma_rivi = [1, 4, 7, 10, 11, 20, 30]

    print(oikea.osumat_paikoillaan(oma_rivi))
