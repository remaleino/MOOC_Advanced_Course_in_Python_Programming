class Tehtava:
    vapaa_id = 0

    def __init__(self, kuvaus: str, koodari: str, tyomaara: int):
        self.kuvaus = kuvaus
        self.koodari = koodari
        self.tyomaara = tyomaara
        self.valmis = False
        Tehtava.vapaa_id += 1
        self.__id = Tehtava.vapaa_id

    @property
    def id(self):
        return self.__id

    def on_valmis(self):
        return self.valmis

    def merkkaa_valmiiksi(self):
        self.valmis = True

    def __str__(self):
        def onko_valmis():
            if self.valmis:
                return "VALMIS"
            else:
                return "EI VALMIS"
        return f"{self.__id}: {self.kuvaus} ({self.tyomaara} tuntia), koodari {self.koodari} {onko_valmis()}"


class Tilauskirja:
    def __init__(self):
        self._tk = []

    def lisaa_tilaus(self, kuvaus, koodari, tyomaara):
        self._tk.append(Tehtava(kuvaus, koodari, tyomaara))

    def kaikki_tilaukset(self):
        return self._tk

    def koodarit(self):
        return list(set([a.koodari for a in self._tk]))

    def merkkaa_valmiiksi(self, id: int):
        for r in self._tk:
            if r.id == id:
                r.merkkaa_valmiiksi()
                return
        raise ValueError

    def valmiit_tilaukset(self):
        return [a for a in self._tk if a.valmis == True]

    def ei_valmiit_tilaukset(self):
        return [a for a in self._tk if a.valmis == False]

    def koodarin_status(self, koodari: str):
        if koodari in self.koodarit():
            a = len([a for a in self.valmiit_tilaukset() if a.koodari == koodari])
            b = len([a for a in self.ei_valmiit_tilaukset()
                    if a.koodari == koodari])
            c = sum([a.tyomaara for a in self.valmiit_tilaukset()
                    if a.koodari == koodari])
            d = sum([a.tyomaara for a in self.ei_valmiit_tilaukset()
                    if a.koodari == koodari])
            return (a, b, c, d)
        raise ValueError


class T_Sovellus:
    def __init__(self):
        self.__luettelo = Tilauskirja()

    def ohje(self):
        print("komennot:")
        print("0 lopetus")
        print("1 lisää tilaus")
        print("2 listaa valmiit")
        print("3 listaa ei valmiit")
        print("4 merkitse tehtävä valmiiksi")
        print("5 koodarit")
        print("6 koodarin status")

    def l_tilaus(self):
        k = input("kuvaus: ")
        a = input("koodari ja työmääräarvio: ")
        try:
            a = a.split(" ")
            self.__luettelo.lisaa_tilaus(k, a[0], int(a[1]))
            print("lisätty!")
        except:
            print("virheellinen syöte")

    def v_suoritus(self):
        lista = self.__luettelo.valmiit_tilaukset()
        if lista:
            for i in lista:
                print(i)
        else:
            print("ei valmiita")

    def ev_suoritus(self):
        lista = self.__luettelo.ei_valmiit_tilaukset()
        if lista:
            for i in lista:
                print(i)

    def mv_suoritus(self):
        i = input("tunniste: ")
        try:
            self.__luettelo.merkkaa_valmiiksi(int(i))
            print("merkitty valmiiksi")
        except:
            print("virheellinen syöte")

    def k_tulosta(self):
        for r in self.__luettelo.koodarit():
            print(r)

    def s_suorita(self):
        n = input("koodari: ")
        try:
            t = self.__luettelo.koodarin_status(n)
            print(
                f"työt: valmiina {t[0]} ei valmiina {t[1]}, tunteja: tehty {t[2]} tekemättä {t[3]}")
        except:
            print("virheellinen syöte")

    def suorita(self):
        self.ohje()
        while True:
            print("")
            komento = input("komento: ")
            if komento == "0":
                break
            elif komento == "1":
                self.l_tilaus()
            elif komento == "2":
                self.v_suoritus()
            elif komento == "3":
                self.ev_suoritus()
            elif komento == "4":
                self.mv_suoritus()
            elif komento == "5":
                self.k_tulosta()
            elif komento == "6":
                self.s_suorita()
            else:
                self.ohje()


sovellus = T_Sovellus()
sovellus.suorita()
