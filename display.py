import pygame
import os
from mail import ReceivedMail

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 320

font: pygame.font.Font = None
lcd = None

def init():
    global font, lcd

    os.putenv('SDL_FBDEV', '/dev/fb1')
    pygame.init()

    lcd = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.mouse.set_visible(False)
    lcd.fill((0, 0, 0))
    pygame.display.update()

    font = pygame.font.SysFont(None, 48)
    print("Display initialized")

def set_mail_info(mail: ReceivedMail, amount_unread: int): 
    img = font.render("test", True, (255, 255, 255))
    lcd.blit(img, (100, 100))
    pygame.display.update()
    print("Updated display")
