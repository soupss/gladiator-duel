from game import Game


def main():
    game = Game()
    while game.isRunning():
        game.events()
        game.update()
    del game


if __name__ == "__main__":
    main()
