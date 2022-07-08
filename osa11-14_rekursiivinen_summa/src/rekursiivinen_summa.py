def summa(luku: int):

    if luku <= 1:
        return luku
    return luku + summa(luku - 1)


if __name__ == "__main__":
    tulos = summa(3)
    print(tulos)

    print(summa(5))
    print(summa(10))
