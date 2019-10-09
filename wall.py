import pygame
from pygame.sprite import Sprite

class Wall(Sprite):
    def __init__(self, size, color, row, column):
        super().__init__()
        self.height = size
        self.width = size
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.row = row
        self.column = column

    def update(self, keys, *args):
        pygame.screen.blit(self.image, self.rect)