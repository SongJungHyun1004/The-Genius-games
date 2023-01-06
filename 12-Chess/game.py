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

global numG
global numR
numG = 1
numR = 1
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

        if (510 <= x <= 510+80 and 35 <= y <= 35+80) or (140 <= x <= 140+80 and 830 <= y <= 830+80):
            x = -1
        elif (420 <= x <= 500 and 35 <= y <= 35+80) or (230 <= x <= 310 and 830 <= y <= 830+80):
            x = -2
        elif (330 <= x <= 410 and 35 <= y <= 35+80) or (320 <= x <= 400 and 830 <= y <= 830+80):
            x = -3
        elif (240 <= x <= 320 and 35 <= y <= 35+80) or (410 <= x <= 490 and 830 <= y <= 830+80):
            x = -4
        elif (150 <= x <= 230 and 35 <= y <= 35+80) or (500 <= x <= 580 and 830 <= y <= 830+80):
            x = -5
        elif (60 <= x <= 140 and 35 <= y <= 35+80) or (590 <= x <= 670 and 830 <= y <= 830+80):
            x = -6

        else:
            x, y = -10, -10

    return x, y

def canMove(curPiece, x, y):
    global numG
    global numR
    if jang.rect.x == x and jang.rect.y == y:
        temp = jang
    elif sang.rect.x == x and sang.rect.y == y:
        temp = sang
    elif king.rect.x == x and king.rect.y == y:
        temp = king
    elif ja.rect.x == x and ja.rect.y == y:
        temp = ja
    elif enemy_jang.rect.x == x and enemy_jang.rect.y == y:
        temp = enemy_jang
    elif enemy_sang.rect.x == x and enemy_sang.rect.y == y:
        temp = enemy_sang
    elif enemy_king.rect.x == x and enemy_king.rect.y == y:
        temp = enemy_king
    elif enemy_ja.rect.x == x and enemy_ja.rect.y == y:
        temp = enemy_ja
    else:
        return True

    if temp.color == curPiece.color:
        return False
    else:
        num = 0
        if curPiece.color == "green":
            num = numG
            numG = numG + 1
        elif curPiece.color == "red":
            num = numR
            numR = numR + 1
        temp.taked(num)
        return True


def draw(screen):
    screen.blit(inplay_screen, (0, 0))
    screen.blit(board_img, board_Rect)
    if jang.rect.x < 0:
        n = -jang.rect.x
        if jang.color == "green":
            screen.blit(jang.object, (50+n*90, 830))
        elif jang.color == "red":
            screen.blit(jang.object, (600-n*90, 35))
    else:
        screen.blit(jang.object, board[jang.rect.x][jang.rect.y])
    if sang.rect.x < 0:
        n = -sang.rect.x
        if sang.color == "green":
            screen.blit(sang.object, (50+n*90, 830))
        elif sang.color == "red":
            screen.blit(sang.object, (600-n*90, 35))
    else:
        screen.blit(sang.object, board[sang.rect.x][sang.rect.y])
    if king.rect.x < 0:
        n = -king.rect.x
        if king.color == "green":
            screen.blit(king.object, (50+n*90, 830))
        elif king.color == "red":
            screen.blit(king.object, (600-n*90, 35))
    else:
        screen.blit(king.object, board[king.rect.x][king.rect.y])
    if ja.rect.x < 0:
        n = -ja.rect.x
        if ja.color == "green":
            screen.blit(ja.object, (50+n*90, 830))
        elif ja.color == "red":
            screen.blit(ja.object, (600-n*90, 35))
    else:
        screen.blit(ja.object, board[ja.rect.x][ja.rect.y])
    if enemy_sang.rect.x < 0:
        n = -enemy_sang.rect.x
        if enemy_sang.color == "green":
            screen.blit(enemy_sang.object, (50+n*90, 830))
        elif enemy_sang.color == "red":
            screen.blit(enemy_sang.object, (600-n*90, 35))
    else:
        screen.blit(enemy_sang.object, board[enemy_sang.rect.x][enemy_sang.rect.y])
    if enemy_jang.rect.x < 0:
        n = -enemy_jang.rect.x
        if enemy_jang.color == "green":
            screen.blit(enemy_jang.object, (50+n*90, 830))
        elif enemy_jang.color == "red":
            screen.blit(enemy_jang.object, (600-n*90, 35))
    else:
        screen.blit(enemy_jang.object, board[enemy_jang.rect.x][enemy_jang.rect.y])
    if enemy_king.rect.x < 0:
        n = -enemy_king.rect.x
        if enemy_king.color == "green":
            screen.blit(enemy_king.object, (50+n*90, 830))
        elif enemy_king.color == "red":
            screen.blit(enemy_king.object, (600-n*90, 35))
    else:
        screen.blit(enemy_king.object, board[enemy_king.rect.x][enemy_king.rect.y])
    if enemy_ja.rect.x < 0:
        n = -enemy_ja.rect.x
        if enemy_ja.color == "green":
            screen.blit(enemy_ja.object, (50+n*90, 830))
        elif enemy_ja.color == "red":
            screen.blit(enemy_ja.object, (600-n*90, 35))
    else:
        screen.blit(enemy_ja.object, board[enemy_ja.rect.x][enemy_ja.rect.y])

