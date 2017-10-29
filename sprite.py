import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
MCYELLOW = (226, 179, 9)


class Player(pygame.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # Instead we could load a proper pciture of a car...
        self.image = pygame.image.load("BoySprite3.png").convert_alpha()

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
        self.image = pygame.image.load("chickenSmall.png").convert_alpha()

        self.rect = self.image.get_rect()

    def fall(self, pixels):
        self.rect.y += pixels

class Burger(pygame.sprite.Sprite):
    def __init__(self, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # Draw the car (a rectangle!)
        self.image = pygame.image.load("burger.png").convert_alpha()

        self.rect = self.image.get_rect()

    def fall(self, pixels):
        self.rect.y += pixels

class apple(pygame.sprite.Sprite):
    def __init__(self, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # Draw the car (a rectangle!)
        self.image = pygame.image.load("apple.png").convert_alpha()

        self.rect = self.image.get_rect()

    def fall(self, pixels):
        self.rect.y += pixels

class Fries(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(MCYELLOW)
        self.image.set_colorkey(MCYELLOW)

        self.image = pygame.image.load("FriesSprite.png").convert_alpha()

        self.rect = self.image.get_rect()

    def fall(self, pixels):
        self.rect.y += pixels

class Spinach(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(MCYELLOW)
        self.image.set_colorkey(MCYELLOW)

        self.image = pygame.image.load("spinach2.png").convert_alpha()

        self.rect = self.image.get_rect()

    def fall(self, pixels):
        self.rect.y += pixels

class pear(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(MCYELLOW)
        self.image.set_colorkey(MCYELLOW)

        self.image = pygame.image.load("pear2.png").convert_alpha()

        self.rect = self.image.get_rect()

    def fall(self, pixels):
        self.rect.y += pixels

class cookie(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(MCYELLOW)
        self.image.set_colorkey(MCYELLOW)

        self.image = pygame.image.load("cookie2.png").convert_alpha()

        self.rect = self.image.get_rect()

    def fall(self, pixels):
        self.rect.y += pixels

class cherry(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(MCYELLOW)
        self.image.set_colorkey(MCYELLOW)

        self.image = pygame.image.load("cherry2.png").convert_alpha()

        self.rect = self.image.get_rect()

    def fall(self, pixels):
        self.rect.y += pixels