import pygame
from src.resources import Board, Astar
from src.resources.Point import Square
from src.resources.Astar import A_star
from src.util import board_utils
from enum import Enum

import time


class Colors(Enum):
    barrier = (0, 0, 0)
    visited = (0, 255, 0)
    empty = (255, 255, 255)
    path = (255, 69, 0)


# pygamesetup
pygame.init()
# defining the width and height
size = (int(1920), int(1080))
# defining margin and block size
MARGIN = 1
BLOCK_SIZE = 50


screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True


font = pygame.font.Font(pygame.font.get_default_font(), int(BLOCK_SIZE / 5))
maze = Board.Board(5, 5, size, screen, MARGIN, BLOCK_SIZE, font, offset=50)

a_star = Astar.A_star(maze)

# font


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    # NOTE: in the grid, elements should be accesed as [row][column] and NOT [column][row].
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # left clicks make current cell barrier
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            try:
                column, row = board_utils.get_square(pos, MARGIN, BLOCK_SIZE)
                maze.make_barrier(row, column)
            except:
                print("out of bounds")
                print(pos)

        # rigth clicks delete current cell and make it empty
        if pygame.mouse.get_pressed()[2]:
            try:
                pos = pygame.mouse.get_pos()
                column, row = board_utils.get_square(pos, MARGIN, BLOCK_SIZE)

                maze.make_empty(row, column)
            except:
                print("out of bounds")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                # making square goal
                # TODO: ensure that just one goal exist per maze

                pos = pygame.mouse.get_pos()
                column, row = board_utils.get_square(pos, MARGIN, BLOCK_SIZE)
                maze.make_goal(row, column, a_star)

            if event.key == pygame.K_d:
                # deleting current square and leaving it white
                pos = pygame.mouse.get_pos()
                column, row = board_utils.get_square(pos, MARGIN, BLOCK_SIZE)
                maze.make_empty(row, column)

            if event.key == pygame.K_s:
                pos = pygame.mouse.get_pos()
                column, row = board_utils.get_square(pos, MARGIN, BLOCK_SIZE)
                maze.make_start(row, column, a_star)

            if event.key == pygame.K_i:
                pos = pygame.mouse.get_pos()
                column, row = board_utils.get_square(pos, MARGIN, BLOCK_SIZE)

                # g and h functions

                # getting current square
                currentSquare = maze.grid[row][column]
                print(f"g: {currentSquare.euclidean_distance(maze.start)}")
                print(f"h: {currentSquare.euclidean_distance(maze.goal)}")
                print(
                    f"f: {currentSquare.euclidean_distance(maze.start)+currentSquare.euclidean_distance(maze.goal)}"
                )

                # drawing data
                g = maze.font.render(
                    f"g: {currentSquare.euclidean_distance(maze.start)}", True, "black"
                )
                h = maze.font.render(
                    f"h: {currentSquare.euclidean_distance(maze.goal)}", True, "black"
                )
                f = maze.font.render(
                    f"f: {currentSquare.euclidean_distance(maze.goal) + currentSquare.euclidean_distance(maze.start)}",
                    True,
                    "black",
                )

                screen.blit(g, (0, 0))

                currentSquare.make_path()

                print(maze.grid[row][column].compute_neighbors(maze))
            if event.key == pygame.K_r:
                if not maze.has_goal() and not maze.has_start():
                    maze.add_message("Maze could not be solved")
                    maze.add_message("Goal and start point")
                    maze.add_message("Not setted properly")
                else:
                    maze.add_message("solving...")
                    solver = A_star(maze)
                    solver.solve()

                # before solving...
            if event.key == pygame.K_SPACE:
                print("pressing space")
                pos = pygame.mouse.get_pos()

                # getting square
                column, row = board_utils.get_square(pos, MARGIN, BLOCK_SIZE)

    screen.fill("cadetblue4")

    maze.draw()

    # fill the screen with a color to wipe away anything from last frame

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
