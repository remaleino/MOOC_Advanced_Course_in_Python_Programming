import pygame
import random


class Kolikko():
    def __init__(self, y):
        self.ovi = pygame.image.load("ovi.png")
        self.y = y
        self.x = random.randint((50+self.ovi.get_width()),
                                (853-100-self.ovi.get_width()))
        self.arvo = False

    def uus_sijainti(self):
        self.x = random.randint((50+self.ovi.get_width()),
                                (853-100-self.ovi.get_width()))
        self.arvo = False

    def kolikon_arvot(self):
        return (self.x, self.y)

    def onko_taskussa(self):
        return self.arvo

    def napataan(self):
        self.arvo = True


class Robotti():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.h_pituus = 18
        self.hyppy = False

    def hyppaa(self):
        if self.hyppy:
            if self.h_pituus >= -18:
                neg = 1
                if self.h_pituus < 0:
                    neg = -1
                self.y -= self.h_pituus**2*0.1*neg
                self.h_pituus -= 1
            else:
                self.hyppy = False
                self.h_pituus = 18

    def arvot(self):
        return (self.x, self.y)


class Hirvio():
    def __init__(self, y: int):
        self.ovi = pygame.image.load("ovi.png")
        self.x = random.randint((50+self.ovi.get_width()),
                                (853-100-self.ovi.get_width()))
        self.y = y
        self.nopeus = 1

    def uus_sijainti(self):
        self.x = random.randint((50+self.ovi.get_width()),
                                (853-100-self.ovi.get_width()))

    def liiku(self):
        self.x += self.nopeus
        if self.x >= 853-100-self.ovi.get_width() and self.nopeus > 0:
            self.nopeus = -self.nopeus
        if self.x <= 50+self.ovi.get_width() and self.nopeus < 0:
            self.nopeus = -self.nopeus

    def arvot(self):
        return (self.x, self.y)


class Salama():
    def __init__(self):
        self.a_x = random.randrange(602, 698)
        self.koord = [[self.a_x, 150]]
        self.pisteita = 30
        self.muodosta_pisteet()

    def muodosta_pisteet(self):
        y_s = 0
        x_s = 0
        for i in range(self.pisteita):
            x = random.randrange(-5, 5)
            y = random.randrange(5, 8)
            if y_s + y >= 99:
                self.koord.append(
                    [self.koord[i][0]+x, self.koord[i][1]+(99-y_s)])
                break
            if x_s + x <= 600-self.a_x or x_s + x >= 700-self.a_x:
                break
            y_s += y
            x_s += x
            self.koord.append([self.koord[i][0]+x, self.koord[i][1]+y])

    def uusi_isku(self):
        self.koord = [[self.a_x, 150]]
        self.muodosta_pisteet()

    def palauta_koord(self):
        return self.koord


