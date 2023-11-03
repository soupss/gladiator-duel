from Game import Game


def main():
    game = Game()
    while game.isRunning():
        game.events()
        game.update()


if __name__ == "__main__":
    main()
