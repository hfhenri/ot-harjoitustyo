from pixels.fire import Fire
from pixels.wood import Wood
from pixels.water import Water
from pixels.oil import Oil


class Wire:

    """
    The Wire-class contains the logic for pixels behaving like wire.
    It stays in place and becomes active when touched by Fire.
    The signal in the wire last a few seconds and lights Wood and Oil on fire.
    The signal can be extinguished with Water.
    """

    type_id = 11
    color = "#4a0c0c"
    solid = True

    FIRE_POWER = 20

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.power = 0
        self.updated = False

    def step(self, simulation):
        new_power = 0
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = self.x + dx, self.y + dy
            neighbor = simulation.get_pixel(nx, ny)
            if isinstance(neighbor, Fire):
                new_power = max(new_power, Wire.FIRE_POWER)
            elif hasattr(neighbor, 'type_id') and neighbor.type_id == Wire.type_id:
                new_power = max(new_power, neighbor.power - 1)

        self.power = max(0, new_power)

        self.color = "#ffa500" if self.power > 0 else "#4a0c0c"

        if self.power > 0:
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                nx, ny = self.x + dx, self.y + dy
                neighbor = simulation.get_pixel(nx, ny)
                if isinstance(neighbor, (Wood, Oil)):
                    simulation.remove_pixel(nx, ny)
                    simulation.add_pixel(Fire(nx, ny))
                if isinstance(neighbor, Water):
                    self.power = max(0, self.power - 2)

        return True
