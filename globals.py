from enum import Enum
from typing import List, Tuple
import pygame


class Window:
    WINDOW_SIZE = 600
    GRID_SIZE = 20
    GRID_COUNT = WINDOW_SIZE // GRID_SIZE


class Colour:
    BLACK = (10, 10, 10)
    RED = (255, 0, 0)
    DARK_RED = (200, 0, 0)
    FOOD_COLOUR = (255, 50, 50)


class Direction(Enum):
    """Enum for storing directional constants"""

    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Object:
    def __init__(self) -> None:
        pass

    def draw(
        self,
        position: Tuple[int, int],
        surface: pygame.Surface,
        colour: Tuple[int, int, int],
    ):
        rect = pygame.Rect(
            position[0] * Window.GRID_SIZE,  # X pos
            position[1] * Window.GRID_SIZE,  # Y pos
            Window.GRID_SIZE - 1,  # Width
            Window.GRID_SIZE - 1,  # Height
        )
        pygame.draw.rect(surface, colour, rect)
