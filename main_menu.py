import pygame
pygame.init()
import sys

TEXTCOLOR = (250, 235, 215)
BACKGROUND_COLOR = (139, 101, 8)
alien_image1 = pygame.image.load('images/bluerobot.png')
alien_image2 = pygame.image.load('images/greenrobot.png')
alien_image3 = pygame.image.load('images/purplerobot.png')

class Main_Menu:
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.bg_color = TEXTCOLOR
        self.title = "Space Invaders"
        self.robottext1 = " = 150"
        self.robottext2 = " = 100"
        self.robottext3 = " = 50"
        self.presstext = "Press any key to play"
        self.font = pygame.font.SysFont(None, 100)
        self.robot_font = pygame.font.SysFont(None, 50)
        self.robot1 = alien_image1
        self.robot2 = alien_image2
        self.robot3 = alien_image3

    def start(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.titlemsg()
        self.robot1msg()
        self.robot2msg()
        self.robot3msg()
        self.presstextmsg()
        self.screen.blit(self.robot1, (self.ai_settings.screen_width/3, 140))
        self.screen.blit(self.robot2, (self.ai_settings.screen_width/3, 190))
        self.screen.blit(self.robot3, (self.ai_settings.screen_width/3, 240))

    def titlemsg(self):
        self.msg_image = self.font.render(self.title, True, (TEXTCOLOR))
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = (400, 90)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def robot1msg(self):
        self.msg_image = self.robot_font.render(self.robottext1, True, (TEXTCOLOR))
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = (self.ai_settings.screen_width/2 + 50, 150)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def robot2msg(self):
        self.msg_image = self.robot_font.render(self.robottext2, True, (TEXTCOLOR))
        self.msg_image_rect = self.msg_image_rect.get_rect()
        self.msg_image_rect.center = (self.ai_settings.screen_width/2 + 50, 200)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def robot3msg(self):
        self.msg_image = self.robot_font.render(self.robottext3, True, (TEXTCOLOR))
        self.msg_image_rect = self.msg_image_rect.get_rect()
        self.msg_image_rect.center = (self.ai_settings.screen_width/2 + 50, 250)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def presstextmsg(self):
        self.msg_image = self.font.render(self.presstext, True, (TEXTCOLOR))
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = (self.ai_settings.screen_width/2 + 50, 300)
        self.screen.blit(self.msg_image, self.msg_image_rect)






