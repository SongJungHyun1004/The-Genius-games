import pygame.image

class Sang:
    def __init__(self, color, xp, yp):
        if color == "green":
            self.object = pygame.image.load("img/sang_green.png")
        elif color == "red":
            img = pygame.image.load("img/sang_red.png")
            self.object = pygame.transform.rotate(img, 180)
        self.rect = self.object.get_rect()
        self.rect.x = xp
        self.rect.y = yp

class Jang:
    def __init__(self, color, xp, yp):
        if color == "green":
            self.object = pygame.image.load("img/jang_green.png")
        elif color == "red":
            img = pygame.image.load("img/jang_red.png")
            self.object = pygame.transform.rotate(img, 180)
        self.rect = self.object.get_rect()
        self.rect.x = xp
        self.rect.y = yp

class King:
    def __init__(self, color, xp, yp):
        if color == "green":
            self.object = pygame.image.load("img/king_green.png")
        elif color == "red":
            img = pygame.image.load("img/king_red.png")
            self.object = pygame.transform.rotate(img, 180)
        self.rect = self.object.get_rect()
        self.rect.x = xp
        self.rect.y = yp

class Ja:
    def __init__(self, color, xp, yp, hu):
        if hu:
            if color == "green":
                self.object = pygame.image.load("img/hu_green.png")
            elif color == "red":
                img = pygame.image.load("img/hu_red.png")
                self.object = pygame.transform.rotate(img, 180)
        else:
            if color == "green":
                self.object = pygame.image.load("img/ja_green.png")
            elif color == "red":
                img = pygame.image.load("img/ja_red.png")
                self.object = pygame.transform.rotate(img, 180)
        self.rect = self.object.get_rect()
        self.rect.x = xp
        self.rect.y = yp

