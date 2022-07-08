from math import sqrt


def neliojuuret(luvut: list):
    return [sqrt(alkio) for alkio in luvut]


if __name__ == "__main__":
    rivit = neliojuuret([1, 2, 3, 4])
    for rivi in rivit:
        print(rivi)
