# TEE RATKAISUSI TÄHÄN:
class Raha:
    def __init__(self, eurot: int, sentit: int):
        self.__eurot = eurot
        self.__sentit = sentit

    def __luvut(self, a: int, b: int):
        if b < 10:
            b = b * 0.01
            return a+b
        elif b >= 10:
            return a + (b*0.01)

    def __str__(self):
        return '{:.2f} eur'.format(self.__luvut(self.__eurot, self.__sentit))

    def __eq__(self, toinen):
        l1 = self.__luvut(self.__eurot, self.__sentit)
        l2 = self.__luvut(toinen.__eurot, toinen.__sentit)
        if l1 == l2:
            return True
        return False

    def __ne__(self, toinen):
        l1 = self.__luvut(self.__eurot, self.__sentit)
        l2 = self.__luvut(toinen.__eurot, toinen.__sentit)
        if l1 != l2:
            return True
        return False

    def __lt__(self, toinen):
        l1 = self.__luvut(self.__eurot, self.__sentit)
        l2 = self.__luvut(toinen.__eurot, toinen.__sentit)
        if l1 < l2:
            return True
        return False

    def __gt__(self, toinen):
        l1 = self.__luvut(self.__eurot, self.__sentit)
        l2 = self.__luvut(toinen.__eurot, toinen.__sentit)
        if l1 > l2:
            return True
        return False

    def __add__(self, toinen):
        l1 = self.__luvut(self.__eurot, self.__sentit)
        l2 = self.__luvut(toinen.__eurot, toinen.__sentit)
        l3 = str(l1 + l2).split(".")
        if len(l3[1]) < 2:
            l3[1] += "0"
        return Raha(int(l3[0]), int(l3[1]))

    def __sub__(self, toinen):
        l1 = self.__luvut(self.__eurot, self.__sentit)
        l2 = self.__luvut(toinen.__eurot, toinen.__sentit)
        l3 = round(l1 - l2, 2)
        if l3 > 0:
            l3 = str(l3).split(".")
            if len(l3[1]) < 2:
                l3[1] += "0"
            return Raha(int(l3[0]), int(l3[1]))
        else:
            raise ValueError(f"negatiivinen tulos ei sallittu")


if __name__ == "__main__":
    raha1 = Raha(15, 95)
    raha2 = Raha(15, 95)
    print(raha1 + raha2)
