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
        font: pygame.font.Font,
        offset: int,
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

        self.font = font

        self.offset = offset

        # handles last five actions
        self.history = ["Game started..."]

    """
    Draws the board in pygame.
    """

    # applying some offset
    def draw(self) -> str:
        # calculating how many blocks will take the padding

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

        # dibujamos los mensajes de texto
        for index, text in enumerate(self.history[-5:]):
            img = self.font.render(text, True, "black")

            self.screen.blit(img, (1680, 50 + index * 20))

    # assign actual pos for each square in the grid, since at this point they're just "blind" tiles or square
    # TODO: not needed
    def assign_pos(self):
        for i in range(0, self.rows):
            for j in range(0, self.columns):
                self.grid[i][j].row = j
                self.grid[i][j].column = i

    # function that writes the corresponding h,g values for each node
    def write(self, square: Square, i, j):
        text = self.font.render(
            f"f:{square.f} g: {square.g}", True, Colors.barrier.value
        )
        rect = text.get_rect()

        rect.x = j * self.block_size + self.block_size // 2
        rect.y = i * self.block_size + self.block_size // 2

        self.screen.blit(text, rect)

    def set_g(self, row, column, value):
        pass

    def make_barrier(self, row: int, column: int) -> None:
        self.grid[row][column].make_barrier()

    def make_path(self, pos: tuple):
        self.grid[pos[0]][pos[1]].change_color()

    def make_goal(self, row: int, column: int, a_star) -> None:
        if self.goal == (None, None):
            self.grid[row][column].make_goal()
            self.goal = (row, column)
            self.history.append(f"Goal set: ({row},{column})")

    def make_start(self, row: int, column: int, a_star) -> None:
        self.grid[row][column].make_start()
        self.start = (row, column)
        a_star.start = self.grid[row][column]

        self.history.append(f"Start point set: ({row},{column})")

    def make_empty(self, row: int, column: int) -> None:
        # TODO: modify
        self.grid[row][column].make_empty()

    def get_g(self, row, column):
        return self.grid[row][column].g

    def add_message(self, msg):
        self.history.append(msg)

    def has_goal(self) -> bool:
        return self.goal != (None, None)

    def has_start(self) -> bool:
        return self.start != (None, None)

    """
    if goal and start are setted, they return the corresponding square object
    """

    def get_start(self) -> Square:
        if self.start != (None, None):
            (row, column) = self.start
            return self.grid[row][column]

    def get_goal(self) -> Square:
        if self.start != (None, None):
            (row, column) = self.goal
            return self.grid[row][column]
