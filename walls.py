import pygame

# Colors
RED = (140, 7, 0)


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
