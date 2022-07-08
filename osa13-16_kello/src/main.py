# TEE RATKAISUSI TÄHÄN:
import pygame
from datetime import datetime
import math

pygame.init()
naytto = pygame.display.set_mode((640, 480))
kello = pygame.time.Clock()
while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
    nyt = datetime.now()
    h = nyt.hour
    m = nyt.minute
    s = nyt.second
    pii = math.pi
    kulma_s = (s/60*pii*2, 120)
    kulma_m = (m/60*pii*2, 110)
    kulma_h = (h/12*pii*2, 80)

    def x(i: float):
        return (320+math.cos(i[0]-math.radians(90))*i[1])

    def y(i: float):
        return (240+math.sin(i[0]-math.radians(90))*i[1])
    naytto.fill((0, 0, 0))
    pygame.draw.ellipse(naytto, (255, 0, 0),
                        (640/2-300/2, 480/2-300/2, 300, 300), 4)
    pygame.draw.circle(naytto, (255, 0, 0), (640/2, 480/2), 15)
    pygame.draw.line(naytto, (0, 0, 255), (640/2, 480/2),
                     (x(kulma_s), y(kulma_s)), 2)
    pygame.draw.line(naytto, (0, 0, 255), (640/2, 480/2),
                     (x(kulma_m), y(kulma_m)), 4)
    pygame.draw.line(naytto, (0, 0, 255), (640/2, 480/2),
                     (x(kulma_h), y(kulma_h)), 6)
    pygame.display.flip()
    kello.tick(60)
