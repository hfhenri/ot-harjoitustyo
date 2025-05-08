
class Empty:

    """
    The Empty-class is the default pixel for an empty cell.
    It doesn't interact with anything.
    """

    type_id = 0
    color = "black"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def step(self):
        return False
