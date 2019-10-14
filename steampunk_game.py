import sys
import pygame
pygame.init()

from time import sleep
from pygame.locals import *
from settings import Settings
from ship import Ship
from game_stats import GameStats
from scoreboard import Scoreboard
from bullet import Bullet
from robot import Robot
from pygame.sprite import Group

WINDOWWIDTH = 980
WINDOWHEIGHT = 464
TEXTCOLOR = (250, 235, 215)
BACKGROUND_COLOR = (139, 101, 8)
Surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

alien_image1 = pygame.image.load('images/bluerobot.png')
alien_image2 = pygame.image.load('images/greenrobot.png')
alien_image3 = pygame.image.load('images/purplerobot.png')
alien_image4 = pygame.image.load('images/redrobot.png')
robottext1 = " = 10"
robottext2 = " = 20"
robottext3 = " = 30"
robottext4 = ' = ???'
robot_font = pygame.font.SysFont(None, 60)
cannon_sound = pygame.mixer.Sound('sounds/cannon.wav')

def drawText(text, font, surf, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surf.blit(textobj, textrect)

class Game:
    def __init__(self):
        pygame.init()
        self.ai_settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Steampunk Robot")
        self.font = pygame.font.SysFont(None, 90)
        self.ship = Ship(self.ai_settings, self.screen)
        self.bullets = pygame.sprite.Group()

    def run_game(self):

        while True:
            self.check_events()
            self.ship.update()
            self.update_bullets()
            self.update_screen()

            #Start Screen
            self.screen.fill(BACKGROUND_COLOR)
            drawText('Robot Invaders', self.font, self.screen, (765), (150))
            self.screen.blit(alien_image1, (800, 300))
            self.screen.blit(alien_image2, (800, 400))
            self.screen.blit(alien_image3, (800, 500))
            self.screen.blit(alien_image4, (800, 600))
            drawText(robottext1, robot_font, self.screen, (990), (320))
            drawText(robottext2, robot_font, self.screen, (990), (420))
            drawText(robottext3, robot_font, self.screen, (990), (520))
            drawText(robottext4, robot_font, self.screen, (990), (620))

            pygame.display.update()

            pygame.display.flip()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)

    def check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.fire_cannon

    def check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def fire_cannon(self):
        if len(self.bullets) < self.ai_settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                 self.bullets.remove(bullet)

    def update_screen(self):
        self.screen.fill(self.ai_settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()

Game()







