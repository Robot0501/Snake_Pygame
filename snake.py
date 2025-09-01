from globals import (
    Object,
    Colour,
    Direction,
    Window,
)
import pygame
from typing import Tuple, cast


class SnakeSegment(Object):
    def __init__(self, position: Tuple[int, int]) -> None:
        self.position = position

    def draw(self, surface: pygame.Surface):
        """Draw the snake segment"""
        super().draw(self.position, surface, Colour.RED)


class Snake:
    def __init__(self):
        self.reset()

    def reset(self):
        self.direction = Direction.RIGHT
        self.segments = [SnakeSegment((Window.GRID_COUNT // 2, Window.GRID_COUNT // 2))]
        self.growing = False

    def change_direction(self, new_direction: Direction):
        opposite_directions = {
            Direction.UP: Direction.DOWN,
            Direction.DOWN: Direction.UP,
            Direction.LEFT: Direction.RIGHT,
            Direction.RIGHT: Direction.LEFT,
        }
        if new_direction != opposite_directions.get(self.direction):
            self.direction = new_direction

    def update(self) -> bool:
        """Update Snake position and return True if game should continue"""
        head = self.segments[0].position

        new_head = list(head)
        if self.direction == Direction.UP:
            new_head[1] -= 1
        elif self.direction == Direction.DOWN:
            new_head[1] += 1
        elif self.direction == Direction.LEFT:
            new_head[0] -= 1
        elif self.direction == Direction.RIGHT:
            new_head[0] += 1

        # Wrap around screen
        new_head[0] = new_head[0] % Window.GRID_COUNT
        new_head[1] = new_head[1] % Window.GRID_COUNT

        # Check for self-collision
        if tuple(new_head) in [segment.position for segment in self.segments]:
            return False

        # Typing system went weird when converting from list to tuple
        # Force convert here to tuple with cast
        # Add new head
        self.segments.insert(0, SnakeSegment(cast(tuple, tuple(new_head))))

        # Remove tail if not growing
        if not self.growing:
            self.segments.pop()
        else:
            self.growing = False

        return True

    def draw(self, surface: pygame.Surface):
        for segment in self.segments:
            segment.draw(surface)

    def grow(self):
        """Make snake grow on next update"""
        self.growing = True
