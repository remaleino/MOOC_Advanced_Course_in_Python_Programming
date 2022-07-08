import pygame
import random
pygame.init()
naytto = pygame.display.set_mode((640, 480))
robo = pygame.image.load("robo.png")
korkeus = robo.get_height()
leveys = robo.get_width()
kello = pygame.time.Clock()
l = []
while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
    naytto.fill((0, 0, 0))
    if random.randint(1, 50) == 1:
        x = random.randint(0, 640-leveys)
        l.append([x, 0-korkeus])
    if l:
        for a in l:
            if a[1] < 480-korkeus:
                a[1] += 1
            if a[1] == 480-korkeus:
                if a[0] <= (620-leveys) / 2:
                    a[0] -= 1
                else:
                    a[0] += 1
            naytto.blit(robo, (a[0], a[1]))
    pygame.display.flip()
    kello.tick(60)
