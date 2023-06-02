from src.styles.theme import COLORS

import pygame


class Button():
    def __init__(self, image: str, text_button: str, positionX: int, positionY: int, scale: int, sizeFont: int = 20, colorFont: str = COLORS["white"]) -> None:
        self._image_width = image.get_width() if image is not None else positionX
        self._image_heigth = image.get_height() if image is not None else positionY
        self.text = pygame.font.Font("src/fonts/font.ttf", sizeFont).render(text_button, True, colorFont)
        self.image = pygame.transform.scale(image, (int(self._image_width * scale), (int(self._image_heigth * scale)))) if image is not None else self.text
        self.rect = self.image.get_rect(center=(positionX, positionY))
        self.text_rect = self.text.get_rect(center=(positionX, positionY))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
