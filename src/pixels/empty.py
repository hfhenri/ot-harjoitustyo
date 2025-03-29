class Empty:
    id = 0
    color = "black"

    def __init__(self, x, y):
        self.old_x = x
        self.old_y = y
        self.x = x
        self.y = y
    
    def step(self, simulation):
        return False
