import pygame
import game

def isMouseOn(mousePos, rect):
    return rect.x <= mousePos[0] <= rect.x + rect.w and rect.y <= mousePos[1] <= rect.y + rect.h

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
    pygame.mouse.set_cursor(pygame.cursors.arrow)

    screen.blit(main_screen, (0, 0))
    play_button_Rect = play_button.get_rect()
    play_button_Rect.x = 220
    play_button_Rect.y = 700

    buttonOnSound = pygame.mixer.Sound("sound/buttonOn.ogg")
    gamePlaySound = pygame.mixer.Sound("sound/gamePlay.ogg")

    main_menu = True
    sound = False
    keep_sound = False

    while main_menu:
        mousePosition = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type  == pygame.QUIT:
                main_menu = False

        if sound == True and keep_sound == False:
            buttonOnSound.play()
            keep_sound = True

        if isMouseOn(mousePosition, play_button_Rect):
            sound = True
            screen.blit(play_button, play_button_Rect)
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu = False
                gamePlaySound.play()
                game.play(screen)
        else:
            sound = False
            keep_sound = False
            screen.blit(play_button2, play_button_Rect)
        pygame.display.flip() # pygame.display.update()
        # clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()