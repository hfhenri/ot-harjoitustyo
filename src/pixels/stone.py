class Stone:
    """
    The Stone-class contains the logic for pixels behaving like stone.
    Its immovable and doesn't interact with anyting.
    """

    type_id = 3
    color = "gray"

    def __init__(self, x, y):
        self.updated = False
        self.x = x
        self.y = y

    def step(self):
        return False
