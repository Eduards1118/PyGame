import pygame
from pygame.examples.music_drop_fade import volume
pygame.mixer.pre_init(44100,-16,1,512)
pygame.init()

pygame.mixer.music.load("sounds/Eduards Paradniks - bird.mp3")
pygame.mixer.music.play(-1)

s = pygame.mixer.Sound("sounds/Eduards Paradniks - catch.ogg") #wav

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
vol = 1.0

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
            elif event.key == pygame.K_LEFT:
                vol -= 0.1
                pygame.mixer.music.set_volume(vol)
            elif event.key == pygame.K_RIGHT:
                vol += 0.1
                pygame.mixer.music.set_volume(vol)
            elif event.key == pygame.K_RETURN:
                s.play()

            # ch = s.play()
            # ch.pause()

clock.tick(FPS)


