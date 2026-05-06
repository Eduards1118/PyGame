import pygame
pygame.init()

pygame.mixer.music.load("sounds/Eduards Paradniks - bird.mp3")
pygame.mixer.music.play(-1)

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





pygame.display.update()
clock = pygame.time.Clock()
flPause = False
FPS = 60
flRunning = True
while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flPause = not flPause
                if flPause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

clock.tick(FPS)


