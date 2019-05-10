import pygame

# ИГРОК
PLAYER_WIDTH = 20
PLAYER_HEIGHT = 20

# Colors
WHITE = (255, 255, 255)


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
