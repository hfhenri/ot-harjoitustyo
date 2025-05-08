
from pixels.liquid import liquid_flow_logic
from pixels.fire import Fire
from pixels.empty import Empty


class Water:

    """
    The Water-class contains the logic for pixels behaving like water.
    It behaves like a liquid and turns into steam in contact with Lava.
    """

    type_id = 2
    color = "blue"
    liquid = True

    def __init__(self, x, y):
        self.updated = False
        self.x = x
        self.y = y

    def move_self(self, x, y):
        self.x = x
        self.y = y

    def step(self, simulation):
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = self.x + dx, self.y + dy
            neighbor = simulation.can_move_return(nx, ny)
            if isinstance(neighbor, Fire):
                simulation.remove_pixel(nx, ny)
                simulation.add_pixel(Empty(nx, ny))

        return liquid_flow_logic(simulation, self)
