# tee ratkaisu tänne
def  pienin_keskiarvo(henkilo1: dict, henkilo2: dict, henkilo3: dict):
    def lt(h: dict):
        summa = 0
        for arvo in h.values():
            if type(arvo) == int:
                summa += arvo
        return summa
    if lt(henkilo1) < lt(henkilo2) and lt(henkilo1) < lt(henkilo3):
        return henkilo1
    elif lt(henkilo2) < lt(henkilo1) and lt(henkilo2) < lt(henkilo3):
        return henkilo2
    else:
        return henkilo3


    

if __name__ == "__main__":
    henkilo1 = {"nimi": "Keijo", "tulos1": 2, "tulos2": 3, "tulos3": 3}
    henkilo2 = {"nimi": "Reijo", "tulos1": 5, "tulos2": 1, "tulos3": 8}
    henkilo3 = {"nimi": "Veijo", "tulos1": 3, "tulos2": 1, "tulos3": 1}

    print(pienin_keskiarvo(henkilo1, henkilo2, henkilo3))
