class Stone:
    type_id = 3
    color = "gray"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def step(self, *args):
        return False
