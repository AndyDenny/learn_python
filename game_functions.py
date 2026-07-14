import sys
import pygame
import bullet

def check_events(game_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            key_up(event, ship)
        if event.type == pygame.KEYDOWN:
            key_down(event, game_settings, screen, ship, bullets)
        if event.type == pygame.QUIT:
            sys.exit()


def key_down(event, game_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.flag_moving_right = True
    if event.key == pygame.K_LEFT:
        ship.flag_moving_left = True
    if event.key == pygame.K_SPACE:
        if len(bullets) < game_settings.bullets_allowed :
            new_bullet = bullet.Bullet(game_settings, screen, ship)
            bullets.add(new_bullet)

def key_up(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.flag_moving_right = False
    if event.key == pygame.K_LEFT:
        ship.flag_moving_left = False


def update_screen(game_settings, screen, ship, bullets):
    screen.fill(game_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()