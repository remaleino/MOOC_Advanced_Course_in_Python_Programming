# TEE RATKAISUSI TÄHÄN:
class Alkio:
    """ Luokka mallintaa yhtä alkiota binääripuussa """

    def __init__(self, arvo, vasen_lapsi: 'Alkio' = None, oikea_lapsi: 'Alkio' = None):
        self.arvo = arvo
        self.vasen_lapsi = vasen_lapsi
        self.oikea_lapsi = oikea_lapsi


def suurin_alkio(juuri: Alkio):
    suurin = juuri.arvo
    if juuri.vasen_lapsi is not None:
        suurin = max(suurin, suurin_alkio(juuri.vasen_lapsi))
    if juuri.oikea_lapsi is not None:
        suurin = max(suurin, suurin_alkio(juuri.oikea_lapsi))
    return suurin


if __name__ == "__main__":
    puu = Alkio(3)

    puu.vasen_lapsi = Alkio(5)
    puu.vasen_lapsi.vasen_lapsi = Alkio(7)
    puu.vasen_lapsi.oikea_lapsi = Alkio(10)
    puu.vasen_lapsi.oikea_lapsi.vasen_lapsi = Alkio(3)
    puu.oikea_lapsi = Alkio(13)
    puu.oikea_lapsi.oikea_lapsi = Alkio(6)
    puu.oikea_lapsi.oikea_lapsi.vasen_lapsi = Alkio(11)
    print(suurin_alkio(puu))
