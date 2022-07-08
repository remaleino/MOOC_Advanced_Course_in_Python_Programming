from queue import Empty


class Henkilo:
    def __init__(self, nimi: str):
        self._nimi = nimi
        self._numerot = []
        self._osoite = None

    def lisaa_numero(self, num: str):
        self._numerot.append(num)

    def lisaa_osoite(self, o: str):
        self._osoite = o

    def nimi(self):
        return self._nimi

    def numerot(self):
        return self._numerot

    def osoite(self):
        return self._osoite


class Puhelinluettelo:
    def __init__(self):
        self.__henkilot = {}

    def lisaa_numero(self, nimi: str, numero: str):
        if not nimi in self.__henkilot:
            self.__henkilot[nimi] = Henkilo(nimi)
        self.__henkilot[nimi].lisaa_numero(numero)

    def lisaa_osoite(self, nimi: str, o: str):
        if not nimi in self.__henkilot:
            self.__henkilot[nimi] = Henkilo(nimi)
        self.__henkilot[nimi].lisaa_osoite(o)

    def tiedot(self, nimi: str):
        if not nimi in self.__henkilot:
            return None
        return self.__henkilot[nimi]

    def kaikki_tiedot(self):
        return self.__henkilot


class PuhelinluetteloSovellus:
    def __init__(self):
        self.__luettelo = Puhelinluettelo()

    def ohje(self):
        print("komennot: ")
        print("0 lopetus")
        print("1 numeron lisäys")
        print("2 haku")
        print("3 osoitteen lisäys")

    def numeron_lisays(self):
        nimi = input("nimi: ")
        numero = input("numero: ")
        self.__luettelo.lisaa_numero(nimi, numero)

    def haku(self):
        nimi = input("nimi: ")
        olio = self.__luettelo.tiedot(nimi)
        try:
            if not olio.numerot():
                raise ValueError
            for numero in olio.numerot():
                print(numero)
        except:
            print("numero ei tiedossa")
        try:
            if olio.osoite() == None:
                raise ValueError
            print(olio.osoite())
        except:
            print("osoite ei tiedossa")

    def osoitteen_lisays(self):
        nimi = input("nimi: ")
        osoite = input("osoite: ")
        self.__luettelo.lisaa_osoite(nimi, osoite)

    def suorita(self):
        self.ohje()
        while True:
            print("")
            komento = input("komento: ")
            if komento == "0":
                break
            elif komento == "1":
                self.numeron_lisays()
            elif komento == "2":
                self.haku()
            elif komento == "3":
                self.osoitteen_lisays()
            else:
                self.ohje()


sovellus = PuhelinluetteloSovellus()
sovellus.suorita()
