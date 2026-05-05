import pygame
from random import randint

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
balls_surf = [pygame.image.load('image/' + path).convert_alpha() for path in balls_image]


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, speed, surf, group):
        super().__init__()
        self.image = surf
        self.rect = self.image.get_rect(center=(x, 0))
        self.speed = speed
        self.add(group)

    def update(self, H):
        if self.rect.y < H - self.rect.height:
            self.rect.y += self.speed
        else:
            self.kill()


def createBall(group):
    indx = randint(0, len(balls_surf) - 1)
    x = randint(20, W - 20)
    speed = randint(1, 4)
    return Ball(x, speed, balls_surf[indx], group)

balls = pygame.sprite.Group()


back_surf = pygame.image.load("image/back1.jpg").convert()
back_surf = pygame.transform.scale(back_surf, (W, H))

telega_surf = pygame.image.load("image/telega.png").convert_alpha()
telega_rect = telega_surf.get_rect(midbottom=(W // 2, H - 10))

balls_data = ({'path':  '2.png', 'score': 100},
              {'path':  '3.png', 'score': 150},
              {'path':  '4.png', 'score': 200})

move = 0
player_speed = 8

createBall(balls)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.USEREVENT:
            createBall(balls)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move = player_speed
            elif event.key == pygame.K_LEFT:
                move = -player_speed

        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                move = 0

    telega_rect.x += move

    if telega_rect.left < 0:
        telega_rect.left = 0
    if telega_rect.right > W:
        telega_rect.right = W


    sc.fill((0, 0, 0))
    sc.blit(back_surf, (0, 0))
    balls.draw(sc)
    sc.blit(telega_surf, telega_rect)

    pygame.display.update()
    balls.update(H)
    clock.tick(FPS)

pygame.quit()