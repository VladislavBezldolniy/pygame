import pygame


# ИГРОК
PLAYER_WIDTH = 20
PLAYER_HEIGHT = 20
PLAYER_SPEED = 6


# Colors

WHITE = (255, 255, 255)
RED = (140, 7, 0)
BACK = (61, 56, 59)

# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60


class Player(pygame.sprite.Sprite):

    # Функция конструктор
    def __init__(self, x, y):
        # Вызов метовдов класса родителя
        pygame.sprite.Sprite.__init__(self)

        # Создаем спрайт
        self.image = pygame.Surface([PLAYER_WIDTH, PLAYER_HEIGHT])
        self.image.fill(WHITE)

        # указываем на x, y
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        self.change_x = 0
        self.change_y = 0
        self.walls = None

    def changespeed(self, x, y):
        # Приводим в движение
        self.change_x += x
        self.change_y += y

    def update(self):
        # влево/вправо
        self.rect.x += self.change_x

        # Врезание в стену <-->
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # врезаемся при движении вправо
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # -//- влево
                self.rect.left = block.rect.right

        # Вверх/вниз
        self.rect.y += self.change_y

        # Проверка столкновений
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:

            # Обновление позиции
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom


class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):

        # вызов метода родителя
        pygame.sprite.Sprite.__init__(self)

        # выставляем высоту, ширину и цвет
        self.image = pygame.Surface([width, height])
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


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

    screen.fill(BACK)

    all_sprite_list.draw(screen)  # отрисовуем все спрайты из списка методм draw

    # or use flip to update full surface
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
