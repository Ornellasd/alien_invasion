import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
## a class to represent a single alien in the fleet.

    def __init__(self, ai_settings, screen):
        ## initialize alien and set starting position
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load the alien image and set its rect attribute
        self.image = pygame.image.load('images/scaled_ufo.png')
        self.rect = self.image.get_rect()

        # start each new alien near top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store alien's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        # draw alien at its current location
        self.screen.blit(self.image, self.rect)