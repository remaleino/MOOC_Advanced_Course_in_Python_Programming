# TEE RATKAISUSI TÄHÄN:
def hinta_alle_4_euroa(tuote):
    return tuote[1] < 4


def hae(tuotteet: list, kriteeri: callable):
    return [a for a in tuotteet if kriteeri(a) == True]


if __name__ == "__main__":
    tuotteet = [("banaani", 5.95, 12), ("omena", 3.95, 3), ("appelsiini",
                                                            4.50, 2), ("vesimeloni", 4.95, 22), ("Kaali", 0.99, 1)]
    for tuote in hae(tuotteet, hinta_alle_4_euroa):
        print(tuote)
