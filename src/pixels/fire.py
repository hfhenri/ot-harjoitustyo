import random
from pixels.wood import Wood
from pixels.oil import Oil


class Fire:
    """
    The Fire-class contains the logic for pixels behaving like fire.
    It disappears after a few seconds and spreads in Wood and Oil.
    """
    type_id = 8
    color = "orange"

    MAX_LIFETIME = 30
    SPREAD_CHANCE = 0.3

    def __init__(self, x, y):
        self.updated = False
        self.x = x
        self.y = y
        self.lifetime = 0

    def move_self(self, x, y):
        self.y = y
        self.x = x

    def step(self, simulation):
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = self.x + dx, self.y + dy
            neighbor = simulation.can_move_return(nx, ny)
            if isinstance(neighbor, (Wood, Oil)):
                if random.random() < Fire.SPREAD_CHANCE:
                    simulation.remove_pixel(nx, ny)
                    simulation.add_pixel(Fire(nx, ny))

        self.lifetime += 1
        if self.lifetime > Fire.MAX_LIFETIME:
            simulation.remove_pixel(self.x, self.y)
            return False

        return False
