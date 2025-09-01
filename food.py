from globals import (
    Object,
    Window,
    Colour,
)
import random
import pygame
from typing import Tuple


class Food(Object):
    """Class Representing The Food"""

    def __init__(self) -> None:
        self.position = self.generate_position()

    def generate_position(self) -> Tuple[int, int]:
        """Generate a random position for the food"""
        return (
            random.randint(0, Window.GRID_COUNT - 1),
            random.randint(0, Window.GRID_COUNT - 1),
        )

    def draw(self, surface: pygame.Surface):
        super().draw(self.position, surface, Colour.FOOD_COLOUR)
