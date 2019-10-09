import pygame
import sys

def load_image(name):
    image = pygame.image.load(name)
    return image

class Animate(pygame.sprite.Sprite):
    def __init__(self):
        super(Animate, self).__init__()
        self.images = []
        self.images.append(load_image('images/bluerobot.png'))
        self.images.append(load_image('images/bluerobot2.png'))
        self.images.append(load_image('images/bluerobot3.png'))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(5, 5, 64, 64)

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

def main():
    pygame.init()
    screen = pygame.display.set_mode((250, 250))

    my_sprite = Animate()
    my_group = pygame.sprite.Group(my_sprite)

    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        my_group.update()
        my_group.draw(screen)
        pygame.display.flip()

main()