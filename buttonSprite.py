import pygame
from math import floor

from constants import (
    BUTTON_HEIGHT,
    BUTTON_WIDTH,
    BUTTON_COLOR,
    BUTTON_LAST_COLOR,
    BUTTON_TEXT_COLOR,
    GAME_GRID_SIZE,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)


class Button(pygame.sprite.Sprite):
    def __init__(self, position_index, button_index):
        print("Test")
        print(position_index, button_index, button_index + 1)
        pygame.sprite.Sprite.__init__(self)

        # Save indices for later use
        self.position_index = position_index
        self.button_index = button_index

        # Generate button surface
        self.image = pygame.Surface((BUTTON_WIDTH, BUTTON_HEIGHT))
        self.image.fill(BUTTON_COLOR)

        # Fill with specific color
        if self.button_index + 1 == GAME_GRID_SIZE * GAME_GRID_SIZE:
            self.image.fill(BUTTON_LAST_COLOR)

        (b_x, b_y, b_width, b_height) = self.get_positions()

        # Add Text
        font = pygame.font.SysFont("Arial", 25)
        text = font.render(str(self.button_index + 1), True, BUTTON_TEXT_COLOR)
        text_rect = text.get_rect(center=(b_width / 2, b_height / 2))
        self.image.blit(text, text_rect)

        # Position Sprite
        self.rect = self.image.get_rect()
        self.rect.center = (b_x, b_y)

    def get_position_index(self):
        return self.position_index

    def get_button_index(self):
        return self.button_index

    def set_position_index(self, position_index):
        self.position_index = position_index

    def update_position(self):
        print("Update Position")
        print(self.position_index, self.button_index)
        (b_x, b_y, b_width, b_height) = self.get_positions()

        # Position Sprite
        self.rect = self.image.get_rect()
        self.rect.center = (b_x, b_y)

    def get_positions(self):
        # Position
        b_width = SCREEN_WIDTH / GAME_GRID_SIZE
        b_x = (self.position_index % GAME_GRID_SIZE) * b_width + b_width / 2
        b_height = SCREEN_HEIGHT / GAME_GRID_SIZE
        b_y = floor(self.position_index / GAME_GRID_SIZE) * b_height + b_height / 2

        return (b_x, b_y, b_width, b_height)
