# TEE RATKAISUSI TÄHÄN:
class Pankkitili:
    def __init__(self, nimi: str, tn: str, saldo: int):
        self.__nimi = nimi
        self.__tn = tn
        self.__saldo = saldo

    def __palvelumaksu(self):
        self.__saldo -= (self.__saldo * 0.01)

    def talleta(self, summa: float):
        self.__saldo += summa
        self.__palvelumaksu()

    def nosta(self, summa: float):
        self.__saldo -= summa
        self.__palvelumaksu()

    @property
    def saldo(self):
        return self.__saldo


if __name__ == "__main__":
    tili = Pankkitili("Raimo Rahakas", "12345-6789", 1000)
    tili.nosta(100)
    print(tili.saldo)
    tili.talleta(100)
    print(tili.saldo)
