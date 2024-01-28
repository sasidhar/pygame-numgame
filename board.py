import pygame
from random import choice

from constants import (
    BUTTON_WIDTH,
    BUTTON_COLOR,
    BUTTON_HEIGHT,
    GAME_GRID_SIZE,
    BUTTON_PADDING,
    BUTTON_TEXT_COLOR,
    BUTTON_LAST_COLOR,
    GAME_BACKGROUND,
    GAME_HEIGHT,
    GAME_WIDTH,
    GAME_DONE_HEIGHT,
    GAME_DONE_PADDING,
)


def checkGameCompletion():
    for index, item in enumerate(GAME_BOARD):
        if index != item:
            return False
    return True


def generateBoardPosition():
    board = list(range(0, GAME_GRID_SIZE * GAME_GRID_SIZE))
    randomized_board = []
    while len(board) > 0:
        board_choice = choice(board)
        randomized_board.append(board_choice)
        board.remove(board_choice)
    return randomized_board


GAME_BOARD = generateBoardPosition()


def updateBoard(displaysurface, displace=0):
    blank_value = GAME_GRID_SIZE * GAME_GRID_SIZE - 1
    blank_index = GAME_BOARD.index(blank_value)
    if abs(displace) == 1:
        if displace == -1 and blank_index % GAME_GRID_SIZE == 0:
            return
        if displace == 1 and blank_index % GAME_GRID_SIZE == GAME_GRID_SIZE - 1:
            return

    swap_index = blank_index + displace
    if swap_index >= 0 and swap_index <= blank_value:
        temp = GAME_BOARD[swap_index]
        GAME_BOARD[swap_index] = GAME_BOARD[blank_index]
        GAME_BOARD[blank_index] = temp
        drawBoard(displaysurface)

    is_game_completed = checkGameCompletion()
    if is_game_completed:
        drawGameCompletion(displaysurface)


def drawGameCompletion(displaysurface):
    drawButton(
        displaysurface,
        0,
        (GAME_HEIGHT / 2) - GAME_DONE_HEIGHT,
        GAME_WIDTH - 2 * GAME_DONE_PADDING,
        GAME_DONE_HEIGHT,
        "GAME DONE",
        False,
    )


def drawBoard(displaysurface):
    displaysurface.fill(GAME_BACKGROUND)
    for i in range(0, GAME_GRID_SIZE):
        for j in range(0, GAME_GRID_SIZE):
            b_width = BUTTON_WIDTH
            b_height = BUTTON_HEIGHT
            b_x = j * BUTTON_WIDTH + (j + 1) * BUTTON_PADDING
            b_y = i * BUTTON_HEIGHT + (i + 1) * BUTTON_PADDING
            b_text = GAME_BOARD[(i * GAME_GRID_SIZE + j)] + 1
            is_last = b_text == GAME_GRID_SIZE * GAME_GRID_SIZE
            drawButton(displaysurface, b_x, b_y, b_width, b_height, b_text, is_last)
    pygame.display.update()


def drawButton(displaysurface, x, y, width, height, button_text, is_last):
    if is_last:
        return

    button_background_color = BUTTON_COLOR
    if is_last:
        button_background_color = BUTTON_LAST_COLOR
    pygame.draw.rect(displaysurface, button_background_color, (x, y, width, height))
    font = pygame.font.SysFont("Arial", 25)
    text = font.render(str(button_text), True, BUTTON_TEXT_COLOR)
    text_rect = text.get_rect(center=(x + width / 2, y + height / 2))
    displaysurface.blit(text, text_rect)
