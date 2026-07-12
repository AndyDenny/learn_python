import pygame

class Ship:

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('assets/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.flag_moving_right = False
        self.flag_moving_left = False

    def update(self):
        if self.flag_moving_right:
            self.rect.centerx += 1
        if self.flag_moving_left:
            self.rect.centerx -= 1


    def blitme(self):
        self.screen.blit(self.image, self.rect)