import pygame
pygame.init()

sc = pygame.display.set_mode((600,400), pygame.DOUBLEBUF, pygame.RESIZABLE)
pygame.display.set_caption("Mana pirma programma")
pygame.display.set_icon(pygame.image.load("chile.png"))

clock = pygame.time.Clock()
FPS = 60
W = 600
H = 400
x = W // 2
y = H // 2
speed = 5
move = 0

WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)

flLeft = flRight = False


flRunning = True
while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RIGHT:
        #         flRight = True
        #     elif event.key == pygame.K_LEFT:
        #         flLeft = True
        # elif event.type == pygame.KEYUP:
        #     if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
        #         flLeft = flRight = False


        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and (event.mod & pygame.KMOD_RCTRL):
                move = +speed
            elif event.key == pygame.K_LEFT and (event.mod & pygame.KMOD_LCTRL):
                move = -speed
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                move = 0
    x += move


    # if flLeft:
    #     x -= speed
    # elif flRight:
    #     x += speed




    # keys = pygame.key.get_pressed()
    #
    # if keys[pygame.K_LEFT]:
    #     x -= speed
    # elif keys[pygame.K_RIGHT]:
    #     x += speed
    # elif keys[pygame.K_UP]:
    #     y -= speed
    # elif keys[pygame.K_DOWN]:
    #     y += speed




    sc.fill(WHITE)
    pygame.draw.rect(sc, BLUE, (x,y,10,20))
    pygame.display.update()


    clock.tick(FPS)
