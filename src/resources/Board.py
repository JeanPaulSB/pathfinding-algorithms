import pygame
from .Point import Square
from .Point import Colors


class Board:
    """
    Represents all the board gam
    rows: number of rows for the desired board
    columns: number of columns for the desired board
    size: pygame display size


    0 -> black color: barrier
    1 -> white color: empty
    2 -> green color: visited
    3 -> orange color: rigth pathh
    4 -> blue: goal

    """

    def __init__(
        self,
        rows: int,
        columns: int,
        size: tuple,
        screen: pygame.display,
        margin: float,
        block_size: float,
    ):
        self.size = size
        self.margin = margin
        self.block_size = block_size

        self.rows = (self.size[1] + self.margin) // block_size
        self.columns = (self.size[0] + self.margin) // block_size

        self.grid = [
            [Square(column=i, row=j) for i in range(self.columns)]
            for j in range(self.rows)
        ]
        self.screen = screen

        self.goal = (None, None)
        self.start = (None, None)

    """
    Draws the board in pygame.
    """

    def draw(self) -> str:
        for i in range(0, self.rows):
            for j in range(0, self.columns):
                color = self.grid[i][j].color.value
                pygame.draw.rect(
                    self.screen,
                    color,
                    [
                        (self.block_size + self.margin) * j,
                        (self.block_size + self.margin) * i,
                        self.block_size,
                        self.block_size,
                    ],
                )

    # assign actual pos for each square in the grid, since at this point they're just "blind" tiles or square
    # TODO: not needed
    def assign_pos(self):
        for i in range(0, self.rows):
            for j in range(0, self.columns):
                self.grid[i][j].row = j
                self.grid[i][j].column = i

    # returns the fscore for the specified square or tile
    def get_score(self, row: int, column: int) -> None:
        print(self.grid[column][row].euclidean_distance(self.start))
        print(self.grid[column][row].euclidean_distance(self.goal))
        print(f"accessed {(row,column)}")
        # print(self.grid[row][column].compute_fscore(self.goal, self.start))

    def make_barrier(self, row: int, column: int) -> None:
        self.grid[row][column].make_barrier()

        """
        # it also tries to check neighbors...

        # obtainig rigth element
        # NOTE: misc functions
        """
        self.grid[row][column].compute_neighbors(self.grid)
        print(row, column)

        print(self.grid[row][column].euclidean_distance(self.goal))
        print(self.grid[row][column].neighbors)

    def make_goal(self, row: int, column: int) -> None:
        self.grid[row][column].make_goal()
        self.goal = (row, column)

    def make_start(self, row: int, column: int) -> None:
        self.grid[row][column].make_start()
        self.start = (row, column)

    def make_empty(self, row: int, column: int) -> None:
        # TODO: modify
        self.grid[row][column] = Square(color=Colors.empty, column=column, row=row)
        print(f"hacemos blanco el punto {row,column}")
