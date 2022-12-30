import pygame
import piece

inplay_screen = pygame.image.load("img/inplay_screen.png")
board_img = pygame.image.load("img/board.png")
board_Rect = board_img.get_rect()
board_Rect.x = round((inplay_screen.get_rect().w - board_Rect.w) / 2)
board_Rect.y = round((inplay_screen.get_rect().h - board_Rect.h) / 2)

board_block = round(board_Rect.w/3)
piece_block = pygame.image.load("img/ja_green.png").get_rect().w
offset = round((board_block - piece_block)/2)
first = (board_Rect.x + offset, board_Rect.y + offset)
board = [
    [first] * 4
    for _ in range(3)
]
def get_firstPosition():
    board_block = round(board_Rect.w / 3)
    piece_block = pygame.image.load("img/ja_green.png").get_rect().w
    offset = round((board_block - piece_block) / 2)
    first = (board_Rect.x + offset, board_Rect.y + offset)
    return first

def batch(screen):
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] = tuple(sum(e) for e in zip(board[i][j], (board_block*i, board_block*j)))

    global sang, jang, king, ja
    global enemy_sang, enemy_jang, enemy_king, enemy_ja
    sang_x, sang_y = board[0][3]
    king_x, king_y = board[1][3]
    jang_x, jang_y = board[2][3]
    ja_x, ja_y = board[1][2]
    sang = piece.Sang("green", sang_x, sang_y)
    king = piece.King("green", king_x, king_y)
    jang = piece.Jang("green", jang_x, jang_y)
    ja = piece.Ja("green", ja_x, ja_y, hu=False)

    enemy_jang_x, enemy_jang_y = board[0][0]
    enemy_king_x, enemy_king_y = board[1][0]
    enemy_sang_x, enemy_sang_y = board[2][0]
    enemy_ja_x, enemy_ja_y = board[1][1]
    enemy_sang = piece.Sang("red", enemy_sang_x, enemy_sang_y)
    enemy_king = piece.King("red", enemy_king_x, enemy_king_y)
    enemy_jang = piece.Jang("red", enemy_jang_x, enemy_jang_y)
    enemy_ja = piece.Ja("red", enemy_ja_x, enemy_ja_y, hu=False)

    screen.blit(jang.object, jang.rect)
    screen.blit(king.object, king.rect)
    screen.blit(sang.object, sang.rect)
    screen.blit(ja.object, ja.rect)

    screen.blit(enemy_jang.object, enemy_jang.rect)
    screen.blit(enemy_king.object, enemy_king.rect)
    screen.blit(enemy_sang.object, enemy_sang.rect)
    screen.blit(enemy_ja.object, enemy_ja.rect)

def fixedPosition(mousePos):
    x, y = mousePos[0], mousePos[1]
    if board_Rect.x <= x <= board_Rect.x + board_Rect.w and board_Rect.y <= y <= board_Rect.y + board_Rect.h:
        for i in range(len(board)):
            for j in range(len(board[0])):
                x2, y2 = board_Rect.x + board_block*i, board_Rect.y + board_block*j
                if x2 <= x <= x2 + piece_block and y2 <= y <= y2 + piece_block:
                    # x, y = board[i][j]
                    x, y = i, j
    else:
        x, y = -1, -1

    return x, y

def play(screen):

    screen.blit(inplay_screen, (0, 0))
    screen.blit(board_img, board_Rect)
    batch(screen)

    running = True
    turn = "green"

    while running:
        mousePosition = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type  == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                fixed_x, fixed_y = fixedPosition(mousePosition)

                # if turn == "green":
                #
                # elif turn == "red":




        pygame.display.flip()