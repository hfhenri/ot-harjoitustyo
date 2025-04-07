import random


class Water:
    type_id = 2
    color = "blue"

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def move_self(self, x, y):

        self.x = x
        self.y = y

    def step(self, simulation):
        if simulation.can_move(self.x, self.y + 1):
            self.move_self(self.x, self.y + 1)
            simulation.moved = True
            return True

        if random.choice([True, False]):
            if simulation.can_move(self.x - 1, self.y):
                self.move_self(self.x - 1, self.y)
                simulation.moved = True
                return True

        if simulation.can_move(self.x + 1, self.y):
            self.move_self(self.x + 1, self.y)
            simulation.moved = True
            return True

        return False
