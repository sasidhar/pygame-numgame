import pygame
from pygame.locals import *

from constants import GAME_HEIGHT, GAME_WIDTH, GAME_BACKGROUND
from board import drawBoard
 
pygame.init()

displaysurface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
displaysurface.fill(GAME_BACKGROUND)
pygame.display.set_caption("NumGame 1.0")

run = True

drawBoard(displaysurface)

while run:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run =False

        if event.type == pygame.KEYDOWN:
            pass


pygame.quit()