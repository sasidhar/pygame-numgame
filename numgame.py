import pygame
from pygame.locals import *

from constants import GAME_HEIGHT, GAME_WIDTH, GAME_GRID_SIZE
from board import drawBoard, updateBoard

pygame.init()


displaysurface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("NumGame 1.0")

run = True

drawBoard(displaysurface)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                updateBoard(displaysurface, +1)

            if event.key == pygame.K_RIGHT:
                updateBoard(displaysurface, -1)

            if event.key == pygame.K_UP:
                updateBoard(displaysurface, GAME_GRID_SIZE)

            if event.key == pygame.K_DOWN:
                updateBoard(displaysurface, -1 * GAME_GRID_SIZE)


pygame.quit()
