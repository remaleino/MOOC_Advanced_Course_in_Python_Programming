import pygame
import random
pygame.init()
naytto = pygame.display.set_mode((640, 480))
kivi = pygame.image.load("kivi.png")
robo = pygame.image.load("robo.png")
korkeus = kivi.get_height()
leveys = kivi.get_width()
kello = pygame.time.Clock()
oikealle = False
vasemmalle = False
l = []
x_r = robo.get_width()+100
oikealle = False
vasemmalle = False
fontti = pygame.font.SysFont("Arial", 24)
pisteet = 0


def leveys_arvo(i: int):
    if i+leveys >= x_r and i + leveys <= x_r+robo.get_width():
        return True
    if i >= x_r and i <= x_r+robo.get_width():
        return True
    return False


while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
        if tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key == pygame.K_RIGHT:
                oikealle = True
            if tapahtuma.key == pygame.K_LEFT:
                vasemmalle = True
        if tapahtuma.type == pygame.KEYUP:
            if tapahtuma.key == pygame.K_RIGHT:
                oikealle = False
            if tapahtuma.key == pygame.K_LEFT:
                vasemmalle = False
    teksti = fontti.render(f"Pisteet: {pisteet}", True, (255, 0, 0))
    naytto.fill((0, 0, 0))
    if oikealle and x_r <= 640 - robo.get_width()-2:
        x_r += 4
    if vasemmalle and x_r >= 2:
        x_r -= 4
    if random.randint(1, 100) == 1:
        x = random.randint(0, 640-leveys)
        l.append([x, 0-korkeus])
    onko_sisalla = list(filter(lambda a: (
        (a[1]+korkeus) >= 480 - robo.get_height()) and leveys_arvo(a[0]), l))
    if onko_sisalla:
        pisteet += 1
        l.remove(onko_sisalla[0])
    onko_ulkona = list(filter(lambda a: a[1]+korkeus > 480, l))
    if onko_ulkona:
        l.clear()
        pisteet = 0
    l = list(map(lambda a: [a[0], a[1]+1], l))
    if l:
        for a in l:
            naytto.blit(kivi, (a[0], a[1]))
    naytto.blit(teksti, ((640-teksti.get_width()-50), 10))
    naytto.blit(robo, (x_r, 480-robo.get_height()))
    pygame.display.flip()
    kello.tick(60)
