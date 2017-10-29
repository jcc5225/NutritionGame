import pygame
import random
from sprite import Player
from sprite import Chicken
from sprite import Fries
from sprite import Burger
from sprite import apple
from sprite import cherry
from sprite import Spinach
from sprite import pear
from sprite import cookie

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
MCYELLOW = ( 226, 179, 9)
BROWN = (153, 76, 0)

WIDTH = 700
HEIGHT = 300




def main():
    pygame.init()

    obesityLevel = 5
    flagger = 30
    flag2 = 0

    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Nutrition Game")

    carryOn = True

    clock = pygame.time.Clock()

    title = pygame.image.load('StartLogo.png')
    subtitle = pygame.image.load('Subtitle.png')

    all_sprites_list = pygame.sprite.Group()
    bad_foods_list = pygame.sprite.Group()
    good_foods_list = pygame.sprite.Group()

    font = pygame.font.Font(None, 15)
    text = font.render("HEALTH", 1, (10, 10, 10))

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
            player.moveLeft(4)

        if keys[pygame.K_UP] and player.rect.x > 0 and flag2 == 0:
            flag2 = 1

        if flagger <= 30 and flagger > 15 and flag2 == 1:
            flagger -= 1
            player.jump(5)
        elif flagger <= 15 and flagger != 0 and flag2 == 1:
            flagger -= 1
            player.jump(-5)
        elif flagger == 0 and flag2 == 1:
            flagger = 30
            flag2 = 0

        if keys[pygame.K_RIGHT]:
            player.moveRight(4)

        if player.rect.x >= WIDTH - 15:
            carryOn = False


        screen.fill(MCYELLOW)
        screen.blit(title, (110, 75))
        screen.blit(subtitle, (200, 130))
        pygame.draw.rect(screen, BROWN, [0, 270, WIDTH, 270],0)
        all_sprites_list.update()
        all_sprites_list.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    sprite1 = Chicken(32, 32)
    sprite1.rect.x = 125
    sprite1.rect.y = 250
    all_sprites_list.add(sprite1)
    bad_foods_list.add(sprite1)
    sprite2 = Fries(32, 32)
    sprite2.rect.x = 40
    sprite2.rect.y = 210
    all_sprites_list.add(sprite2)
    bad_foods_list.add(sprite2)
    sprite3 = Burger(32, 32)
    sprite3.rect.x = 400
    sprite3.rect.y = 250
    all_sprites_list.add(sprite3)
    bad_foods_list.add(sprite3)
    sprite4 = apple(32, 32)
    sprite4.rect.x = 210
    sprite4.rect.y = 250
    good_foods_list.add(sprite4)
    all_sprites_list.add(sprite4)
    sprite5 = cherry(32, 32)
    sprite5.rect.x = 295
    sprite5.rect.y = 210
    all_sprites_list.add(sprite5)
    good_foods_list.add(sprite5)
    sprite6 = pear(32, 32)
    sprite6.rect.x = 470
    sprite6.rect.y = 200
    all_sprites_list.add(sprite6)
    good_foods_list.add(sprite6)
    sprite7 = Spinach(32, 32)
    sprite7.rect.x = 570
    sprite7.rect.y = 250
    all_sprites_list.add(sprite7)
    good_foods_list.add(sprite7)
    sprite8 = cookie(32, 32)
    sprite8.rect.x = 750
    sprite8.rect.y = 210
    all_sprites_list.add(sprite8)
    bad_foods_list.add(sprite8)
    carryOn = True
    player.rect.x = 0
    direction  = 1
    while carryOn:

        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                carryOn = False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: #Pressing 'x' Key will quit
                     carryOn=False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.rect.x > 0:
            player.moveLeft(4)

        if keys[pygame.K_RIGHT]:
            player.moveRight(4)
            if direction < 0:
                player.image = pygame.transform.flip(player.image, True, False)
                direction = 1

        if keys[pygame.K_UP] and player.rect.x > 0 and flag2 == 0:
            flag2 = 1

        if flagger <= 30 and flagger > 15 and flag2 == 1:
            flagger -= 1
            player.jump(5)
        elif flagger <= 15 and flagger != 0 and flag2 == 1:
            flagger -= 1
            player.jump(-5)
        elif flagger == 0 and flag2 == 1:
            flagger = 30
            flag2 = 0

        if keys[pygame.K_RIGHT]:
            player.moveRight(4)

        screen.fill(MCYELLOW)

        screen.blit(text, (WIDTH - 100 ,0))
        pygame.draw.rect(screen, BLACK, [WIDTH - 50, 1, obesityLevel*5, 6])
        pygame.draw.rect(screen, BROWN, [0, 270, WIDTH, 270],0)
        all_sprites_list.update()
        all_sprites_list.draw(screen)
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()