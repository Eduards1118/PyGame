import pygame
pygame.init()

W = 600
H = 400
sc = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)
pygame.display.set_caption("Rect klase")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

ground = H - 70
jump_force = 20
move = jump_force + 1

speed_x = 0

hero = pygame.Surface((40, 50))
hero.fill(BLUE)

rect = hero.get_rect(centerx=W // 2)
rect.bottom = ground

clock = pygame.time.Clock()
FPS = 60

flRunning = True

while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flRunning = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and rect.bottom == ground:
                move = -jump_force

            if event.key == pygame.K_LEFT:
                speed_x = -5
            if event.key == pygame.K_RIGHT:
                speed_x = 5

        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                speed_x = 0


    if move <= jump_force:
        if rect.bottom + move < ground:
            rect.bottom += move
            if move < jump_force:
                move += 1
        else:
            rect.bottom = ground
            move = jump_force + 1


    rect.x += speed_x


    if rect.right < 0:
        rect.left = W
    elif rect.left > W:
        rect.right = 0


    sc.fill(WHITE)
    sc.blit(hero, rect)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
