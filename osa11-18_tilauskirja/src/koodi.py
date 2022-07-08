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


if __name__ == "__main__":
    t = Tilauskirja()
    t.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
    t.koodarin_status("JohnDoe")
