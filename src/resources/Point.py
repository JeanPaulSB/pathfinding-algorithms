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

    # getting neighbors function

    # str rep
    def __str__(self):
        return str(self.color)

    def __repr__(self) -> str:
        return self.color.name
