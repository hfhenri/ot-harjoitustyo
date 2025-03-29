import random

class Sand:
    id = 1
    color = "yellow"

    def __init__(self, x, y):
        self.old_x = x
        self.old_y = y
        self.x = x
        self.y = y

    def move_self(self, x, y):
        self.old_x = self.x
        self.old_y = self.y
        self.x = x
        self.y = y
        
    def step(self, simulation):
        if simulation.can_move(self.x, self.y, self.x, self.y + 1):
            self.move_self(self.x, self.y + 1)
            simulation.moved = True
            return True
        else:
            if random.choice([True, False]):
                if simulation.can_move(self.x, self.y, self.x - 1, self.y + 1):
                    self.move_self(self.x - 1, self.y + 1)
                    simulation.moved = True
                    return True
                elif simulation.can_move(self.x, self.y, self.x + 1, self.y + 1):
                    self.move_self(self.x + 1, self.y + 1)
                    simulation.moved = True
                    return True
            else:
                    if simulation.can_move(self.x, self.y, self.x + 1, self.y + 1):
                        self.move_self(self.x + 1, self.y + 1)
                        simulation.moved = True
                        return True
                    elif simulation.can_move(self.x, self.y, self.x - 1, self.y + 1):
                        self.move_self(self.x - 1, self.y + 1)
                        simulation.moved = True
                        return True
