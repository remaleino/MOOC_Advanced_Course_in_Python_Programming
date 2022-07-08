# TEE RATKAISUSI TÄHÄN:
import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")
x = 0
y = 480-robo.get_height()

oikealle = False
vasemmalle = False
ylos = False
alas = False
kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key == pygame.K_LEFT:
                vasemmalle = True
            if tapahtuma.key == pygame.K_RIGHT:
                oikealle = True
            if tapahtuma.key == pygame.K_UP:
                ylos = True
            if tapahtuma.key == pygame.K_DOWN:
                alas = True
        if tapahtuma.type == pygame.KEYUP:
            if tapahtuma.key == pygame.K_LEFT:
                vasemmalle = False
            if tapahtuma.key == pygame.K_RIGHT:
                oikealle = False
            if tapahtuma.key == pygame.K_UP:
                ylos = False
            if tapahtuma.key == pygame.K_DOWN:
                alas = False

        if tapahtuma.type == pygame.QUIT:
            exit()

    if oikealle and x <= 640 - robo.get_width()-2:
        x += 2
    if vasemmalle and x >= 2:
        x -= 2
    if ylos and y >= 2:
        y -= 2
    if alas and y <= 480 - robo.get_height()-2:
        y += 2

    naytto.fill((0, 0, 0))
    naytto.blit(robo, (x, y))
    pygame.display.flip()

    kello.tick(60)
