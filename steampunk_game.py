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
from main_menu import Main_Menu
from robot import Robot
from wall import Wall

WINDOWWIDTH = 980
WINDOWHEIGHT = 464
TEXTCOLOR = (250, 235, 215)
BACKGROUND_COLOR = (139, 101, 8)
Surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

alien_image1 = pygame.image.load('images/bluerobot.png')
alien_image2 = pygame.image.load('images/greenrobot.png')
alien_image3 = pygame.image.load('images/purplerobot.png')

cannon_sound = pygame.mixer.Sound('sounds/cannon.wav')


def terminate():
    pygame.quit()
    sys.exit()

def PlayerPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                return

class Steampunk:
    def __init__(self):
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Robot Invasion")

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.robots = pygame.sprite.Group()

        self.create_fleet()

    def run_game(self):
        while True:
            self.check_events()

            if self.stats.game_active:
                self.ship.update()
                self.update_bullets()
                self.update_aliens()

            self.update_screen()

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
        if len(self.bullets) < self.settings.bullets_allowed:
            new_cannon = Bullet(self)
            self.bullets.add(new_cannon)

    def update_cannons(self):
        self.bullets.update()

        for cannon in self.bullets.copy():
            if cannon.rect.bottom <= 0:
                self.bullets.remove(cannon)

    def check_bullet_robot_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.robots, True, True)

        if collisions:
            for robots in collisions.values():
                self.stats.score += self.settings.alien_points * len(robots)
            self.sb.prep_score()
            self.sb.check_high_score()

        if pygame.sprite.collide_mask(self.bullets, robots):
            pygame.mixer.music.stop()
            cannon_sound.play()

        if not self.robots:
            self.bullets.empty()
            self.create_fleet()
            self.settings.increase_speed()

            self.stats.level += 1
            self.sb.prep_level()

    def update_robots(self):
        self.check_fleet_edges()
        self.robots.update()

        if pygame.sprite.spritecollideany(self.ship, self.robots):
            self.ship_hit()

        self.check_robot_bottom()

    def check_robots_bottom(self):
        screen_rect = self.screen.get_rect()
        for robot in self.robots.sprites():
            if robot.rect.bottom >= screen_rect.bottom:
                self.ship_hit()
                break

    def ship_hit(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            self.robots.empty()
            self.bullets.empty()

            self.create_fleet()
            self.ship.center_ship()

            sleep(0.5)

        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def create_fleet(self):
        robot = Robot(self)
        robot_width, robot_height = robot.rect.size
        robot_space = self.settings.screen_width - (2 * robot_width)
        number_of_robots = robot_space // (2 * robot_width)

        ship_height = self.ship.rect.height
        ship_space = (self.settings.screen_height - (3 * robot_height) - ship_height)
        rows = robot_space // (2 * robot_height)

        for row_number in range(rows):
            for robot_number in range(number_of_robots):
                self.create_robot(robot_number, row_number)

    def create_robot(self, robot_number, row_number):
        robot = Robot(self)
        robot_width, robot_height = robot.rect.size
        robot.x = robot_width + 2 * robot_width * robot_number
        robot.rect.x = robot.x
        robot.rect.y = robot.rect.height + 2 * robot.rect.height * row_number
        self.robots.add(robot)

    def check_fleet_edges(self):
        for robot in self.robots.sprites():
            if robot.check_edges():
                self.change_fleet_direction()
                break

    def change_fleet_direction(self):
        for robot in self.robots.sprites():
            robot.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.bltime()
        for cannon in self.bullets.sprites():
            cannon.draw_bullet()
        self.robots.draw(self.screen)

        self.sb.show_score()

        pygame.display.flip()

def play():
    Main_Menu(None, None)
    pygame.display.update()
    PlayerPressKey()

    Steampunk()
    game_on = True

    while game_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    game_on = False

    pygame.display.update()
    PlayerPressKey()

play()






