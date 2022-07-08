import pygame
import random


class RobolleRahaa:
    def __init__(self):
        pygame.init()
        self.kello = pygame.time.Clock()
        self.spekseja()
        self.kuvat()
        self.nappainten_alkuasetus()

        pygame.display.set_caption("Robolle Rahaa")

        self.silmukka()

    def spekseja(self):
        self.leveys = 800
        self.korkeus = 600
        self.naytto = pygame.display.set_mode((self.leveys, self.korkeus))
        self.nopeus_x = 7
        self.nopeus_y = 7
        self.laskuri = 0
        self.ennatys = 0
        self.fontti = pygame.font.SysFont("John Hubbard", 50)
        self.fontti_pieni = pygame.font.SysFont("John Hubbard", 25)

    def kuvat(self):
        self.kolikko = pygame.image.load("kolikko.png")
        self.robo1 = pygame.image.load("robo.png")
        self.robo2 = pygame.image.load("robo.png")
        self.kolikko_rect = self.kolikko.get_rect()
        self.robo1_rect = self.robo1.get_rect(
            midleft=(self.leveys-self.leveys, self.korkeus/2))
        self.robo2_rect = self.robo2.get_rect(
            midright=(self.leveys, self.korkeus/2))

    def nappainten_alkuasetus(self):
        self.ylos = False
        self.alas = False
        self.ylos2 = False
        self.alas2 = False

    def silmukka(self):
        while True:
            self.tapahtumat()
            self.robo_liikkuu()
            self.kolikko_liikkuu()
            self.koko_naytto()

    def tapahtumat(self):
        for self.tapahtuma in pygame.event.get():
            if self.tapahtuma.type == pygame.QUIT:
                exit()

    def robo_liikkuu(self):
        if self.tapahtuma.type == pygame.KEYDOWN:
            if self.tapahtuma.key == pygame.K_UP:
                self.ylos = True
            if self.tapahtuma.key == pygame.K_DOWN:
                self.alas = True
            if self.tapahtuma.key == pygame.K_RIGHT:
                self.ylos2 = True
            if self.tapahtuma.key == pygame.K_LEFT:
                self.alas2 = True

        if self.tapahtuma.type == pygame.KEYUP:
            if self.tapahtuma.key == pygame.K_UP:
                self.ylos = False
            if self.tapahtuma.key == pygame.K_DOWN:
                self.alas = False
            if self.tapahtuma.key == pygame.K_RIGHT:
                self.ylos2 = False
            if self.tapahtuma.key == pygame.K_LEFT:
                self.alas2 = False

        if self.ylos:
            self.robo1_rect.y -= 7
        if self.alas:
            self.robo1_rect.y += 7
        if self.ylos2:
            self.robo2_rect.y -= 7
        if self.alas2:
            self.robo2_rect.y += 7

        if self.robo2_rect.y < 0:
            self.robo2_rect.y = 0
        if self.robo1_rect.y < 0:
            self.robo1_rect.y = 0

        if (self.robo2_rect.y + self.robo2.get_height() > 600):
            self.robo2_rect.y = 600 - self.robo2.get_height()
        if (self.robo1_rect.y + self.robo1.get_height() > 600):
            self.robo1_rect.y = 600 - self.robo1.get_height()

    def kolikko_liikkuu(self):
        self.kolikko_rect = self.kolikko_rect.move(
            self.nopeus_x, self.nopeus_y)
        if self.kolikko_rect.left < 0 or self.kolikko_rect.right > self.leveys:
            self.kolikko_keskelle()
        if self.kolikko_rect.top < 0 or self.kolikko_rect.bottom > self.korkeus:
            self.nopeus_y = -self.nopeus_y
        if self.kolikko_rect.colliderect(self.robo1_rect) or self.kolikko_rect.colliderect(self.robo2_rect):
            self.nopeus_x = -self.nopeus_x
            self.nopeus_y = -self.nopeus_y
            self.laskuri += 1

    def kolikko_keskelle(self):
        global nopeus_x, nopeus_y
        self.kolikko_rect.center = (self.leveys/2, self.korkeus/2)
        self.nopeus_y *= random.choice((1, -1))
        self.nopeus_x *= random.choice((1, -1))
        self.pisteiden_nollaus()

    def pisteiden_nollaus(self):
        if self.laskuri > self.ennatys:
            self.ennatys = self.laskuri
        self.laskuri = 0

    def koko_naytto(self):
        self.naytto.fill((255, 150, 150))
        self.naytto.blit(self.robo1, self.robo1_rect)
        self.naytto.blit(self.robo2, self.robo2_rect)
        self.naytto.blit(self.kolikko, self.kolikko_rect)
        teksti = self.fontti.render(
            "Robon lompakossa: " + str(self.laskuri) + " €", True, (219, 219, 219))
        ennatys = self.fontti_pieni.render(
            "Isoin summa lompakossa pelin aikana: " + str(self.ennatys) + " €", True, (219, 219, 219))
        self.naytto.blit(teksti, (210, 550))
        self.naytto.blit(ennatys, (2, 0))
        pygame.display.flip()
        self.kello.tick(60)


if __name__ == "__main__":
    RobolleRahaa()
