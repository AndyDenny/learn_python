import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.width, game_settings.height))
    ship = Ship(screen)
    pygame.display.set_caption('Invasion')

    while True:
        screen.fill(game_settings.bg_color)
        ship.blitme()
        gf.check_events()
        pygame.display.flip()

run_game()