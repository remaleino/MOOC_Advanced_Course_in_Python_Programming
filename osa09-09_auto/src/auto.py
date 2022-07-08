# TEE RATKAISUSI TÄHÄN:
class Auto:
    def __init__(self):
        self.__tankki = 0
        self.__km = 0

    def tankkaa(self):
        self.__tankki = 60

    def aja(self, km: int):
        for i in range(1, km+1):
            if self.__tankki == 0:
                break
            self.__tankki -= 1
            self.__km += 1

    def __str__(self):
        return f"Auto: ajettu {self.__km} km, bensaa {self.__tankki} litraa"


if __name__ == "__main__":
    auto = Auto()
    print(auto)
    auto.tankkaa()
    print(auto)
    auto.aja(20)
    print(auto)
    auto.aja(50)
    print(auto)
    auto.aja(10)
    print(auto)
    auto.tankkaa()
    auto.tankkaa()
    print(auto)
