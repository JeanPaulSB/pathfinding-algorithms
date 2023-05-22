"""
pos: mouse coordinates x,y as tuple
margin: margin between squares as defined in the grid generation
block_size: block size of each square inside the grid

returns:
the corresponding row and colum for the clicked square, so you can access
to the board or maze grid and make the corresponding changes

"""


def get_square(pos: tuple, margin: float, block_size=int) -> tuple:
    column, row = pos[0] // (block_size + margin), pos[1] // (block_size + margin)
    return (column, row)


def a_star():
    pass
