import pygame
import random
from enum import Enum
from typing import List, Tuple

pygame.init()

WINDOW_SIZE = 600
GRID_SIZE = 20
GRID_COUNT = WINDOW_SIZE // GRID_SIZE

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
            position[0] * GRID_SIZE,  # X pos
            position[1] * GRID_SIZE,  # Y pos
            GRID_SIZE - 1,  # Width
            GRID_SIZE - 1,  # Height
        )
        pygame.draw.rect(surface, colour, rect)


class SnakeSegment(Object):
    def __init__(self, position: Tuple[int, int]) -> None:
        self.position = position
        super().__init__()

    def draw(self, surface: pygame.Surface):
        """Draw the snake segment"""
        super().draw(self.position, surface, RED)


class Food(Object):
    """Class Representing The Food"""

    def __init__(self) -> None:
        self.position = self.generate_position()
        super().__init__()

    def generate_position(self) -> Tuple[int, int]:
        """Generate a random position for the food"""
        return (random.randint(0, GRID_COUNT - 1), random.randint(0, GRID_COUNT - 1))

    def draw(self, surface: pygame.Surface):
        super().draw(self.position, surface, FOOD_COLOUR)


class Snake:
    def __init__(self):
        self.reset()

    def reset(self):
        self.direction = Direction.RIGHT
        self.segments = [SnakeSegment((GRID_COUNT // 2, GRID_COUNT // 2))]
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
        new_head[0] = new_head[0] % GRID_COUNT
        new_head[1] = new_head[0] % GRID_COUNT

        # Check for self-collision
        if tuple(new_head) in [segment.position for segment in self.segments]:
            return False

        # Typing system went weird when converting from list to tuple
        # Force convert here to tuple
        tupled_new_head = new_head[0], new_head[1]

        # Add new head
        self.segments.insert(0, SnakeSegment(tupled_new_head))

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


class Game:
    """Main game Class"""

    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
        pygame.display.set_caption("My Snake Game")
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.game_speed = 10

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction(Direction.UP)
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction(Direction.DOWN)
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction(Direction.LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction(Direction.RIGHT)
        return True

    def update(self):
        if not self.snake.update():
            self.reset_game()
            return

        if self.snake.segments[0].position == self.food.position:
            self.snake.grow()
            self.food.position = self.food.generate_position()
            self.score += 1
            if self.score % 5 == 0:
                self.game_speed += 1

    def draw(self):
        self.screen.fill(BLACK)
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        pygame.display.flip()

    def reset_game(self):
        self.snake.reset()
        self.food = Food()
        self.score = 0
        self.game_speed = 10

    def run(self):
        """Main game loop"""
        running = True
        while running:
            running = self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(self.game_speed)


if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
