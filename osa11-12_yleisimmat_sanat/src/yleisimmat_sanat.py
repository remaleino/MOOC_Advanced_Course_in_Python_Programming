import string


def yleisimmat_sanat(tiedoston_nimi: str, raja: int):
    m = string.punctuation
    skirja = {}
    with open(tiedoston_nimi) as f:
        for line in f:
            line.strip()
            for a in line.split():
                s = a.lower()
                s = "".join([al for al in a if al not in m])
                if s not in skirja:
                    skirja[s] = 0
                skirja[s] += 1
    return {a: skirja[a] for a in skirja if skirja[a] >= raja}


if __name__ == "__main__":
    print(yleisimmat_sanat("comprehensions.txt", 3))
