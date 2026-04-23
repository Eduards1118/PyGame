from tokenize import group

import pygame

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
            # self.rect.y = 0
