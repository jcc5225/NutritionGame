#!/usr/bin/python -tt

import pygame
import random
from sprite import Player
from sprite import Chicken
from sprite import Fries

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
MCYELLOW = ( 226, 179, 9)
BROWN = (153, 76, 0)

WIDTH = 700
HEIGHT = 300

playerScore = 0



def main():
    pygame.init()

    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Nutrition Game")

    carryOn = True

    clock = pygame.time.Clock()

    all_sprites_list = pygame.sprite.Group()

    player = Player(15, 25)
    player.rect.x = WIDTH/2
    player.rect.y = HEIGHT - 25 - 30
    all_sprites_list.add(player)

    while carryOn:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                carryOn = False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: #Pressing 'x' Key will quit
                     carryOn=False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.rect.x > 0:
            player.moveLeft(5)

        if keys[pygame.K_RIGHT]:
            player.moveRight(5)

        if player.rect.x >= WIDTH - 15:
            carryOn = False


        screen.fill(MCYELLOW)
        pygame.draw.rect(screen, BROWN, [0, 270, WIDTH, 270],0)
        all_sprites_list.update()
        all_sprites_list.draw(screen)
        pygame.display.flip()

        clock.tick(60)

    carryOn = True
    player.rect.x = 0
    while carryOn:

        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                carryOn = False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: #Pressing 'x' Key will quit
                     carryOn=False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.rect.x > 0:
            player.moveLeft(5)

        if keys[pygame.K_RIGHT] and player.rect.x <= WIDTH-15:
            player.moveRight(5)


        screen.fill(MCYELLOW)
        pygame.draw.rect(screen, BROWN, [0, 270, WIDTH, 270],0)
        all_sprites_list.update()
        all_sprites_list.draw(screen)
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
