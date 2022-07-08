# TEE RATKAISUSI TÄHÄN:
import pygame
import math

pygame.init()
naytto = pygame.display.set_mode((640, 480))
robo = pygame.image.load("robo.png")
korkeus = robo.get_height()
leveys = robo.get_width()
kulma = 0
kello = pygame.time.Clock()
while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
    naytto.fill((0, 0, 0))
    for i in range(1, 11):
        a = 6.28/10
        i = i*a
        x = 320+math.cos(kulma+i)*100-leveys/2
        y = 240+math.sin(kulma+i)*100-korkeus/2
        naytto.blit(robo, (x, y))
    pygame.display.flip()
    kulma += 0.01
    kello.tick(60)
