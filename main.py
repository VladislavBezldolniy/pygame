import pygame
from player import *
from walls import *

# ИГРОК

PLAYER_SPEED = 6

# Сolor

BLACK = (0, 15, 0)


# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60


# инициализируем pygames
pygame.init()

# создаем экран
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# название окна
pygame.display.set_caption('Test 3')

# Список со всеми спрайтами
all_sprite_list = pygame.sprite.Group()

# создание блоков-стен (x, y, width, height) список для отрисовки всех спрайтов
wall_list = pygame.sprite.Group()

wall = Wall(0, 0, 10, 600)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(10, 0, 790, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(10, 200, 600, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(10, 400, 600, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(750, 0, 10, 600)
wall_list.add(wall)
all_sprite_list.add(wall)

# создаем обьект player класса Player(x, y) --> и задаем стартовое положение
player = Player(50, 50)
player.walls = wall_list

all_sprite_list.add(player)

clock = pygame.time.Clock()

done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-PLAYER_SPEED, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(PLAYER_SPEED, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -PLAYER_SPEED)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, PLAYER_SPEED)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(PLAYER_SPEED, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-PLAYER_SPEED, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, PLAYER_SPEED)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -PLAYER_SPEED)

    all_sprite_list.update()

    screen.fill(BLACK)

    all_sprite_list.draw(screen)  # отрисовуем все спрайты из списка методм draw

    # or use flip to update full surface
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
