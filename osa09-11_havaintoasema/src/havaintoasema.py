# TEE RATKAISUSI TÄHÄN:
class Havaintoasema:
    def __init__(self, nimi: str):
        self.__nimi = nimi
        self.__lista = []

    def lisaa_havainto(self, havainto: str):
        self.__lista.append(havainto)

    def viimeisin_havainto(self):
        if bool(self.__lista):
            return self.__lista[-1]
        return ""

    def havaintojen_maara(self):
        return len(self.__lista)

    def __str__(self):
        return f"{self.__nimi}, {self.havaintojen_maara()} havaintoa"


if __name__ == "__main__":
    asema = Havaintoasema("Kumpula")
    asema.lisaa_havainto("Sadetta 10mm")
    asema.lisaa_havainto("Aurinkoista")
    print(asema.viimeisin_havainto())

    asema.lisaa_havainto("Ukkosta")
    print(asema.viimeisin_havainto())

    print(asema.havaintojen_maara())
    print(asema)
