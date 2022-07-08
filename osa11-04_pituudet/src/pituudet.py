def pituudet(listat: list):
    return[len(alkio) for alkio in listat]


if __name__ == "__main__":
    listat = [[1, 2, 3, 4, 5], [324, -1, 31, 7], []]
    print(pituudet(listat))
