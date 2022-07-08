# TEE RATKAISUSI TÄHÄN:
def vokaalilla_alkavat(sanat: list):
    return [a for a in sanat if a[0].lower() in "aeiouyäö"]


if __name__ == "__main__":
    klista = ["auto", "mopo", "Etana", "kissa", "Koira", "OMENA", "appelsiini"]
    for vok in vokaalilla_alkavat(klista):
        print(vok)
