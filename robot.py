import pygame
from pygame.sprite import Sprite

alien_image1 = pygame.image.load('images/bluerobot.png')
alien_image2 = pygame.image.load('images/greenrobot.png')
alien_image3 = pygame.image.load('images/purplerobot.png')

class Robot(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = alien_image1
        self.rect = self.image.get_rect()

        self.image1 = alien_image2
        self.rect1 = self.image1.get_rect()

        self.image2 = alien_image3
        self.rect2 = self.image2.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.rect1.x = self.rect1.width
        self.rect1.y = self.rect1.height

        self.rect2.x = self.rect2.width
        self.rect2.y = self.rect2.height

        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        if self.rect1.right >= screen_rect.right or self.rect1.left <= 0:
            return True
        if self.rect2.right >= screen_rect.right or self.rect2.left <= 0:
            return True

    def update(self):
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
        self.rect1.x = self.x
        self.rect2.x = self.x






