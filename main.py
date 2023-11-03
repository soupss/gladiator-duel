import pygame


def main():
    game = Game
    while(game.isRunning):
        game.events()
        game.update()
    game.close()
