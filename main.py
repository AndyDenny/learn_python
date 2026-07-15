import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group

def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.width, game_settings.height))
    ship = Ship(game_settings, screen)
    alien = Alien(game_settings, screen)
    bullets = Group()
    pygame.display.set_caption('Invasion')

    while True:
        gf.check_events(game_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(game_settings, screen, ship, alien, bullets)

run_game()