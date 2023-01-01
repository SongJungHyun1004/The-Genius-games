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
for i in range(len(board)):
    for j in range(len(board[0])):
        board[i][j] = tuple(sum(e) for e in zip(board[i][j], (board_block * i, board_block * j)))

def get_firstPosition():
    board_block = round(board_Rect.w / 3)
    piece_block = pygame.image.load("img/ja_green.png").get_rect().w
    offset = round((board_block - piece_block) / 2)
    first = (board_Rect.x + offset, board_Rect.y + offset)
    return first

def generate():
    global sang, jang, king, ja
    global enemy_sang, enemy_jang, enemy_king, enemy_ja

    sang = piece.Sang("green", 0, 3, selected=False)
    king = piece.King("green", 1, 3, selected=False)
    jang = piece.Jang("green", 2, 3, selected=False)
    ja = piece.Ja("green", 1, 2, hu=False, selected=False)

    enemy_jang = piece.Jang("red", 0, 0, selected=False)
    enemy_king = piece.King("red", 1, 0, selected=False)
    enemy_sang = piece.Sang("red", 2, 0, selected=False)
    enemy_ja = piece.Ja("red", 1, 1, hu=False, selected=False)

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
        x, y = -10, -10

    return x, y

# def isThereMyPiece():
#     if

def draw(screen):
    screen.blit(board_img, board_Rect)
    screen.blit(jang.object, board[jang.rect.x][jang.rect.y])
    screen.blit(king.object, board[king.rect.x][king.rect.y])
    screen.blit(sang.object, board[sang.rect.x][sang.rect.y])
    screen.blit(ja.object, board[ja.rect.x][ja.rect.y])

    screen.blit(enemy_jang.object, board[enemy_jang.rect.x][enemy_jang.rect.y])
    screen.blit(enemy_king.object, board[enemy_king.rect.x][enemy_king.rect.y])
    screen.blit(enemy_sang.object, board[enemy_sang.rect.x][enemy_sang.rect.y])
    screen.blit(enemy_ja.object, board[enemy_ja.rect.x][enemy_ja.rect.y])

