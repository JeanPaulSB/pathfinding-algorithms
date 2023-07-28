from .Point import Square
from .Point import Colors
from src.util.board_utils import euclidean_distance

"""

g(n) -> distance from start to point
h(n) -> distance from the point to the goal


f -> g + h

"""


class A_star:
    def __init__(self, maze):
        self.maze = maze
        self.grid = maze.grid
        self.open = []  # list of open nodes
        self.closed = []  # list of close nodes
        self.start = maze.get_start()
        self.goal = maze.get_goal()

    def trace_path(self) -> list:
        path = []
        current = self.goal

        while current != self.start:
            path.append(current)
            current = current.parent
            print(path)

    def solve(self):
        self.reset()

        self.open.append(self.start)

        while len(self.open) > 0:
            current = self.open[0]

            for node in self.open:
                if node.f < current.f or node.f == current.f and node.h < current.h:
                    current = node

            self.open.remove(current)
            self.closed.append(current)

            if current == self.goal:
                print("lo encontramos")
                return

            for neighbor in node.compute_neighbors(self.maze):
                if neighbor.is_barrier() or neighbor in self.closed:
                    pass

                costToNeighbor = current.g + euclidean_distance(current, neighbor)
                if (
                    costToNeighbor < neighbor.g
                    or neighbor not in self.open
                    and neighbor.is_barrier() == False
                ):
                    neighbor.g = costToNeighbor
                    neighbor.h = euclidean_distance(neighbor, self.goal)
                    neighbor.parent = current

                    if (
                        neighbor.is_barrier() == False
                        and neighbor != self.start
                        and neighbor != self.goal
                    ):
                        neighbor.make_path()

                    if neighbor not in self.open:
                        self.open.append(neighbor)

    def reset(self):
        self.open = []
        self.closed = []
