import pygame
from random import choice

from constants import BUTTON_WIDTH, BUTTON_COLOR, BUTTON_HEIGHT, GAME_GRID_SIZE, BUTTON_PADDING, BUTTON_TEXT_COLOR, BUTTON_LAST_COLOR

def generateBoardPosition():
    board = list(range(0, GAME_GRID_SIZE* GAME_GRID_SIZE))
    randomized_board = []
    while len(board) > 0:
        board_choice = choice(board)
        randomized_board.append(board_choice)
        board.remove(board_choice)
    return randomized_board

def drawBoard(displaysurface):
    board = generateBoardPosition()
    print(board)
    for i in range(0, GAME_GRID_SIZE):
        for j in range(0, GAME_GRID_SIZE):
            b_width = BUTTON_WIDTH
            b_height = BUTTON_HEIGHT
            b_x = j * BUTTON_WIDTH + (j + 1) * BUTTON_PADDING
            b_y = i * BUTTON_HEIGHT + (i + 1) * BUTTON_PADDING
            b_text = board[(i * GAME_GRID_SIZE + j)] + 1
            is_last = b_text == GAME_GRID_SIZE * GAME_GRID_SIZE
            drawButton(displaysurface, b_x, b_y, b_width, b_height, b_text, is_last)
    pygame.display.update()


def drawButton(displaysurface, x, y, width, height, button_text, is_last):
    button_background_color = BUTTON_COLOR
    if is_last:
        button_background_color = BUTTON_LAST_COLOR
    pygame.draw.rect(displaysurface, button_background_color, (x,y,width, height))
    font = pygame.font.SysFont('Arial', 25)
    text = font.render(str(button_text), True, BUTTON_TEXT_COLOR)
    text_rect = text.get_rect(center=(x + width/2, y + height/2))
    displaysurface.blit(text, text_rect)
    