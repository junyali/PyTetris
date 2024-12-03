# PyTetris 03/12/2024

## // Imports \\ ##
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import sys
import random
import pygame

## // CONSTANTS \\ ##
cell_size = 32
grid_width = 10
grid_height = 24

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (240, 0, 0)
GREEN = (0, 240, 0)
BLUE = (0, 0, 240)
YELLOW = (240, 240, 0)
ORANGE = (240, 160, 0)
CYAN = (0, 240, 240)
MAGENTA = (160, 0, 240)

COLOURS = [RED, GREEN, BLUE, YELLOW, ORANGE, CYAN, MAGENTA]

class Tetromino:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.colour = random.choice(COLOURS)
        self.rotation = 0


class Tetris:
    def __init__(self):
        self.width = grid_width
        self.height = grid_height
        self.cell_size = cell_size
        self.grid = [
            [0 for _ in range(self.width // self.cell_size)] for _ in range(self.height // self.cell_size)
        ]
        self.score = 0
        self.game_over = False

if __name__ == '__main__':
    Game = Tetris()
