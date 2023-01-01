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
        if self.rect.x == mouseX and self.rect.y == mouseY:
            self.selected = True
            print("select sang")
        else:
            self.selected = False
            print("deselect sang")

    def move(self, movX, movY):
        self.rect.x = movX
        self.rect.y = movY
        self.selected = False
        print("move sang")


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
        if self.rect.x == mouseX and self.rect.y == mouseY:
            self.selected = True
            print("select jang")
        else:
            self.selected = False
            print("deselect jang")

    def move(self, movX, movY):
        self.rect.x = movX
        self.rect.y = movY
        self.selected = False
        print("move jang")

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
        if self.rect.x == mouseX and self.rect.y == mouseY:
            self.selected = True
            print("select king")
        else:
            self.selected = False
            print("deselect king")

    def move(self, movX, movY):
        self.rect.x = movX
        self.rect.y = movY
        self.selected = False
        print("move king")

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
        if self.rect.x == mouseX and self.rect.y == mouseY:
            self.selected = True
            print("select ja")
        else:
            self.selected = False
            print("deselect ja")

    def move(self, movX, movY):
        self.rect.x = movX
        self.rect.y = movY
        self.selected = False
        print("move ja")

