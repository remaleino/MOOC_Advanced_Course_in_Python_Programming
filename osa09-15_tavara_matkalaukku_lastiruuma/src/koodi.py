# Tee ratkaisusi tähän:
class Tavara:
    def __init__(self, nimi: str, paino: int):
        self.__nimi = nimi
        self.__paino = paino

    def nimi(self):
        return self.__nimi

    def paino(self):
        return self.__paino

    def __str__(self):
        return f"{self.__nimi} ({self.__paino} kg)"


class Matkalaukku:
    def __init__(self, mp: int):
        self.__ml = []
        self.__mp = mp

    def lisaa_tavara(self, tavara: Tavara):
        if self.__mt_kelpaa(tavara.paino()):
            self.__ml.append(tavara)

    def __mt_kelpaa(self, paino: int):
        if (self.__yht_s() + paino) <= self.__mp:
            return True
        return False

    def tulosta_tavarat(self):
        for rivi in self.__ml:
            print(rivi)

    def paino(self):
        return self.__yht_s()

    def raskain_tavara(self):
        if not bool(self.__ml):
            return None
        l = [self.__ml[-1]]
        for rivi in self.__ml:
            if rivi.paino() >= l[0].paino():
                l[0] = rivi
        return l[0]

    def __str__(self):
        return f"{len(self.__ml)} {self.__huolto(len(self.__ml))} ({self.__yht_s()} kg)"

    def __huolto(self, i: int):
        if i == 1:
            return "tavara"
        return "tavaraa"

    def __yht_s(self):
        return sum([a.paino() for a in self.__ml])


class Lastiruuma:
    def __init__(self, mp: int):
        self.__ml = []
        self.__mp = mp

    def lisaa_matkalaukku(self, matkalaukku: Matkalaukku):
        if self.__mt_kelpaa(matkalaukku.paino()):
            self.__ml.append(matkalaukku)

    def __mt_kelpaa(self, paino: int):
        if (self.__yht_s() + paino) <= self.__mp:
            return True
        return False

    def tulosta_tavarat(self):
        for rivi in self.__ml:
            rivi.tulosta_tavarat()

    def __str__(self):
        return f"{len(self.__ml)} {self.__huolto(len(self.__ml))}, tilaa {self.__mp - self.__yht_s()} kg"

    def __huolto(self, i: int):
        if i == 1:
            return "matkalaukku"
        return "matkalaukkua"

    def __yht_s(self):
        return sum([a.paino() for a in self.__ml])


if __name__ == "__main__":
    kirja = Tavara("Aapiskukko", 2)
    puhelin = Tavara("Nokia 3210", 1)
    tiiliskivi = Tavara("Tiiliskivi", 4)

    adan_laukku = Matkalaukku(10)
    adan_laukku.lisaa_tavara(kirja)
    adan_laukku.lisaa_tavara(puhelin)

    pekan_laukku = Matkalaukku(10)
    pekan_laukku.lisaa_tavara(tiiliskivi)

    lastiruuma = Lastiruuma(1000)
    lastiruuma.lisaa_matkalaukku(adan_laukku)
    lastiruuma.lisaa_matkalaukku(pekan_laukku)

    print("Ruuman matkalaukuissa on seuraavat tavarat:")
    lastiruuma.tulosta_tavarat()
