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
pygame.draw.rect(sc,WHITE,(10,10,50,100),2)
pygame.draw.line(sc,GREEN,(220,20), (350,50),5)
pygame.draw.aaline(sc,GREEN,(220,40), (350,70),5)
pygame.draw.lines(sc,RED,True,[(40,10), (100,60), (300,150)],3)
pygame.draw.polygon(sc,BLUE, [[150,210], [180,250], [90,290], [30,230]],3)
pygame.draw.circle(sc,WHITE,(300,250), 120)
pygame.draw.circle(sc,BLACK,(300,250), 90)
pygame.draw.circle(sc,WHITE,(300,250), 60)
pygame.draw.circle(sc,BLACK,(300,250), 30)
pygame.draw.ellipse(sc,GREEN,(400,50, 100,50),3)
pi = 3.14
pygame.draw.arc(sc,RED, (450,60,50,100), pi, 2*pi, 5)
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


