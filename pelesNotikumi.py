import pygame
from pygame import MOUSEBUTTONUP

pygame.init()

sc = pygame.display.set_mode((600,400), pygame.DOUBLEBUF)
pygame.display.set_caption("Pamat elementi")
pygame.display.set_icon(pygame.image.load("chile.png"))

WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)

sp = ep = None
flStartDraw = False
clock = pygame.time.Clock()
FPS = 60
pygame.mouse.set_visible(False)

flRunning = True
while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        sc.fill(WHITE)
        mpos = pygame.mouse.get_pos()
        if pygame.mouse.get_focused():
            pygame.draw.circle(sc, RED, mpos,5)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #print("Nospiesta poga: ", event.button)
            flStartDraw = True
            sp = event.pos
        elif event.type == pygame.MOUSEMOTION:
            # print("Peles pozicija", event.pos)
            #print("Peles pedejas kustibas izmaiņa", event.rel)
            if flStartDraw:
                pos = event.pos

                width = pos[0] - sp[0]
                height = pos[1] - sp[1]


                rect = pygame.Rect(sp[0], sp[1], width, height)
                rect.normalize()
                pygame.draw.rect(sc, BLUE, rect)


            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                flStartDraw = False
            pygame.display.update()
    clock.tick(FPS)