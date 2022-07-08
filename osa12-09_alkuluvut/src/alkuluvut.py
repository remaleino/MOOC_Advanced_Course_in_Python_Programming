def alkuluvut():
    luku = 2

    def suodata(i):
        luku1 = 2
        for a in range(2, (i+2)):
            if a == (i+1):
                break
            if (i+1) % a == 0 and a != i:
                continue
            luku1 += 1
        if luku1 == (i+1):
            return luku1
        else:
            return suodata(i + 1)
    while True:
        yield luku
        luku = suodata(luku)


if __name__ == "__main__":
    luvut = alkuluvut()
    for i in range(4):
        print(next(luvut))
