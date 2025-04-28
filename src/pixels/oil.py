from pixels.liquid import liquid_flow_logic, liquid_float_on_water_logic

class Oil:
    type_id = 7
    liquid = True
    color = "#281E15"

    def __init__(self, x, y):
        self.updated = False
        self.x = x
        self.y = y

    def move_self(self, x, y):
        self.x = x
        self.y = y

    def step(self, simulation):
        should_rise = liquid_float_on_water_logic(simulation, self)

        if should_rise:
            return True

        return liquid_flow_logic(simulation, self)
