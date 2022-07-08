# tee ratkaisusi tänne
import json


class Pelaaja():
    def __init__(self, nimi: str, kans: str, syottoja: int, maaleja: int, penal: int, joukkue: str, peleja: int):
        self.nimi = nimi
        self.kans = kans
        self.syottoja = syottoja
        self.maaleja = maaleja
        self.penal = penal
        self.joukkue = joukkue
        self.peleja = peleja
        self._pisteet = syottoja + maaleja

    def __str__(self):
        return(f"{self.nimi:21}{self.joukkue}{self.maaleja:>4} +{self.syottoja:>3} ={self._pisteet:>4}")


class Pelaajat():
    def __init__(self):
        self.lista = []

    def lisaa_tiedot(self, tiedosto: str):
        try:
            with open(tiedosto) as t:
                data = t.read()
            tiedot = json.loads(data)
            for a in tiedot:
                self.lisaa_pelaaja(Pelaaja(
                    a["name"], a["nationality"], a["assists"], a["goals"], a["penalties"], a["team"], a["games"]))
        except:
            raise ValueError
        finally:
            print(f"luettiin {len(self.lista)} pelaajan tiedot")

    def lisaa_pelaaja(self, pelaaja: Pelaaja):
        self.lista.append(pelaaja)

    def hae_pelaaja(self, nimi: str):
        for a in self.lista:
            if a.nimi == nimi:
                return a

    def hae_joukkueet(self):
        return sorted(set([a.joukkue for a in self.lista]))

    def hae_maat(self):
        return sorted(set([a.kans for a in self.lista]))

    def hae_joukkueen_pelaajat(self, joukkue: str):
        return sorted(list(filter(lambda a: a.joukkue == joukkue, self.lista)), key=lambda x: x._pisteet, reverse=True)

    def hae_maan_pelaajat(self, maa: str):
        return sorted(list(filter(lambda a: a.kans == maa, self.lista)), key=lambda x: x._pisteet, reverse=True)

    def eniten_pisteita(self, maara: int):
        return sorted(self.lista, key=lambda x: (x._pisteet, x.maaleja), reverse=True)[:maara]

    def eniten_maaleja(self, maara: int):
        return sorted(sorted(self.lista, key=lambda x: x.peleja), key=lambda x: x.maaleja,  reverse=True)[:maara]


def main():
    pelaajat = Pelaajat()
    tiedosto = input("tiedosto: ")
    pelaajat.lisaa_tiedot(tiedosto)
    print("")
    print("komennot:")
    print("0 lopeta")
    print("1 hae pelaaja")
    print("2 joukkueet")
    print("3 maat")
    print("4 joukkueen pelaajat")
    print("5 maan pelaajat")
    print("6 eniten pisteitä")
    print("7 eniten maaleja")
    while True:
        print("")
        i = input("komento: ")
        if i == "0":
            break
        elif i == "1":
            nimi = input("nimi: ")
            print(pelaajat.hae_pelaaja(nimi))
            print("")
        elif i == "2":
            l = pelaajat.hae_joukkueet()
            for a in l:
                print(a)
        elif i == "3":
            l = pelaajat.hae_maat()
            for a in l:
                print(a)
        elif i == "4":
            joukkue = input("joukkue: ")
            l = pelaajat.hae_joukkueen_pelaajat(joukkue)
            print("")
            for a in l:
                print(a)
        elif i == "5":
            maa = input("maa: ")
            l = pelaajat.hae_maan_pelaajat(maa)
            print("")
            for a in l:
                print(a)
        elif i == "6":
            maara = input("kuinka monta: ")
            l = pelaajat.eniten_pisteita(int(maara))
            print("")
            for a in l:
                print(a)
        elif i == "7":
            maara = input("kuinka monta: ")
            l = pelaajat.eniten_maaleja(int(maara))
            print("")
            for a in l:
                print(a)


main()
