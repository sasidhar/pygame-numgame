import pygame

from constants import *


class GameCompletion(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        x = 0
        y = (SCREEN_HEIGHT / 2) - GAME_DONE_HEIGHT
        width = SCREEN_WIDTH - 2 * GAME_DONE_PADDING
        height = GAME_DONE_HEIGHT

        # Generate button surface
        self.image = pygame.Surface((width, height))
        self.image.fill(GAME_DONE_BACKGROUND)

        # Add Text
        font = pygame.font.SysFont("Arial", 25)
        text = font.render(GAME_DONE_TEXT, True, GAME_DONE_TEXT_COLOR)
        text_rect = text.get_rect(center=(width / 2, height / 2))
        self.image.blit(text, text_rect)

        # Position Sprite
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

        # Set layer
        self._layer = 10
