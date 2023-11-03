import pygame


class Player:
    def __init__(self, pos, color):
        self.color = color
        size = width, height = (60,60)
        print(pos, size)
        self.rect = pygame.Rect(pos, size)


    def update(self):
        self.rect(draw)


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
