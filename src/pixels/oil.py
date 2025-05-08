from pixels.liquid import liquid_flow_logic, liquid_float_on_water_logic


class Oil:

    """
    The Oil-class contains the logic for pixels behaving like oil.
    It behaves like a liquid and is flammable.
    """

    type_id = 7
    liquid = True
    color = "#281E15"

    def __init__(self, x, y):
        self.updated = False
        self.y = y
        self.x = x

    def move_self(self, x, y):
        self.x = x
        self.y = y

    def step(self, simulation):
        should_rise = liquid_float_on_water_logic(simulation, self)

        if should_rise:
            return False

        return liquid_flow_logic(simulation, self)
