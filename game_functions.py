import sys
import pygame

def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            key_up(event, ship)
        if event.type == pygame.KEYDOWN:
            key_down(event, ship)
        if event.type == pygame.QUIT:
            sys.exit()

def key_down(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.flag_moving_right = True
    if event.key == pygame.K_LEFT:
        ship.flag_moving_left = True


def key_up(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.flag_moving_right = False
    if event.key == pygame.K_LEFT:
        ship.flag_moving_left = False


def update_screen(game_settings, screen, ship):
    screen.fill(game_settings.bg_color)
    ship.blitme()
    pygame.display.flip()