import pygame
from globals import (
    Window,
    Colour,
    Direction,
)
from typing import Tuple
from globals import Object


class Menu_Box(Object):
    def __init__(
        self,
        position: Tuple[int, int],
        size: Tuple[float, float],
        colour,
        text: str,
        text_colour,
    ) -> None:
        self.position = position
        self.length = size[0]
        self.width = size[1]
        self.colour = colour
        self.text = text
        self.text_colour = text_colour
        self.selected = False

    def draw(self, surface: pygame.Surface, font: pygame.font.Font):
        rect = super().draw(self.position, surface, self.colour)
        text = font.render(self.text, True, self.text_colour, self.colour)
        surface.blit(text, rect)


class Main_Menu:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((Window.WINDOW_SIZE, Window.WINDOW_SIZE))
        pygame.display.set_caption("My Snake Game")
        self.clock = pygame.time.Clock()
        self.game_speed = 10

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

    def update(self):
        pass

    def draw(self):
        self.screen.fill(Colour.BLACK)

        pygame.display.flip()

    def run(self):
        running = True
        while running:
            running = self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(self.game_speed)
