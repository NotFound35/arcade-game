import pygame, sys
from bullet import Bullet
from ino import Ino


def command(screen, user, bullets):

    for events in pygame.event.get():
            if events.type == pygame.QUIT:
                sys.exit()
            elif events.type == pygame.KEYDOWN:
                if events.key == pygame.K_d:
                    user.mright = True
                elif events.key == pygame.K_a:
                    user.mleft = True
                elif events.key == pygame.K_SPACE:
                    new_bullet = Bullet(screen, user)
                    bullets.add(new_bullet)
            elif events.type == pygame.KEYUP:
                if events.key == pygame.K_d:
                    user.mright = False
                elif events.key == pygame.K_a:
                    user.mleft = False


def update(bg_color, screen, user, inos, bullets):
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    user.out()
    for ino in inos.sprites():
        ino.draw_ino()
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def update_inos(inos):
    inos.update()


def create_army(screen, inos):
    ino = Ino(screen)
    ino_width = ino.rect.width
    ino_height = ino.rect.height
    number_ino_x = int((800 - 2 * ino_width) / ino_width)
    number_ino_y = int((800 - 200 +ino_height) / ino_height)

    for row_number in range(number_ino_y - 5):
        for ino_number in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + ino_width * ino_number
            ino.y = ino_height + ino_height * row_number
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + ino.rect.height * row_number
            inos.add(ino)

        
