import pygame
pygame.init()

W = 600
H = 400
sc = pygame.display.set_mode((600,400), pygame.DOUBLEBUF)
pygame.display.set_caption("Mana pirma programma")
pygame.display.set_icon(pygame.image.load("chile.png"))
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)

surf = pygame.Surface((W,200))
bita = pygame.Surface((50,10))
bita2 = pygame.Surface((50,10))
surf.fill(BLUE)
bita.fill(RED)
bita2.fill(GREEN)

# surf_alpha = pygame.Surface((W, 100))
# pygame.draw.rect(surf_alpha, BLUE, (0,0,W,100))
# surf_alpha.set_alpha(128) #causpidums no 0 lidz 255
# surf.blit(surf_alpha,(0,50))
# sc.blit(surf,(50,50))
#
# pygame.display.update()
clock = pygame.time.Clock()
FPS = 60

x, y = 0, 0
bx, by = 0, 150
bx2,by2 = W,50

flRunning = True
while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    surf.fill(BLUE)
    surf.blit(bita, (bx,by))
    if bx < W:
        bx += 5
    else:
        bx = 0

    if y < H:
        y += 1
    else:
        y = 0


    surf.blit(bita2, (bx2, by2))
    if bx2 > 0:
        bx2 -=5
    else:
        bx2 = W


    sc.fill(WHITE)
    sc.blit(surf, (x,y))
    pygame.display.update()

    clock.tick(FPS)


