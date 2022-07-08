def poista_pienemmat(luvut: list, raja: int):
    return [alkio for alkio in luvut if alkio >= raja]


if __name__ == "__main__":
    lukuja = [1, 65, 32, -6, 9, 11]
    print(poista_pienemmat(lukuja, 10))

    print(poista_pienemmat([-4, 7, 8, -100], 0))
