# TEE RATKAISUSI TÄHÄN:
def jarjesta_tuotantokausien_mukaan(alkiot: list):
    def tuot(a: dict):
        return a["kausia"]
    return sorted(alkiot, key=tuot)


if __name__ == "__main__":
    sarjat = [{"nimi": "Dexter", "pisteet": 8.6, "kausia": 9}, {"nimi": "Friends",
                                                                "pisteet": 8.9, "kausia": 10},  {"nimi": "Simpsons", "pisteet": 8.7, "kausia": 32}]

    for sarja in jarjesta_tuotantokausien_mukaan(sarjat):
        print(f"{sarja['nimi']}  {sarja['kausia']} tuotantokautta")
