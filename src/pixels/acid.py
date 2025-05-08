import random
from pixels.liquid import liquid_flow_logic
from pixels.stone import Stone
from pixels.wood import Wood
from pixels.sand import Sand
from pixels.oil import Oil


class Acid:

    """
    The Acid-class contains the logic for pixels behaving like acid.
    It dissolves Stone, Wood, Sand and Oil pixels and turns them into acid pixels.
    """

    type_id = 9
    liquid = True
    color = "#00FF00"

    def __init__(self, x, y):
        self.updated = False
        self.x = x
        self.y = y

    def move_self(self, x, y):
        self.y = y
        self.x = x

    def step(self, simulation):
        for x, y in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            dx, dy = self.x + x, self.y + y
            neighbor = simulation.can_move_return(dx, dy)
            if isinstance(neighbor, (Stone, Wood, Sand, Oil)):
                simulation.remove_pixel(dx, dy)
                simulation.add_pixel(Acid(dx, dy))
                simulation.changed = True

        moved = liquid_flow_logic(simulation, self)
        if moved:
            return True

        if random.choice([True, False]):
            if simulation.can_move(self.x - 1, self.y):
                self.move_self(self.x - 1, self.y)
                return True
            if simulation.can_move(self.x + 1, self.y):
                self.move_self(self.x + 1, self.y)
                return True
        else:
            if simulation.can_move(self.x + 1, self.y):
                self.move_self(self.x + 1, self.y)
                return True
            if simulation.can_move(self.x - 1, self.y):
                self.move_self(self.x - 1, self.y)
                return True

        return False
