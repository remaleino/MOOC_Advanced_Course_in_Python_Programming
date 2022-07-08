# Tee ratkaisusi tähän:
class Sekuntikello:
    def __init__(self):
        self.sekunnit = 0
        self.minuutit = 0
    def tick(self):
        if self.minuutit == 59 and self.sekunnit == 59:
            self.minuutit = 0
            self.sekunnit = 0
        elif self.sekunnit == 59:
            self.sekunnit = 0
            self.minuutit += 1
        else:
            self.sekunnit +=1
    def __str__(self):
        s = self.sekunnit
        m = self.minuutit
        if self.sekunnit < 10:
            s = "0"+str(s)
        if self.minuutit < 10:
            m = "0"+str(m)
        return f"{m}:{s}"
if __name__ == "__main__":
    kello = Sekuntikello()
    for i in range(62):
        print(kello)
        kello.tick()