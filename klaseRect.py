import pygame
pygame.init()

W = 600
H = 400
sc = pygame.display.set_mode((600,400), pygame.DOUBLEBUF)
pygame.display.set_caption("Rect klase")
pygame.display.set_icon(pygame.image.load("chile.png"))
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)

hero = pygame.Surface((40,50))
hero.fill(BLUE)
#rect = hero.get_rect(center=(W//2, H//2))
rect = hero.get_rect(topright=(100,100))
#print(rect.topright)

rect1 = pygame.Rect((150,10,30,30))
rect2 = pygame.Rect((180,40,30,30))
print(rect1)
rect1.move_ip(20,20)
print(rect1)


sc.fill(WHITE)
sc.blit(hero,rect)
pygame.display.update()


clock = pygame.time.Clock()
FPS = 60
flRunning = True
while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    clock.tick(FPS)


