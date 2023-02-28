import pygame
from person import User
import commands
from pygame.sprite import Group

def run():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('WOrld')
    bg_color = (255, 222, 173)
    user = User(screen)
    bullets = Group()
    inos = Group()
    commands.create_army(screen, inos)


    while True:
        commands.command(screen, user, bullets)
        user.update_movement()
        commands.update(bg_color, screen, user, inos, bullets)
        commands.update_bullets(bullets)
        commands.update_inos(inos)




run()
