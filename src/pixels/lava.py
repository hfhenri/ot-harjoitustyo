from pixels.liquid import liquid_flow_logic
from pixels.steam import Steam
from pixels.wood import Wood
from pixels.water import Water
from pixels.oil import Oil
from pixels.fire import Fire


class Lava:

    """
    The Lava-class contains the logic for pixels behaving like lava.
    It behaves like a liquid and light Wood and Oil on fire.
    """

    type_id = 4
    liquid = True
    color = "red"

    def __init__(self, x, y):
        self.updated = False
        self.y = y
        self.x = x

    def move_self(self, x, y):
        self.y = y
        self.x = x

    def step(self, simulation):

        cell_below = simulation.can_move_return(self.x, self.y + 1)
        cell_above = simulation.can_move_return(self.x, self.y - 1)
        cell_left = simulation.can_move_return(self.x - 1, self.y)
        cell_right = simulation.can_move_return(self.x + 1, self.y)

        cells_iter = [cell_below, cell_above, cell_left, cell_right]
        for cell in cells_iter:

            if cell is None:
                continue

            cell_x = cell.x
            cell_y = cell.y

            if isinstance(cell, Water):
                simulation.remove_pixel(cell_x, cell_y)
                simulation.add_pixel(Steam(cell_x, cell_y))

            elif isinstance(cell, (Wood, Oil)):
                simulation.remove_pixel(cell_x, cell_y)
                simulation.add_pixel(Fire(cell_x, cell_y))

        return liquid_flow_logic(simulation, self)
