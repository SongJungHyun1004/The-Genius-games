import pygame.image

class Sang:
    def __init__(self, color, xp, yp, selected):
        if color == "green":
            self.object = pygame.image.load("img/sang_green.png")
        elif color == "red":
            img = pygame.image.load("img/sang_red.png")
            self.object = pygame.transform.rotate(img, 180)
        self.color = color
        self.rect = self.object.get_rect()
        self.rect.x = xp
        self.rect.y = yp
        self.selected = selected

    def select(self, mouseX, mouseY):
        if -10 < self.rect.x < 0:
            if self.rect.x == mouseX:
                self.selected = True
            else:
                self.selected = False
            return
        if self.rect.x == mouseX and self.rect.y == mouseY:
            self.selected = True
        else:
            self.selected = False

    def move(self, movX, movY):
        if -10 < self.rect.x < 0:
            if self.color == "green":
                self.object = pygame.image.load("img/sang_green.png")
            elif self.color == "red":
                img = pygame.image.load("img/sang_red.png")
                self.object = pygame.transform.rotate(img, 180)
        self.rect.x = movX
        self.rect.y = movY
        self.selected = False

    def taked(self, num):
        if self.color == "green":
            img = pygame.image.load("img/sang_red.png")
            self.object = pygame.transform.rotate(img, 180)
            self.color = "red"
        elif self.color == "red":
            self.object = pygame.image.load("img/sang_green.png")
            self.color = "green"
        self.object = pygame.transform.scale(self.object, (80, 80))
        self.rect.x = -num

class Jang:
    def __init__(self, color, xp, yp, selected):
        if color == "green":
            self.object = pygame.image.load("img/jang_green.png")
        elif color == "red":
            img = pygame.image.load("img/jang_red.png")
            self.object = pygame.transform.rotate(img, 180)
        self.color = color
        self.rect = self.object.get_rect()
        self.rect.x = xp
        self.rect.y = yp
        self.selected = selected

    def select(self, mouseX, mouseY):
        if -10 < self.rect.x < 0:
            if self.rect.x == mouseX:
                self.selected = True
            else:
                self.selected = False
            return
        if self.rect.x == mouseX and self.rect.y == mouseY:
            self.selected = True
        else:
            self.selected = False

    def move(self, movX, movY):
        if -10 < self.rect.x < 0:
            if self.color == "green":
                self.object = pygame.image.load("img/jang_green.png")
            elif self.color == "red":
                img = pygame.image.load("img/jang_red.png")
                self.object = pygame.transform.rotate(img, 180)
        self.rect.x = movX
        self.rect.y = movY
        self.selected = False

    def taked(self, num):
        if self.color == "green":
            img = pygame.image.load("img/jang_red.png")
            self.object = pygame.transform.rotate(img, 180)
            self.color = "red"
        elif self.color == "red":
            self.object = pygame.image.load("img/jang_green.png")
            self.color = "green"
        self.object = pygame.transform.scale(self.object, (80, 80))
        self.rect.x = -num

class King:
    def __init__(self, color, xp, yp, selected):
        if color == "green":
            self.object = pygame.image.load("img/king_green.png")
        elif color == "red":
            img = pygame.image.load("img/king_red.png")
            self.object = pygame.transform.rotate(img, 180)
        self.color = color
        self.rect = self.object.get_rect()
        self.rect.x = xp
        self.rect.y = yp
        self.selected = selected

    def select(self, mouseX, mouseY):
        if -10 < self.rect.x < 0:
            if self.rect.x == mouseX:
                self.selected = True
            else:
                self.selected = False
            return
        if self.rect.x == mouseX and self.rect.y == mouseY:
            self.selected = True
        else:
            self.selected = False

    def move(self, movX, movY):
        if -10 < self.rect.x < 0:
            if self.color == "green":
                self.object = pygame.image.load("img/king_green.png")
            elif self.color == "red":
                img = pygame.image.load("img/king_red.png")
                self.object = pygame.transform.rotate(img, 180)
        self.rect.x = movX
        self.rect.y = movY
        self.selected = False

    def taked(self, num):
        self.rect.x = -10
        if self.color == "green":
            # img = pygame.image.load("img/king_red.png")
            # self.object = pygame.transform.rotate(img, 180)
            # self.color = "red"
            return "R"
        elif self.color == "red":
            return "G"
        #     self.object = pygame.image.load("img/king_green.png")
        #     self.color = "green"
        # self.object = pygame.transform.scale(self.object, (80, 80))


class Ja:
    def __init__(self, color, xp, yp, hu, selected):
        if color == "green":
            self.object = pygame.image.load("img/ja_green.png")
        elif color == "red":
            img = pygame.image.load("img/ja_red.png")
            self.object = pygame.transform.rotate(img, 180)
        self.rect = self.object.get_rect()
        self.rect.x = xp
        self.rect.y = yp
        self.color = color
        self.hu = hu
        self.selected = selected

    def change(self):
        if self.hu:
            if self.color == "green":
                self.object = pygame.image.load("img/hu_green.png")
            elif self.color == "red":
                img = pygame.image.load("img/hu_red.png")
                self.object = pygame.transform.rotate(img, 180)
        else:
            if self.color == "green":
                self.object = pygame.image.load("img/ja_green.png")
            elif self.color == "red":
                img = pygame.image.load("img/ja_red.png")
                self.object = pygame.transform.rotate(img, 180)

    def select(self, mouseX, mouseY):
        if -10 < self.rect.x < 0:
            if self.rect.x == mouseX:
                self.selected = True
            else:
                self.selected = False
            return
        if self.rect.x == mouseX and self.rect.y == mouseY:
            self.selected = True
        else:
            self.selected = False

    def move(self, movX, movY):
        if -10 < self.rect.x < 0:
            if self.color == "green":
                self.object = pygame.image.load("img/ja_green.png")
            elif self.color == "red":
                img = pygame.image.load("img/ja_red.png")
                self.object = pygame.transform.rotate(img, 180)
        self.rect.x = movX
        self.rect.y = movY
        self.selected = False

    def taked(self, num):
        if self.color == "green":
            img = pygame.image.load("img/ja_red.png")
            self.object = pygame.transform.rotate(img, 180)
            self.color = "red"
        elif self.color == "red":
            self.object = pygame.image.load("img/ja_green.png")
            self.color = "green"
        self.hu = False
        self.object = pygame.transform.scale(self.object, (80, 80))
        self.rect.x = -num
