import pygame
from random import choice

from buttonSprite import Button


from constants import (
    BUTTON_WIDTH,
    BUTTON_COLOR,
    BUTTON_HEIGHT,
    GAME_GRID_SIZE,
    BUTTON_PADDING,
    SCREEN_BACKGROUND,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    GAME_DONE_HEIGHT,
    GAME_DONE_PADDING,
    BUTTON_TEXT_COLOR,
)

buttonsGroup = pygame.sprite.Group()


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
    else:
        return

    button1 = None
    button2 = None
    for button in buttonsGroup:
        if button.get_position_index() == swap_index:
            button1 = button
        if button.get_position_index() == blank_index:
            button2 = button

    # Swap buttons
    button1.set_position_index(blank_index)
    button1.update_position()
    button2.set_position_index(swap_index)
    button2.update_position()

    is_game_completed = checkGameCompletion()
    if is_game_completed:
        drawGameCompletion(displaysurface)


def drawGameCompletion(displaysurface):
    x = 0
    y = (SCREEN_HEIGHT / 2) - GAME_DONE_HEIGHT
    width = SCREEN_WIDTH - 2 * GAME_DONE_PADDING
    height = GAME_DONE_HEIGHT

    pygame.draw.rect(displaysurface, BUTTON_COLOR, (x, y, width, height))
    font = pygame.font.SysFont("Arial", 25)
    text = font.render(str("GAME DONE!"), True, BUTTON_TEXT_COLOR)
    text_rect = text.get_rect(center=(x + width / 2, y + height / 2))
    displaysurface.blit(text, text_rect)


def drawBoard(screen):
    screen.fill(SCREEN_BACKGROUND)

    if len(buttonsGroup) == 0:
        for position_index, button_index in enumerate(GAME_BOARD):
            button = Button(position_index, button_index)
            buttonsGroup.add(button)


def is_position_empty(position):
    for button in buttonsGroup:
        if (
            button.get_position_index() == position
            and button.get_button_index() == GAME_GRID_SIZE * GAME_GRID_SIZE - 1
        ):
            return True
    return False
