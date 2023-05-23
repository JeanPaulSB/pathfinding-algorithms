from .Point import Square
from .Point import Colors

"""

g(n) -> distance from the point to the goal
h(n) -> distance from start to point

"""


class A_star:
    def __init__(self, maze):
        self.maze = maze
        self.grid = maze.grid
        self.goal = self.maze.get_goal()
        self.start = self.maze.get_start()
        self.open = []  # list of open nodes
        self.closed = []  # list of close nodes

    def lowest_f(self) -> Square:
        lowest_f = 1000000

        for node in self.open:
            if (
                node.compute_fscore(self.goal.get_pos(), self.start.get_pos())
                < lowest_f
            ):
                node.f = lowest_f
                lowest_node = node

        return lowest_node

    def solve(self):
        self.reset()
        # resetting
        self.open.append(self.start)

        while len(self.open) > 0:
            current = self.lowest_f()
            self.open.remove(current)
            self.closed.append(current)

            if current == self.goal:
                return

            for neighbor in current.compute_neighbors(self.grid):
                if neighbor in self.closed:
                    pass
                else:
                    neighbor.g = current.g + neighbor.euclidean_distance(
                        current.get_pos()
                    )
                    neighbor.h = neighbor.euclidean_distance(self.goal.get_pos())
                    neighbor.f = neighbor.h + neighbor.g

            return

    # resets algorithms
    def reset(self):
        self.open = []
        self.closed = []

    def color_origin(self):
        self.grid[0][0].change_color()
