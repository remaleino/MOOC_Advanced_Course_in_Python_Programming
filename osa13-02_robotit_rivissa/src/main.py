# TEE RATKAISUSI TÄHÄN:
import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))
robo = pygame.image.load("robo.png")
naytto.fill((0, 0, 0))
leveys = robo.get_width()
korkeus = robo.get_height()
x = leveys
for i in range(0, 10):
    naytto.blit(robo, (x, korkeus))
    x += leveys
pygame.display.flip()
while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
