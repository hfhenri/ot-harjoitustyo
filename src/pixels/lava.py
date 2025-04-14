import time

from pixels.liquid import liquid_flow_logic
from pixels.steam import Steam
from pixels.wood import Wood
from pixels.water import Water

class Lava:
    type_id = 4
    color = "red"

    def __init__(self, x, y):
        self.updated = False
        self.x = x
        self.y = y

    def move_self(self, x, y):
        self.x = x
        self.y = y

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
            elif isinstance(cell, Wood):
                if cell.contact_timer is None:
                    cell.contact_timer = time.time()
                    continue
                if time.time() - cell.contact_timer > 1:
                    simulation.remove_pixel(cell_x, cell_y)

        return liquid_flow_logic(simulation, self)
