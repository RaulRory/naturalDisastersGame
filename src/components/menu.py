import pygame
from src.styles.theme import COLORS
from .button import Button
from src.screens.screens import Screens


class Menu():
    def __init__(self, screen) -> None:
        self.__screen = screen
        self.__position_mouse = None

    def __update_image(self, buttons) -> None:
        for button in buttons:
            button.update(self.__screen)

    def display_menu(self):
        pygame.mixer.music.load("src/sound/music.mp3")
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play()
        is_enabled = True
        title = Button(None, "DISASTER", 640, 80, 1, 50, COLORS["black"])
        play = Button(pygame.image.load("src/imgs/background_buttom.png"), "Jogar", 640, 200, 0.7)
        instructions = Button(pygame.image.load("src/imgs/background_buttom.png"), "Instruções", 640, 320, 0.7)
        sound = Button(pygame.image.load("src/imgs/background_buttom.png"), "Configurações", 640, 440, 0.7)

        self.__update_image([title, play, instructions, sound])
        running = True

        while running:
            self.__position_mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play.checkForInput(self.__position_mouse):
                        Screens(self.__screen).first_phase()
                    if instructions.checkForInput(self.__position_mouse):
                        Screens(self.__screen).instructions()
                    if sound.checkForInput(self.__position_mouse):
                        Screens(self.__screen).config_sound(is_enabled)

            pygame.display.update()
