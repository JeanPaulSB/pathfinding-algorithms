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
    def assign_pos(self):
        for i in range(0, self.rows):
            for j in range(0, self.columns):
                self.grid[i][j].row = i
                self.grid[i][j].column = i

    def make_barrier(self, column: int, row: int) -> None:
        self.grid[column][row] = Square(color=Colors.barrier, column=column, row=row)
        # it also tries to check neighbors...
        #
        # obtainig rigth element
        self.grid[column][row].compute_neighbors(self.grid)
        print(self.grid[column][row].euclidean_distance(self.goal))
        self.grid[column][row].change_color()
        print(self.grid[column][row].neighbors)

    def make_goal(self, column: int, row: int) -> None:
        self.grid[column][row] = Square(color=Colors.goal, column=column, row=row)
        self.goal = (column, row)

        print(f"hacemos azul el punto {column,row}")

    def make_empty(self, column: int, row: int) -> None:
        self.grid[column][row] = Square(color=Colors.empty, column=column, row=row)
        print(f"hacemos blanco el punto {row,column}")
