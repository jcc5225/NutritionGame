import pygame

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
MCYELLOW = ( 226, 179, 9)


class Player(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # Instead we could load a proper pciture of a car...
        self.image = pygame.image.load("images/BoySprite3.png").convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels

    def jump(self, pixels):
        self.rect.y -= pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels


class Chicken(pygame.sprite.Sprite):
    def __init__(self, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # Draw the car (a rectangle!)
        self.image = pygame.image.load("images/chickenSmall.png").convert_alpha()

        self.rect = self.image.get_rect()

    def fall(self, pixels):
        self.rect.y += pixels


class Fries(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(MCYELLOW)
        self.image.set_colorkey(MCYELLOW)

        self.image = pygame.image.load("images/FriesSprite.png").convert_alpha()

        self.rect = self.image.get_rect()

    def fall(self, pixels):
        self.rect.y += pixels
