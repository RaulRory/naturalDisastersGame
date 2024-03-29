import pygame
import os.path
from pygame.sprite import Sprite
from src.styles.theme import COLORS
from src.components.button import Button
from src.components.character import Character
from src.components.people import People
from src.components.rain import Rain


class BackGround(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.scale = 1.2
        self.__screen = screen
        self.image = pygame.image.load('src/imgs/background.png')
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * self.scale) , (int(self.image.get_height() * self.scale))))
        self.rect = self.image.get_rect()

    def update(self):
        self.__screen.blit(self.image, (int(self.image.get_width()) + self.rect.x, 0))
        if self.rect.x == -int(self.image.get_width()):
            self.__screen.blit(self.image, (int(self.image.get_width()) + self.rect.x, 0))
            self.rect.x = 0
        self.rect.x -= 3

class Screens():
    def __init__(self, screen) -> None:
        self.__screen = screen
        self.__position_mouse = None

    def first_phase(self):

        background = BackGround(self.__screen)
        protagonist = Character(self.__screen)
        people = People(protagonist)

        inimy_1 = Rain(protagonist)
        inimy_2 = Rain(protagonist)
        inimy_3 = Rain(protagonist)
        sprites = pygame.sprite.Group()
        sprites.add(background, protagonist, people, inimy_1, inimy_2, inimy_3)
        running = True
        while running:
            pygame.time.Clock().tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            if protagonist.life == 0:
                self.__game_over(protagonist.points)
            protagonist.animate()
            sprites.draw(self.__screen)
            sprites.update()
            pygame.display.flip()

    def __game_over(self, points):
        title = pygame.font.Font("src/fonts/font.ttf", 20).render("GameOver", True, COLORS["black"])
        punctuation = pygame.font.Font("src/fonts/font.ttf", 20).render("Pontuação", True, COLORS["black"])
        point = pygame.font.Font("src/fonts/font.ttf", 20).render(f"{points} Pontos", True, COLORS["black"])
        

        self.__screen.fill(COLORS["primary"])
        self.__screen.blit(title, (560, 50))
        self.__screen.blit(punctuation, (560, 200))
        self.__screen.blit(point, (560, 260))

        try_again = Button(pygame.image.load("src/imgs/background_buttom.png"), "Tentar Novamente", 640, 440, 1)

        try_again.update(self.__screen)

        running = True
        while running:
            self.__position_mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if try_again.checkForInput(self.__position_mouse):
                        with open("src/files/POINTS.txt", 'a') as file_points:
                            file_points.write(f"Pontuação do Jogador(a) da vez: {points}")

                        self.first_phase()

            pygame.display.update()

    def config_sound(self, is_enabled):
        title_font = pygame.font.Font("src/fonts/font.ttf", 40)
        title = title_font.render("Configurações", True, COLORS["black"])
        config_button = Button(pygame.image.load("src/imgs/background_buttom.png"), "Ligar/Desligar", 640, 320, 1)

        self.__screen.fill(COLORS["primary"])
        self.__screen.blit(title, (360, 50))
        config_button.update(self.__screen)

        while True:
            self.__position_mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN and config_button.checkForInput(self.__position_mouse):
                    if is_enabled:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()

            pygame.display.update()

    def instructions(self):
        title = pygame.font.Font("src/fonts/font.ttf", 40).render("Instruções", True, COLORS["black"])
        line_1 = pygame.font.Font("src/fonts/font.ttf", 16).render("O objetivo do jogo é desviar dos obstáculos e ", True, COLORS["black"])
        line_2 = pygame.font.Font("src/fonts/font.ttf", 16).render("salvar as vítimas dessa triste enchente.", True, COLORS["black"]) 
        line_3 = pygame.font.Font("src/fonts/font.ttf", 16).render("Você deve usar as setas do teclado", True, COLORS["black"])
        line_4 = pygame.font.Font("src/fonts/font.ttf", 16).render("para salvar as vítimas.", True, COLORS["black"])

        play = Button(pygame.image.load("src/imgs/background_buttom.png"), "Jogar", 640, 520, 1)

        self.__screen.fill(COLORS["primary"])
        self.__screen.blit(title, (460, 20))
        self.__screen.blit(line_1, (360, 150))
        self.__screen.blit(line_2, (360, 200))
        self.__screen.blit(line_3, (360, 250))
        self.__screen.blit(line_4, (360, 300))

        play.update(self.__screen)

        while True:
            self.__position_mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN and play.checkForInput(self.__position_mouse):
                    self.first_phase()

            pygame.display.update()

    def ranking(self):
        title = pygame.font.Font("src/fonts/font.ttf", 40).render("Ranking Jogadores", True, COLORS["black"])
        play = Button(pygame.image.load("src/imgs/background_buttom.png"), "Jogar", 640, 520, 1)

        check_file = os.path.exists("src/files/POINTS.txt")
        data_file = None
        if(check_file):
            with open("src/files/POINTS.txt", 'r') as file_points:
                points = file_points.readlines()
                
                for line in points:
                    data_file = pygame.font.Font("src/fonts/font.ttf", 16).render(line, True, COLORS["black"])
                    
        self.__screen.fill(COLORS["primary"])
        self.__screen.blit(title, (340, 20))
        if(check_file):
            self.__screen.blit(data_file, (360, 150))
        play.update(self.__screen)
        
        while True:
            self.__position_mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN and play.checkForInput(self.__position_mouse):
                    self.first_phase()

            pygame.display.update()

