# TEE RATKAISUSI TÄHÄN:
import pygame
import random

pygame.init()
naytto = pygame.display.set_mode((640, 480))
pallo = pygame.image.load("pallo.png")
kello = pygame.time.Clock()
korkeus = pallo.get_height()
leveys = pallo.get_width()
x = random.randint(0, 640-leveys)
y = random.randint(0, 480-korkeus)
nopeus_x = 2
nopeus_y = 2
while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
    naytto.fill((0, 0, 0))
    naytto.blit(pallo, (x, y))
    if y >= 480 - korkeus and nopeus_y > 0:
        nopeus_y = -nopeus_y
    if x >= 640 - leveys and nopeus_x > 0:
        nopeus_x = -nopeus_x
    if y <= 0 and nopeus_y < 0:
        nopeus_y = -nopeus_y
    if x <= 0 and nopeus_x < 0:
        nopeus_x = -nopeus_x
    x += nopeus_x
    y += nopeus_y
    pygame.display.flip()
    kello.tick(60)
