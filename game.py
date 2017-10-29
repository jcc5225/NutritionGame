#!/usr/bin/python -tt

import pygame
import random
from sprite import Car
from sprite import Chicken
from sprite import Fries

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
MCYELLOW = ( 226, 179, 9)

WIDTH = 400
HEIGHT = 500



def main():
    pygame.init()

    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Nutrition Game")

    carryOn = True

    clock = pygame.time.Clock()

    all_sprites_list = pygame.sprite.Group()

    playerCar = Car(RED, 20, 30)
    playerCar.rect.x = WIDTH/2
    playerCar.rect.y = 450
    sprite1 = Chicken(16, 16)
    sprite1.rect.x , sprite1.rect.y = random.randrange(0,WIDTH-16), 0
    sprite2 = Fries(6, 10)
    sprite2.rect.x, sprite2.rect.y = random.randrange(0,WIDTH-6), 0
    all_sprites_list.add(playerCar)
    all_sprites_list.add(sprite1)
    all_sprites_list.add(sprite2)

    while carryOn:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                carryOn = False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: #Pressing 'x' Key will quit
                     carryOn=False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and playerCar.rect.x > 0:

            playerCar.moveLeft(5)
        if keys[pygame.K_RIGHT] and playerCar.rect.x < (WIDTH - 20):
            playerCar.moveRight(5)

        sprite1.fall(1)
        sprite2.fall(2)


        screen.fill(MCYELLOW)


        all_sprites_list.update()

        all_sprites_list.draw(screen)
        pygame.display.flip()

        clock.tick(60)


    pygame.quit()

if __name__ == '__main__':
    main()
