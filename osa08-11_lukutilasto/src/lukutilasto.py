# Tee ratkaisusi tähän:
class  Lukutilasto:
    def __init__(self):
        self.lukuja = 0
        self.summ = 0

    def lisaa_luku(self, luku:int):
        self.lukuja += 1
        self.summ += luku

    def lukujen_maara(self):
        return self.lukuja
    def summa(self):
        if self.lukuja != 0:
            return self.summ
        else:
            return 0
    def keskiarvo(self):
        if self.lukuja != 0:
            return self.summ / self.lukuja
        else:
            return 0
def main():
    print("Anna lukuja:")
    tilasto = Lukutilasto()
    paril = Lukutilasto()
    parit = Lukutilasto()
    while True:
        luku = input()
        if int(luku) != -1:
            tilasto.lisaa_luku(int(luku))
            if int(luku) %2== 0:
                paril.lisaa_luku(int(luku))
            else:
                parit.lisaa_luku(int(luku))
        else:
            print("Summa:", tilasto.summa())
            print("Keskiarvo:", tilasto.keskiarvo())
            print("Parillisten summa:", paril.summa())
            print("Parittomien summa:", parit.summa())
            break
main()