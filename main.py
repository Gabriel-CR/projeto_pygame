import pygame

pygame.init()

x = 1280
y = 720
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption("BatleForce")

class Background:
    def __init__(self):
        self.img = pygame.image.load('images/bg.jpg').convert_alpha()
        self.bg = pygame.transform.scale(self.img, (x, y))

    def att(self):
        screen.blit(self.bg, (0, 0))

class Missel:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

        self.img = pygame.image.load('images/missile.png').convert_alpha()
        self.missel = pygame.transform.scale(self.img, (x / 25, x / 25))

    def shot(self):
        screen.blit(self.missel, (self.x, self.y))

class Aviao:
    def __init__(self):
        self.x = x/2
        self.y = y/2

        self.img = pygame.image.load('images/space.png').convert_alpha()
        self.space = pygame.transform.scale(self.img, (x / 10, x / 10))

        self.missel = Missel()

    def sky(self, key):
        if key == pygame.K_RIGHT:
            self.x += 10
        elif key == pygame.K_LEFT:
            self.x -= 10
        elif key == pygame.K_DOWN:
            self.y += 10
        elif key == pygame.K_UP:
            self.y -= 10

    def att(self):
        screen.blit(self.space, (self.x, self.y))

class Nave:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.flag = True

        self.img = pygame.image.load('images/spaceship.png').convert_alpha()
        self.nave = pygame.transform.scale(self.img, (x / 10, x / 10))

    def sky(self):
        if self.x > x - 115:
            self.flag = False
        elif self.x <= 0:
            self.flag = True
        
        if self.flag:
            self.x += 1
        else:
            self.x -= 1

    def att(self):
        self.sky()
        screen.blit(self.nave, (self.x, self.y))

bg = pygame.image.load('images/bg.jpg').convert_alpha()
bg = pygame.transform.scale(bg, (x, y))

rodando = True

background = Background()
plane = Aviao()
nave = Nave()

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        elif event.type == pygame.KEYDOWN:
            plane.sky(event.key)

    background.att()
    plane.att()
    nave.att()

    pygame.display.update()