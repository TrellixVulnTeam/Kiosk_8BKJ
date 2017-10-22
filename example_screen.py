import pygame
from pygame.locals import *
from Utils import config
from Input import input_handler
from Elements import subwindow

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class Cursor(subwindow.ChildElement):
    def __init__(self, parent_window):
        super().__init__(parent_window)
        self.x = 0
        self.y = 0

    def update(self):
        super().update()
        pos = input_handler.get_cursor()
        if pos.is_valid:
            self.x = pos.x_pos
            self.y = pos.y_pos

    def draw(self):
        super().draw()
        pygame.draw.circle(self.screen, BLUE, [self.x, self.y], 40)


class Rectangle(subwindow.ChildElement):
    def __init__(self, parent_window):
        self.priority = 0
        super().__init__(parent_window)
        self.x = config.res_width / 2
        self.y = config.res_height / 2

    def update(self):
        super().update()

    def draw(self):
        super().draw()
        pygame.draw.rect(self.screen, BLACK, [150, 10, 50, 20])


def example():
    pygame.init()
    size = [config.res_width, config.res_height]
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

    done = False

    window = subwindow.Subwindow(screen)
    Cursor(window)
    Rectangle(window)

    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == K_q:
                    done = True

        screen.fill(WHITE)

        window.update()
        window.draw()

    pygame.quit()
