import pygame
from random import randint
from ball import Ball
from bildes import speed

pygame.init()

pygame.time.set_timer(pygame.USEREVENT, 2000)
W = 600
H = 400
sc = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)
pygame.display.set_caption("Mana pirmā programma")
icon = pygame.image.load("chile.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
FPS = 60

balls_image = ['ball_squ.png', 'ball_sn_lpd.png', 'ball_lion.png']
balls_surf = [pygame.image.load('image/'+path).convert_alpha() for path in balls_image]

def createBall(group):
    indx = randint(0,len(balls_surf)-1)
    x = randint(20, W-20)
    speed = randint(1,4)

    return Ball(x, speed, balls_surf[indx], group)

balls = pygame.sprite.Group()


back = pygame.image.load("image/back1.jpg").convert()


# balls = pygame.sprite.Group(
#     Ball(W//2, 1, "image/ball_squ.png"),
#     Ball(W//2 - 250, 2, "image/ball_sn_lpd.png"),
#     Ball(W//2 + 50, 3, "image/ball_lion.png")
# )

createBall(balls)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.USEREVENT:
            createBall(balls)


    sc.blit(back, (0,0))

    balls.draw(sc)
    balls.update(H)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()