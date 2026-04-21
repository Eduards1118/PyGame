import pygame
pygame.init()

print(pygame.font.get_fonts())

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

f_sys = pygame.font.SysFont('inkfree', 82, 7,  10)
sc_text = f_sys.render('Daugavpils', 0, RED, BLUE)
pos = sc_text.get_rect(center=(W//2,H//2))

def draw_text():
    sc.fill(WHITE)
    sc.blit(sc_text, pos)
    pygame.display.update()

draw_text()

clock = pygame.time.Clock()
FPS = 60
flRunning = True

while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flRunning = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pygame.mouse.get_rel()

    if pygame.mouse.get_focused() and pos.collidepoint(pygame.mouse.get_pos()):
        btns = pygame.mouse.get_pressed()
        if btns[0]:
            rel = pygame.mouse.get_rel()
            pos.move_ip(rel)
            draw_text()

    clock.tick(FPS)

pygame.quit()