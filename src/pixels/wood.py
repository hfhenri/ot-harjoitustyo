
class Wood:

    """
    The Wood-class contains the logic for pixels behaving like wood.
    It stays in place and lights on fire when touched by Lava or another Fire pixel. 
    """

    type_id = 5
    color = "#A1662F"

    def __init__(self, x, y):
        self.updated = False
        self.x = x
        self.y = y

    def step(self):

        return False
