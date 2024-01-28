# External Imports
import pygame

# Internal Imports
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, GAME_GRID_SIZE, GAME_TITLE
from game import (
    drawBoard,
    updateBoard,
    buttonsGroup,
    is_position_empty,
    checkGameCompletion,
)

# Init pygame
pygame.init()


# Create Game Window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(GAME_TITLE)


# frame rate
clock = pygame.time.Clock()
FPS = 60

# Draw Board
drawBoard(screen)

# Game loop
run = True
while run:
    clock.tick(FPS)

    # update sprite group
    buttonsGroup.update()

    # draw sprite group
    buttonsGroup.draw(screen)

    # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False

        is_game_completed = checkGameCompletion()

        if not is_game_completed:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    updateBoard(screen, +1)

                if event.key == pygame.K_RIGHT:
                    updateBoard(screen, -1)

                if event.key == pygame.K_UP:
                    updateBoard(screen, GAME_GRID_SIZE)

                if event.key == pygame.K_DOWN:
                    updateBoard(screen, -1 * GAME_GRID_SIZE)

            # handle MOUSEBUTTONUP
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                # get a list of all sprites that are under the mouse cursor
                clicked_sprites = [s for s in buttonsGroup if s.rect.collidepoint(pos)]

                if len(clicked_sprites) == 1:
                    button_clicked = clicked_sprites[0]
                    button_index = button_clicked.get_button_index()
                    position_index = button_clicked.get_position_index()

                    if button_index + 1 < GAME_GRID_SIZE * GAME_GRID_SIZE:
                        displace = 0
                        # Top
                        if position_index > GAME_GRID_SIZE - 1:
                            if is_position_empty(position_index - GAME_GRID_SIZE):
                                displace = GAME_GRID_SIZE

                        # Right
                        if position_index % GAME_GRID_SIZE < GAME_GRID_SIZE - 1:
                            if is_position_empty(position_index + 1):
                                displace = -1

                        # Bottom
                        if position_index < (GAME_GRID_SIZE - 1) * GAME_GRID_SIZE:
                            if is_position_empty(position_index + GAME_GRID_SIZE):
                                displace = -1 * GAME_GRID_SIZE

                        # Left
                        if position_index % GAME_GRID_SIZE > 0:
                            if is_position_empty(position_index - 1):
                                displace = 1

                        if displace != 0:
                            print("Displace")
                            print(displace)
                            updateBoard(screen, displace)
                        else:
                            print("Failing Displace")
                            print(displace)

    # upate display
    pygame.display.flip()

pygame.quit()
