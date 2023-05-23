from enum import Enum
from typing import Optional


class Colors(Enum):
    barrier = (0, 0, 0)  # black
    visited = (0, 255, 0)  # green
    empty = (255, 255, 255)  # white
    path = (255, 69, 0)  # ?
    goal = (0, 0, 255)  # blue
    start = (255, 0, 0)


class Square:
    # represents a square inside the board
    def __init__(
        self,
        row: Optional[int] = None,
        column: Optional[int] = None,
        color=Colors.empty,
    ) -> None:
        self.color = color
        self.column = column
        self.row = row
        self.h = 0
        self.g = 0
        self.f = 0
        self.neighbors = []
        self.parent = None

    # getting neighbors function
    # NOTE: some weird bug...
    def compute_neighbors(self, grid) -> list:
        print(f"compute_neighbor pos : {self.column, self.row}")
        # ok so we need to go to the leftoutermost top position
        temp_col = self.column - 1
        temp_row = self.row - 1
        # we start the loop in temp_col and temp_row respectively
        temp_neighbors = []
        for i in range(temp_row, temp_row + 3):
            for j in range(temp_col, temp_col + 3):
                if (i, j) == (self.row, self.column):
                    pass
                else:
                    try:
                        # so it append elements in this direction top-left,left,bottom-left,bottom,bottom-right,right,top-righ

                        temp_neighbors.append(grid[i][j])
                    except:
                        temp_neighbors.append(None)

        self.neighbors = temp_neighbors
        return self.neighbors

    def euclidean_distance(self, square: tuple) -> float:
        # TODO: ensure that goal actually exists
        # NOTE: returning an int and normalizing the distance by multiplying it for 10
        if square[0]:
            return int(
                ((self.row - square[0]) ** 2 + (self.column - square[1]) ** 2)
                ** (1 / 2)
                * 10
            )

    def manhattan_distance(self, goal: tuple) -> float:
        # TODO: ensure that goal actually exists
        if goal[0]:
            return abs(self.column - goal[0]) + abs(self.row - goal[1])

    def get_pos(self):
        return (self.row, self.column)

    def change_color(self):
        self.color = Colors.visited

    def is_barrier(self):
        return self.color.name == "barrier"

    def make_barrier(self):
        self.color = Colors.barrier

    def make_goal(self):
        self.color = Colors.goal

    def make_empty(self):
        self.color = Colors.empty

    def make_path(self):
        self.color = Colors.path

    def make_start(self):
        self.color = Colors.start

    # str rep
    def __str__(self):
        return str(self.color)

    def __repr__(self) -> str:
        return self.color.name

    def __eq__(self, other):
        return self.get_pos() == other.get_pos()
