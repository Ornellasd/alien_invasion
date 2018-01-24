import pygame 
from pygame.sprite import Sprite

class Star(Sprite):
## a class to represent background stars.

    def __init__(self, screen):
        super().__init__()
        self.screen = screen

        # load the star image and set its rect attributes
        self.image = pygame.image.load('images/scaled_star.png')
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x) 

    def blitme(self):
        self.screen.blit(self.image, self.rect)