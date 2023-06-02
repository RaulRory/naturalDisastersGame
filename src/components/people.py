import pygame
import random
from pygame.sprite import Sprite


class People(Sprite):
    def __init__(self, character):
        super().__init__()
        scale = 1.2
        self.__character = character
        self.__sprite = pygame.image.load('src/imgs/femalePlayer.png')
        self.__pos_init = random.randrange(50, 720 - 100)
        self.__velocity = random.randrange(1, 7)
        self.__sprite_list = []
        for index in range(4):
            character_image = self.__sprite.subsurface((index * 57.25, 60), (57.25, 73))
            character_image = pygame.transform.scale(character_image, (int(character_image.get_width() * scale), (int(character_image.get_height() * scale))))
            self.__sprite_list.append(character_image)

        self.index_initial_character = 0
        self.image = self.__sprite_list[self.index_initial_character]
        self.rect = self.image.get_rect(x=280, y=self.__pos_init)
        self.rect.y = random.randrange(50, 720 - 100)

    def __reborn(self):
        self.rect.x = 1280
        self.rect.y = random.randrange(50, 720 - 80)
        self.__velocity = random.randrange(2, 7)

    def update(self):
        if self.rect.topright[0] < 0:
            self.__reborn()
        elif self.rect.colliderect(self.__character):
            self.__reborn()
            self.__character.points += 50
        self.rect.x -= self.__velocity