def rearrange(turn):
    global numG
    global numR

    if sang.color == turn and sang.rect.x < -1:
        sang.rect.x += 1
    if jang.color == turn and jang.rect.x < -1:
        jang.rect.x += 1
    if king.color == turn and king.rect.x < -1:
        king.rect.x += 1
    if ja.color == turn and ja.rect.x < -1:
        ja.rect.x += 1
    if enemy_sang.color == turn and enemy_sang.rect.x < -1:
        enemy_sang.rect.x += 1
    if enemy_jang.color == turn and enemy_jang.rect.x < -1:
        enemy_jang.rect.x += 1
    if enemy_king.color == turn and enemy_king.rect.x < -1:
        enemy_king.rect.x += 1
    if enemy_ja.color == turn and enemy_ja.rect.x < -1:
        enemy_ja.rect.x += 1
    if turn == "green":
        numG -= 1
    elif turn == "red":
        numR -= 1

def play(screen):

    generate()

    selectSound = pygame.mixer.Sound("sound/click.ogg")
    moveSound = pygame.mixer.Sound("sound/move.ogg")

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
                        selectSound.play()
                        if -10 < sang.rect.x < 0:
                            if fixed_y != 0:
                                sang.move(fixed_x, fixed_y)
                                moved = True
                                rearrange(turn)
                        if abs(fixed_x-sang.rect.x) == 1 and abs(fixed_y-sang.rect.y) == 1:
                            if canMove(sang, fixed_x, fixed_y):
                                sang.move(fixed_x, fixed_y)
                                moved = True
                    if jang.selected and jang.color == "green":
                        selectSound.play()
                        if -10 < jang.rect.x < 0:
                            if fixed_y != 0:
                                jang.move(fixed_x, fixed_y)
                                moved = True
                                rearrange(turn)
                        if abs(fixed_x-jang.rect.x) + abs(fixed_y-jang.rect.y) == 1:
                            if canMove(jang, fixed_x, fixed_y):
                                jang.move(fixed_x, fixed_y)
                                moved = True
                    if king.selected and king.color == "green":
                        selectSound.play()
                        if -10 < king.rect.x < 0:
                            if fixed_y != 0:
                                king.move(fixed_x, fixed_y)
                                moved = True
                                rearrange(turn)
                        if (abs(fixed_x-king.rect.x) == 1 and abs(fixed_y-king.rect.y) == 1) or abs(fixed_x-king.rect.x) + abs(fixed_y-king.rect.y) == 1:
                            if canMove(king, fixed_x, fixed_y):
                                king.move(fixed_x, fixed_y)
                                moved = True
                    if ja.selected and ja.color == "green":
                        selectSound.play()
                        if -10 < ja.rect.x < 0:
                            if fixed_y != 0:
                                ja.move(fixed_x, fixed_y)
                                moved = True
                                rearrange(turn)
                        if ja.hu:
                            if abs(fixed_x - ja.rect.x) + abs(
                                    fixed_y - ja.rect.y) == 1 or ja.rect.y - fixed_y== 1:
                                if canMove(ja, fixed_x, fixed_y):
                                    ja.move(fixed_x, fixed_y)
                                    moved = True
                        else:
                            if fixed_x - ja.rect.x == 0 and ja.rect.y - fixed_y== 1:
                                if canMove(ja, fixed_x, fixed_y):
                                    ja.move(fixed_x, fixed_y)
                                    if fixed_y == 0:
                                        ja.hu = True
                                        ja.change()
                                    moved = True
                    if enemy_sang.selected and enemy_sang.color == "green":
                        selectSound.play()
                        if -10 < enemy_sang.rect.x < 0:
                            if fixed_y != 0:
                                enemy_sang.move(fixed_x, fixed_y)
                                moved = True
                                rearrange(turn)
                        if abs(fixed_x-enemy_sang.rect.x) == 1 and abs(fixed_y-enemy_sang.rect.y) == 1:
                            if canMove(enemy_sang, fixed_x, fixed_y):
                                enemy_sang.move(fixed_x, fixed_y)
                                moved = True
                    if enemy_jang.selected and enemy_jang.color == "green":
                        selectSound.play()
                        if -10 < enemy_jang.rect.x < 0:
                            if fixed_y != 0:
                                enemy_jang.move(fixed_x, fixed_y)
                                moved = True
                                rearrange(turn)
                        if abs(fixed_x-enemy_jang.rect.x) + abs(fixed_y-enemy_jang.rect.y) == 1:
                            if canMove(enemy_jang, fixed_x, fixed_y):
                                enemy_jang.move(fixed_x, fixed_y)
                                moved = True
                    if enemy_king.selected and enemy_king.color == "green":
                        selectSound.play()
                        if -10 < enemy_king.rect.x < 0:
                            if fixed_y != 0:
                                enemy_king.move(fixed_x, fixed_y)
                                moved = True
                                rearrange(turn)
                        if (abs(fixed_x-enemy_king.rect.x) == 1 and abs(fixed_y-enemy_king.rect.y) == 1) or abs(fixed_x-enemy_king.rect.x) + abs(fixed_y-enemy_king.rect.y) == 1:
                            if canMove(enemy_king, fixed_x, fixed_y):
                                enemy_king.move(fixed_x, fixed_y)
                                moved = True
                    if enemy_ja.selected and enemy_ja.color == "green":
                        selectSound.play()
                        if -10 < enemy_ja.rect.x < 0:
                            if fixed_y != 0:
                                enemy_ja.move(fixed_x, fixed_y)
                                moved = True
                                rearrange(turn)
                        if enemy_ja.hu:
                            if abs(fixed_x - enemy_ja.rect.x) + abs(
                                    fixed_y - enemy_ja.rect.y) == 1 or enemy_ja.rect.y - fixed_y== 1:
                                if canMove(enemy_ja, fixed_x, fixed_y):
                                    enemy_ja.move(fixed_x, fixed_y)
                                    moved = True
                        else:
                            if fixed_x - enemy_ja.rect.x == 0 and enemy_ja.rect.y - fixed_y== 1:
                                if canMove(enemy_ja, fixed_x, fixed_y):
                                    enemy_ja.move(fixed_x, fixed_y)
                                    if fixed_y == 0:
                                        enemy_ja.hu = True
                                        enemy_ja.change()
                                    moved = True

                    if moved:
                        moveSound.play()
                        turn = "red"
                    else:
                        if sang.color == "green":
                            sang.select(fixed_x, fixed_y)
                        if jang.color == "green":
                            jang.select(fixed_x, fixed_y)
                        if king.color == "green":
                            king.select(fixed_x, fixed_y)
                        if ja.color == "green":
                            ja.select(fixed_x, fixed_y)
                        if enemy_sang.color == "green":
                            enemy_sang.select(fixed_x, fixed_y)
                        if enemy_jang.color == "green":
                            enemy_jang.select(fixed_x, fixed_y)
                        if enemy_king.color == "green":
                            enemy_king.select(fixed_x, fixed_y)
                        if enemy_ja.color == "green":
                            enemy_ja.select(fixed_x, fixed_y)

                elif turn == "red":
                    if enemy_sang.selected and enemy_sang.color == "red":
                        selectSound.play()
                        if -10 < enemy_sang.rect.x < 0:
                            if fixed_y != 3:
                                enemy_sang.move(fixed_x, fixed_y)
                                moved = True
                                rearrange(turn)
                        if abs(fixed_x - enemy_sang.rect.x) == 1 and abs(fixed_y - enemy_sang.rect.y) == 1:
                            if canMove(enemy_sang, fixed_x, fixed_y):
                                enemy_sang.move(fixed_x, fixed_y)
                                moved = True
                    if enemy_jang.selected and enemy_jang.color == "red":
                        selectSound.play()
                        if -10 < enemy_jang.rect.x < 0:
                            if fixed_y != 3:
                                enemy_jang.move(fixed_x, fixed_y)
                                moved = True
                                rearrange(turn)
                        if abs(fixed_x - enemy_jang.rect.x) + abs(fixed_y - enemy_jang.rect.y) == 1:
                            if canMove(enemy_jang, fixed_x, fixed_y):
                                enemy_jang.move(fixed_x, fixed_y)
                                moved = True
                    if enemy_king.selected and enemy_king.color == "red":
                        selectSound.play()
                        if -10 < enemy_king.rect.x < 0:
                            if fixed_y != 3:
                                enemy_king.move(fixed_x, fixed_y)
                                moved = True
                                rearrange(turn)
                        if (abs(fixed_x - enemy_king.rect.x) == 1 and abs(fixed_y - enemy_king.rect.y) == 1) or abs(
                                fixed_x - enemy_king.rect.x) + abs(fixed_y - enemy_king.rect.y) == 1:
                            if canMove(enemy_king, fixed_x, fixed_y):
                                enemy_king.move(fixed_x, fixed_y)
                                moved = True
                    if enemy_ja.selected and enemy_ja.color == "red":
                        selectSound.play()
                        if -10 < enemy_ja.rect.x < 0:
                            if fixed_y != 3:
                                enemy_ja.move(fixed_x, fixed_y)
                                moved = True
                                rearrange(turn)
                        if enemy_ja.hu:
                            if abs(fixed_x - enemy_ja.rect.x) + abs(fixed_y - enemy_ja.rect.y) == 1  or fixed_y - enemy_ja.rect.y == 1:
                                if canMove(enemy_ja, fixed_x, fixed_y):
                                    enemy_ja.move(fixed_x, fixed_y)
                                    moved = True
                        else:
                            if fixed_x - enemy_ja.rect.x == 0 and fixed_y - enemy_ja.rect.y == 1:
                                if canMove(enemy_ja, fixed_x, fixed_y):
                                    enemy_ja.move(fixed_x, fixed_y)
                                    if fixed_y == 3:
                                        enemy_ja.hu = True
                                        enemy_ja.change()
                                    moved = True
                    if sang.selected and sang.color == "red":
                        selectSound.play()
                        if -10 < sang.rect.x < 0:
                            if fixed_y != 3:
                                sang.move(fixed_x, fixed_y)
                                moved = True
                                rearrange(turn)
                        if abs(fixed_x - sang.rect.x) == 1 and abs(fixed_y - sang.rect.y) == 1:
                            if canMove(sang, fixed_x, fixed_y):
                                sang.move(fixed_x, fixed_y)
                                moved = True
                    if jang.selected and jang.color == "red":
                        selectSound.play()
                        if -10 < jang.rect.x < 0:
                            if fixed_y != 3:
                                jang.move(fixed_x, fixed_y)
                                moved = True
                                rearrange(turn)
                        if abs(fixed_x - jang.rect.x) + abs(fixed_y - jang.rect.y) == 1:
                            if canMove(jang, fixed_x, fixed_y):
                                jang.move(fixed_x, fixed_y)
                                moved = True
                    if king.selected and king.color == "red":
                        selectSound.play()
                        if -10 < king.rect.x < 0:
                            if fixed_y != 3:
                                king.move(fixed_x, fixed_y)
                                moved = True
                                rearrange(turn)
                        if (abs(fixed_x - king.rect.x) == 1 and abs(fixed_y - king.rect.y) == 1) or abs(
                                fixed_x - king.rect.x) + abs(fixed_y - king.rect.y) == 1:
                            if canMove(king, fixed_x, fixed_y):
                                king.move(fixed_x, fixed_y)
                                moved = True
                    if ja.selected and ja.color == "red":
                        selectSound.play()
                        if -10 < ja.rect.x < 0:
                            if fixed_y != 3:
                                ja.move(fixed_x, fixed_y)
                                moved = True
                                rearrange(turn)
                        if ja.hu:
                            if abs(fixed_x - ja.rect.x) + abs(fixed_y - ja.rect.y) == 1  or fixed_y - ja.rect.y == 1:
                                if canMove(ja, fixed_x, fixed_y):
                                    ja.move(fixed_x, fixed_y)
                                    moved = True
                        else:
                            if fixed_x - ja.rect.x == 0 and fixed_y - ja.rect.y == 1:
                                if canMove(ja, fixed_x, fixed_y):
                                    ja.move(fixed_x, fixed_y)
                                    if fixed_y == 3:
                                        ja.hu = True
                                        ja.change()
                                    moved = True

                    if moved:
                        moveSound.play()
                        turn = "green"
                    else:
                        if enemy_sang.color == "red":
                            enemy_sang.select(fixed_x, fixed_y)
                        if enemy_jang.color == "red":
                            enemy_jang.select(fixed_x, fixed_y)
                        if enemy_king.color == "red":
                            enemy_king.select(fixed_x, fixed_y)
                        if enemy_ja.color == "red":
                            enemy_ja.select(fixed_x, fixed_y)
                        if sang.color == "red":
                            sang.select(fixed_x, fixed_y)
                        if jang.color == "red":
                            jang.select(fixed_x, fixed_y)
                        if king.color == "red":
                            king.select(fixed_x, fixed_y)
                        if ja.color == "red":
                            ja.select(fixed_x, fixed_y)

        pygame.display.flip()