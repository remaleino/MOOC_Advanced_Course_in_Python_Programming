# TEE RATKAISUSI TÄHÄN:
import re


def on_viikonpaiva(merkkijono: str):
    if re.search("ma|ti|ke|to|pe|la|su", merkkijono):
        return True
    return False


def kaikki_vokaaleja(merkkijono: str):
    if len(merkkijono) == len(re.findall("[aeuioåöäy]", merkkijono)):
        return True
    return False


def kellonaika(merkkijono: str):
    if re.match("[0-1][0-9]:[0-5][0-9]:[0-5][0-9]|[2][0-4]:[0-5][0-9]:[0-5][0-9]", merkkijono):
        return True
    return False


if __name__ == "__main__":
    print(kellonaika("12:43:01"))
    print(kellonaika("AB:01:CD"))
    print(kellonaika("17:59:59"))
    print(kellonaika("33:66:77"))
