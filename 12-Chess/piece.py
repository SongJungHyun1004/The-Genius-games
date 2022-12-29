import pygame.image

class Sang:
    def __init__(self, xp, yp):
        self.object = pygame.image.load("img/sang_green.png")
        self.rect = self.object.get_rect()
        self.rect.x = xp
        self.rect.y = yp

class Jang:
    def __init__(self, xp, yp):
        self.object = pygame.image.load("img/jang_green.png")
        self.rect = self.object.get_rect()
        self.rect.x = xp
        self.rect.y = yp

class King:
    def __init__(self, xp, yp):
        self.object = pygame.image.load("img/king_green.png")
        self.rect = self.object.get_rect()
        self.rect.x = xp
        self.rect.y = yp

class Ja:
    def __init__(self, xp, yp):
        self.object = pygame.image.load("img/ja_green.png")
        self.rect = self.object.get_rect()
        self.rect.x = xp
        self.rect.y = yp

