# tee ratkaisu tänne
def rivien_summat(matriisi: list):
    for i in matriisi:
        summa = sum(i)
        i.append(summa)

if __name__ == "__main__":
    matriisi = [[1, 2], [3, 4]]
    rivien_summat(matriisi)
    print(matriisi)