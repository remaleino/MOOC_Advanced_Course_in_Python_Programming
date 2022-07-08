# TEE RATKAISUSI TÄHÄN:
class Paivays:
    def __init__(self, d: int, m: int, y: int):
        self.d = d
        self.m = m
        self.y = y

    def __luku(self, d: int, m: int, y: int):
        m = m + (y*12)
        d = d + (m * 30)
        return d

    def __eq__(self, toinen):
        p1 = self.__luku(self.d, self.m, self.y)
        p2 = self.__luku(toinen.d, toinen.m, toinen.y)
        if p1 == p2:
            return True
        return False

    def __ne__(self, toinen):
        p1 = self.__luku(self.d, self.m, self.y)
        p2 = self.__luku(toinen.d, toinen.m, toinen.y)
        if p1 != p2:
            return True
        return False

    def __lt__(self, toinen):
        p1 = self.__luku(self.d, self.m, self.y)
        p2 = self.__luku(toinen.d, toinen.m, toinen.y)
        if p1 < p2:
            return True
        return False

    def __gt__(self, toinen):
        p1 = self.__luku(self.d, self.m, self.y)
        p2 = self.__luku(toinen.d, toinen.m, toinen.y)
        if p1 > p2:
            return True
        return False

    def __add__(self, i: int):
        p1 = self.__luku(self.d, self.m, self.y)
        p1 += i
        d = p1 % 30
        m = ((p1 - d) // 30) % 12
        y = (((p1 - d) // 30) - m) // 12
        return Paivays(d, m, y)

    def __sub__(self, toinen):
        p1 = self.__luku(self.d, self.m, self.y)
        p2 = self.__luku(toinen.d, toinen.m, toinen.y)
        return abs(p1 - p2)

    def __str__(self):
        return(f"{self.d}.{self.m}.{self.y}")


if __name__ == "__main__":
    p1 = Paivays(4, 10, 2020)
    p2 = Paivays(2, 11, 2020)
    p3 = Paivays(28, 12, 1985)

    print(p2-p1)
    print(p1-p2)
    print(p1-p3)
