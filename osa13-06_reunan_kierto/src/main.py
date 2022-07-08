# TEE RATKAISUSI TÄHÄN:
# TEE RATKAISUSI TÄHÄN:
import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))
robo = pygame.image.load("robo.png")
y = 0
x = 0
nopeus = 1
korkeus = robo.get_height()
leveys = robo.get_width()
kello = pygame.time.Clock()
while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
    naytto.fill((0, 0, 0))
    naytto.blit(robo, (x, y))
    pygame.display.flip()
    if x <= 640 - leveys and y == 0:
        x += nopeus
    if x == 640-leveys and y <= 480-korkeus:
        y += nopeus
    if x >= 0 and y == 480-korkeus:
        x += -nopeus
    if x == 0 and y >= 0:
        y += -nopeus
    kello.tick(60)
