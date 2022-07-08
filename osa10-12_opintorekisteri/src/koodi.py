class Kurssi:
    def __init__(self, nimi: str, arvosana: str, op: str):
        self.__nimi = nimi
        self._arvosana = arvosana
        self.__op = op

    def nimi(self):
        return self.__nimi

    def arvosana(self):
        return self._arvosana

    def set_a(self, a: str):
        self._arvosana = a

    def op(self):
        return self.__op


class Opintorekisteri:
    def __init__(self):
        self.__lista = {}

    def lisaa_kurssi(self, n: str, a: str, o: str):
        if not n in self.__lista:
            self.__lista[n] = Kurssi(n, a, o)
        if a > self.__lista[n].arvosana():
            self.__lista[n].set_a(a)

    def hae_suoritus(self, n: str):
        if n in self.__lista:
            return self.__lista[n]
        return None

    def tilastot(self):
        return self.__lista


class O_Sovellus:
    def __init__(self):
        self.__luettelo = Opintorekisteri()

    def ohje(self):
        print("1 lisää suoritus")
        print("2 hae suoritus")
        print("3 tilastot")
        print("0 lopetus")

    def l_suoritus(self):
        k = input("kurssi: ")
        a = input("arvosana: ")
        o = input("opintopisteet: ")
        self.__luettelo.lisaa_kurssi(k, a, o)

    def h_suoritus(self):
        k = input("kurssi: ")
        olio = self.__luettelo.hae_suoritus(k)
        if olio == None:
            print("ei suoritusta")
        else:
            print(f"{olio.nimi()} ({olio.op()} op) arvosana {olio.arvosana()}")

    def tilastot(self):
        l = self.__luettelo.tilastot()
        al = {"5": "", "4": "", "3": "", "2": "", "1": ""}
        s = sum([int(l[a].op()) for a in l])
        for a in l:
            print(a)
            if l[a].arvosana() in al:
                al[l[a].arvosana()] += "x"
        print(f"suorituksia {len(l)} kurssilta, yhteensä {s} opintopistettä")
        print(
            f"keskiarvo {round(((sum([int(l[a].arvosana()) for a in l]))/len(l)), 1)}")
        print("arvosanajakauma")
        for a in al:
            print(f"{a}: {al[a]}")

    def suorita(self):
        self.ohje()
        while True:
            print("")
            komento = input("komento: ")
            if komento == "0":
                break
            elif komento == "1":
                self.l_suoritus()
            elif komento == "2":
                self.h_suoritus()
            elif komento == "3":
                self.tilastot()
            else:
                self.ohje()


sovellus = O_Sovellus()
sovellus.suorita()
