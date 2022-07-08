# TEE RATKAISUSI TÄHÄN:
import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.MOUSEMOTION:
            x = tapahtuma.pos[0]-robo.get_width()/2
            y = tapahtuma.pos[1]-robo.get_height()/2

            naytto.fill((0, 0, 0))
            naytto.blit(robo, (x, y))
            pygame.display.flip()

        if tapahtuma.type == pygame.QUIT:
            exit()
