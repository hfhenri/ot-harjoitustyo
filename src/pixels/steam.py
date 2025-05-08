from pixels.liquid import liquid_flow_logic, liquid_float_on_water_logic


class Steam:

    """
    The Steam-class contains the logic for pixels behaving like steam.
    It behaves like a liquid that flows upwards.
    """

    type_id = 6
    color = "white"

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.updated = False

    def move_self(self, x, y):
        self.y = y
        self.x = x

    def step(self, simulation):
        should_float = liquid_float_on_water_logic(simulation, self)

        if should_float:
            return True

        return liquid_flow_logic(simulation, self, up=True)
