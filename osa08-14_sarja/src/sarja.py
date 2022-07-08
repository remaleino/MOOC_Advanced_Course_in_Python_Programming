# Tee ratkaisusi tähän:
class Sarja:
    def __init__(self, nimi:str, kaudet: int, genre: list):
        self.nimi = nimi
        self.kaudet = kaudet
        self.genre = genre
        self.arvosanat = []
    def arvostele(self, arvosana:int):
        self.arvosanat.append(arvosana)
    def __str__(self):
        arvostelut = "ei arvosteluja"
        genret = ", ".join(self.genre)
        if len(self.arvosanat) != 0:
            keskiarvo = "{:.1f}".format(sum(self.arvosanat) / len(self.arvosanat))
            arvostelut = f"arvosteluja {len(self.arvosanat)}, keskiarvo {keskiarvo} pistettä"
        return(f"{self.nimi} ({self.kaudet} esityskautta)\ngenret: {genret}\n{arvostelut}")
def arvosana_vahintaan(arvosana: float, sarjat: list):
    return [alkio for alkio in sarjat if (sum(alkio.arvosanat)/len(alkio.arvosanat)) > arvosana]
def sisaltaa_genren(genre: str, sarjat: list):
    return [alkio for alkio in sarjat if genre in alkio.genre]
if __name__ == "__main__":
    dexter = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    print(dexter)