class Peli():

    def __init__(self):
        pygame.init()
        self.n_leveys = 853
        self.n_korkeus = 480
        self.naytto = pygame.display.set_mode((self.n_leveys, self.n_korkeus))
        self.robo = pygame.image.load("robo.png")
        self.s_ovi = pygame.image.load("ovi.png")
        self.u_ovi = pygame.image.load("ovi.png")
        self.kolik = pygame.image.load("kolikko.png")
        self.hirv = pygame.image.load("hirvio.png")
        self.kello = pygame.time.Clock()
        self.lattia_y = 325+self.robo.get_height()
        self.robotti = Robotti(0, 325)
        self.kolikko = Kolikko(self.lattia_y-self.kolik.get_height()-2)
        self.hirvio = Hirvio(self.lattia_y-self.hirv.get_height())
        self.salama = Salama()
        self.vasemmalle = False
        self.oikealle = False
        self.ajastettu_tapahtuma = pygame.USEREVENT+1
        self.aseta_laskuri(5000)
        self.vaihto = True
        self.valikko = True
        self.peli = False
        self.pisteet = 0
        self.silmukka()

    def silmukka(self):
        while True:
            self.tutki_tapahtumat()
            if self.valikko:
                self.piirra_valikko()
            if self.peli:
                self.piirra_pelin_naytto()

    def piirra_valikko(self):
        self.naytto.fill((0, 0, 0))
        fontti_o = pygame.font.Font(pygame.font.get_default_font(), 50)
        fontti_t = pygame.font.Font(pygame.font.get_default_font(), 20)
        otsikko = fontti_o.render(
            "Not Alone in the Darkness", True, (255, 255, 255))
        teksti = ["An one lonely robot came to a haunted mansion",
                  "to collect all old treasures left by unnamed travelers.",
                  "It is hard to find treasures, when you are all alone in the darkness.",
                  "Or maybe not that alone...", "", "Use LEFT, UP, RIGHT to move the robot."]
        self.naytto.blit(otsikko, (self.n_leveys/2-otsikko.get_width()/2, 125))
        for i in range(1, len(teksti)+1):
            rivi = fontti_t.render(teksti[i-1], True, (255, 255, 255))
            self.naytto.blit(
                rivi, (self.n_leveys/2-rivi.get_width()/2, (175+i*20)))
        ala_o = fontti_t.render("Press ENTER to start.", True, (255, 255, 255))
        self.naytto.blit(ala_o, (self.n_leveys/2-ala_o.get_width()/2, 425))
        pygame.display.flip()
        self.kello.tick(60)

    def piirra_pelin_naytto(self):
        if self.oikealle and self.robotti.x <= self.n_leveys - self.robo.get_width()-2:
            self.robotti.x += 5
        if self.vasemmalle and self.robotti.x >= 2:
            self.robotti.x -= 5
        self.napattu_r()
        self.napattu_k(self.kolikko, self.robotti.x, self.robotti.y)
        if self.robotti.x >= self.n_leveys-100 and self.kolikko.onko_taskussa():
            self.pisteet += 1
            self.kolikko.uus_sijainti()
            self.hirvio.uus_sijainti()
            self.robotti.x = 0
        if self.vaihto:
            self.piirra_pimeys()
        else:
            self.piirra_salama_iskee()

    def piirra_salama_iskee(self):
        self.naytto.fill((255, 255, 255))
        fontti = pygame.font.Font(pygame.font.get_default_font(), 40)
        pygame.draw.rect(self.naytto, (0, 0, 0),
                         pygame.Rect(375, 175, 100, 150), 6)
        pygame.draw.rect(self.naytto, (0, 0, 0),
                         pygame.Rect(385, 185, 80, 130), 4)
        pisteet = fontti.render(
            f"{self.pisteet}", True, (0, 0, 0))
        self.naytto.blit(pisteet, (425-pisteet.get_width() /
                         2, 245-pisteet.get_height()/2))
        self.naytto.blit(
            self.s_ovi, (50, self.lattia_y-self.s_ovi.get_height()))
        self.naytto.blit(self.u_ovi, (self.n_leveys-100,
                         self.lattia_y-self.u_ovi.get_height()))

        def piirra_s(koord: list):
            for a in range(0, len(koord)):
                if a == len(koord)-1:
                    break
                pygame.draw.aaline(self.naytto, (0, 0, 0), [koord[a][0], koord[a][1]], [
                    koord[a+1][0], koord[a+1][1]], 3)
        piirra_s(self.salama.palauta_koord())
        pygame.draw.rect(self.naytto, (0, 0, 0),
                         pygame.Rect(600, 150, 100, 100), 4)
        pygame.draw.line(self.naytto, (0, 0, 0), (650, 150), (650, 249), 4)
        pygame.draw.line(self.naytto, (0, 0, 0), (600, 200), (699, 200), 4)
        self.naytto.blit(self.robo, (self.robotti.x, self.robotti.y))
        self.robotti.hyppaa()
        if self.kolikko.arvo == False:
            self.naytto.blit(self.kolik, (self.kolikko.x, self.kolikko.y))
        self.hirvio.liiku()
        self.naytto.blit(self.hirv, (self.hirvio.x, self.hirvio.y))
        pygame.display.flip()
        self.kello.tick(60)

    def piirra_pimeys(self):
        self.naytto.fill((0, 0, 0))
        self.naytto.blit(
            self.s_ovi, (50, self.lattia_y-self.s_ovi.get_height()))
        self.naytto.blit(self.u_ovi, (self.n_leveys-100,
                         self.lattia_y-self.u_ovi.get_height()))
        pygame.draw.rect(self.naytto, (255, 255, 255),
                         pygame.Rect(600, 150, 100, 100), 4)
        pygame.draw.line(self.naytto, (255, 255, 255),
                         (650, 150), (650, 249), 4)
        pygame.draw.line(self.naytto, (255, 255, 255),
                         (600, 200), (699, 200), 4)
        self.naytto.blit(self.robo, (self.robotti.x, self.robotti.y))
        self.robotti.hyppaa()
        self.hirvio.liiku()
        pygame.display.flip()
        self.kello.tick(60)

    def tutki_tapahtumat(self):
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                exit()
            if self.valikko:
                if tapahtuma.type == pygame.KEYDOWN:
                    if tapahtuma.key == pygame.K_RETURN:
                        self.peli = True
                        self.valikko = False
            if self.peli:
                if tapahtuma.type == pygame.KEYDOWN:
                    if tapahtuma.key == pygame.K_RIGHT:
                        self.oikealle = True
                    if tapahtuma.key == pygame.K_LEFT:
                        self.vasemmalle = True
                    if tapahtuma.key == pygame.K_UP:
                        self.robotti.hyppy = True
                if tapahtuma.type == pygame.KEYUP:
                    if tapahtuma.key == pygame.K_RIGHT:
                        self.oikealle = False
                    if tapahtuma.key == pygame.K_LEFT:
                        self.vasemmalle = False
                if tapahtuma.type == self.ajastettu_tapahtuma:
                    if self.vaihto:
                        self.aseta_laskuri(1500)
                        self.vaihto = False
                    else:
                        self.salama.uusi_isku()
                        self.aseta_laskuri(3000)
                        self.vaihto = True

    def napattu_k(self, k: Kolikko, x: int, y: int):
        sijainnit = self.kolikko.kolikon_arvot()
        leveys1 = (x + self.robo.get_width() >=
                   sijainnit[0] and x + self.robo.get_width() <= sijainnit[0]+self.kolik.get_width())
        leveys2 = (x <= sijainnit[0] +
                   self.kolik.get_width() and x >= sijainnit[0])
        korkeus = y+self.robo.get_height() >= sijainnit[1]
        if (leveys1 and korkeus) or (leveys2 and korkeus):
            self.kolikko.napataan()

    def napattu_r(self):
        r_arvot = self.robotti.arvot()
        h_arvot = self.hirvio.arvot()
        leveys1 = (r_arvot[0] + self.robo.get_width() >=
                   h_arvot[0] and r_arvot[0] + self.robo.get_width() <= h_arvot[0]+self.hirv.get_width())
        leveys2 = (r_arvot[0] <= h_arvot[0]+self.hirv.get_width()
                   and r_arvot[0] >= h_arvot[0])
        korkeus = r_arvot[1]+self.robo.get_height() >= h_arvot[1]
        if (leveys1 and korkeus) or (leveys2 and korkeus):
            self.pisteet = 0
            self.robotti.x = 0
            self.valikko = True
            self.peli = False

    def aseta_laskuri(self, i: int):
        return pygame.time.set_timer(self.ajastettu_tapahtuma, i)


if __name__ == "__main__":
    Peli()
