import pygame
from src.components.menu import Menu
from src.styles.theme import COLORS
from sys import exit


def main():

    pygame.init()

    width = 1280
    height = 720

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Main Menu')

    clock = pygame.time.Clock()
    FPS = 60

    playing = True

    while playing:

        clock.tick(FPS)
        screen.fill(COLORS["primary"])
        Menu(screen).display_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()


if __name__ == "__main__":
    main()
