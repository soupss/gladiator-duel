import pygame
import sys


class Game:
    def __init__(self):
        pygame.init()
        window_width = 640
        window_height = 480
        window_size = (window_width, window_height)
        self.screen = pygame.display.set_mode(window_size)
        pygame.display.set_caption('Duel')
        self.running = True


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
        self.screen.fill((0, 120, 255))
        pygame.display.flip()
