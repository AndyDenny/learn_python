import pygame

class Ship:

    def __init__(self, settings, screen):
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('assets/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.flag_moving_right = False
        self.flag_moving_left = False

    def update(self):
        if self.flag_moving_right:
            self.center += self.settings.ship_speed_factor
        if self.flag_moving_left:
            self.center -= self.settings.ship_speed_factor
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)