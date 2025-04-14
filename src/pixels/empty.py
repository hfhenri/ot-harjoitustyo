class Empty:
    type_id = 0
    color = "black"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def step(self):
        return False
