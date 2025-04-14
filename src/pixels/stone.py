class Stone:
    type_id = 3
    color = "gray"

    def __init__(self, x, y):
        self.updated = False
        self.x = x
        self.y = y

    def step(self):
        return False
