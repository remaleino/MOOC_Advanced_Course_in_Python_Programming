# Tee ratkaisusi tähän:
class Kello:
    def __init__(self, h: int, m: int, s: int):
        self.h = h
        self.m = m
        self.s = s
    def aseta(self, h: int, m:int):
        self.h = h
        self.m = m
        self.s = 0
    def tick(self):
        if self.h == 23 and self.m == 59 and self.s == 59:
            self.h = 0
            self.m = 0
            self.s = 0
        elif self.m == 59 and self.s == 59:
            self.h +=1
            self.m = 0
            self.s = 0
        elif self.s == 59:
            self.s = 0
            self.m += 1
        else:
            self.s +=1
    def __str__(self):
        tu = self.h
        mi = self.m
        se = self.s
        if self.s < 10:
            se = "0"+str(se)
        if self.m < 10:
            mi = "0"+str(mi)
        if self.h < 10:
            tu = "0"+str(tu)
        return f"{tu}:{mi}:{se}"
if __name__ == "__main__":
    kello = Kello(23, 59, 55)
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)

    kello.aseta(12, 5)
    print(kello)