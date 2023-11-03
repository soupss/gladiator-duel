import sys
import pygame

from settings import WINDOW_WIDTH, WINDOW_HEIGHT, GREEN, WHITE
from player import Player


class Game:
    def __init__(self):
        pygame.init()
        window_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
        self.screen = pygame.display.set_mode(window_size)
        pygame.display.set_caption('Duel')
        self.running = True
        self.player1 = Player((400, 400), GREEN)


    def __del__(self):
        pygame.quit()
        sys.exit()


    def isRunning(self):
        if self.running:
            return True
        else:
            return False


    def events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

    def update(self):
        WHITE = (255, 255, 255)
        self.screen.fill(WHITE)
        self.player1.draw(self.screen)
        pygame.display.flip()
