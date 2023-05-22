from enum import Enum
from typing import Optional


class Colors(Enum):
    barrier = (0, 0, 0)
    visited = (0, 255, 0)
    empty = (255, 255, 255)
    path = (255, 69, 0)
    goal = (0, 0, 255)


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
        self.neighbors = []

    # getting neighbors function
    def compute_neighbors(self, grid) -> list:
        print(self.column, self.row)
        # ok so we need to go to the leftoutermost top position
        temp_col = self.column - 1
        temp_row = self.row - 1
        # we start the loop in temp_col and temp_row respectively
        for i in range(temp_col, temp_col + 3):
            for j in range(temp_row, temp_row + 3):
                if (i, j) == (self.column, self.row):
                    pass
                else:
                    try:
                        # so it append elements in this direction top-left,left,bottom-left,bottom,bottom-right,right,top-righ
                        if not grid[i][j].is_barrier():
                            self.neighbors.append(grid[i][j])
                        else:
                            self.neighbors.append(None)

                    except:
                        self.neighbors.append(None)

    def euclidean_distance(self, goal: tuple) -> float:
        if goal[0]:
            return ((self.column - goal[0]) ** 2 + (self.row - goal[1]) ** 2) ** (
                1 / 2
            ) * 10

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

    # str rep
    def __str__(self):
        return str(self.color)

    def __repr__(self) -> str:
        return self.color.name
