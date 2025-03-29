from pixels.empty import Empty

class Simulation:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.moved = False

        self.grid = []

        for x in range(self.width):
            new_row = []
            for y in range(self.height):
                new_row.append(Empty(x, y))

            self.grid.append(new_row)

        self.movement_queue = []

    def can_move(self, x1, y1, x2, y2):
        if 0 <= x2 < self.width and 0 <= y2 < self.height:
            return type(self.grid[x2][y2]) is Empty
        return False
    
    def clear_queue(self):
        self.movement_queue.clear()
    
    def add_pixel(self, pixel):
        self.grid[pixel.x][pixel.y] = pixel
    
    def move_pixel(self, x1, y1, x2, y2):
        pixel = self.grid[x1][y1]
        self.grid[x2][y2] = pixel
        self.grid[x1][y1] = Empty(x1, y1)
    
    def simulate(self):
        self.moved = False

        for x in range(self.width):
            for y in range(self.height - 2, -1, -1):
                cell = self.grid[x][y]
                moved = cell.step(self)

                if moved:
                    self.move_pixel(cell.old_x, cell.old_y, cell.x, cell.y)
                    self.movement_queue.append(cell)
                