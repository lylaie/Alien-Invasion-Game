import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, window):
        super(Ship, self).__init__()

        self.ai_settings = ai_settings
        self.window = window
        self.image = pygame.image.load('images/ship.bmp')

        self.rect = self.image.get_rect()
        self.window_rect = window.get_rect()
        self.rect.centerx = self.window_rect.centerx
        self.rect.bottom = self.window_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.window_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center

    def blitme(self):
        self.window.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.window_rect.centerx
