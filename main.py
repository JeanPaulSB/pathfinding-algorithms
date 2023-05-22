import pygame
from src.resources import Board
from src.util import board_utils
from enum import Enum


class Colors(Enum):
    barrier = (0, 0, 0)
    visited = (0, 255, 0)
    empty = (255, 255, 255)
    path = (255, 69, 0)


# pygamesetup
pygame.init()
# defining the width and height
size = (1920 - 200, 1080 - 50)
# defining margin and block size
MARGIN = 1
BLOCK_SIZE = 10


screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True

maze = Board.Board(50, 20, size, screen, MARGIN, BLOCK_SIZE)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column, row = board_utils.get_square(pos, MARGIN, BLOCK_SIZE)
            maze.make_barrier(row, column)

            print(row, column)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                # making square goal
                # TODO: ensure that just one goal exist per maze
                pos = pygame.mouse.get_pos()
                column, row = board_utils.get_square(pos, MARGIN, BLOCK_SIZE)
                maze.make_goal(row, column)

            if event.key == pygame.K_d:
                # deleting current square and leaving it white
                pos = pygame.mouse.get_pos()
                column, row = board_utils.get_square(pos, MARGIN, BLOCK_SIZE)
                maze.make_empty(row, column)

            if event.key == pygame.K_s:
                pos = pygame.mouse.get_pos()
                column, row = board_utils.get_square(pos, MARGIN, BLOCK_SIZE)
                maze.make_start(row, column)
            if event.key == pygame.K_i:
                # getting heuristic info
                pos = pygame.mouse.get_pos()
                column, row = board_utils.get_square(pos, MARGIN, BLOCK_SIZE)
                maze.get_score(row, column)
                print("pressed i ")

    screen.fill("black")
    maze.draw()

    # fill the screen with a color to wipe away anything from last frame

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
