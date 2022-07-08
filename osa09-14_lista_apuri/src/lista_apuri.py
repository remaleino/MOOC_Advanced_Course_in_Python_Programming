# TEE RATKAISUSI TÄHÄN:
class ListaApuri:
    @classmethod
    def suurin_frekvenssi(self, lista: list):
        sa = {}
        for a in lista:
            if a not in sa:
                sa[a] = 0
            if a in sa:
                sa[a] += 1
        return max(sa, key=sa.get)

    @classmethod
    def tuplia(self, lista: list):
        sa = {}
        for a in lista:
            if a not in sa:
                sa[a] = 0
            if a in sa:
                sa[a] += 1
        return len(dict(filter(lambda k: k[1] > 1, sa.items())))


if __name__ == "__main__":
    luvut = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListaApuri.suurin_frekvenssi(luvut))
    print(ListaApuri.tuplia(luvut))
