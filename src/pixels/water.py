
from pixels.liquid import liquid_flow_logic

class Water:
    type_id = 2
    color = "blue"

    def __init__(self, x, y):
        self.updated = False
        self.x = x
        self.y = y

    def move_self(self, x, y):
        self.x = x
        self.y = y

    def step(self, simulation):
        return liquid_flow_logic(simulation, self)
