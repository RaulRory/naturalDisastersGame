import pygame
import random
from pygame.sprite import Sprite


class Rain(Sprite):
    def __init__(self, character):
        super().__init__()
        scale = 0.1
        self.__character = character
        self.__sprite = pygame.image.load('src/imgs/inimy.jpeg')
        self.__sprite = pygame.transform.scale(self.__sprite, (int(self.__sprite.get_width() * scale), (int(self.__sprite.get_height() * scale))))
        self.__pos_init = random.randrange(50, 720 - 100)
        self.__velocity = random.randrange(1, 7)
        self.image = self.__sprite
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
            self.__character.life -= 1
        self.rect.x -= self.__velocity
