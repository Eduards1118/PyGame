import pygame
pygame.init()

print(pygame.image.get_extended())

W = 600
H = 400
sc = pygame.display.set_mode((600,400), pygame.RESIZABLE)
pygame.display.set_caption("Mana pirma programa")
pygame.display.set_icon(pygame.image.load("chile.png"))

WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)

sand_surf = pygame.image.load("image/5.jpg").convert()
car_surf = pygame.image.load("image/4.jpg").convert()
start_surf = pygame.image.load("image/3.png").convert_alpha()
finish_surf = pygame.image.load("image/2.png").convert_alpha()

car_rect = car_surf.get_rect(center=(W//2, H//2))
car_surf.set_colorkey(WHITE)

car_up = car_surf
car_down = pygame.transform.flip(car_surf,0,1)
car_left = pygame.transform.rotate(car_surf,90)
car_right = pygame.transform.rotate(car_surf,-90)


speed_x = 0
speed_y = 0
speed = 5

car = car_up

clock = pygame.time.Clock()
FPS = 60
flRunning = True

while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flRunning = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                speed_y = -speed
                car = car_up
            if event.key == pygame.K_s:
                speed_y = speed
                car = car_down
            if event.key == pygame.K_a:
                speed_x = -speed
                car = car_left
            if event.key == pygame.K_d:
                speed_x = speed
                car = car_right

        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_w, pygame.K_s):
                speed_y = 0
            if event.key in (pygame.K_a, pygame.K_d):
                speed_x = 0


    car_rect.x += speed_x
    car_rect.y += speed_y


    sc.blit(sand_surf,(0,0))
    sc.blit(start_surf, (0,0))
    sc.blit(start_surf, (400,325))
    sc.blit(car, car_rect)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()