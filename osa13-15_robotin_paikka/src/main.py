# TEE RATKAISUSI TÄHÄN:
import pygame
import random
pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")
m_x = 0
m_y = 0
leveys = robo.get_width()
korkeus = robo.get_height()
x = random.randint(0, 640-leveys)
y = random.randint(0, 480-korkeus)
while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
            m_x = tapahtuma.pos[0]
            m_y = tapahtuma.pos[1]
        if tapahtuma.type == pygame.QUIT:
            exit()
    naytto.fill((0, 0, 0))
    if (m_x >= x and m_x <= x+leveys) and (m_y >= y and m_y <= y+korkeus):
        x = random.randint(0, 640-leveys)
        y = random.randint(0, 480-korkeus)
    naytto.blit(robo, (x, y))
    pygame.display.flip()  # TEE RATKAISUSI TÄHÄN:
