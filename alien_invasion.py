import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
    # iniitialize pygame, settings and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # make a ship
    ship = Ship(screen)
    
    # main game loop
    while True:
        
        # watch for keyboard/mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # redraw the screen during each pass through loop
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        
        # make most recently drawn screen visibile
        pygame.display.flip()

run_game()