import pygame

pygame.init()

width = 1000
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Main Menu')

clock = pygame.time.Clock()
FPS = 60
WHITE = (255, 255, 255)


def draw_buttom(name_buttom, positionX, positiony):
    font = pygame.font.SysFont('arial', 50)
    text = font.render(name_buttom, True, WHITE)
    align_text = text.get_rect(center=(positionX, positiony))
    screen.blit(text, align_text)


def display_menu():
    draw_buttom("Jogar", 520, 100)
    draw_buttom("Instruções", 520, 200)
    draw_buttom("Ligar/Desligar", 520, 300)
    draw_buttom("Som", 520, 400)


playing = True


while playing:
    clock.tick(FPS)

    display_menu()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print('Mudar de Tela')

    pygame.display.update()

pygame.quit()
