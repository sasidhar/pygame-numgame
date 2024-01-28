from pygame import Color

## Game Constants
GAME_BACKGROUND = Color(255, 255, 255)
GAME_WIDTH = 300
GAME_HEIGHT = 350
GAME_GRID_SIZE = 3

## Button Constants
BUTTON_PADDING = 5
BUTTON_HEIGHT = (GAME_HEIGHT - (GAME_GRID_SIZE + 1) * BUTTON_PADDING)/GAME_GRID_SIZE
BUTTON_WIDTH = (GAME_WIDTH - (GAME_GRID_SIZE + 1) * BUTTON_PADDING)/GAME_GRID_SIZE
BUTTON_COLOR = Color(38, 70, 83)
BUTTON_TEXT_COLOR = Color(255, 255, 255)
BUTTON_LAST_COLOR = Color(42, 157, 143)