import time

class Wood:
    type_id = 5
    color = "#A1662F"
    contact_timer = None

    def __init__(self, x, y):
        self.updated = False
        self.x = x
        self.y = y

    def step(self):

        if self.contact_timer is not None:
            if time.time() - self.contact_timer > 1:
                self.contact_timer = None

        return False
