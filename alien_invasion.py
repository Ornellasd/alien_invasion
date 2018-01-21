import sys
import pygame

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    pygame.display.set_caption('Alien Invasion')
    bg_color = (230, 230, 230)

    # main game loop
    while True:
    
        # Watch for keyboard/mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # redraw the screen during each pass through loop
        screen.fill(bg_color)
        
        # make most recently drawn screen visibile
        pygame.display.flip()

run_game()