import pygame

pygame.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

class Square:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        WIN.fill((0, 0, 0))
        pygame.draw.rect(WIN, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
        pygame.display.flip()

    def walk(self, key):
        if key == pygame.K_LEFT:
            self.x -= 10
        elif key == pygame.K_RIGHT:
            self.x += 10
        elif key == pygame.K_DOWN:
            self.y += 10
        elif key == pygame.K_UP:
            self.y -= 10

def main():
    run = True
    tom = Square(0, 0, 100, 100, (255, 0, 0))

    while run:
        clock = pygame.time.Clock()
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                tom.walk(event.key)
                
        tom.draw()
        
    pygame.quit()

main()