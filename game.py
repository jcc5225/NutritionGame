#!/usr/bin/python -tt

import pygame
from sprite import Car

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)



def main():
    pygame.init()

    size = (700, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Nutrition Game")

    carryOn = True

    clock = pygame.time.Clock()

    all_sprites_list = pygame.sprite.Group()

    playerCar = Car(RED, 20, 30)
    playerCar.rect.x = 350
    playerCar.rect.y = 450
    all_sprites_list.add(playerCar)

    while carryOn:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                carryOn = False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: #Pressing the x Key will quit the game
                     carryOn=False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            playerCar.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            playerCar.moveRight(5)
            
            # First, clear the screen to white.
        screen.fill(WHITE)
            #The you can draw different shapes and lines or add text to your background stage.
        pygame.draw.rect(screen, RED, [55, 200, 100, 70],0)
        pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
        pygame.draw.ellipse(screen, BLACK, [20,20,250,100], 2)

        all_sprites_list.update()

        all_sprites_list.draw(screen)
        pygame.display.flip()

        clock.tick(60)


    pygame.quit()

if __name__ == '__main__':
    main()
