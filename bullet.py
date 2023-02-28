import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, user):
        super(Bullet, self,).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 5, 15)
        self.color = (0, 0, 0)
        self.speed = 3.5
        self.rect.centerx = user.rect.centerx
        self.rect.top = user.rect.top
        self.y = float(self.rect.y)


    def update(self):
        self.y -= self.speed
        self.rect.y = self.y



    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
