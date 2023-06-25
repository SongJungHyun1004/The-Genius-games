import pygame.image

class Piece:
    def __init__(self, color, xp, yp, selected, piece_type):
        self.color = color
        self.selected = selected
        self.piece_type = piece_type
        self.object = self.load_image()
        self.rect = self.object.get_rect()
        self.rect.x = xp
        self.rect.y = yp

    def load_image(self):
        image_path = f"img/{self.piece_type}_{self.color}.png"
        image = pygame.image.load(image_path)
        if self.color == "red":
            image = pygame.transform.rotate(image, 180)
        return image

    def select(self, mouseX, mouseY):
        if -10 < self.rect.x < 0:
            self.selected = (self.rect.x == mouseX)
        else:
            self.selected = (self.rect.x == mouseX and self.rect.y == mouseY)

    def move(self, movX, movY):
        if -10 < self.rect.x < 0:
            self.object = self.load_image()
        self.rect.x = movX
        self.rect.y = movY
        self.selected = False

    def taked(self, num):
        if self.color == "green":
            self.color = "red"
        else:
            self.color = "green"
        self.object = self.load_image()
        self.object = pygame.transform.scale(self.object, (80, 80))
        self.rect.x = -num

class Sang(Piece):
    def __init__(self, color, xp, yp, selected):
        super().__init__(color, xp, yp, selected, "sang")

class Jang(Piece):
    def __init__(self, color, xp, yp, selected):
        super().__init__(color, xp, yp, selected, "jang")

class King(Piece):
    def __init__(self, color, xp, yp, selected):
        super().__init__(color, xp, yp, selected, "king")

class Ja(Piece):
    def __init__(self, color, xp, yp, hu, selected):
        super().__init__(color, xp, yp, selected, "ja")
        self.hu = hu

    def change(self):
        if self.hu:
            self.piece_type = "hu"
        else:
            self.piece_type = "ja"
        self.object = self.load_image()

    def taked(self, num):
        super().taked(num)
        self.hu = False
