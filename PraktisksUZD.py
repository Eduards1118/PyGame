import pygame
pygame.init()

sc = pygame.display.set_mode((600,400), pygame.DOUBLEBUF)
pygame.display.set_caption("Pamat elementi")
pygame.display.set_icon(pygame.image.load("chile.png"))

WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)

n = 15


for i in range(n):
    pygame.draw.line(sc, RED, (100, 200), (100 + i*10, 300), 1)


for i in range(n):
    pygame.draw.line(sc, RED, (240, 200), (100 + i*10, 300), 1)


for i in range(n):
    pygame.draw.line(sc, RED, (200, 100), (100 + i*10, 300), 1)



pygame.display.update()


clock = pygame.time.Clock()
FPS = 60
flRunning = True

while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    #pygame.time.delay(20)
    clock.tick(FPS)


