import pygame

from globals import (
    Window,
    Colour,
    Direction,
)
from snake import Snake
from food import Food

pygame.init()


class Game:
    """Main game Class"""

    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((Window.WINDOW_SIZE, Window.WINDOW_SIZE))
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
        self.screen.fill(Colour.BLACK)
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
