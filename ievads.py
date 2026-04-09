import pygame
pygame.init()

pygame.display.set_mode((600,400), pygame.DOUBLEBUF)
pygame.display.set_caption("Mana pirma programma")
pygame.display.set_icon(pygame.image.load("chile.png"))
clock = pygame.time.Clock()
FPS = 60
flRunning = True
while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #exit()
            pygame.quit()
            flRunning = False
    #pygame.time.delay(20)
    clock.tick(FPS)

print("Programma pilda kodu")
