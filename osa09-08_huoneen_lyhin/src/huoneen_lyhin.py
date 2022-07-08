# TEE RATKAISUSI TÄHÄN:
class Henkilo:
    def __init__(self, nimi: str, pituus: int):
        self.nimi = nimi
        self.pituus = pituus

    def __str__(self):
        return self.nimi


class Huone:
    def __init__(self):
        self.lista = []

    def lisaa(self, henkilo: Henkilo):
        self.lista.append(henkilo)

    def on_tyhja(self):
        return not bool(self.lista)

    def lyhin(self):
        if not bool(self.lista):
            return None
        for alkio in self.lista:
            if alkio.pituus == min(a.pituus for a in self.lista):
                return alkio

    def poista_lyhin(self):
        if not bool(self.lista):
            return None
        i = self.lista.index(self.lyhin())
        return self.lista.pop(i)

    def tulosta_tiedot(self):
        print(
            f"Huoneessa {len(self.lista)} henkilöä, yhteispituus {sum([a.pituus for a in self.lista])} cm")
        for rivi in self.lista:
            print(f"{rivi.nimi} ({rivi.pituus} cm)")


if __name__ == "__main__":
    huone = Huone()

    huone.lisaa(Henkilo("Lea", 183))
    huone.lisaa(Henkilo("Kenya", 182))
    huone.lisaa(Henkilo("Nina", 172))
    huone.lisaa(Henkilo("Auli", 186))
    huone.tulosta_tiedot()

    print()

    poistettu = huone.poista_lyhin()
    print(f"Otettiin huoneesta {poistettu.nimi}")

    print()

    huone.tulosta_tiedot()
