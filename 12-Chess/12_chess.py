import pygame
import game

def isMouseOn(mousePos, buttonPos, button_size):
    return buttonPos[0] <= mousePos[0] <= buttonPos[0] + button_size[0] and buttonPos[1] <= mousePos[1] <= buttonPos[1] + button_size[1]

def main():
    SCREEN_WIDTH = 708
    SCREEN_HEIGHT = 940

    pygame.init()
    # clock = pygame.time.Clock()
    # FPS = 30

    icon = pygame.image.load("img/12chess_icon.png")
    main_screen = pygame.image.load("img/main_screen.png")
    play_button = pygame.image.load("img/play_button.png")
    play_button2 = pygame.image.load("img/play_button2.png")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_icon(icon)
    pygame.display.set_caption("십이장기 12-Chess")

    screen.blit(main_screen, (0, 0))
    play_button_position = (220, 700)
    play_button_size = play_button.get_rect().size
    screen.blit(play_button, play_button_position)
    pygame.display.flip()
    running = True

    while running:
        mousePosition = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type  == pygame.QUIT:
                running = False

        if isMouseOn(mousePosition, play_button_position, play_button_size):
            if event.type == pygame.MOUSEBUTTONDOWN:
                game.play(screen)
            screen.blit(play_button2, play_button_position)
        else:
            screen.blit(play_button, play_button_position)
        pygame.display.flip() # pygame.display.update()
        # clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()