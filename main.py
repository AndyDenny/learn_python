import sys
import pygame
from settings import Settings

def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(game_settings.width, game_settings.height)
    pygame.display.set_caption('Invasion')

    while True:
        screen.fill(game_settings.bg_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()

run_game()