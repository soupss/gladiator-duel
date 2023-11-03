import pygame


def init():
    pygame.init()
    window_width = 640
    window_height = 480
    window_size = (window_width, window_height)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption('Pygame Window')


def update():
    screen.fill((0, 120, 255))
    pygame.display.flip()


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


def close():
    pygame.quit()
    sys.exit()


while(1):
    init()
    update()
    events()
    close()
