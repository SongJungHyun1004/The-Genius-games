import pygame
import piece

def batch(screen):
    box = [[]]
    sang = piece.Sang(119, 641)
    king = piece.King(282, 641)
    jang = piece.Jang(445, 641)
    ja = piece.Ja(282, 479)

    screen.blit(jang.object, jang.rect)
    screen.blit(king.object, king.rect)
    screen.blit(sang.object, sang.rect)
    screen.blit(ja.object, ja.rect)

def play(screen):
    inplay_screen = pygame.image.load("img/inplay_screen.png")
    board = pygame.image.load("img/board.png")
    screen.blit(inplay_screen, (0, 0))
    screen.blit(board, (110, 145))
    batch(screen)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type  == pygame.QUIT:
                running = False

        pygame.display.flip()