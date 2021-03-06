import pygame


class Ship:
    def __init__(self, ai_game):
        # Инит корабля
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Загружаем корабль и получаем прямоугольник
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
