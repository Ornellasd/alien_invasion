import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
##
from stars import Star
##
import game_functions as gf

def run_game():
    # iniitialize pygame, settings and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # make a ship, a group of bullets and a group of aliens.
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()

    # create fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # make background star
    star = Star(screen)

    # main game loop
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets, star)    
    
run_game()