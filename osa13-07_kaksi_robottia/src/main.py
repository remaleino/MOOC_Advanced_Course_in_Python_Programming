# TEE RATKAISUSI TÄHÄN:
import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))
robo = pygame.image.load("robo.png")
kello = pygame.time.Clock()
korkeus = robo.get_height() + 10
leveys = robo.get_width()
nopeus_a = 1
nopeus_b = 2
x_a = 0
x_b = 0
while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
    naytto.fill((0, 0, 0))
    naytto.blit(robo, (x_a, 0))
    naytto.blit(robo, (x_b, korkeus))
    if x_a == 640 - leveys and nopeus_a > 0:
        nopeus_a = -nopeus_a
    if x_b == 640 - leveys and nopeus_b > 0:
        nopeus_b = -nopeus_b
    if x_a == 0 and nopeus_a < 0:
        nopeus_a = -nopeus_a
    if x_b == 0 and nopeus_b < 0:
        nopeus_b = -nopeus_b
    x_a += nopeus_a
    x_b += nopeus_b
    pygame.display.flip()
    kello.tick(60)
