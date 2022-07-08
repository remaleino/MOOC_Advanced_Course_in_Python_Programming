# TEE RATKAISUSI TÄHÄN:
def suodata_kielletyt(merkkijono: str, kielletyt: str):
    return "".join([a for a in merkkijono if a not in kielletyt])


if __name__ == "__main__":
    lause = "Suo! kuokka, ja python: hieno yhdistelmä!??!?!"
    suodatettu = suodata_kielletyt(lause, "!?:,.")
    print(suodatettu)