def play(screen):
    screen.blit(inplay_screen, (0, 0))
    generate()

    running = True
    turn = "green"

    while running:
        mousePosition = pygame.mouse.get_pos()
        draw(screen)

        for event in pygame.event.get():
            if event.type  == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                fixed_x, fixed_y = fixedPosition(mousePosition)

                moved = False
                if turn == "green":
                    if sang.selected and sang.color == "green":
                        if abs(fixed_x-sang.rect.x) == 1 and abs(fixed_y-sang.rect.y) == 1:
                            sang.move(fixed_x, fixed_y)
                            moved = True
                    if jang.selected and jang.color == "green":
                        if abs(fixed_x-jang.rect.x) + abs(fixed_y-jang.rect.y) == 1:
                            jang.move(fixed_x, fixed_y)
                            moved = True
                    if king.selected and king.color == "green":
                        if (abs(fixed_x-king.rect.x) == 1 and abs(fixed_y-king.rect.y) == 1) or abs(fixed_x-king.rect.x) + abs(fixed_y-king.rect.y) == 1:
                            king.move(fixed_x, fixed_y)
                            moved = True
                    if ja.selected and ja.color == "green":
                        if ja.hu:
                            if abs(fixed_x - ja.rect.x) + abs(
                                    fixed_y - ja.rect.y) == 1 or ja.rect.y - fixed_y== 1:
                                ja.move(fixed_x, fixed_y)
                                moved = True
                        else:
                            if fixed_x - ja.rect.x == 0 and ja.rect.y - fixed_y== 1:
                                ja.move(fixed_x, fixed_y)
                                if fixed_y == 0:
                                    ja.hu = True
                                    ja.change()
                                moved = True
                    if enemy_sang.selected and enemy_sang.color == "green":
                        if abs(fixed_x-enemy_sang.rect.x) == 1 and abs(fixed_y-enemy_sang.rect.y) == 1:
                            enemy_sang.move(fixed_x, fixed_y)
                            moved = True
                    if enemy_jang.selected and enemy_jang.color == "green":
                        if abs(fixed_x-enemy_jang.rect.x) + abs(fixed_y-enemy_jang.rect.y) == 1:
                            enemy_jang.move(fixed_x, fixed_y)
                            moved = True
                    if enemy_king.selected and enemy_king.color == "green":
                        if (abs(fixed_x-enemy_king.rect.x) == 1 and abs(fixed_y-enemy_king.rect.y) == 1) or abs(fixed_x-enemy_king.rect.x) + abs(fixed_y-enemy_king.rect.y) == 1:
                            enemy_king.move(fixed_x, fixed_y)
                            moved = True
                    if enemy_ja.selected and enemy_ja.color == "green":
                        if enemy_ja.hu:
                            if abs(fixed_x - enemy_ja.rect.x) + abs(
                                    fixed_y - enemy_ja.rect.y) == 1 or enemy_ja.rect.y - fixed_y== 1:
                                enemy_ja.move(fixed_x, fixed_y)
                                moved = True
                        else:
                            if fixed_x - enemy_ja.rect.x == 0 and enemy_ja.rect.y - fixed_y== 1:
                                enemy_ja.move(fixed_x, fixed_y)
                                if fixed_y == 0:
                                    enemy_ja.hu = True
                                    enemy_ja.change()
                                moved = True

                    if moved:
                        turn = "red"
                    else:
                        sang.select(fixed_x, fixed_y)
                        jang.select(fixed_x, fixed_y)
                        king.select(fixed_x, fixed_y)
                        ja.select(fixed_x, fixed_y)
                        enemy_sang.select(fixed_x, fixed_y)
                        enemy_jang.select(fixed_x, fixed_y)
                        enemy_king.select(fixed_x, fixed_y)
                        enemy_ja.select(fixed_x, fixed_y)

                elif turn == "red":
                    if enemy_sang.selected and enemy_sang.color == "red":
                        if abs(fixed_x - enemy_sang.rect.x) == 1 and abs(fixed_y - enemy_sang.rect.y) == 1:
                            enemy_sang.move(fixed_x, fixed_y)
                            moved = True
                    if enemy_jang.selected and enemy_jang.color == "red":
                        if abs(fixed_x - enemy_jang.rect.x) + abs(fixed_y - enemy_jang.rect.y) == 1:
                            enemy_jang.move(fixed_x, fixed_y)
                            moved = True
                    if enemy_king.selected and enemy_king.color == "red":
                        if (abs(fixed_x - enemy_king.rect.x) == 1 and abs(fixed_y - enemy_king.rect.y) == 1) or abs(
                                fixed_x - enemy_king.rect.x) + abs(fixed_y - enemy_king.rect.y) == 1:
                            enemy_king.move(fixed_x, fixed_y)
                            moved = True
                    if enemy_ja.selected and enemy_ja.color == "red":
                        if enemy_ja.hu:
                            if abs(fixed_x - enemy_ja.rect.x) + abs(fixed_y - enemy_ja.rect.y) == 1  or fixed_y - enemy_ja.rect.y == 1:
                                enemy_ja.move(fixed_x, fixed_y)
                                moved = True
                        else:
                            if fixed_x - enemy_ja.rect.x == 0 and fixed_y - enemy_ja.rect.y == 1:
                                enemy_ja.move(fixed_x, fixed_y)
                                if fixed_y == 3:
                                    enemy_ja.hu = True
                                    enemy_ja.change()
                                moved = True
                    if sang.selected and sang.color == "red":
                        if abs(fixed_x - sang.rect.x) == 1 and abs(fixed_y - sang.rect.y) == 1:
                            sang.move(fixed_x, fixed_y)
                            moved = True
                    if jang.selected and jang.color == "red":
                        if abs(fixed_x - jang.rect.x) + abs(fixed_y - jang.rect.y) == 1:
                            jang.move(fixed_x, fixed_y)
                            moved = True
                    if king.selected and king.color == "red":
                        if (abs(fixed_x - king.rect.x) == 1 and abs(fixed_y - king.rect.y) == 1) or abs(
                                fixed_x - king.rect.x) + abs(fixed_y - king.rect.y) == 1:
                            king.move(fixed_x, fixed_y)
                            moved = True
                    if ja.selected and ja.color == "red":
                        if ja.hu:
                            if abs(fixed_x - ja.rect.x) + abs(fixed_y - ja.rect.y) == 1  or fixed_y - ja.rect.y == 1:
                                ja.move(fixed_x, fixed_y)
                                moved = True
                        else:
                            if fixed_x - ja.rect.x == 0 and fixed_y - ja.rect.y == 1:
                                ja.move(fixed_x, fixed_y)
                                if fixed_y == 3:
                                    ja.hu = True
                                    ja.change()
                                moved = True

                    if moved:
                        turn = "green"
                    else:
                        enemy_sang.select(fixed_x, fixed_y)
                        enemy_jang.select(fixed_x, fixed_y)
                        enemy_king.select(fixed_x, fixed_y)
                        enemy_ja.select(fixed_x, fixed_y)
                        sang.select(fixed_x, fixed_y)
                        jang.select(fixed_x, fixed_y)
                        king.select(fixed_x, fixed_y)
                        ja.select(fixed_x, fixed_y)

        pygame.display.flip()