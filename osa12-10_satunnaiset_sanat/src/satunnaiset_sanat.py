from random import choices


def sanageneraattori(kirjaimet: str, pituus: int, maara: int):
    i = 0
    while i < maara:
        yield "".join(choices(kirjaimet, k=pituus))
        i += 1


if __name__ == "__main__":
    sanagen = sanageneraattori("abcdefg", 3, 5)
    for sana in sanagen:
        print(sana)
