# TEE RATKAISUSI TÄHÄN:
import pygame
import random
pygame.init()
naytto = pygame.display.set_mode((640, 480))
robo = pygame.image.load("robo.png")
naytto.fill((0, 0, 0))
leveys = robo.get_width()
korkeus = robo.get_height()
for i in range(0, 1000):
    naytto.blit(robo, (random.randint(0, 640-leveys),
                random.randint(0, 480-korkeus)))
pygame.display.flip()
while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
